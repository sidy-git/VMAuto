# -*- coding: utf-8 -*-
import configparser
import os.path


class GlobalVar:
    file = "output/global_var.ini"
    default_session = "global"
    init_flag = False

    config = configparser.ConfigParser()

    @staticmethod
    def init():
        if not GlobalVar.init_flag:
            # print("init GlobalVar ini file success")
            GlobalVar.config.read(GlobalVar.file)
            GlobalVar.init_flag = True

    @staticmethod
    def close():
        GlobalVar.config.write(open(GlobalVar.file, 'w'))
        GlobalVar.init_flag = False

    @staticmethod
    def add(key, value):
        GlobalVar.init()
        if not GlobalVar.config.has_section(GlobalVar.default_session):
            GlobalVar.config.add_section(GlobalVar.default_session)
        if type(value) != str:
            value = str(value)
        temp_value = value.replace(" ", "").replace("\r", "").replace("\n", "").replace("%", "%%")
        GlobalVar.config.set(GlobalVar.default_session, key, temp_value)
        GlobalVar.config.write(open(GlobalVar.file, "w"))

    @staticmethod
    def get(key):
        GlobalVar.init()
        if GlobalVar.config.has_option(GlobalVar.default_session, key):
            temp = str(GlobalVar.config.get(GlobalVar.default_session, key))
            return temp
        else:
            return None

    @staticmethod
    def clear_all(key):
        GlobalVar.init()
        if GlobalVar.config.has_option(GlobalVar.default_session, key):
            GlobalVar.config.remove_option(GlobalVar.default_session, key)
            # print("remove " + key)
        index = 1
        batch_key = key + str(index)
        while GlobalVar.config.has_option(GlobalVar.default_session, batch_key):
            GlobalVar.config.remove_option(GlobalVar.default_session, batch_key)
            index += 1
            batch_key = key + str(index)
        GlobalVar.close()

    @staticmethod
    def add_more(key, value):
        GlobalVar.init()
        index = 1
        batch_key = key + str(index)
        while GlobalVar.config.has_option(GlobalVar.default_session, batch_key):
            index += 1
            batch_key = key + str(index)
        GlobalVar.add(batch_key, value)


# print(GlobalVar.get("context1"))
# GlobalVar.clear_all("context")
# print(GlobalVar.get("context1"))
# GlobalVar.add_more("context", "context1")
# GlobalVar.add_more("context", "context2")
# GlobalVar.add_more("context", "context3")
# GlobalVar.add_more("context", "context4")
# GlobalVar.add_more("context", "context5")
