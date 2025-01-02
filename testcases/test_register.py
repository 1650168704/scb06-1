"""
Author:王梓涵
Time:2024/12/30 22:23
E-mail:1650168704@qq.com
company:暂无
"""

import pytest
from common.handle_regular import cases
from common.handle_conf import conf
from requests import request


class TestRegister:
    """注册接口的"""

    @pytest.mark.parametrize("case", cases)
    def test_register(self, case):
        """
        根据注册接口的测试用例，来驱动测试接口
        :param case:测试数据
        :return:
        """
        # 1.准备测试数据
        headers = eval(conf.get("env", "headers"))
        url = conf.get("env", "url") + case["url"]
        method = case["method"]
        data = eval(case["data"])
        expected = eval(case["expected"])
        sql = case["check_sql"]
        # 2.发送请求
        response = request(method=method, headers=headers, url=url, json=data)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果：", res)
        # 3.断言
