# Rattlesnake
# Sends notifcations to the desktop.
# calicojack1720
# Created: 8/26/24
# Updated: 8/27/24

# file -- main.py --

from submit import send_notification

notification_title = input("Enter the notification title: ")
notification_message = input("Enter the notification message: ")

send_notification(notification_title, notification_message)