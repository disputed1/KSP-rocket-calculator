class Point(object):
    """Point in space."""

    surfaceAltitude = property(lambda s: s.altitude - s.planet.radius)

    def __init__(self, planet, altitude):
        self.planet = planet
        self.altitude = altitude

    @property
    def g(self):
        return self.planet.g(self.altitude)

    @property
    def pressure(self):
    	"""Air pressure in given point (measured in atmospheres)."""
    	if self.planet.hasAtmosphere:
    		rv = self.planet.pressureAt(self.altitude)
    	else:
    		rv = 0.0
    	return rv

    @property
    def density(self):
        if self.planet.knowDensity:
            rv = self.planet.densityAt(self.altitude)
        else:
            rv = 0.0
        return rv

    @property
    def standingOnSurface(self):
        return abs(self.altitude - self.planet.radius) < 1e-2

    def changeAlt(self, val):
        self.altitude += val

    def copy(self):
        cls = type(self)
        return cls(self.planet, self.altitude)