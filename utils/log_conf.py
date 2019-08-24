
import os
import time
import logging
import logging.handlers
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_dir = BASE_DIR + '/data/'


# 日志管理
def init_logger(file_name):
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")   # 当前时间
    log_file_name = now_time + file_name            # 使用当前时间当做log日志的文件名
    log_file = os.path.join(data_dir, "log/", log_file_name)
    dir_path = os.path.dirname(log_file)
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except Exception:
        pass

    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=20 * 1024 * 1024, backupCount=10, encoding='utf-8')
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger_instance = logging.getLogger('logs')
    logger_instance.addHandler(handler)
    logger_instance.setLevel(logging.DEBUG)
    return logger_instance