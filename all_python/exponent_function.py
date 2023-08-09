# An exponent function is basically going to allow us to take a certain number and raise it to a specific power
#print(2**3)
def raise_to_power (base_num, power_num):
    result = 1
    for i in range(power_num):
        result = result*base_num
    return result

print(raise_to_power(2,8))
