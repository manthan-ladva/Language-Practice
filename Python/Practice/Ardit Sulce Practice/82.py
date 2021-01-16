import ephem

jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
distance_au_unit = jupiter.sun_distance
distance_km = distance_au_unit * 149597870.691
print(distance_km)
