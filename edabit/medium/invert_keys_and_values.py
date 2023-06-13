def invert(input_dict):
    output_dict = {}

    for key in input_dict:
        output_dict[input_dict[key]] = key

    return output_dict

print(invert({ "z": "q", "w": "f" }))
print(invert({ "a": 1, "b": 2, "c": 3 }))
print(invert({ "zebra": "koala", "horse": "camel" }))
