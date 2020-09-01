#%%
from astropy import units as u
import natpy as nat
import imp
imp.reload(nat)

nat.set_active_unit([nat.c, nat.hbar])

nat.convert(nat.hbar * nat.c, u.GeV*u.fm)