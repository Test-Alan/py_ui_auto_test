import allure
from poium import PageElement, PageElements
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.log_conf import init_logger

logger = init_logger("log.txt")

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
            elem = WebDriverWait(context, self.time_out).until(EC.visibility_of_element_located(self.locator))
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
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象已访问" % ':'.join(self.locator))
            return self.get_element(context)

        else:
            # 截图
            # insert_img(context,  '-'.join(self.locator) + "对象未找到截图.png")
            allure.attach(context.get_screenshot_as_png(), name='-'.join(self.locator) + "对象未找到截图.png", attachment_type=AttachmentType.PNG)
            # 日志
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象未找到" % ':'.join(self.locator))
            return self.get_element(context)


class FindElements(PageElements):
    def get_element(self, context):
        try:
            elem = WebDriverWait(context, self.time_out).until(EC.visibility_of_all_elements_located(self.locator))
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
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象已访问" % ':'.join(self.locator))
            return self.get_element(context)

        else:
            # 截图
            # insert_img(context, '-'.join(self.locator) + "对象未找到截图.png")
            allure.attach(context.get_screenshot_as_png(), name='-'.join(self.locator) + "对象未找到截图.png", attachment_type=AttachmentType.PNG)
            # 日志
            logger.info(format(self.__class__.__name__) + "页面" + "%s对象未找到" % ':'.join(self.locator))
            return self.get_element(context)


