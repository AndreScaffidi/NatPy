from astropy.units.core import dimensionless_unscaled
import numpy
import sys 
sys.path.append("../")
import natpy

import pytest

def test_conversions():

    #Standard Astropy Convert
    #expect: 1 km = 1000 m
    assert( (1*natpy.km) == natpy.convert( 1*natpy.km, natpy.m ) )

    #Convert seconds to metres.
    #expect: 1s = 299792458 m
    assert( natpy.convert(1*natpy.s, natpy.m) == ( 299792458 *natpy.m ) )
    
    #Convert composite unit.
    #expect: (cm^-1)/(t keV) = 9.46e17 / (t yr keV)
    assert( natpy.convert(1*natpy.cm**(-1)/(natpy.t * natpy.keV), (natpy.t * natpy.yr * natpy.keV)**(-1)) == ( 9.4607304725808e+17 * (natpy.t * natpy.yr *natpy.keV)**(-1) ) )

    #switch units, determine Planck length
    natpy.set_active_units("planck")
    #expect: 1 = 1.616255 e-35 m
    assert( natpy.convert( 1*natpy.dimensionless_unscaled, natpy.m) == 1.6162550244237053e-35 * natpy.m )

    #Conversion factor, i.e. number
    #expect: 1 GeV^3 = 0.00768 fm^3
    assert( natpy.convert( natpy.GeV**(-3), natpy.fm**3 ) == 0.007683505576381198 )
    #And directly converting, keeping quantity
    assert( natpy.convert( 1*natpy.GeV**(-3), natpy.fm**3 ) == 0.007683505576381197 * natpy.fm**3 )


def test_access():
    #c in full
    assert( natpy.const.c.value == 299792458.0)
    assert( natpy.const.c.unit == 'm / s')
    #assert( natpy.const.c.dtype == 'float64')
    assert( natpy.const.c.name == 'Speed of light in vacuum')
    assert( natpy.const.c.uncertainty == 0.0)
    assert( natpy.const.c.reference == 'CODATA 2018')

    #hbar abbrev
    hbarA = natpy.const.hbar.abbrev
    assert( hbarA == 'hbar')

    #au name
    assert(natpy.const.au.name == 'Astronomical Unit')

    #custom unit
    assert( natpy.const.k_e.value == 8987551792.261171)
    assert( natpy.const.k_e.unit == 'm / F')
    assert( natpy.const.k_e.name == 'Coulomb constant')
    assert( natpy.const.k_e.uncertainty == 0.0)
    assert( natpy.const.k_e.reference == 'CODATA 2018')
    
#if __name__ == '__main__':
#    test_conversions()
#    test_access()
