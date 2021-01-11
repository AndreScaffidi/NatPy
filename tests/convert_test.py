import natpy
from astropy.units.core import dimensionless_unscaled
import numpy
import sys
sys.path.append("../")

print(" ")
print("Standard Astropy Convert")
print("expect: 1 km = 1000 m")
print((1*natpy.km).to_string(), " = ",
      natpy.convert(1*natpy.km, natpy.m).to_string())
print("----------------------------------")
print(" ")
print("Convert seconds to metres.")
print("expect: 1s = 299792458 m")
print((1*natpy.s).to_string(), " = ",
      natpy.convert(1*natpy.s, natpy.m).to_string())
print("----------------------------------")

print("Convert composite unit.")
print("expect: (cm^-1)/(t keV) = 9.46e17 / (t yr keV)")
print((1*natpy.cm**(-1) / (natpy.t * natpy.keV)).to_string(), " = ", natpy.convert(1 *
                                                                                   natpy.cm**(-1)/(natpy.t * natpy.keV), (natpy.t * natpy.yr * natpy.keV)**(-1)).to_string())
print("----------------------------------")

print("switch units, determine Planck length")
natpy.set_active_units("planck")
print("expect: 1 = 1.616255 e-35 m")
print((1*natpy.dimensionless_unscaled).to_string(), " = ",
      natpy.convert(1*natpy.dimensionless_unscaled, natpy.m).to_string())
print("----------------------------------")
