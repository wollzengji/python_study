import psutil
print(psutil.cpu_count()) # CPU逻辑数量

print(psutil.cpu_count(logical=False)) # CPU物理核心



for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))