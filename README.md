# CESI - Escape No Game

Projet des �coles CESI, Serveur de message cod� en Python.
Contenant un serveur, recevant les messages. 
Et un client, envoyant des messages.

Le programme peut tourner en local suffit de changer l'ip par "localhost" ou "127.0.0.1"

J'ai �galement fait un programme pour transformer le Client.Py en Client.Exe pour �viter l'installation de Python. 

## Re-Build -> Version Exe

Pour installer le modulle cx_Freeze on fait la commande suivante :
```
pip install cx_Freeze --upgrade
```
Et pour generer le .exe il suffit de rentrer : 
```
python setup.py build
```

Et voil� !