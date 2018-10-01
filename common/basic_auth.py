"""基本認証に必要なクレデンシャルを送信するクラス"""

class BasicAuth():
    """BasicAuthクラス"""
    def __init__(self, driver, hosts, is_ssl=True):
        """BasicAuthのコンストラクタ

        :rtype: selenium.webdriver driver
        :rtype: array hosts
        :rtype: boolean is_ssl
        """
        self.driver = driver
        self.hosts = hosts
        self.is_ssl = is_ssl
        self.login = ''
        self.pwd = ''

    def send_credentials(self, login, pwd):
        """認証が必要なホストにユーザー名とパスワード付きのURLでアクセスする

        :rtype: string login
        :rtype: string pwd
        """
        protocol = 'https://' if self.is_ssl else 'http://'
        for host in self.hosts:
            self.driver.get(protocol + login + ':' + pwd + '@' + host + '/')
