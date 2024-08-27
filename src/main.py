# Rattlesnake
# Sends notifcations to the desktop.
# calicojack1720
# Created: 8/26/24
# Updated: 8/26/24

from notifypy import Notify

notification_title = input("Enter the notification title: ")
notification_message = input("Enter the notification message: ")

notification = Notify()
notification.title = notification_title
notification.message = notification_message
notification.send()