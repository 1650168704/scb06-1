"""
Author:王梓涵
Time:2024/12/27 13:09
E-mail:1650168704@qq.com
company:暂无
"""
import re
import os
from common.handle_path import CASES_PATH
from common.handle_excels import HandleExcel
from common.handle_conf import conf


def handle_regular(data):
    """
    正则匹配规则，匹配替换#中的数据
    :return: 匹配成功后的字符串
    """
    for case in data:
        for key in ["data", "check_sql"]:
            if key in case and isinstance(case[key], str):
                case[key] = re.sub("#(.*?)#", lambda m: conf.get("test_cases", m.group(1)) or m.group(), case[key])
    return data


file = os.path.join(CASES_PATH, "cases.xlsx")
res = HandleExcel(file, "register")
cases = handle_regular(res.read_data())

if __name__ == '__main__':
    pass
