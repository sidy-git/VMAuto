# -*- coding: utf-8 -*-
# This is a sample Python script.
import sys
import auto_model
import manu_model
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) == 1:
        manu_model.manu_run()
    elif len(sys.argv) == 2:
        auto_model.auto_run(sys.argv[1])
    else:
        print("argument error!")
