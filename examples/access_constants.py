import numpy
import sys
sys.path.append("../")
import natpy  # noqa

print("---------- print c in full -----------------")
print(natpy.const.c)
print("--------------------------------------------")

print("---------- print hbar abbrev ---------------")
print(natpy.const.hbar.abbrev)
print("--------------------------------------------")

print("---------- print au name -------------------")
print(natpy.const.au.name)
print("--------------------------------------------")

print("---------- print custom unit ---------------")
print(natpy.const.k_e)
print("--------------------------------------------")

print("---------- product of access units ---------")
print(natpy.const.hbar * natpy.const.c)
print("--------------------------------------------")
