"""
Author:王梓涵
Time:2024/12/25 16:19
E-mail:1650168704@qq.com
company:暂无
"""
import os
from common.handle_path import CONF_PATH
from configparser import ConfigParser


class HandleConf(ConfigParser):
    """操作配置文件的封装"""

    def __init__(self, filename):
        """
        始化HandleConf对象，并读取指定的配置文件。
        :param filename:配置文件的路径
        """
        super().__init__(interpolation=None)  # None时，不会对任何配置项的值进行插值替换
        self.filename = filename
        self.read(filename, encoding="utf-8")

    def write_conf(self, section_name, key, value):
        """
        把数据写入到配置文件conf.ini中
        :param section_name: 标签名
        :param key:要写入的键名
        :param value:要写入的值
        :return:
        """
        if not self.has_section(section_name):
            self.add_section(section_name)
            # 设置新键值对
        self.set(section_name, key, value)
        # 将配置写回文件
        with open(self.filename, "w", encoding="utf8") as f:
            self.write(f)


file = os.path.join(CONF_PATH, "conf.ini")
conf = HandleConf(file)

if __name__ == '__main__':
    hc = HandleConf(file)
    hc.write_conf("test_cases", "reg_name", "reg_name")
    hc.write_conf("test_cases", "mobile_phone", "mobile_phone")
