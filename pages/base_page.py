from time import sleep
import allure

from poium import Page, PageElement, PageElements
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.log_conf import init_logger

logger = init_logger("log.txt")


class BasePage(Page):

    # 获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] * 0.9
                y1 = self.get_size()[1] / 2
                x2 = self.get_size()[0] / 10
                self.driver.swipe(x1, y1, x2, y1)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 向右滑动
    def swipe_right(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] / 10
                y1 = self.get_size()[1] / 2
                x2 = self.get_size()[0] * 0.9
                self.driver.swipe(x1, y1, x2, y1)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 向上滑动
    def swipe_up(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] / 2
                y1 = self.get_size()[1] * 0.9
                y2 = self.get_size()[1] / 10
                self.driver.swipe(x1, y1, x1, y2)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 向下滑动
    def swipe_down(self, count=1, time=0.5):
        try:
            for i in range(count):
                x1 = self.get_size()[0] / 2
                y1 = self.get_size()[1] / 10
                y2 = self.get_size()[1] * 0.9
                self.driver.swipe(x1, y1, x1, y2)
                sleep(time)
        except Exception as e:
            logger.info(e)

    # 滑动的方向
    def swipe_on(self, direction, count, time):
        try:
            if direction == 'up':
                self.swipe_up(count, time)
            elif direction == 'down':
                self.swipe_down(count, time)
            elif direction == 'right':
                self.swipe_right(count, time)
            else:
                self.swipe_left(count, time)
        except Exception as e:
            logger.info(e)

    # 截图
    # def insert_img(driver, file_name):
    #     now_time = time.strftime("%Y_%m_%d")  # 当前时间
    #     scre_dir = os.path.join(data_dir, "screenshots/")
    #     path = scre_dir + now_time
    #     if not os.path.exists(path):
    #         os.mkdir(path)
    #     image_dir = os.path.join(scre_dir, now_time, file_name)
    #     print(image_dir)
    #     driver.get_screenshot_as_file(image_dir)





class FindElement(PageElement):
    # 黑名单，用来处理一些不定时的弹框。
    black_list = []
    # 限制查找次数
    count = 0

    def get_element(self, context):
        try:
            elem = WebDriverWait(context, self.time_out).until(EC.visibility_of_element_located(self.locator))
        except:
            if self.count > 2:
                raise ("已经超过最大查找次数!")
            self.count += 1
            # 判断黑名单元素是否出现
            for black in self.black_list:
                black_elements = context.find_elements(*black)
                if len(black_elements) >= 1:
                    black_elements[0].click()
                    logger.info("黑名单{}元素出现，已点击!".format(black))
                    return self.get_element(context)
                else:
                    logger.info("黑名单{}元素未出现!".format(black))
            else:
                return None

        else:
            try:
                style_red = 'arguments[0].style.border="2px solid red"'
                context.execute_script(style_red, elem)
            except BaseException:
                return elem
            return elem

    def find(self, context) -> WebElement:
        element = self.get_element(context)
        if element is not None:
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象已访问" % ':'.join(self.locator))
            return element

        else:
            # 截图
            # insert_img(context,  '-'.join(self.locator) + "对象未找到截图.png")
            allure.attach(context.get_screenshot_as_png(), name='-'.join(self.locator) + "对象未找到截图.png", attachment_type=AttachmentType.PNG)
            # 日志
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象未找到" % ':'.join(self.locator))
            return element


class FindElements(PageElements):

    def find(self, context):
        if self.get_element(context) is not None:
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象已访问" % ':'.join(self.locator))
            return context.find_elements(*self.locator)

        else:
            # 截图
            # insert_img(context, '-'.join(self.locator) + "对象未找到截图.png")
            allure.attach(context.get_screenshot_as_png(), name='-'.join(self.locator) + "对象未找到截图.png", attachment_type=AttachmentType.PNG)
            # 日志
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象未找到" % ':'.join(self.locator))
            return []


