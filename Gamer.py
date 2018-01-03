from Devices.SonyXZ import SonyZX as Device
from Utils.Elements import Chess, PlayGround
from Utils.Logger import Logger

import cv2 as cv
from time import sleep
from os import path, remove


class Gamer(object):
    def __init__(self):
        self.device = Device()
        self.chess = Chess(path.join('Images', 'chess.png'))
        self.play_ground = PlayGround()
        self.logger = Logger('Log/')

    def __scan(self):
        pos = 0
        for i in range(500, 1000):
            res = []
            for j in range(len(self.play_ground.raw_png[i]) - 1):
                # if chess locates at screen center
                if self.chess.top_left[0] <= j <= self.chess.bottom_right[0]:
                    res.append(0)
                else:
                    prev_color = int(self.play_ground.raw_png[i][j])
                    next_color = int(self.play_ground.raw_png[i][j + 1])
                    diff_color = abs(prev_color - next_color)
                    if diff_color < 2:
                        diff_color = 0
                    res.append(diff_color)
            if sum(res) >= 10:
                cnt = 0
                for j in range(len(res)):
                    if res[j] > 0:
                        cnt += 1
                        pos += j
                pos //= cnt
                break
        return pos

    def __distance(self, x_dest: int):
        x_src_left = self.chess.top_left[0]
        x_src_right = self.chess.bottom_right[0]
        x_src = (x_src_right - x_src_left) // 2 + x_src_left
        x_diff = abs(x_dest - x_src)
        return x_diff

    def play(self):
        # get screen cap
        screencap_filename = self.device.get_screencap()
        # update raw png data
        self.play_ground.read_png(screencap_filename)
        self.chess.update_loc(self.play_ground)

        pos = self.__scan()
        dist = self.__distance(pos)

        # save data
        playground_img = self.play_ground.raw_png
        cv.rectangle(playground_img, self.chess.top_left, self.chess.bottom_right, 128, 3)
        cv.line(playground_img, (pos, 0), (pos, 1920), 0, 3)
        screencap_img = cv.imread(screencap_filename)
        self.logger.log(playground_img, screencap_img)

        # move
        self.device.press(self.device.coef * dist)

        # remove temp screen shot
        remove(screencap_filename)


def main():
    gamer = Gamer()
    gamer.logger.clear_step()
    for i in range(80):
        gamer.play()
        sleep(2)


if __name__ == '__main__':
    main()
