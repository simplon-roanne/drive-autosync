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

# Cette dépendance contient la librairie python-daemon, mais cette fois installée via "pip"
sudo apt install python-pip
sudo pip install python-daemon

# Fichier de configuration pour ignorer certains dossiers trop lourds
cp .driveignore ~/GDrive/
