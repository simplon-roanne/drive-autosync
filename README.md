# Drive AutoSync

Upload changes in your Google Drive folder every few minutes on Linux.
Displays a status icon ( gnome app indicator ) indicating whether it's up to date or uploading.

It's a very basic automation, intended for personnal use, around the great google drive cli program https://github.com/prasmussen/gdrive.

Tested on Ubuntu 18.04.

# Dependencies

- prasmussen/gdrive
- PyGObject 
- daemon ( module python )
- At the moment the program requires the Google Drive folder to be "~/GDrive" ( needs custom config file )

# Setup

You need to install prasmussen/gdrive, and PyGObject.

```bash
sudo add-apt-repository ppa:twodopeshaggy/drive
sudo apt-get update
sudo apt-get install drive
drive init ~/GDrive
sudo apt install gir1.2-appindicator3-0.1
sudo pip install python-daemon
git clone https://github.com/simplon-roanne/drive-autosync
drive init ~/GDrive
```


# Usage
``` 
python drive-autosync.py
```

# Run at startup

 Run program at startup : https://askubuntu.com/questions/48321/how-do-i-start-applications-automatically-on-login

Run this command at startup : python /home/MONDOSSIER/drive-autosync/drive-autosync.py


# Contributing

Would be amazing and welcomed if you want to build a proper deamon program with me.