import numpy
from . import constants as natpy_const
import astropy.constants as const
from astropy import units as u
from .natural_unit_class import NaturalUnit
"""
Library of default natural bases, and the method to set base.
"""

##Default Nautral Unit Conventions
default_conventions = {
    "hbar_c": [const.hbar, const.c],
    "HEP": [const.c, const.hbar, const.k_B],
    "atomic": [const.e, const.m_e, const.hbar, const.k_B],
    "planck": [const.c, const.hbar, const.G, const.k_B],
    "stoney": [const.c, const.G, natpy_const.k_e, const.e],
    "schrodinger": [const.G, const.hbar, const.k_B, natpy_const.k_e, const.e],
    "geometrised": [const.G, const.c] 
}

def set_active_units(unit_in):
    if isinstance(unit_in, str):
        if not unit_in in default_conventions:
            raise ValueError("Default natural units not implemented.")
        else:
            NaturalUnit.ClearNaturalUnits()
            for x in default_conventions[unit_in]:
                NaturalUnit(x)
    else:
        unit_in = list(unit_in)
        if not all(isinstance(x, u.quantity.Quantity) for x in unit_in):
            raise ValueError("Input must be a list of quantities, or a string corresponding to a default set of natural units.")
        else:
            NaturalUnit.ClearNaturalUnits()
            for x in unit_in:
                NaturalUnit(x)
    return
    
def get_active_units():
    return NaturalUnit._registry

def list_active_units(full_name=False):
    result = []
    if full_name:
        for x in NaturalUnit._registry:
            result.append(x.name)
    else:
        for x in NaturalUnit._registry:
            result.append(x.abbrev)
    return result