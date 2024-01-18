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
