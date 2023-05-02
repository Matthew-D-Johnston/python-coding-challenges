WORLD_LANDMASS = 148940000

def area_of_country(country, area):
  proportion = round((area / WORLD_LANDMASS) * 100, 2)

  # return f"{country} is {proportion}% of the total world's landmass"
  return "{country} is {proportion}% of the total world's landmass".format(country=country, proportion=proportion)

print(area_of_country("Russia", 17098242))
print(area_of_country("USA", 9372610))
print(area_of_country("Iran", 1648195))
