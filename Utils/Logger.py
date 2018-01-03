from os import path, mkdir
from shutil import rmtree
import cv2 as cv


class Logger(object):
    def __init__(self, log_path: str()):
        self.log_path = log_path
        self.step_filename = path.join(self.log_path, 'step')
        self.step = self.__get_step()

    def __get_step(self):
        step = 0
        if path.isfile(self.step_filename):
            with open(self.step_filename, 'r') as file:
                step = int(file.read())
        else:
            with open(self.step_filename, 'w') as file:
                file.write(str(0))
                step = 0
        return step

    def __del__(self):
        with open(self.step_filename, 'w') as file:
            file.write(str(self.step))

    def log(self, processed_img, screencap_img=None):
        pimg_filename = path.join(self.log_path, str(self.step) + '.png')
        cv.imwrite(pimg_filename, processed_img)
        if screencap_img is not None:
            simg_filename = path.join(self.log_path, 'screen_' + str(self.step) + '.png')
            cv.imwrite(simg_filename, screencap_img)
        self.step += 1

    def clear_step(self):
        self.step = 0
        with open(self.step_filename, 'w') as file:
            file.write(str(self.step))
        if path.isdir(self.log_path):
            rmtree(self.log_path)
        mkdir(self.log_path)
