import logging
import logging.handlers
import time
import os
import allure
from poium import PageElement, PageElements
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_dir = BASE_DIR + '/data/'

# 日志管理
def init_logger(file_name):
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")   # 当前时间
    log_file_name = now_time + file_name            # 使用当前时间当做log日志的文件名
    log_file = os.path.join(data_dir, "log/", log_file_name)
    dir_path = os.path.dirname(log_file)
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except Exception:
        pass

    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=20 * 1024 * 1024, backupCount=10, encoding='utf-8')
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger_instance = logging.getLogger('logs')
    logger_instance.addHandler(handler)
    logger_instance.setLevel(logging.DEBUG)
    return logger_instance

loggerr = init_logger("log.txt")

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
    def get_element(self, context):
        try:
            elem = WebDriverWait(context, self.time_out).until(EC.presence_of_element_located(self.locator))
        except:
            return None

        else:
            try:
                style_red = 'arguments[0].style.border="2px solid red"'
                context.execute_script(style_red, elem)
            except BaseException:
                return elem
            return elem

    def find(self, context):
        if self.get_element(context) is not None:
            loggerr.info(format(self.__class__.__name__) + "页面" + "%s对象已访问" % ':'.join(self.locator))
            return self.get_element(context)

        else:
            # 截图
            # insert_img(context,  '-'.join(self.locator) + "对象未找到截图.png")
            allure.attach(context.get_screenshot_as_png(), name='-'.join(self.locator) + "对象未找到截图.png", attachment_type=AttachmentType.PNG)
            # 日志
            loggerr.info(format(self.__class__.__name__) + "页面" + "%s对象未找到" % ':'.join(self.locator))
            return self.get_element(context)


class FindElements(PageElements):
    def get_element(self, context):
        try:
            elem = WebDriverWait(context, self.time_out).until(EC.presence_of_all_elements_located(self.locator))
        except:
            return None

        else:
            try:
                style_red = 'arguments[0].style.border="2px solid red"'
                context.execute_script(style_red, elem)
            except BaseException:
                return elem
            return elem

    def find(self, context):
        if self.get_element(context) is not None:
            loggerr.info(format(self.__class__.__name__) + "页面" + "%s对象已访问" % ':'.join(self.locator))
            return self.get_element(context)

        else:
            # 截图
            # insert_img(context, '-'.join(self.locator) + "对象未找到截图.png")
            allure.attach(context.get_screenshot_as_png(), name='-'.join(self.locator) + "对象未找到截图.png", attachment_type=AttachmentType.PNG)
            # 日志
            loggerr.info(format(self.__class__.__name__) + "页面" + "%s对象未找到" % ':'.join(self.locator))
            return self.get_element(context)


