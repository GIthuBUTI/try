def sum_list(list):
    sum = 0
    for number in list:
        sum += number
    return sum

the_list = [7.5, 4.98, 0.834, 7, 1.1]

from colorama import init
from termcolor import colored
init()

for item in the_list:
    if item != the_list[-1]:
        print('{} + '.format(item), end="")
    else:
        print('{} = '.format(item), end="")
print(colored('{}'.format(sum_list(the_list)), 'blue', 'on_green'))
