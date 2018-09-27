"""Htmlページ関連の処理を提供する"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 定数を定義
WAIT_TIME = 3

class Page():
    """Pageクラス"""
    def __init__(self, driver):
        """Pageクラスのコンストラクタ"""
        self.driver = driver

    def click_with_key_down(self, element, key):
        """指定されたキーを押した状態で指定された要素をクリックする

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        :rtype: string key
        """
        actions = ActionChains(self.driver)
        actions.key_down(key).click(element).key_up(key).perform()

    def scroll_to_element(self, id_or_class):
        """IDもしくはクラスで指定された要素までスクロールする

        :rtype: string id_or_class
        """
        element = self.get_element_by_id(id_or_class)
        if element is None:
            element = self.get_element_by_class_name(id_or_class)
        if element is None:
            print('[' + id_or_class + ']にスクロールする事ができませんでした。')
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        return element

    def focus_on_tab(self, index=-1):
        """指定のタブにフォーカスを当てる

        indexが指定されていない場合は、最後のタブにフォーカスを当てる

        :rtype: number index
        """
        tab_index = index
        if index == -1:
            tab_index = len(self.driver.window_handles) - 1

        target_tab = self.driver.window_handles[tab_index]
        self.driver.switch_to.window(target_tab)

    def force_click(self, element):
        """JavaScript経由で指定の要素をクリックする。

        element.is_displayed()がFalseの要素でもクリックできる。
        """
        self.driver.execute_script('$(arguments[0]).click();', element)

    def get_element(self, selected_by, value):
        """指定された要素を取得する。

        ロードが終わるまで待ってから、要素を取得する。

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        try:
            is_located = EC.presence_of_element_located((selected_by, value))
            return WebDriverWait(self.driver, WAIT_TIME).until(is_located)
        except TimeoutException:
            return None

    def get_elements(self, selected_by, value):
        """指定された要素を全て取得する。

        ロードが終わるまで待ってから、要素を取得する。

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        try:
            is_located = EC.presence_of_all_elements_located((selected_by, value))
            return WebDriverWait(self.driver, WAIT_TIME).until(is_located)
        except TimeoutException:
            return None

    def get_element_by_id(self, element_id):
        """指定されたIDの要素を取得する。

        ロードが終わるまで待ってから、要素を取得する。

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        return self.get_element(By.ID, element_id)

    def get_element_by_class_name(self, class_name):
        """指定されたクラスの要素を取得する。

        ロードが終わるまで待ってから、要素を取得する。

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        return self.get_element(By.CLASS_NAME, class_name)

    def get_elements_by_class_name(self, class_name):
        """指定されたクラスの要素を全て取得する。

        ロードが終わるまで待ってから、要素を取得する。

        :rtype: selenium.webdriver.remote.webelement.WebElement element
        """
        return self.get_elements(By.CLASS_NAME, class_name)
