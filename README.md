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
<<<<<<< HEAD
2. Run `import natpy`
3. Specify natural units by passing `astropy.units.quantity.Quantity` objects into `NaturalUnit`. E.g. 
=======
2. Run `import natpy`.
3. Access physical constants with symbol:
>>>>>>> 9c72503b54a4b0fe051abed7aa0077b7894b86c5
```
>>> natpy.c
<Quantity 2.99792458e+08 m / s>

>>> natpy.hbar
<Quantity 1.05457182e-34 J s>
```

4. Specify base of natural units with `natpy.set_active_units()`. Pass a string corresponding to a list of default natural units, or a list of physical constants to set your own. List of default bases found in `natpy/default_values.py`. (will markdown later)

5. Run `natpy.convert()` to convert between units, including necessary factors of natural units. Pass just unit objects to obtain conversion factors. Pass quantity objects to perform conversions. E.g.
```
>>> natpy.convert(u.kg, u.keV)
5.6173581670146864e+32

>>> natpy.convert(9.11e-31 * u.kg, u.keV)
<Quantity 511.74132902 keV>
```
