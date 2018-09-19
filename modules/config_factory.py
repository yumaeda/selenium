# -*- coding: utf-8 -*-
"""設定情報を作成するクラス"""

import io
import ConfigParser

class ConfigFactory():
    """ConfigFactoryクラス"""
    def __init__(self, config_file):
        """ConfigFactoryのコンストラクタ"""
        self.config_file = config_file

    def create(self):
        """設定を取得する"""
        with open(self.config_file) as file_pointer:
            config_contents = file_pointer.read()

        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(config_contents))
        return config
