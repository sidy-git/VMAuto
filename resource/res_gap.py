# -*- coding: utf-8 -*-
import os
import shutil
import sys

from common.common_api import CommonApi
from common.global_var import GlobalVar

curdir = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHONPATH'] = curdir
pythonpath = os.getenv('PYTHONPATH')
print("pythonpath: " + pythonpath)




def run():
    imgdir = GlobalVar.get("imgSaveDir")
    if imgdir is None:
        print("get imgdir failed")
        exit(-1)
    CommonApi.copy_files("resource/img", imgdir)


run()
