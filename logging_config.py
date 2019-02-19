"""
logging配置
"""

import os
import logging.config

# 当前目录下 log 文件夹
logfile_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log")

# log文件名
logfile_name = 'app.log'

# 如果不存在定义的日志目录就创建一个
os.makedirs(logfile_dir, exist_ok=True)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'details': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][%(name)s][%(filename)s:%(lineno)d]' \
                        '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
            
        },
        'simple': {
            'format': '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d]%(message)s',
            'datefmt': "%m-%d %H:%M:%S"
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'details2file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'details',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 20,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'details2file'],
            'level':"DEBUG",
            'propagate': False
        }
    },
}

def init():
    logging.config.dictConfig(LOGGING_DIC)

if __name__ == '__main__':

    def load_my_logging_cfg():
        logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
        logger = logging.getLogger('')  # 生成一个log实例
        logger.info('It works!')  # 记录该文件的运行状态
    load_my_logging_cfg()