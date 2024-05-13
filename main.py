# -*- coding: utf-8 -*-
# This is a sample Python script.
import os
import sys
import auto_model
import manu_model
from common.common_api import CommonApi

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) == 1:
        manu_model.manu_run()
    elif len(sys.argv) == 2:
        os_type = CommonApi.get_os_type()
        path_separator = '/'
        if os_type == 'win':
            path_separator = '\\'
        file_dir = os.path.dirname(os.path.abspath(__file__))

        auto_model.auto_run(file_dir + path_separator + "config" + path_separator + os_type + path_separator + sys.argv[1])
    else:
        print("argument error!")
