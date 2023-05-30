def time_saved(speed_limit, avg_speed, distance):
  sl_time = distance / speed_limit
  as_time = distance / avg_speed

  time_saved_in_hours = sl_time - as_time
  return round(time_saved_in_hours * 60, 1)

print(time_saved(80, 90, 40))
print(time_saved(80, 90, 4000))
print(time_saved(80, 100, 40))
print(time_saved(80, 100, 10))