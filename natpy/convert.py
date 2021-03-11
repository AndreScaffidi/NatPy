from .natural_unit_class import NaturalUnit
from astropy.units.core import UnitConversionError
import numpy
import astropy.units


def ConversionDimensionality(initial_unit, target_unit):
    natural_bases = NaturalUnit._natural_bases
    initial_dimvec = [initial_unit.decompose().powers,
                      initial_unit.decompose().bases]
    target_dimvec = [target_unit.decompose().powers,
                     target_unit.decompose().bases]
    # Change-of-Unit Dimensionality Vector
    cou_dimvec = numpy.empty_like(natural_bases, dtype=int)
    for i in range(len(natural_bases)):
        cou_dimvec[i] = ((target_dimvec[0][
            target_dimvec[1].index(natural_bases[i])]
            if natural_bases[i] in target_dimvec[1] else 0)
            - (initial_dimvec[0][
                initial_dimvec[1].index(natural_bases[i])]
                if natural_bases[i] in initial_dimvec[1] else 0))
    return cou_dimvec


def CoUNaturalDimensionality(cou_dimvec):
    natural_matrix = NaturalUnit._natural_matrix
    if natural_matrix.ndim < 2:
        if numpy.linalg.matrix_rank([natural_matrix, cou_dimvec]) <= 1:
            result = numpy.array([cou_dimvec[0]/natural_matrix[0]])
        else:
            raise UnitConversionError
    else:
        natural_matrix_pseudoinv = NaturalUnit._natural_matrix_pseudoinv
        result = natural_matrix_pseudoinv @ cou_dimvec

    return result


def QuantityConvert(initial_quantity, target_unit):
    """Convert an input quantity to a target set of units considering 
    natural dimensionality. Quantity is multiplied by required factors 
    of natural units, then astropy conversion is applied 
    for remaining rescaling factors."""

    initial_unit = initial_quantity.unit

    cou_dimvec = ConversionDimensionality(initial_unit, target_unit)

    try:
        cou_naturaldim = CoUNaturalDimensionality(cou_dimvec)
    except:
        raise UnitConversionError(
            f"Units {initial_quantity.unit} and {target_unit} \
                 not compatible after considering natural dimensionality.")
        raise
    natural_conv_factor = numpy.prod(
        numpy.array(NaturalUnit._registry, dtype=object)**cou_naturaldim
    )

    try:
        result = (natural_conv_factor * initial_quantity).to(target_unit)
    except UnitConversionError:
        raise UnitConversionError(
            f"Units {initial_quantity.unit} and {target_unit} \
                 not compatible after considering natural dimensionality.")
    return result


def UnitConvert(initial_unit, target_unit):

    cou_dimvec = ConversionDimensionality(initial_unit, target_unit)

    cou_naturaldim = CoUNaturalDimensionality(cou_dimvec)

    natural_conv_factor = numpy.prod(
        numpy.array(NaturalUnit._registry, dtype=object)**cou_naturaldim
    )
    scale_conv_factor = (
        initial_unit * natural_conv_factor.unit / target_unit).decompose()

    if scale_conv_factor.bases != []:
        raise UnitConversionError(
            f"Units {initial_unit} and {target_unit} \
            not compatible after considering natural dimensionality.")
    result = natural_conv_factor.value * scale_conv_factor.scale

    return result


def convert(initial_unit, target_unit):
    """Attempts astropy conversion method. Upon failure, attempts 
    to rescale initial_unit by factors of natural units to compatible unit. 
    Then retries astropy conversion."""

    if not (isinstance(initial_unit, astropy.units.core.UnitBase)
            or isinstance(initial_unit, astropy.units.quantity.Quantity)):
        raise ValueError(
            "initial_unit must be an astropy unit or quantitiy object.")

    if not isinstance(target_unit, astropy.units.core.UnitBase):
        raise ValueError("target_unit must be an astropy unit object.")

    try:
        return initial_unit.to(target_unit)
    except UnitConversionError:
        if isinstance(initial_unit, astropy.units.quantity.Quantity):
            return QuantityConvert(initial_unit, target_unit)
        else:  # is astropy.units.core.Unit from prev check
            return UnitConvert(initial_unit, target_unit)
    except Exception as e:
        raise e
