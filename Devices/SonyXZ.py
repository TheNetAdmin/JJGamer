from Devices.BaseDevice import BaseDevice


class SonyZX(BaseDevice):
    def __init__(self):
        self.width = 1080
        self.height = 1920
        self.coef = 1.575
        BaseDevice.__init__(self, width=self.width, height=self.height)
