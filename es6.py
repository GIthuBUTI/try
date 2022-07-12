class CSVFile():
    def __init__(self, name):
        if type(name) != str:
           raise TypeError('Errore: Il nome del file non è una stringa.')
        try:
            f = open(name, 'r')
        except FileNotFoundError as e:
            print(e)
            exit()
        else:
            f.close()
            self.name = name
    
#aprire il file e tornare i dati dal file CSV come lista di liste
    def get_data(self):
        
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            print('Non esiste alcun file con quel nome, ho ricevuto questo errore: {}'.format(e))
            exit()

        lista = []
        for line in my_file:
            elements = line.split(',')
            lista.append(elements)
        my_file.close()
        return lista

my_var = CSVFile('h')
print(my_var.get_data())