#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 18:49:55 2023

@author: holly

constants = {
    'a_V': 15.67,
    'a_S': 17.23,
    'a_C': 0.714,
    'a_A': 93.15,
    'delta': 11.2,
    'k': -0.5,
    'm_n': 939.56542052,
    'm_p': 938.27208816,
    'm_e':0.51099895000
    }

# constants, Mev/c^2
a_V = 15.67
a_S = 17.23
a_C = 0.714
a_A = 93.15
delta = 11.2
k = -0.5
m_n =  939.56542052
m_p = 938.27208816
m_e = 0.51099895000

"""
constants = {
    'a_V': 15.67,
    'a_S': 17.23,
    'a_C': 0.714,
    'a_A': 93.15,
    'delta': 11.2,
    'k': -0.5,
    'm_n': 939.56542052,
    'm_p': 938.27208816,
    'm_e':0.51099895000
    }


def a_P_chooser(A,Z, constants):
    """Makes correct selection for pairing term based on mass, proton, and 
    nucleus number."""
    N = A - Z
    if (N%2 != 0) and (Z%2 != 0):
        a_P = constants['delta']
    elif (N%2 == 0) and (Z%2 == 0) :
        a_P = -1*constants['delta']
    elif (A%2 is not int):
        a_P = 0
    else:
        print("fuck")
    return a_P, A, N, Z

a_P, A, N, Z = a_P_chooser(204, 82, constants)
print(a_P, 'a_P', N, "N")


def SEMF(a_P, A, N, Z, constants):
    """ Computes the mass of an atom using the SEMF."""
    bound_masses = N * constants['m_n'] + Z *constants['m_p'] + Z*constants['m_e']
    volume_surface = -constants['a_V']*A + constants['a_S']*A**(2/3)
    coupled = constants['a_C']*(Z**2/A**(1/3))
    asymmetry = constants['a_A']*(((N - Z)**2)/(4*A))
    pairing = a_P * A**(constants['k'])
    SEMF_mass = bound_masses + volume_surface + coupled + asymmetry + pairing
    return SEMF_mass

SEMF_mass = SEMF(a_P, A, N, Z, constants)
print('SEMF_mass', SEMF_mass, "MeV/C^2")

# x MeV/c^2 = x * 1.782661922e-30kg/MeV/c^2
# x kg = x * 6.022e+26 amu/kg

def MeV_c2_to_amu(SEMF_mass):
    """ Converts MeV/c^2 to amu """
    SEMF_mass = SEMF_mass * 1.782661922e-30 #kg
    SEMF_mass = SEMF_mass * 6.022e+26 # amu

    return SEMF_mass

SEMF_mass = MeV_c2_to_amu(SEMF_mass)
print("SEMF_mass", SEMF_mass, 'amu')
  
def mass_difference(given_mass, SEMF_mass):
    """ Calculates difference between given mass and SEMF-predicted mass in 
    amu."""
    difference = abs(given_mass - SEMF_mass)
    return difference

difference = mass_difference(203.9730436, SEMF_mass)
print("difference", difference, "amu")

