## What do this code ?
This script send you a sms on your phone when you get a new grade on pronote using a HTTP request to free mobile
I advise you to run on a serveur (a NAS for e.g.) else, you need to run it continualy on a laptop or other.
The sms looks like this :

**Vous avez recu une nouvelle note le [date] qui est de [note] en [matière] avec un coefficient de [coefficient].**
                     
**La moyenne de la classe est [moyenne de classe] et la meilleure note est [meilleure note]**

**Cette note fais passer votre moyenne a [votre moyenne]**

When you run the code, you will have a sms with your last mark, like a confirmation that the script is correctly running.

## Dependencies
This code use the librairy pronotepy.
You can install with : `pip install -U pronotepy`

You need also a Free mobile account and activate sms notifications in my options
Then, notice your id (sms_id in the program) and your password (sms_key in the program)

## The code

```python
#import libraries
import pronotepy
from pronotepy.ent import ac_orleans_tours # your ent
import time
import requests

#initialize the variables
last_grade = ''

# connect to pronote using the ENT
client = pronotepy.Client(
    'https://0000000a.index-education.net/pronote/eleve.html',
    username='username', # your id ENT !!!
    password="password", # your mdp
    ent=ac_orleans_tours) # your academie


def send_grade(message) :
    sms_id = 'sms_id' # id Free Mobile
    sms_key = 'sms_key' # password in sms notifications in my options
    res = requests.get(f'https://smsapi.free-mobile.fr/sendmsg?user={sms_id}&pass={sms_key}&msg={message}') # envoie
    print(f'le message {message} a été envoyé') # Confirmation

def check_new_grade(last_grade) : # check if they are a new grade
    grade = []
    for grade in client.current_period.grades:  # iterate over all the grades
        grade.append(f'''Vous avez recu une nouvelle note le {grade.date} qui est de {grade.grade}/{grade.out_of} en {grade.subject.name} avec un coefficient de {grade.coefficient}.
                     
La moyenne de la classe est {grade.average} et la meilleure note est {grade.max}

Cette note fais passer votre moyenne a {client.current_period.overall_average}''') 

        
    grade.sort(reverse=True) # sort by date
    if grade[0] != last_grade : # check if it's a new grade
        return grade[0]
    
    else :
        return False

while True :
    check = check_new_grade(last_grade)

    if check :
        last_grade = check
        send_grade(check)
    
    time.sleep(600) # To not surcharge the serveur
```
