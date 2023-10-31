def check_input_type(input_value):
    if isinstance(input_value, str):
        return "String"
    elif isinstance(input_value, int):
        return "Integer"
    else:
        return "Special Character"

# Test cases
input1 = "Hello"
input2 = 12345
input3 = "@"
input4 = 3.14  # This will be considered a special character

print(f"{input1} is of type: {check_input_type(input1)}")
print(f"{input2} is of type: {check_input_type(input2)}")
print(f"{input3} is of type: {check_input_type(input3)}")
print(f"{input4} is of type: {check_input_type(input4)}")
