from plyer import notification
import time

if __name__=='__main__':
    while True:
        notification.notify(
            title="*** Take rest ***",message="Taking rest reduces stress, improves mood and facilitates better metabolism",app_icon="D:/Python Project/notification-icon.ico",timeout=5
        )
        time.sleep(20)