import notify2
import os
import pyudev
from os import getcwd


icon = os.path.join(getcwd(),"resources", "mouse.png")

notify2.init('USB Project')

startupNotification = notify2.Notification("USB Listener",
                         "Listening for USB device changes...",
                         icon   
                        )
startupNotification.show()

deviceAddedNotification = notify2.Notification("USB Listener",
                         "Setting DPI...",
                         icon   
                        )


context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        deviceAddedNotification.show()
