# -*- coding: UTF-8 -*-
import unittest,os
from myunittest import testlib
from parameterized import parameterized


# 创建一个测试类，继承unittest
class PramaTest(unittest.TestCase):

    # 代表给紧接着它的测试函数参数化
    @parameterized.expand([
        [0,1,2],
        [1,1.33333333,2.43333333],
        [2,'1','11'],
        [3, 1.1, '11.1'],
        [4, 1, 2],[5,1,2],[6,1,2],[7,1,2],[8,1,2],[9,1,2],[10,1,2],[11,1,2],[12,1,2],
    ])
    def test_add(self,x,y,z):
        """
        测试testlib的add方法
        :param x: 第一个数
        :param y: 第二个数
        :param z: 期望结果
        :return:
        """
        print(x)
        self.assertEqual(testlib.add(x,y),z)


if __name__ == '__main__':
    unittest.main()
