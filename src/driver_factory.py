# -*- coding: utf-8 -*-
"""Docker用のChromeドライバーを作成するクラス"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverFactory():
    """Docker用のChromeドライバーファクトリー"""
    def __init__(self):
        """DockerDriverFactoryのコンストラクタ"""
        self.cmd_executor = 'http://selenium-hub:4444/wd/hub'
        self.capabilities = DesiredCapabilities.CHROME

    def set_capabilities(self, capabilities):
        """ブラウザのCapabilitiesをセットする"""
        self.capabilities = capabilities

    def create(self):
        """ドライバを取得する"""
        return webdriver.Remote(
            command_executor=self.cmd_executor,
            desired_capabilities=self.capabilities)
