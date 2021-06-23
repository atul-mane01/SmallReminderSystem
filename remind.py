import time

from plyer import notification

if __name__=="__main__":
    notification.notify(
        title="Wake Up Dear",
        message="Today We have Complete this Task and we will finish this task ",
        app_name="Remiinder",
        app_icon="/remind.ico",
        ticker="WakeUp",
        toast=False,
        timeout =3
    )
    time.sleep(6)

