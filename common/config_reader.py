# -*- coding: utf-8 -*-
import configparser
import os.path

from common.common_api import CommonApi
from common.global_var import GlobalVar


class ConfigReader:
    init_flag = False

    config = configparser.ConfigParser()

    @staticmethod
    def init(file):
        if not ConfigReader.init_flag:
            print("init GlobalVar ini file success, cfg= " + file)
            ConfigReader.config.read(file, encoding="utf-8")
            ConfigReader.init_flag = True

    @staticmethod
    def get(section, key):
        if not ConfigReader.init_flag:
            cfg_file = GlobalVar.get("config")
            ConfigReader.init(cfg_file)
        if ConfigReader.config.has_option(section, key):
            temp = str(ConfigReader.config.get(section, key))
            return temp
        else:
            # 根据操作系统类型组装section前缀
            section = CommonApi.get_os_type() + "_" + section
            if ConfigReader.config.has_option(section, key):
                temp = str(ConfigReader.config.get(section, key))
                return temp
            else:
                return None

    @staticmethod
    def get_options(section):
        if not ConfigReader.init_flag:
            print("CongigReader has not been init")
            return None
        return ConfigReader.config.options(section)