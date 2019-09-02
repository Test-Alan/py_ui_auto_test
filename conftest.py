import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "report")


############################

# 配置驱动类型(chrome/firefox/chrome-headless/firefox-headless/app)。
driver_type = "chrome"

# 配置运行的 URL
url = "https://www.baidu.com"

# 失败重跑次数
rerun = "3"

# 运行测试用例的目录或文件
cases_path = "./tests/"

# appium Capabilities
caps = {
    "platformName": "android",
    "deviceName": "mumu",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "autoGrantPermissions": True,
    "noReset": True,

}

############################


# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    global url
    return url


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def driver():
    """
    全局定义浏览器驱动
    :return:
    """
    global dr

    if driver_type == "chrome":
        # 本地chrome浏览器
        dr = webdriver.Chrome()
        dr.maximize_window()

    elif driver_type == "firefox":
        # 本地firefox浏览器
        dr = webdriver.Firefox()
        dr.maximize_window()

    elif driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        dr = webdriver.Chrome(options=chrome_options)

    elif driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        dr = webdriver.Firefox(firefox_options=firefox_options)

    elif driver_type == "grid":
        # 通过远程节点运行
        dr = Remote(command_executor='http://10.2.16.182:4444/wd/hub',
                        desired_capabilities={
                            "browserName": "chrome",
                        })
        dr.maximize_window()
    elif driver_type == "app":
        dr = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    else:
        raise NameError("driver驱动类型定义错误！")

    return dr


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def driver_close():
    yield dr
    dr.quit()
    time.sleep(2)
    print("test end!")



