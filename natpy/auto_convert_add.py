from astropy.units.quantity import Quantity
from astropy.units import dimensionless_unscaled

astropy_ufunc = Quantity.__array_ufunc__


def convert_ufunc(self, function, method, *args, **kwargs):
    if (function.__name__ != "add") and (function.__name__ != "subtract"):
        return astropy_ufunc(self, function, method, *args, **kwargs)
    else:
        if not all(isinstance(x, Quantity) for x in args):
            unit = dimensionless_unscaled
        else:
            unit = self.unit

        new_args = [x.convert(unit) if (isinstance(x, Quantity)) else x for x in args]

        new_kwargs = {
            key: (value.convert(unit) if isinstance(value, Quantity) else value)
            for key, value in kwargs.items()
        }

        return astropy_ufunc(self, function, method, *new_args, **new_kwargs)
