from .convert import convert


from .default_values import default_conventions
from .default_values import set_active_units, list_active_units, get_active_units
from . import constants as const
from astropy.units.core import UnitBase
from astropy.units.quantity import Quantity
from astropy.units import *

UnitBase.convert = convert
Quantity.convert = convert
set_active_units("hbar_c")
