import time

## ------------------ 获取 13 位时间戳 ------------------
def get_current_time():
  current_milli_time = lambda: int(round(time.time() * 1000))
  current_time = current_milli_time()
  # print(current_time)
  return current_time

if __name__ == '__main__':
  get_current_time()


