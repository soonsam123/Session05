"""
Class and some supporting functions for representing and manipulating system functions. 
"""

import math
import lib601.poly as poly
import lib601.util as util


class SystemFunction:
    """
    Represent a system function as a ratio of polynomials in R
    """
    def __init__(self, numeratorPoly, denominatorPoly):
        # Two instances of the Polynomial class as input.
        self.numerator = numeratorPoly
        self.denominator = denominatorPoly
    def poles(self):
        """
        Returns a list of the poles of the system.
        """
        # Cloning the coeffs of the denominator Polynomial.
        poles_coeffs = self.denominator.coeffs[:]
        # Reversing it is the same as solving for R = 1/z
        poles_coeffs.reverse()
        # Return the roots of the Polynomial of the list of coeffs solving for R = 1/z
        return poly.Polynomial(poles_coeffs).roots()
    def poleMagnitudes(self):
        """
        Returns a list of the abs value of each pole.
        """
        # Storing the poles in a list.
        poles_list = self.poles()
        poles_magnitude = []
        # Storing the abs value of each into another list.
        for pole in poles_list:
            poles_magnitude.append(abs(pole))
        return poles_magnitude
    def dominantPole(self):
        """
        Returns one of the poles with greatest MAGNITUDE.
        """
        # Storing the poles magnitude into a list.
        poles_magnitude = self.poleMagnitudes()
        # This module returns the greatest result of each element of the list applyied to
        # the second function, in this case the function is just the number because I want the
        # greatest number of the list.
        return util.argmax(poles_magnitude, lambda x: x)
        
    def __str__(self):
        return 'SF(' + self.numerator.__str__('R') + \
               '/' + self.denominator.__str__('R') + ')'

    __repr__ = __str__


def Cascade(sf1, sf2):
    """
    The output of the fisrt system function is the input of the second.
    """
    # Multiplying the numerators instances of Polynomial.
    numerator = sf1.numerator * sf2.numerator
    # Multiplying the denominators instances of Polynomial.
    denominator = sf1.denominator * sf1.denominator
    return SystemFunction(numerator, denominator)

def FeedbackSubtract(sf1, sf2=None):
    """
    Make the generic expression for the FeedbackSubtract block diagram.
    """
    numerator = sf1.numerator*sf1.denominator*sf2.denominator
    denominator = ((sf1.denominator*sf1.denominator)*sf2.denominator) + (sf1.denominator*sf1.numerator*sf2.numerator)
    return SystemFunction(numerator, denominator)


