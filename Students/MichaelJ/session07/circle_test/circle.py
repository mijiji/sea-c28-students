#!/usr/bin/env python
"""circle class --
fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = radius ** 2 * math.pi

    def getRadius(self):
        return self._radius

    def setRadius(self, radius):
        self._radius = radius
        self._diameter = self._radius * 2

    def getArea(self, radius):
        self._area = radius * 2 * math.pi

    radius = property(getRadius, setRadius, getArea)

    def getDiameter(self):
        return self._diameter

    def setDiameter(self, diameter):
        self.radius = diameter / 2

    def getArea(self, diameter):
        self._area = (diameter / 2) ** 2 * math.pi

    diameter = property(getDiameter, setDiameter, getArea)

    def getArea(self):
        return self._area

    area = property(getArea)

    def circumference(self):
        return (self.radius * 2 * math.pi)

    def __str__(self):
        return "Circle with radius: %s00000" % repr(float(self.radius))

    def __repr__(self):
        return "Circle(%s)" % str(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False
