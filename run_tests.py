# coding=utf-8
import os
import time
import pytest
import click
from conftest import REPORT_DIR
from conftest import cases_path, rerun
from utils.logger import logger


'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python3 run_tests.py  (回归模式，生成HTML报告)
  > python3 run_tests.py -m debug  (调试模式)
'''


def init_env(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(os.path.join(REPORT_DIR, now_time))


@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        init_env(now_time)

        html_report = os.path.join(REPORT_DIR, now_time, "html")
        xml_report = os.path.join(REPORT_DIR, now_time, "xml")
        pytest.main(["-s", "-v",
                     "--alluredir="+xml_report,
                     cases_path,
                     "--reruns", rerun])
        allure_report = "allure generate {xml} -o {html}".format(xml=xml_report, html=html_report)
        logger.info(allure_report)
        os.popen(allure_report)
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
