import os

# 把当前路径添加到系统路径
curPath = os.path.dirname(os.path.abspath(__file__))
print("curPath: " + curPath)
ret = os.system("set path=%path%;" + curPath)
