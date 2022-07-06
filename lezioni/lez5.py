# costrutto try-except
my_var = 'ciao'

try:
    my_var = float(my_var)
except:
    print('non posso convertire "my_var" a numero')
    print('uso il valore di default "0.0" per "my_var"')
    my_var = 0.0

# posso avere l'eccezione dentro l'except
my_var = 'ciao'
try:
    my_var = float(my_var)

# classe base Excepion
except Exception as e:
    print('non posso convertire "my_var" a numero')
    print('la variabile "my_var" valeva: "{}"'.format(my_var))
    print('ho avuto questo errore: "{}"'.format(e))

# posso gestire eccezioni specifiche
my_var = 'ciao'

try:
    my_var = float(my_var)
except:
    print('non posso convertire "my_var" a numero')
    print('uso il valore di default "0.0" per "my_var"')
    my_var = 0.0

