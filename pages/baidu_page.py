from pages.base_page import BasePage, FindElement, FindElements



class BaiduPage(BasePage):
    search_input = FindElement(id_="kw", describe="搜索框")
    search_button = FindElement(id_="su", describe="搜索按钮")
    settings = FindElement(link_text="设置", describe="设置下拉框")
    search_setting = FindElement(css=".setpref", describe="搜索设置选项")
    save_setting = FindElement(css=".prefpanelgo", describe="保存设置")    
    # 定位一组元素
    search_result = FindElements(xpath="//div/h3/a", describe="搜索结果")
