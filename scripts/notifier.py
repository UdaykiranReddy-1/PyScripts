"""
Notifier module

This module provides functions to create desktop notifications on Windows.
It allows you to schedule reminders that are delivered after a delay via a detached subprocess.
"""

import time
import sys
import subprocess
import os


def send_notification(title: str, message: str, duration: int = 10) -> None:
    """
    Send a desktop notification on Windows.

    Args:
        title (str): Title of the notification
        message (str): Message body of the notification
        duration (int): Duration in seconds for which the notification should be shown (default: 10)
    """
    from win10toast import ToastNotifier

    toaster = ToastNotifier()
    toaster.show_toast(
        title=title,
        msg=message,
        duration=duration,
        threaded=True
    )

    # Wait for notification to be shown
    while toaster.notification_active():
        time.sleep(0.005)

def _notify_background(header: str, message: str, minutes: float) -> None:
    """
    Internal function to handle the reminder timing and notification.
    Called only when this script is run as a subprocess.
    
    Args:
        header (str): Header/title for the reminder
        message (str): Detailed message for the reminder
        minutes (float): Number of minutes to wait before showing the reminder
    """
    print(f"✅ Reminder set for {minutes} minutes from now")

    seconds = minutes * 60
    time.sleep(seconds)
    send_notification(title=header, message=message)

def create_reminder(header: str, message: str, minutes: float) -> None:
    """
    Create a reminder that will notify after the specified number of minutes.
    This function spawns a separate Python subprocess to run in the background.

    Args:
        header (str): Header/title for the reminder
        message (str): Detailed message for the reminder
        minutes (float): Number of minutes to wait before showing the reminder
    """
    script_path = os.path.abspath(__file__)
    subprocess.Popen(
        [sys.executable, script_path, header, message, str(minutes)],
        creationflags=subprocess.CREATE_NO_WINDOW  # Launches in a new window without blocking
    )

if __name__ == "__main__":
    # If run as a subprocess with arguments, perform the reminder
    if len(sys.argv) != 4:
        print("Usage: notifier.py <title> <message> <minutes>")
        sys.exit(1)

    title = sys.argv[1]
    message = sys.argv[2]
    minutes = float(sys.argv[3])
    _notify_background(title, message, minutes)
