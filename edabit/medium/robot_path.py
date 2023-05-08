def robot_path(steps):
  destination1 = [2, 3]
  destination2 = [3, -4]
  destination = [0, 0]

  for step in steps:
    match step:
      case 'n':
        destination[0] += 1
      case 's':
        destination[0] -= 1
      case 'e':
        destination[1] += 1
      case 'w':
        destination[1] -= 1
  
  if destination1[0] == destination[0] and destination1[1] == destination[1]:
    return True
  
  if destination2[0] == destination[0] and destination2[1] == destination[1]:
    return True
  
  return False

print(robot_path(["s", "e", "e", "n", "n", "e", "n"]))
print(robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"]))
print(robot_path(["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"]))

# Solution 2:

def robot_path(steps):
  destination1 = [2, 3]
  destination2 = [3, -4]
  destination = [0, 0]

  for step in steps:
    if step == 'n':
      destination[0] += 1
    elif step == 's':
      destination[0] -= 1
    elif step == 'e':
      destination[1] += 1
    elif step == 'w':
      destination[1] -= 1
  
  if destination1[0] == destination[0] and destination1[1] == destination[1]:
    return True
  
  if destination2[0] == destination[0] and destination2[1] == destination[1]:
    return True
  
  return False

print(robot_path(["s", "e", "e", "n", "n", "e", "n"]))
print(robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"]))
print(robot_path(["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"]))