#%%
import numpy
import astropy.units
from astropy import units as u
#%%
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class NaturalUnit(astropy.units.quantity.Quantity):
    _registry = []
    
    def __init__(self, a):
        self._registry.append(self)
        super(NaturalUnit, self).__init__()
        for attr in dir(a):
            try:
                if not attr.startswith("__"):
                    setattr(self, attr, getattr(a, attr))
            except:
                pass
            
    @classmethod
    def NaturalConversionMatrix(cls):
        """Return a MxN Matrix for M base units, N natural units, and a 1xN list of base units."""
        natural_decomposed = numpy.array([[x.unit.decompose().powers, 
                               x.unit.decompose().bases] 
                              for x in cls._registry])
        natural_bases = list(set.union(*[set(), *natural_decomposed[:,1]]))
        natural_matrix = numpy.zeros((len(natural_bases), len(cls._registry)))
        for ind, val in numpy.ndenumerate(natural_matrix):
            try:
                natural_matrix[ind] = natural_decomposed[ind[1]][0][
                    natural_decomposed[ind[1]][1].index(
                        natural_bases[ind[0]])]
            except:
                pass #will except if natural unit has zero of base unit
        return natural_matrix, natural_bases
    
    @classmethod
    def ClearNaturalUnits(cls):
        for x in cls._registry:
            del x
        cls._registry = []
# #%%
# c=NaturalUnit(3.00e8 * u.m/u.s)
# hbar = NaturalUnit(6.63e-34 * u.J*u.s)

# #%%
# x,y=NaturalUnit.NaturalConversionMatrix()
# t=numpy.linalg.pinv(x)@numpy.array([-2,0,2])
# numpy.around(t,8).astype(int)
# # %%
# l=numpy.array([1,2])
# m=numpy.array(NaturalUnit._registry, dtype=object)
# numpy.prod(l*m)