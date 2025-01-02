"""
Author:王梓涵
Time:2024/12/25 17:14
E-mail:1650168704@qq.com
company:暂无
"""
import pymysql
from common.handle_conf import conf


class HandleMysql:
    """数据库操作的封装"""

    def __init__(self):
        """初始化mysql,并连接数据库"""
        self.con = pymysql.connect(
            host=conf.get("mysql", "host"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            port=conf.getint("mysql", "port"),  # 注意这里改为 getint，因为端口号应该是整数
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.con.cursor()

    def find_one(self, sql):
        """
        查询sql返回第一条数据
        :param sql:要查询的sql
        :return:sql语句查询到的第一条数据
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self, sql):
        """
        查询sql返回所有数据
        :param sql:要查询的sql
        :return:sql语句查询到的所有数据
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_count(self, sql):
        """
        sql语句查询到的数据条数
        :param sql:要查询的sql
        :return:查询到的数据条数
        """
        self.con.commit()
        res = self.cur.execute(sql)
        return res

    def update(self, sql):
        """
        增删改操作的方法
        :param sql:增删改的sql语句
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        """关闭游标，关闭连接"""
        self.cur.close()
        self.con.close()
