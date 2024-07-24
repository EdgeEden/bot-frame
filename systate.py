import psutil

def system_stat():
    ram_usage = psutil.virtual_memory()
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage_C = psutil.disk_usage('/')
    reply = "CPU使用率：%.2f%%" % cpu_usage+"\n内存使用率：%d%%" % ram_usage.percent+"\n磁盘使用率：%d%%" % disk_usage_C.percent
    #print(reply)
    return reply


