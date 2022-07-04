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
            if elements[0] != 'Date':   
                elements[1] = str(float(elements[1]))
                list.append(elements) 
        my_file.close()
        return list
        
csv = CSVFile('shampoo_sales.csv')
print(csv)
print(csv.get_data())
