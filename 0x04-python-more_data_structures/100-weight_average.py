#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mul_res = 0
        weight_sum = 0
        for score, weight in my_list:
            mul_res += score * weight
            weight_sum += weight
        return mul_res / weight_sum
