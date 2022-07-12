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
            if elements[0] != 'Data':   
                #elimino l'elemento \n
                try:
                    elements[1] = str(float(elements[1]))
                except ValueError as e:
                    print('Errore di valore in get_data() di CVSFile(): {}'.format(e))
                    
                except Exception as e:
                    print('Errore generico in get_data() di CVSFile(): {}'.format(e))
                    
                                        
                #aggiungo l'elememto modificato a list
                list.append(elements) 
        #chiudo il file
        my_file.close()
    
        return list

class NumericalCSVFile(CSVFile):
    #converte automaticamente a float le vendite
    def __init__(self, name):
        # verifico esista il file
        try:
            f = open(name, 'r')
        #stampo l'errore se il file non esiste
        except FileNotFoundError as e:
            print('Errore in __init__ () di NumericalCVSFile(), file non trovato: {}'.format(e))
           
        #se esiste chiudo il file e inizializzo il nome
        else:
            f.close()
            self.name = name

    
    def get_data(self):
        #eredito get_data
        list = super().get_data()
        lista = []
        for item in list:
            try:
                lista.append(float(item[1]))   
            except ValueError as e:
                print('Errore di valore in get_data() di NumericalCVSFile(): {}'.format(e))
                exit()
                    
            except Exception as e:
                print('Errore generico in get_data() di NumericalCVSFile(): {}'.format(e))
                
        return lista
        

my_var = CSVFile('shampoo_sales.csv')
print(my_var.get_data())

 
    


