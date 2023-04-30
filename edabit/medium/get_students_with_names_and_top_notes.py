def top_note(dict):
  name_top_note = {}
  name_top_note["name"] = dict["name"]
  name_top_note["top_note"] = max(dict["notes"])

  return name_top_note

print(top_note({ "name": "John", "notes": [3, 5, 4] }))
print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))
