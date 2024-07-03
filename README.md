## Que fait ce code ?
Ce script vous envoie un sms quand vous obtenez une nouvelle note pronote de cette manière :

**Vous avez recu une nouvelle note en {Matière} qui est de {Note}/{Max de points (généralement 20)} avec un coefficient de {coef}.**
                     
**La moyenne de la classe est {moyenne de classee}/{Max de points} et la meilleure note est {meilleure note}/{Max de points}**

**Cette note fait passer votre moyenne générale à {moyenne générale}**

Lors du lancement, vous recevrez le message `Programme lancé`, ce qui confirmera que le programme marche correctement

## Dépendances

Ce code utilise pronotepy
Installation : `pip install -U pronotepy`

Vous devez aussi avoir un compte free mobile (actuellement le seul compatible mais libre à vous de l'adapter avec des mails)
Vous devrez activer l'api sms et noter votre identifiant et votre token

## Utilisation du programme

Ce script dois rester continuellement en cours d'exécution pour vérifier vos notes.
Si vous en avez un, je vous recommande d'utiliser un serveur ou un raspberry pi
