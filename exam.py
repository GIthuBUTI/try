def compute_daily_max_difference(time_series):
    list_t = []
    max_difference = []
    day_start = []
    day_end = []
    elements = []
    n = 0
    for item in time_series:
        start = item[0] - item[0] % 86400
        end = start + 86400
        if start not in day_start:
            day_start.append(start)
        if end not in day_end:
            day_end.append(end)
        
        if item[0] < day_end[n]:
            list_t.append(item[1])
        
        else:
            elements.append((max(list_t) - min(list_t))
            print(elements)
            n = n + 1
            list_t =[]
    for i in day_end:
        
             
        
            
    
    print(day_start)
    print(day_end)
    
    
    
        


# aggiungere giorno, media a elements
# aggiungere elements a max
 
        
class ExamException(Exception):
    pass
class CSVFile():
    
    def __init__(self, name):  
        self.name = name
        
    def __str__(self):
        return '{}'.format(self.name)
        
    def get_data(self):
        #verifico che il file esista
        try:
            my_file = open(self.name, 'r')
        #se il file non esiste stampo l'errore
        except Exception as e:
            print('Non esiste alcun file con quel nome, ho ricevuto questo errore: {}'.format(e))
            exit()
        #creo lista vuota
        list = []
        #apro il file
        my_file = open(self.name, 'r')
        for item in my_file:
            #divido gli elementi della lista
            elements = item.split(',')
            if elements[0] != 'epoch':   
                #elimino l'elemento \n
                try:
                    elements[0] = int(elements[0])
                    elements[1] = float(elements[1])
                except ValueError as e:
                    print('Errore di valore in get_data() di CVSFile(): {}'.format(e))
                    
                except Exception as e:
                    print('Errore generico in get_data() di CVSFile(): {}'.format(e))
                    
                                        
                #aggiungo l'elememto modificato a list
                list.append(elements) 
        #chiudo il file
        my_file.close()
    
        return list

class CSVTimeSeriesFile(CSVFile):
    def __init__(self, name):  
        self.name = name

    def get_data(self):
        list = super().get_data()
        return list

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

#print(time_series)
print(compute_daily_max_difference(time_series))