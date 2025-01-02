"""
Author:王梓涵
Time:2024/12/30 15:35
E-mail:1650168704@qq.com
company:暂无
"""
import os
from faker import Faker

from common.handle_conf import HandleConf
from common.handle_path import CONF_PATH


class RandomUserData:
    """生成随机用户名和手机号的工具类"""

    @staticmethod
    def random_user_data():
        """
        生成并返回一个包含随机用户名和手机号的元组。
        并把生成的数据保存到配置文件的"test_cases"里
        :return:
        """
        fake = Faker(locale="zh_CN")
        reg_name = fake.name()
        mobile_phone = fake.phone_number()
        file_ini = os.path.join(CONF_PATH, "conf.ini")
        hc = HandleConf(file_ini)
        hc.write_conf("test_cases", "reg_name", reg_name)
        hc.write_conf("test_cases", "mobile_phone", mobile_phone)

# file_ini = os.path.join(CONF_PATH, "conf.ini")
# print(file_ini)
# rd = RandomUserData()
# reg_name, mobile_phone = rd.random_user_data()
# hc = HandleConf(file_ini)
# hc.write_conf("test_cases", "reg_name", reg_name)
# hc.write_conf("test_cases", "mobile_phone", mobile_phone)
