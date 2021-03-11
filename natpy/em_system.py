import inspect
import sys
from astropy.constants import EMConstant
"""Set the active system for Electromagnetic constants (e, eps0, mu0 etc.)
Overrides the base namespace for each EM constant with the selected system 
value. Other systems can be accesses through subnamespace as in Astropy

E.g. If set to si, natpy.const.e.si -> natpy.const.e, 
               but natpy.const.e.gauss -> natpy.const.e.gauss"""


def set_active_em_system(mode):
    caller_name = inspect.currentframe().f_back.f_globals['__name__']
    for k, v in sys.modules[caller_name].__dict__.items():
        if issubclass(type(v), EMConstant):
            sys.modules[caller_name].__dict__[k] = getattr(v, mode)
