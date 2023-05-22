# Split The Bill
# You're in a restaurant with your friends and it's time to go, but there's still one big problem...
# the bill. Who will pay what? Lucky for you, you've got your computer handy! One simple function
# and the bill is paid——fairly, too!
# The function should take one parameter: an object/dict with two or more name-value pairs that
# represent the members of the group and the amount spent by each.
# Your function should return an object/dict with the same names, showing how much money the members
# should pay or receive.
# Further points:
# The values should be positive numbers if the person should receive money from the group,
# negative numbers if they owe money to the group.
# If value is a decimal, round to two decimal places.
# Example
# 3 friends go out together: A spends £20, B spends £15, and C spends £10.
# The function should return an object/dict showing that A should receive £5, B should receive £0,
# and C should pay £5.
# group = {
#    'A': 20,
#   'B': 15,
#    'C': 10
# }
# split_the_bill(group) # returns {'A': 5, 'B': 0, 'C': -5}
# https://www.codewars.com/kata/5641275f07335295f10000d0

def split_the_bill(x):
    bill_sum = sum(x.values())
    divided = bill_sum / len(x)
    for member, paid in x.items():
        new_val = paid - divided
        if new_val.is_integer():
            x[member] = int(new_val)
        else:
            x[member] = round(new_val, 2)
    return x


print(split_the_bill({'A': 20, 'B': 15, 'C': 10}) == {'A': 5, 'B': 0, 'C': -5})
print(split_the_bill({'A': 40, 'B': 25, 'X': 10}) == {'A': 15, 'B': 0, 'X': -15})
print(split_the_bill({'A': 4, 'B': 3, 'X': 3}) == {'A': 0.67, 'B': -0.33, 'X': -0.33})
print(split_the_bill({'A': -55.33, 'B': -70.33, 'C': -85.33, 'D': 57.67, 'E': -37.33}) == {'A': -17.2, 'B': -32.2, 'C': -47.2, 'D': 95.8, 'E': 0.8})
