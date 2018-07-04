# Drive AutoSync

Drive AutoSync sauvegarde votre dossier personnel ~/GDrive toutes les 2 minutes.
Une icône est alors affichée dans la barre haute de Ubuntu, indiquant si la sauvegarde est effectué ou en attente.

# Installation automatique

```bash
sudo apt-get update # installer les MAJs puis redémarrer le laptop.
cd
sudo apt install git
git clone https://github.com/simplon-roanne/drive-autosync
cd drive-autosync
sudo chmod a+x setup.sh
./setup.sh
# Contrôle clic sur le lien obtenu, se connecter avec son adresse et.simplon, copiez coller le code dans le terminal
```

# Installation manuelle

```bash

# Ajout du registre qui informera le système de l'existence du programme drive
sudo add-apt-repository ppa:twodopeshaggy/drive

# Mise à jour du système pour que le nouveau registre soit pris en compte
sudo apt-get update

# Installation du programme drive
sudo apt-get install drive

# Création du  dossier GDrive dans le dossier home
mkdir ~/GDrive

# Initialisation de Google Drive dans le dossier ~/GDrive 
# !!Attention!! à cette étape : si vous avez une erreur c'est peut-être parce que
# vous n'avez pas le bon programme drive. Me l'indiquer dans ce cas (Gael)
drive init ~/GDrive
#Faire un ctrl+clic sur l'URL proposé dans le Terminal
#Vous connecter avec votre compte et.simplon-roanne et copier-coller le lien obtenu dans le Terminal


# Maintenant il faut installer les dépendances du projet
# Cette première dépendance contient la librairie python "appindicator3", installé via "apt"
sudo apt install gir1.2-appindicator3-0.1
# Cette dépendance contient la librairie python-daemon, mais cette fois installée via "pip"
sudo apt install python-pip
sudo pip install python-daemon

#Installation de git
sudo apt install git

# Enfin !! On peut télécharger le programme drive-autosync
git clone https://github.com/simplon-roanne/drive-autosync


```


# Test de la commande
``` 
cd ~/drive-autosync
python drive-autosync.py
```
Si la commande fonctionne, une icone apparaît en haut et la commande tourne en boucle avec le message "Resolving... Everything up-to date".

# Configurer le programme au démarrage
- Taper "Démarrage" ou "Startup" puis cliquer sur "Applications au démarrage" ou l'équivalent anglais.
- Créer une nouvelle entrée avec cette commande, que vous devez personnaliser : ```python /home/MONDOSSIER/drive-autosync/drive-autosync.py```

# Contribuer
Roadmap pour un outil complet :
- script d'installation avec configuration du chemin du dossier Google Drive
- icône plus jolie
- notification en cas d'erreur
- fichier de log proprement stocké
- bouton pour quitter depuis l'icone
- tests automatisés  

# Aller plus loin
- [Cours Python](https://openclassrooms.com/courses/apprenez-a-programmer-en-python)
- [Exemple de scripts python](https://fr.wikibooks.org/wiki/Programmation_Python/Exemples_de_scripts)
- [Google Drive CLI ( Command Line Interface )](https://github.com/prasmussen/gdrive)
- [Commande linux apt](https://doc.ubuntu-fr.org/apt)
- [Commande linux pip](https://fr.wikipedia.org/wiki/Pip_(gestionnaire_de_paquets))
