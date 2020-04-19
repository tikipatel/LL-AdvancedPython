#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:24:56 2020

@author: pratikbhaipatel
"""

# Lambda functions

# Small anonymous functions
# Can be passed as arguments where you need a function; e.g. callbacks; blocks
# Typically used in place just when neede 
# Defined as: lambda (parameters) : (expression)

# Uses lambdas as in-place functions

def CelciusToFahrenheit(temp):
    return (temp * 9  / 5) + 32

def FahrenheitToCelcius(temp):
    return (temp - 32) * 5 / 9

def main():
    cTemps = [0, 12, 34, 100]
    fTemps = [32, 65, 100, 212]
    
    # use regular functions to convert temps
    print('Using regular functions')
    cToFConverted = list(map(CelciusToFahrenheit, cTemps))
    print(cToFConverted)
    fToCConverted = list(map(FahrenheitToCelcius, fTemps))
    print(fToCConverted)

    # use ambdas to accomplish the same thing
    print('Using lambdas functions')
    cToFConverted = list(map(lambda t: (t * 9  / 5) + 32, cTemps))
    print(cToFConverted)
    fToCConverted = list(map(lambda t: (t - 32) * 5 / 9, fTemps))
    print(fToCConverted)
    

if __name__ == '__main__':
    main()