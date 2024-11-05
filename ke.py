import time
import os
import random
from datetime import datetime

# Đặt khoảng thời gian tối thiểu và tối đa giữa các thao tác (giây)
MIN_SLEEP = 10
MAX_SLEEP = 60

# Đặt khoảng thời gian chờ dài hơn giữa mỗi vòng lặp (giây)
LONG_SLEEP_MIN = 600  # 10 phút
LONG_SLEEP_MAX = 1200  # 20 phút

def random_sleep():
    """Chờ một khoảng thời gian ngẫu nhiên giữa MIN_SLEEP và MAX_SLEEP giây."""
    sleep_time = random.randint(MIN_SLEEP, MAX_SLEEP)
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)

def log_current_time():
    """Ghi thời gian hiện tại vào một file log."""
    with open("temp_keep_alive.log", "a") as f:
        f.write(f"Log current time: {datetime.now()}\n")
    print("Logged current time to temp_keep_alive.log")
    random_sleep()

def list_directory():
    """Liệt kê các file trong thư mục hiện tại."""
    print("Listing current directory contents:")
    os.system("ls -l")
    random_sleep()

def read_log_file():
    """Đọc dòng đầu tiên từ file log nếu tồn tại."""
    if os.path.exists("temp_keep_alive.log"):
        with open("temp_keep_alive.log", "r") as f:
            first_line = f.readline().strip()
            print(f"Reading from log file: {first_line}")
    else:
        print("Log file does not exist.")
    random_sleep()

def create_and_remove_temp_dir():
    """Tạo và xóa một thư mục tạm."""
    os.makedirs("temp_dir", exist_ok=True)
    print("Temporary directory created.")
    time.sleep(1)  # Đợi một chút trước khi xóa
    os.rmdir("temp_dir")
    print("Temporary directory removed.")
    random_sleep()

def check_memory_usage():
    """Kiểm tra bộ nhớ hệ thống."""
    print("Memory usage:")
    os.system("free -h | grep Mem")
    random_sleep()

# Danh sách các thao tác có thể thực hiện
actions = [
    log_current_time,
    list_directory,
    read_log_file,
    create_and_remove_temp_dir,
    check_memory_usage
]

# Vòng lặp chính để duy trì Codespace
while True:
    print("====== Keep Alive Script Running ======")
    
    # Chọn ngẫu nhiên một thao tác từ danh sách và thực hiện nó
    action = random.choice(actions)
    print(f"Performing action: {action.__name__}")
    action()  # Gọi hàm đã chọn ngẫu nhiên

    # Thời gian chờ dài hơn giữa mỗi vòng lặp
    long_sleep_time = random.randint(LONG_SLEEP_MIN, LONG_SLEEP_MAX)
    print(f"Long sleep for {long_sleep_time} seconds...\n")
    time.sleep(long_sleep_time)
