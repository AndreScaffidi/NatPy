import inspect
import sys
from astropy.constants import EMConstant
"""Set the active system for Electromagnetic constants (e, eps0, mu0 etc.)
Overrides the base namespace for each EM constant with the selected system
value. Other systems can be accesses through subnamespace as in Astropy

E.g. If set to si, natpy.const.e.si -> natpy.const.e,
               but natpy.const.e.gauss -> natpy.const.e.gauss"""


def RedefineNamespace(mode, const_module):
    for k, v in const_module.__dict__.items():
        if issubclass(type(v), EMConstant):
            try:
                const_module.__dict__[k] = (
                    getattr(const_module.si.__dict__[k], mode)
                )
            except AttributeError:
                pass  # Wont work if that constant has no attribute of mode
            # In future will possibly add extra methods to obtain system
            # dependent def, but for now this works
