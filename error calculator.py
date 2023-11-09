import math
def divide_error_calculator(values=[]):
    if values == []:
        values = get_values()
    print(values)
    values = normalize_error(values)
    print(values)
    num = div(values)
    print(num)


def get_values():
    values = []
    for i in range(2):
        val = float(input("enter the value:\n"))
        error = float(input("enter the error:\n"))
        values.append([val, error])
    return values


def normalize_error(values):
    norm_values = []
    for value in values:
        norm_values.append((value[0], value[1] / value[0]))
    return norm_values


def div(values):
    num = values[0][0] / values[1][0]
    error = sum_errors(values[0][1], values[1][1])
    error = denormalize(num, error)
    return (num, error)


def sum_errors(err1, err2):
    err1 *= err1
    err2 *= err2
    err = err1 + err2
    err = math.sqrt(err)
    return err


def denormalize(num, error):
    error *= num
    return error


def power(value, power):
    value = normalize_error([value])
    value = value[0]
    num = math.pow(value[0], power)
    return [num, denormalize(num, value[1] * power)]

while(True):
    values = [[float(input("enter the value:\n")), float(input("enter the error:\n"))], [0.60675, 0.0005]]
    print(values)
    values = [power(values[0], 2), values[1]]
    print(values)
    values[1][0] *= 2
    values[1][1] *= 2
    divide_error_calculator(values)




    
