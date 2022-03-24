input_param = 12345

def reverse_no(input_param):

    condition = True
    reverse_no = 0
    while input_param>0:
        remainder = input_param % 10
        reverse_no = (reverse_no *10) + remainder
        input_param = input_param // 10

    return reverse_no

print(reverse_no(input_param))

