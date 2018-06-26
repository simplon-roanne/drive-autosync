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
git clone https://github.com/simplon-roanne/drive-autosync
```

- Configure Google Drive in your Home Directory
```
drive init ~/GDrive
```
- Run program at startup
- Change frequency


# Usage
``` 
python drive-autosync.py
```

# Contributing

Would be amazing and welcomed if you want to build a proper deamon program with me.