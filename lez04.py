print('Oggetto con operazione non in-place')
my_string = 'a,b,c'
print(my_string)
print(my_string.split(','))
print(my_string)

print('Oggetto con operazione in-place')
my_list = [1,2,3,4]
print(my_list)
print(my_list.reverse())    # questo metodo non ritorna nulla
print(my_list)

print('1) Definire un oggetto')
class Person():
    pass             # istruzione nulla, serve per avere un blocco vuoto

person = Person()    # istanziazione classe di oggetto: 
                     # da una generica definizione di oggetto a uno specifico                     
print(person)

print('1.1')
class Person():
    def __init__(self, name, surname):  # init inizializza l'oggetto, se non c'è, viene usata quella di default che non fa nulla
        self.name = name                # self chiama sé stesso come istanza di classe
        self.surname = surname

        

person = Person('Rambaldo','Melandri')
print(person)
print(person.name)
print(person.surname)

print('1.2')
class Person():
    
    def __init__(self, name, surname):  # init inizializza l'oggetto, se non c'è, viene usata quella di default che non fa nulla
        self.name = name                # self chiama sé stesso come istanza di classe
        self.surname = surname
    
    def __str__(self):                  # funzione a uso interno che sovrascrivo , rappresenta l'oggetto in formato stringa
        return 'Person "{} {}"'.format(self.name,self.surname)

person = Person('Rambaldo','Melandri')
print(person)

print('1.3')
import random

class Person():
    
    def __init__(self, name, surname):  
        self.name = name                
        self.surname = surname
    
    def __str__(self):                  
        return 'Person "{} {}"'.format(self.name,self.surname)

    #metodo dell'oggetto. Anche chiamata interfaccia.
    def say_hi(self):  
        random_n = random.randint(0,2)

        if random_n == 0:
            print('Buongiorno, {} {}.'.format(self.name,self.surname))
        elif random_n == 1:
             print('Piacere, {} {}, al vostro servizio'.format(self.name,self.surname))
        elif random_n == 2:
            print('Piacere, Architetto {} {}, al vostro servizio'.format(self.name,self.surname))

person = Person('Rambaldo','Melandri')
person.say_hi()      

print('Estendere un oggetto')
# estendo l'oggetto Persona declinandolo in Studente e Architetto
# tutti i metodi che possedeva Persona sono automaticamente ereditati dagli oggetti Studente e Architetto, posso sovrascriverli o aggiungerne altri

class Student (Person):

    #sovrascrivo la rappresentazione in stringa 
    def __str__(self):
        return 'Student "{} {}"'.format(self.name,self.surname)

class Architect (Person):

    def __str__(self):
        return 'Prof. "{} {}"'.format(self.name,self.surname)

    # sovrascrivo il metodo che saluta l'oggetto
    def say_hi(self):  
        
        print('Buongiorno, Architetto {} {}.'.format(self.name,self.surname))

    # con il super accedo al metodo dell'oggetto padre, anche se sovrascritto 
    def original_say_hi (self):
        super().say_hi()

person = Person('Pietro','Pacciani')
print(person)
person.say_hi()

student = Student('Il','Puma')
print(student)
student.say_hi()

architect = Architect('Rambaldo','Melandri')
print(architect)
architect.say_hi()
architect.original_say_hi()
