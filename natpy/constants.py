import numpy
from astropy import units as u
from astropy import constants as const

"""
Library of Physical Constants. May be updated/added to as necessary
"""

##Constants

k_e = const.Constant("k_e", "Coulomb constant", 1/(4*numpy.pi * const.eps0.value), "m / F", 0.0, system="si", reference=const.eps0.reference)

### Exact
# c     = 299792458 * u.m / u.s
# h     = 6.62607015e-34 * u.J * u.s
# hbar  = h / (2*numpy.pi)
# e     = 1.602176634e-19 * u.C
# Na    = 6.02214076e23 / u.mol
# kb    = 1.380649e-23 * u.J / u.K

# ### Approx
# me       = 9.109387015e-31 * u.kg
# mp       = 1.67262192369e-27 * u.kg
# mn       = 1.67492749804e-27 * u.kg
# epsilon0 = 8.854187128e12 * u.F / u.m
# mu0      = 1.25663706212e-6 * u.N / u.A**2
# ke       = 1/(4*numpy.pi * epsilon0)
# alpha    = 7.2973525693e-3 * u.dimensionless_unscaled
# G        = 6.67430e-11 * u.m**3 / (u.kg * u.s**2)
