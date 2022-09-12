#coding=utf-8
class User:
    """用户类
    """

    def __init__(self, username: str, password: str,key: str):
        """用户
        ~~~
        :param: username: 账号（学号）
        :param: password: 
        :param:
        """
        self.username = username
        self.password = password
        self.key = key

