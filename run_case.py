
import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('.',pattern='test*.py')

#runner = unittest.TextTestRUnner()
#runner.run(suite)

# 使用HTMLTestRunner去生成测试报告

# 1 生成测试报告的文件
test_report = 'test_report.html'

# 2 打开上面的文件，将运行的结果写到测试报告中

with open(test_report,'wb') as f:
    # 创建一个HTMLTestRunner的运行器
    runner = HTMLTestRunner(f,title='测试报告',description='当前版本:v1.0')
    runner.run(suite)
