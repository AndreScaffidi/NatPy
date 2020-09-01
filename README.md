# NatPy
## Convert the units of particle physics quantities
---
### Packages needed:
- astropy
- numpy
<<<<<<< HEAD
=======
---
### Basic Usage

1. Run `import numpy` and `from astropy import units as u`.
2. Run `import naturalpy` and `from natural_units import NaturalUnit`.
3. Specify natural units by passing `astropy.units.quantity.Quantity` objects into `NaturalUnit`. E.g. 
```
>>> c = NaturalUnit( 3e8 * u.m / u.s)
>>> hbar = NaturalUnit( 6.63e-34 * u.J * u.s)
```
4. Run `naturalpy.convert()` to convert between units, including necessary factors of natural units. Pass just unit objects to obtain conversion factors. Pass quantity objects to perform conversions. E.g.
```
>>> naturalpy.convert(u.kg, u.keV)
5.6173581670146864e+32

>>> naturalpy.convert(9.11e-31 * u.kg, u.keV)
<Quantity 511.74132902 keV>
```
>>>>>>> Tom-Dev-Branch
