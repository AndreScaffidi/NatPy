# NatPy
## Convert the units of particle physics quantities
---
### Packages needed:
- astropy
- numpy
- sympy
---
### Basic Usage

Code levarages `astropy.units.core.Unit` and `astropy.units.quantity.Quantity` objects.

1. Run `import numpy` and `from astropy import units as u`.
2. Run `import natpy`.
3. Access physical constants with symbol:
```
>>> natpy.c
<Quantity 2.99792458e+08 m / s>

>>> natpy.hbar
<Quantity 1.05457182e-34 J s>
```

4. Specify base of natural units with `natpy.set_active_units()`. Pass a string corresponding to a list of default natural units, or a list of physical constants to set your own. List of default bases found in `natpy/default_values.py`. (will markdown later)

5. Run `natpy.convert()` to convert between units, including necessary factors of natural units. Pass just unit objects to obtain conversion factors. Pass quantity objects to perform conversions. E.g.
```
# kg to keV
>>> natpy.convert(u.kg, u.keV)
5.6173581670146864e+32

# Electron mass
>>> me = natpy.convert(9.11e-31 * u.kg, u.keV)
>>> me
<Quantity 511.74132902 keV>

# Energy of electron with momentum of 1 MeV 
>>> p = 1 * u.MeV
>>> E = np.sqrt(p**2 + me**2)

# Convert to SI units
>>> natpy.convert(E,u.J)
<Quantity 1.79926309e-13 J>
```
Note: Summing quanties requires conventionally equivalent units.

6. See ```tests/convert_test.py ``` for more examples.