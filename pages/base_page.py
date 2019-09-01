from poium import Page


class BasePage(Page):

    # 获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self):
        x1 = self.get_size()[0] * 0.9
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x2, y1)

    # 向右滑动
    def swipe_right(self):
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] * 0.9
        self.driver.swipe(x1, y1, x2, y1)

    # 向上滑动
    def swipe_up(self):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] * 0.9
        y2 = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y2)

    # 向下滑动
    def swipe_down(self):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y2 = self.get_size()[1] * 0.9
        self.driver.swipe(x1, y1, x1, y2)

    # 滑动的方向
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'right':
            self.swipe_right()
        else:
            self.swipe_left()