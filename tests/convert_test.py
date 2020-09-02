from astropy.units.core import dimensionless_unscaled
import numpy 
from astropy import units as u

import sys
sys.path.append("../")
import natpy
print(" ")
print("Standard Astropy Convert")
print("expect: 1 km = 1000 m")
print((1*u.km).to_string(), " = ", natpy.convert(1*u.km, u.m).to_string())
print("----------------------------------")
print(" ")
print("Convert seconds to metres.")
print("expect: 1s = 299792458 m")
print((1*u.s).to_string(), " = ", natpy.convert(1*u.s, u.m).to_string())
print("----------------------------------")

print("Convert composite unit.")
print("expect: (cm^-1)/(t keV) = 9.46e17 / (t yr keV)")
print((1*u.cm**(-1) / (u.t * u.keV)).to_string(), " = ", natpy.convert(1*u.cm**(-1)/(u.t * u.keV), (u.t * u.yr * u.keV)**(-1)).to_string())
print("----------------------------------")

print("switch units, determine Planck length")
natpy.set_active_units("planck")
print("expect: 1 = 1.616255 e-35 m")
print((1*u.dimensionless_unscaled).to_string(), " = ", natpy.convert(1*u.dimensionless_unscaled, u.m).to_string())
print("----------------------------------")




