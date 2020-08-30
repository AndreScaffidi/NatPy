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
from astropy import units as u
import naturalpy
from natural_units import NaturalUnit

import imp
imp.reload(naturalpy)
NaturalUnit.ClearNaturalUnits()

c=NaturalUnit(299792458 * u.m / u.s)
hbar=NaturalUnit(1.05e-34 * u.J * u.s)
me = 9.11e-31 * u.kg
me_f=naturalpy.convert(me, u.keV)
print("me_i: "+me.to_string())
print("me_f: "+me_f.to_string())

naturalpy.convert(u.kg, u.keV)

#%%

test=u.kg * u.m * u.m / (u.keV * u.s * u.s)
test.decompose().scale