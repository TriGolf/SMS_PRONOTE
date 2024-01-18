#importe les bibliothèques
import pronotepy
from pronotepy.ent import ac_orleans_tours # Votre ent
import time
import requests

#initialise la variable
last_note = ''

#se connecte à pronote
client = pronotepy.Client(
    'https://0000000a.index-education.net/pronote/eleve.html',
    username='username', # votre identifiant ENT !!!
    password="password", # votre mot de passe
    ent=ac_orleans_tours)


def envoyer_note(message) :
    sms_id = 'sms_id' # Votre identifiant Free Mobile
    sms_key = 'sms_key' # La clée obtenue dans mes options puis notifications sms
    res = requests.get(f'https://smsapi.free-mobile.fr/sendmsg?user={sms_id}&pass={sms_key}&msg={message}') # envoie
    print(f'le message {message} a été envoyé') # Confirmation

def verif_nouvelle_note(last_note) : # vérifie s'il y a une nouvelle note
    notes = []
    for grade in client.current_period.grades:  # iterate over all the grades
        notes.append(f'''Vous avez recu une nouvelle note le {grade.date} qui est de {grade.grade}/{grade.out_of} en {grade.subject.name} avec un coefficient de {grade.coefficient}.
                     
La moyenne de la classe est {grade.average} et la meilleure note est {grade.max}

Cette note fais passer votre moyenne a {client.current_period.overall_average}''') 

        
    notes.sort(reverse=True) # trie par date
    if notes[0] != last_note : # vérifie si c'est une nouvelle note
        return notes[0]
    
    else :
        return False

while True :
    verif = verif_nouvelle_note(last_note)

    if verif :
        last_note = verif
        envoyer_note(verif)
    
    time.sleep(600) # Pour ne pas surcharger le serveur pronote
