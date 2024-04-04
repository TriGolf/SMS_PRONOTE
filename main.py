#importe les bibliothèques
import pronotepy
from pronotepy.ent import ac_orleans_tours
import time
import requests
from datetime import datetime

#initialise la variable
last_note = ''

#se connecte à pronote

def connection_pronote():
    client = pronotepy.Client(
        'https://0450047g.index-education.net/pronote/eleve.html',
        username='nom d\' utilisateur', # votre identifiant ENT !!!
        password="Mot de passe", # votre mot de passe
        ent=ac_orleans_tours)
    return client


def envoyer(message) :
    sms_id = 'Identifiant free mobile' # Votre identifiant Free Mobile
    sms_key = 'clée secrète (token)' # La clée obtenue dans mes options puis notifications sms
    res = requests.get(f'https://smsapi.free-mobile.fr/sendmsg?user={sms_id}&pass={sms_key}&msg={message}') # envoie
    print(f"{message}\na été envoyé à {datetime.today().strftime('%d-%m-%Y %H:%M')}")
    
def verif_nouvelle_note(last_note) : # vérifie s'il y a une nouvelle note
    notes = []
    for grade in client.current_period.grades:  # iterate over all the grades
        notes.append(f'''Vous avez recu une nouvelle note en {grade.subject.name} qui est de {grade.grade}/{grade.out_of} avec un coefficient de {grade.coefficient}.
                     
La moyenne de la classe est {grade.average}/{grade.out_of} et la meilleure note est {grade.max}/{grade.out_of}

Cette note fait passer votre moyenne générale à {client.current_period.overall_average}''') 
 
    notes=list(reversed(notes))
    if notes[0] != last_note : # vérifie si c'est une nouvelle note
        return notes[0]
    
    else :
        return False

envoyer("Programme lance")
execution = 0
while 1 :



    try :
        client = connection_pronote()
    except :
        print('échec de connection')
        
    verif = verif_nouvelle_note(last_note)

    if verif :
        last_note = verif
        if execution != 0 :
            envoyer(verif)
        else :
            execution = 1
        
    try : 
        del client
        
    except :
        pass
        
    print(datetime.today().strftime('%H:%M')) #Pour vérifier si le programme marche toujours dans la console
    
    time.sleep(3600) # Pour ne pas surcharger le serveur pronote
