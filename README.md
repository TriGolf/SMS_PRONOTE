## Que fait ce code ?
Ce script vous envoie un sms quand vous obtenez une nouvelle note pronote de cette manière :

**Vous avez recu une nouvelle note le [date] qui est de [note] en [matière] avec un coefficient de [coefficient].**
                     
**La moyenne de la classe est [moyenne de classe] et la meilleure note est [meilleure note]**

**Cette note fais passer votre moyenne a [votre moyenne]**

Lors du lancement, vous recevrez le message "Programme lancé"

## Dépendances

Ce code utilise pronotepy
Installation : `pip install -U pronotepy`

Vous devez aussi avoir un compte free mobile (actuellement le seul compatible)
Vous devrez activer l'api sms et noter votre identifiant et votre token

## Utilisation du programme

Ce script dois rester continuellement en cours d'exécution pour vérifier vos notes.
Si vous en avez un, je vous recommande d'utiliser un serveur ou un raspberry pi
