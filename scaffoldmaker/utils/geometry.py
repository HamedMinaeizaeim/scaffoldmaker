'''
Utility functions for geometry.
Created on Apr 11, 2018

@author: Richard Christie
'''

import math

def getApproximateEllipsePerimeter(a, b):
    '''
    Get perimeter of ellipse using Ramanujan II approximation.
    :param a: Major axis length.
    :param b: Minor axis length.
    :return: Perimeter length.
    '''
    h = ((a-b)/(a+b))**2
    return math.pi*(a + b)*(1.0 + 3.0*h/(10.0 + math.sqrt(4.0 - 3.0*h)))

def getEllipseArcLength(a, b, angle1Radians, angle2Radians):
    '''
    Calculates perimeter distance between two angles by summing line segments at regular angles.
    :param a: Major axis length (On x, 0 / PI).
    :param b: Minor axis length.(On y, PI/2, 3PI/2).
    :param angle1Radians: First angle anticlockwise from major axis.
    :param angle2Radians: Second angle anticlockwise from major axis.
    :return: Perimeter lenge, positive if anticlockwise, otherwise negative.
    '''
    angle1 = min(angle1Radians, angle2Radians)
    angle2 = max(angle1Radians, angle2Radians)
    # Max 100 segments around ellipse
    segmentCount = int(math.ceil(50*(angle2-angle1)/math.pi))
    length = 0.0
    for i in range(segmentCount + 1):
        r = i/segmentCount
        angle = r*angle1 + (1.0 - r)*angle2
        x = ( a*math.cos(angle), b*math.sin(angle) )
        if i > 0:
            delta = math.sqrt((x[0] - lastX[0])*(x[0] - lastX[0]) + (x[1] - lastX[1])*(x[1] - lastX[1]))
            length += delta
        lastX = x
    if angle1Radians < angle2Radians:
        return length
    else:
        return -length

def updateEllipseAngleByArcLength(a, b, inAngleRadians, arcLength):
    '''
    Update angle around ellipse to subtend arcLength around the perimeter.
    Iterates using Newton's method.
    :param inAngleRadians: Initial angle anticlockwise from major axis.
    :param arcLength: Arc length to traverse. Positive=anticlockwise, negative=clockwise.
    :param a: Major axis length (On x, 0 / PI).
    :param b: Minor axis length.(On y, PI/2, 3PI/2).
    :return: New angle, in radians.
    '''
    angle = inAngleRadians
    lengthMoved = 0.0
    lengthTol = (a + b)*1.0E-4  # broader tolerance due to reliance on inexact getEllipseArcLength()
    #print('inAngleRadians', inAngleRadians, ', arcLength', arcLength)
    while math.fabs(arcLength - lengthMoved) > lengthTol:
        t = ( -a*math.sin(angle), b*math.cos(angle) )
        dlength_dangle = math.sqrt(t[0]*t[0] + t[1]*t[1])
        angle += (arcLength - lengthMoved)/dlength_dangle
        lengthMoved = getEllipseArcLength(a, b, inAngleRadians, angle)
        #print('lengthMoved', lengthMoved)
    #print('updateEllipseAngleByArcLength a', a, 'b', b, ', angle', inAngleRadians, ', arcLength', arcLength, ' -> ', angle)
    return angle
