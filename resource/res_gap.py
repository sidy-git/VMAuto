# -*- coding: utf-8 -*-
import os
import shutil
import sys
from common.global_var import GlobalVar

curdir = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHONPATH'] = curdir
pythonpath = os.getenv('PYTHONPATH')
print("pythonpath: " + pythonpath)

def copy_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_folder)
            print(f"Copied {source_file} to {destination_folder}")


def run():
    imgdir = GlobalVar.get("imgSaveDir")
    if imgdir is None:
        print("get imgdir failed")
        exit(-1)
    source_folder = '/path/to/source/folder'
    destination_folder = '/path/to/destination/folder'
    copy_files("resource/img", imgdir)


run()
