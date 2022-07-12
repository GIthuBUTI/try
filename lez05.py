# costrutto try-except
print('1')
my_var = 'ciao'

try:
    my_var = float(my_var)
except:
    print('non posso convertire "my_var" a numero')
    print('uso il valore di default "0.0" per "my_var"')
    my_var = 0.0

print('2')
# posso avere l'eccezione dentro l'except
my_var = 'ciao'
try:
    my_var = float(my_var)

# classe base Excepion
except Exception as e:
    print('non posso convertire "my_var" a numero')
    print('la variabile "my_var" valeva: "{}"'.format(my_var))
    print('ho avuto questo errore: "{}"'.format(e))

print('3')
# posso gestire eccezioni specifiche
my_var = 'ciao'

try:
    my_var = float(my_var)

except TypeError:
    print('non posso convertire "my_var" a numero')
    print('errore di tipo. "my_var" era di tipo "{}".'.format(type(my_var)))

except ValueError:
    print('non posso convertire "my_var" a numero')
    print('errore di valore. "my_var" valeva "{}".'.format(my_var))


except Exception as e:
    print('non posso convertire "my_var" a numero')
    print('errore generico: "{}".'.format(e))
