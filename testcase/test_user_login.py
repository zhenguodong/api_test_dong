"""用户登录"""

import unittest
import requests
import json
import sys
##提升包搜索路径到项目路径，默认到上一级目录搜索，搜索不到的话，再到下一级目录搜索
sys.path.append('..')
## 提升两级路径('../..')
from config import config as cf

from lib.read_excel import get_case_data

class TestUserLogin(unittest.TestCase):
    def test_user_login_normal(self):
        case_data = get_case_data('test_user_data.xlsx',
                                  'TestUserLogin',
                                  'test_user_login_normal')
        url = case_data[1]
        data = case_data[3]
        expect_res = case_data[4]
        data_dict = json.loads(data)
        res = requests.post(url=url, data=data_dict)
        self.assertEquals(expect_res, res.text)