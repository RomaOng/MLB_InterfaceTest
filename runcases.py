import unittest
import os
from common.HtmlTestRunner import HTMLTestRunner

curPath = os.path.dirname(os.path.realpath(__file__))
startdir = os.path.join(curPath, 'testCase')
reportPath = os.path.join(curPath, 'testResult', 'report.html')
rule = 'test*.py'
discover = unittest.defaultTestLoader.discover(startdir, rule)
print(discover)

fp = open(reportPath, 'wb')
runner = HTMLTestRunner(fp,
                        title='王咏琳的测试报告',
                        description='报告如下：',
                        verbosity=2)
runner.run(discover)
fp.close()
