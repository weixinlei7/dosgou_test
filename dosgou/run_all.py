# coding:utf-8
import unittest
from common import HTMLTestRunner_cn
casePath = "D://wei//pycharm//dosgou//case//"
rule = "test_*.py"
discover = unittest.defaultTestLoader.discover(start_dir = casePath,pattern = rule)


reportPath = "D:/wei/pycharm/dosgou/report/"+"result.html"
fp = open(reportPath,'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream = fp,
                                          title = "测试报告",
                                          description = "报告描述")
runner.run(discover)
fp.close()
