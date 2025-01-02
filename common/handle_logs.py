"""
Author:王梓涵
Time:2024/12/25 15:46
E-mail:1650168704@qq.com
company:暂无
"""
import logging
from common.handle_conf import conf


class HandleLogs:
    """处理日志"""

    @staticmethod
    def handle_logs():
        # 创建日志收集器
        logs = logging.getLogger(conf.get("log", "collector_name"))
        logs.setLevel(conf.get("log", "collector_level"))
        # 设置日志的输出渠道和等级
        # 1.输出到日志文件
        sf = logging.FileHandler(conf.get("log", "file_name"), encoding="utf8")
        sf.setLevel(conf.get("log", "sf_level"))
        logs.addHandler(sf)
        # 2.输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log", "sh_level"))
        logs.addHandler(sh)
        # 设置日志输出的格式,并且加载到输出渠道里
        formats = conf.get("log", "formats")
        forma = logging.Formatter(formats)
        sf.setFormatter(forma)
        sh.setFormatter(forma)
        return logs


logs = HandleLogs.handle_logs()
