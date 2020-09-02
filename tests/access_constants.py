import numpy 
from astropy import units as u

import sys
sys.path.append("../")
import natpy

print("---------- print c in full -----------------")
print(natpy.c)
print("--------------------------------------------")

print("---------- print hbar abbrev ---------------")
print(natpy.hbar.abbrev)
print("--------------------------------------------")

print("---------- print au name -------------------")
print(natpy.au.name)
print("--------------------------------------------")

print("---------- print custom unit ---------------")
print(natpy.k_e)
print("--------------------------------------------")

print("---------- product of access units ---------")
print(natpy.hbar * natpy.c)
print("--------------------------------------------")
