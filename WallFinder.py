# Name: Soon Sam R. Santos
# Date: April 04, 2017
# Session: 05
# WallFinder.py

import lib601.sf as sf
import lib601.poly as poly

def controllerSF(k):
    """
    k = the proportional gain applied to the error.
    returns a SystemFunction of a system whose input is the distance error
    and the output is the commanded velocity.
    """
    # V/E = k/1
    return sf.SystemFunction(poly.Polynomial([k]), poly.Polynomial([1]))
def plantSF(T):
    """
    # T = time step duration
    returns a SystemFunction of a system whose input is he commanded velocity
    and the ouput is the actual distance to the wall.
    """
    return sf.SystemFunction(poly.Polynomial([-T,0]), poly.Polynomial([-1,1]))
def sensorSF():
    """
    returns a system function for a system whose input is the actual sensor
    value and whose output is a one-step delayed sensor reading.
    """
    return sf.SystemFunction(poly.Polynomial([1,0]), poly.Polynomial([1]))
def wallFinderSystemSF(T,k):
    """
    returns a system function for a system whose input is the desired distance
    to the wall and whose output is the actual distance to the wall.
    """
    return sf.FeedbackSubtract(sf.Cascade(controllerSF(k), plantSF(T)), sensorSF())

# TestCases
T = 0.1
k = -5
print controllerSF(k)
print plantSF(T)
print sensorSF()
print wallFinderSystemSF(T,k)
