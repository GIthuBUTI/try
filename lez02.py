def sum_list(list):
    sum = 0
    for number in list:
        sum += number
    return sum

the_list = [7.5, 4.98, 0.834, 7, 1.1]

for item in the_list:
    if item != the_list[-1]:
        print('{} + '.format(item))
    else:
        print('{} = '.format(item))
print('{}'.format(sum_list(the_list)))
