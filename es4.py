class CSVFile():
    def __init__(self, name):  
        self.name = name
        
    def __str__(self):
        return '{}'.format(self.name)

    def get_data(self):
        list = []
        my_file = open(self.name, 'r')
        for item in my_file:
            elements = item.split(',')
            for index in range(1, len(elements)):
                if elements[0] != 'Date':
                   elements[1] = elements[index].rstrip('\n')
            list.append(elements) 
        my_file.close()
        return list
        
csv = CSVFile('shampoo_sales.csv')
print(csv)
print(csv.get_data())
