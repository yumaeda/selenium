# -*- coding: utf-8 -*-
"""設定情報を作成するクラス"""

import configparser

class ConfigFactory():
    """ConfigFactoryクラス"""
    def __init__(self, config_file):
        """ConfigFactoryのコンストラクタ"""
        self.config_file = config_file

    def create(self):
        """設定を取得する"""
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_file(open(self.config_file))
        return config
