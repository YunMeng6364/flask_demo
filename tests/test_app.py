# test_app.py
# -*- coding: utf-8 -*-
import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # 在每个测试之前创建一个 Flask 测试客户端
        self.app = app.test_client()

    def tearDown(self):
        # 在每个测试之后清理
        pass

    def test_hello_route(self):
        # 发送 GET 请求到 /hello 路由
        response = self.app.get('/hello')
        # 断言响应状态码为 200
        self.assertEqual(response.status_code, 200)
        # 断言响应内容为 'Hello, World!'
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
