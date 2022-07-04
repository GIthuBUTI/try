my_file = open('shampoo_sales.csv', 'r')

list = []
for item in my_file:
    elements = item.split(',')
    if elements[0] != 'Date':   
        elements[1] = str(float(elements[1]))
        list.append(elements)
            
print(list)
my_file.close()