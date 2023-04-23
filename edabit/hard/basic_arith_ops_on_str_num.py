# Solution 1
def arithmetic_operation(instructions):
    instruction_list = instructions.split(' ')
    first_num = int(instruction_list[0])
    second_num = int(instruction_list[2])
    operator = instruction_list[1]

    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num
        case '//':
            if second_num == 0:
                return -1
            else:
                return first_num // second_num


# Solution 2
# def arithmetic_operation(instructions):
#     instruction_list = instructions.split(' ')
#     first_num = int(instruction_list[0])
#     second_num = int(instruction_list[2])
#     operator = instruction_list[1]
    
#     if operator == '+':
#         return first_num + second_num
#     elif operator == '-':
#         return first_num - second_num
#     elif operator == '*':
#         return first_num * second_num
#     elif operator == '//':
#         if second_num == 0:
#             return -1
#         else:
#             return first_num // second_num

print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 // 12"))
print(arithmetic_operation("12 // 0"))
