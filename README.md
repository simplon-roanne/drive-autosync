# Drive AutoSync

Upload changes in your Google Drive folder every few minutes on Linux.
Displays a status icon ( gnome app indicator ) indicating whether it's up to date or uploading.

It's a very basic automation, intended for personnal use, around the great google drive cli program https://github.com/prasmussen/gdrive.

Tested on Ubuntu 18.04.

# Dependencies

- prasmussen/gdrive
- PyGObject 
- At the moment the program requires the Google Drive folder to be "~/GDrive" ( needs custom config file )

# Setup

```bash
git clone https://github.com/idmkr/drive-autosync
python setup.sh
chmod a+x drive-autosync.sh
./driveautosync.sh
```

# Todo

- Run as proper deamon
- Quit option on the App Indicator menu
- Config file ( ~/.drive-autosync )
- Detect Error status (eg: no update since 10 minutes)

# Contributing

Would be amazing and welcomed if you want to build a proper deamon program with me.