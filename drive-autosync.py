import os
import time
import signal
import daemon 
import threading
import subprocess
import webbrowser

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

APPINDICATOR_ID = 'googledrive'

class DriveAutoSync(object):
    id = ""
    indicator = None
    syncCount = 0
    rootPath = ""

    def __init__(self, id):
        self.id = id
        self.rootPath = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

        self.startDriveSync()

        notify.init(self.id)

    def startDriveSync(self):
        self.setIndicator("loading")

        thread = threading.Thread(target=runInThread, args=(self.endDriveSync, (['drive push -no-prompt'])))
        thread.start()

    def endDriveSync(self):
        #notify.uninit()
        #gtk.main_quit()
        self.setIndicator("valid")
        self.syncCount += 1

        if self.syncCount % 10:
            open( os.getenv('HOME') + "/drive-autosync.log", 'w').close()

        time.sleep(120)

        self.startDriveSync()
    
    def setIndicator(self, status):
        iconDir = self.rootPath + '/icons/'
        iconName = "drive-"+ status +'.svg'
        iconPath = iconDir  + "/" + iconName 

        if self.indicator is None:
            self.indicator = appindicator.Indicator.new(
                self.id, 
                iconPath, 
                appindicator.IndicatorCategory.APPLICATION_STATUS
            )
            self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        else:
            #self.indicator.set_icon_theme_path( iconDir + "./"*(self.syncCount % 2) )
            self.indicator.set_icon_full(iconPath, 'Google Drive Autosync')
        
        self.indicator.set_menu(self.build_menu())

    def build_menu(self):
        menu = gtk.Menu()
        item_info = gtk.MenuItem('Info')
        item_info.connect('activate', self.openRepo)
        menu.append(item_info)
        menu.show_all()
        return menu

    def openRepo(self, _):
        webbrowser.open("https://doc.ubuntu-fr.org/google_drive#drive")


def runInThread(onExit, popenArgs):
    proc = subprocess.Popen(shell=True, cwd=os.path.expanduser("~/GDrive"), *popenArgs)
    proc.wait()
    onExit()
    return

def main():
    #with daemon.DaemonContext():
    sync = DriveAutoSync(APPINDICATOR_ID)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
    gtk.main()