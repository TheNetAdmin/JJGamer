from subprocess import run


class BaseDevice(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screencap_name = 'screen.png'

    def press(self, milli_sec):
        press_time = int(milli_sec)
        run('adb shell input touchscreen swipe 170 187 170 187 ' + str(press_time), shell=True)

    def get_screencap(self):
        run('adb exec-out screencap -p > ' + self.screencap_name, shell=True)
        return self.screencap_name
