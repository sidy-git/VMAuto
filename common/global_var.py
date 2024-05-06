# -*- coding: utf-8 -*-
import configparser


class GlobalVar:
    file = "output/global_var.ini"
    default_session = "global"
    config = configparser.ConfigParser()

    @staticmethod
    def add(key, value):
        if not GlobalVar.config.has_section(GlobalVar.default_session):
            GlobalVar.config.add_section(GlobalVar.default_session)
        temp_value = value.replace(" ", "").replace("\r", "").replace("\n", "")
        GlobalVar.config.set(GlobalVar.default_session, key, temp_value)
        GlobalVar.config.write(open(GlobalVar.file, "w"))

    @staticmethod
    def get(key):
        GlobalVar.config.read(GlobalVar.file, encoding="utf-8")
        if GlobalVar.config.has_option(GlobalVar.default_session, key):
            temp = str(GlobalVar.config.get(GlobalVar.default_session, key))
            return temp
        else:
            return None

