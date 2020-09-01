import numpy
from .constants import *
from astropy import units as u
from .natural_unit_class import NaturalUnit
"""
Library of default natural bases, and the method to set base.
"""

##Default Nautral Unit Conventions
default_conventions = {
    "hbar_c": [hbar, c],
    "HEP": [c, hbar, kb],
    "atomic": [e, me, hbar, kb],
    "planck": [c, hbar, G, kb],
    "stoney": [c, G, ke, e],
    "schrodinger": [G, hbar, kb, ke, e],
    "geometrised": [G, c] 
}

def set_active_unit(unit_in):
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
    

