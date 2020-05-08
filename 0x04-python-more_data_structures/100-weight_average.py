#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return None
    mul_res = 0
    weight_sum = 0
    for score, weight in my_list:
        mul_res += score * weight
        weight_sum += weight
    return mul_res / weight_sum
