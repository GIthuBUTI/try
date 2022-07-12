#controllo che gli input siano corretti
try:
    float(numero)
except:
    #gestire errore

try:
    my_string.split(',')
except:
    #gestire errore

# Creare un'eccezione
class Errore(Exception):
    pass
# Alzare un'eccezione
    raise Errore('Errore generato dal parametro: "{}".'.format(parametro))

#Sanitizzare gli input per prevenire gli errori
#Es1
sesso = 'm'
if sesso not in ['M','F']:
    #gestisci errore

#per prevenire errore
sesso_maiusc = sesso.upper()
if sesso_maiusc not in ['M','F']:
    #gestisci errore

#Es2
sesso = 'M '
if sesso not in ['M','F']:
    #gestisci errore

#per prevenire errore
sesso_pulito = sesso.strip()
if sesso_maiusc not in ['M','F']:
    #gestisci errore
