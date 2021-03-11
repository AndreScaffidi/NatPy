import numpy
from astropy import units as u
from astropy import constants as const
"""
Library of Physical Constants. May be updated/added to as necessary
"""

# Constants

# Coulomb constant = 1/4.pi.eps0, use existing value of eps0
k_e = const.Constant(
    "k_e", "Coulomb constant",
    1/(4*numpy.pi * (const.eps0).to(u.F/u.m).value),
    "m / F", 0.0, system="si",
    reference=const.eps0.reference
)

# Fermi constant cited by PDG in GeV-2/(hbar.c)3,
# here convert to Jm3 during definition
G_F = const.Constant(
    "G_F", "Fermi constant",
    1.1663787e-5 * (u.GeV**(-2)).to(u.J**(-2)) *
    ((const.hbar * const.c)**3).to((u.J*u.m)**3).value,
    "J * m**3",
    6e-07 * 1e-5 * (u.GeV**(-2)).to(u.J**(-2)) *
    ((const.hbar * const.c)**3).to((u.J*u.m)**3).value,
    system="si",
    reference="CODATA2019"
)

from astropy.constants import *  # noqa
