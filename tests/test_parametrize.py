import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath

from pages.baidu_page import BaiduPage

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)



def get_data(file_path):
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


@pytest.mark.parametrize(
    "name, search_key",
    get_data(base_path + "/data/test_data/data_file.json")
    )
def test_baidu_search(name, search_key, driver, base_url):
    page = BaiduPage(driver)
    page.get(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert driver.title == search_key+"_百度搜索"