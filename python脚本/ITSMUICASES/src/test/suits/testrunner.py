#coding=utf-8
import unittest
import HtmlTestRunner

from src.test.cases.test_create_new_model import createnewmodel
class runAll(unittest.TestCase):
    suits = unittest.TestSuite()
    suits.addTest(createnewmodel("test_createnewmodel"))
    if __name__=="__main__":
            htmlPath = "f:\\testReport.html"
            fp = open(htmlPath, "wr")
            runner = HtmlTestRunner.HTMLTestRunner(stream=fp, title="test", description="result")
            runner.run(suits)
            fp.close()





