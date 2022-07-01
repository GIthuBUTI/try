my_file = open('shampoo_sales.csv', 'r')
       
def sum_csv(file):
    values = []
    for item in file:
        elements = item.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = float(elements[1])
            values.append(value)    
    sum = 0
    for item in values:
        sum += item
    return sum

print(sum_csv(my_file))

my_file.close()