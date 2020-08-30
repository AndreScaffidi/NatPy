#%% 
import astropy
import numpy as np
# %%
from astropy import units as u
# %%
x=["a","b"]
"a" in x
# %%
qf = np.array([2,-2,1]).T
qi = np.array([0,0,1]).T
c = np.array([1,-1,0]).T
hbar = np.array([2,-1,1]).T
A = np.array([c,hbar]).T
np.linalg.pinv(A) @(qf - qi)

# %%
class test:
        @classmethod
    def speak(cls):
        print("hi")
        
new = test()
test.speak()
# %%
a={"m":[1,2],"s":[1,-1]}
b={"m":[1e3,2]}
a[0]

for key in a.keys():
    print(a.get(key)[1]==b.get(key)[1])
# %%
from astropy import units as u
u.m.bases

c = 3.00e8 * u.m/u.s
#%%

#%%
u.erg.decompose().bases

x=np.zeros((2,3))

count = 0
for i,j, val in np.ndenumerate(x):
    print(i)
# %%
import numpy as np
from astropy import units as u
import naturalpy
import natural_units
from natural_units import NaturalUnit

import imp
imp.reload(naturalpy)
imp.reload(natural_units)
NaturalUnit.ClearNaturalUnits()

c=NaturalUnit(299792458 * u.m / u.s)
hbar=NaturalUnit( (6.62607015e-34 / (2*np.pi)) * u.J * u.s)
me = 9.11e-31 * u.kg
me_f=naturalpy.convert(me, u.keV)
print("me_i: "+me.to_string())
print("me_f: "+me_f.to_string())

naturalpy.convert(u.kg, u.keV)

fm = 1*u.fm **(-1)
print(naturalpy.convert(fm, u.GeV).to_string())

print(naturalpy.convert(u.cm**(-1), u.yr**(-1)))

#%%

test=u.kg * u.m * u.m / (u.keV * u.s * u.s)
test.decompose().scale

#%%
import numpy as np
a=np.array([1,0,-1])
b=np.array([2,0,-2])
g=np.zeros((1,3))
g.ndim
# np.linalg.matrix_rank([a,b])

a==b

#%%
a=np.array([[0],[0]])
for ind in np.ndenumerate(a):
    print(ind)