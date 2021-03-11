import sys
from .convert import convert

from .default_values import default_conventions
from .default_values import set_active_units, list_active_units, get_active_units
from . import constants as const
from astropy.units.core import UnitBase
from astropy.units.quantity import Quantity
from astropy.units import *
from .auto_convert_add import convert_ufunc
from .em_system import RedefineNamespace

UnitBase.convert = convert
Quantity.convert = convert
set_active_units("hbar_c_eps0")

# Add functionality for auto converting compatible sums
Quantity.__array_ufunc__ = auto_convert_add.convert_ufunc


def set_active_em_system(mode): RedefineNamespace(mode, const)


set_active_em_system('si')
