# Rattlesnake
# Sends notifcations to the desktop.
# calicojack1720
# Created: 8/26/24
# Updated: 8/26/24

from notifypy import Notify

notification = Notify()
notification.title = "Test"
notification.message = "I am testing notifypy"
notification.send()