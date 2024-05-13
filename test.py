import datetime

# 获取当前时间
current_time = datetime.datetime.now()

# 打印当前时间
print(current_time)
if current_time.hour > 12:
    print("12点后")
else:
    print("12点前")
