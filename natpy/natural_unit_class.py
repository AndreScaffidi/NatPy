import numpy
import astropy.units
from astropy import units as u
from functools import reduce
from fractions import Fraction


class NaturalUnit(astropy.units.quantity.Quantity):
    _registry = []

    def __init__(self, a):
        self._registry.append(self)
        super().__init__()
        for attr in dir(a):
            try:
                if not attr.startswith("__"):
                    setattr(self, attr, getattr(a, attr))
            except:
                pass

    @classmethod
    def NaturalConversionMatrix(cls):
        """Generate a MxN Matrix for M base units, N natural units, 
        the Moore-Penrose inverse of this matrix,
        and a 1xN list of base units.
        Assigns these outputs as attributes of the NaturalUnit class"""

        natural_decomposed = numpy.array([[x.unit.decompose().powers,
                                           x.unit.decompose().bases]
                                          for x in cls._registry], dtype=object)

        natural_bases = list(set.union(*[set(), *natural_decomposed[:, 1]]))
        natural_matrix = numpy.zeros((len(natural_bases), len(cls._registry)))
        for ind, val in numpy.ndenumerate(natural_matrix):
            try:
                natural_matrix[ind] = natural_decomposed[ind[1]][0][
                    list(natural_decomposed[ind[1]][1]).index(natural_bases[ind[0]])]
            except:
                pass  # will except if natural unit has zero of base unit
        pseudoinv = numpy.linalg.pinv(natural_matrix.astype(int))
        def to_frac(x): return Fraction(x).limit_denominator(10**8)
        natural_matrix_pseudoinv = numpy.vectorize(to_frac)(pseudoinv)

        cls._natural_matrix = natural_matrix
        cls._natural_matrix_pseudoinv = natural_matrix_pseudoinv
        cls._natural_bases = natural_bases

    @classmethod
    def ClearNaturalUnits(cls):
        for x in cls._registry:
            del x
        cls._registry = []
        cls._natural_matrix = None
        cls._natural_matrix_pseudoinv = None
        cls._natural_bases = None
