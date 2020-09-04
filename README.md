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
 
1. Run `import natpy`.
2. Access physical constants with symbol:
```
>>> natpy.const.c
<class 'astropy.constants.codata2018.CODATA2018'> name='Speed of light in vacuum' value=299792458.0 uncertainty=0.0 unit='m / s' reference='CODATA 2018'>


>>> natpy.const.hbar
<class 'astropy.constants.codata2018.CODATA2018'> name='Reduced Planck constant' value=1.0545718176461565e-34 uncertainty=0.0 unit='J s' reference='CODATA 2018'>

```

3. Specify base of natural units with `natpy.set_active_units()`. Pass a string corresponding to a list of default natural units, or a list of physical constants to set your own. List of default bases found in `natpy/default_values.py`. 

4. Run `natpy.convert()` to convert between units, including necessary factors of natural units. Pass just unit objects to obtain conversion factors. Pass quantity objects to perform conversions. E.g.
```
>>> natpy.convert(u.kg, u.keV)
5.6173581670146864e+32

>>> natpy.convert(9.11e-31 * u.kg, u.keV)
<Quantity 511.74132902 keV>
```
