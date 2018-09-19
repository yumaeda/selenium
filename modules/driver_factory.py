# -*- coding: utf-8 -*-
"""Chromeドライバーを作成するクラス"""

from selenium import webdriver
import selenium.webdriver.chrome.service as chrome_service

# 定数の定義
DRIVER_LOAD_TIME = 3

class DriverFactory():
    """DriverFactoryクラス"""
    def __init__(self):
        """DriverFactoryのコンストラクタ"""
        self.driver_svc = chrome_service.Service('/usr/local/bin/chromedriver')
        self.driver_svc.start()

    def create(self):
        """ドライバを取得する"""
        capabilities = {
            'chrome.binary': '/Applications/Google Chrome Canary.app/'
                             'Contents/MacOS/Google Chrome Canary',
            'chromeOptions': {'args': ['--headless', '--no-sandbox', '--disable-notifications']}
        }
        chrome_driver = webdriver.Remote(self.driver_svc.service_url, capabilities)
        chrome_driver.implicitly_wait(DRIVER_LOAD_TIME)
        return chrome_driver
