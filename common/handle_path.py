"""
Author:王梓涵
Time:2024/12/25 16:06
E-mail:1650168704@qq.com
company:暂无
"""
import os

# 当前文件的父父文件夹位置
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件的位置
CONF_PATH = os.path.join(BASE_PATH, "conf")
# 用例数据的位置
CASES_PATH = os.path.join(BASE_PATH, "data")
# 报告地址
REPORTS_PATH = os.path.join(BASE_PATH, "reports")
