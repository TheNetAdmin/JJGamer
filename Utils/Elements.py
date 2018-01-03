import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class PlayGround(object):
    def __init__(self):
        self.raw_png = None

    def read_png(self, filename):
        self.raw_png = cv.imread(filename, 0)


class Chess(object):
    def __init__(self, filename):
        self.raw_png = None
        self.top_left = None
        self.bottom_right = None
        self.width = 0
        self.height = 0
        self.read_png(filename)

    def read_png(self, filename):
        self.raw_png = cv.imread(filename, 0)
        self.width, self.height = self.raw_png.shape[1::-1]

    def get_img(self):
        return self.raw_png

    def update_loc(self, pg: PlayGround):
        result = cv.matchTemplate(pg.raw_png, self.raw_png, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        self.top_left = max_loc
        self.bottom_right = (self.top_left[0] + self.width, self.top_left[1] + self.height)
