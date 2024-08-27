# file -- submit.py --

def send_notification(notification_title, notification_message):
    from notifypy import Notify

    notification = Notify()
    notification.title = notification_title
    notification.message = notification_message
    notification.send()