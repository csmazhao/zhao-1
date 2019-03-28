# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
import json
import requests
import common.conf as conf
import common.excelaction as excelaction
from common.sendemail import sendreport
from common.signture import sign
import common.userinfo as userinfo
import common.logger as logger
import sys
import time

# data_path = os.path.dirname(__file__) + '\\test_data\\' # 测试用例数据文件所在目录
data_path = conf.testdata_path

test_reports = []  # 添加一个数组用来存储测试结果
for file in os.listdir(
        data_path):  # 循环读取目录下的文件
    child = os.path.join('%s%s' % (
    data_path, file))  # 将文件名和路径拼接好
    logger.info("当前打开的文件：" + child)
    fl = open(
        child)  # 打开文件
    try:
        cases = json.load(fl)
        for key in cases:  # 循环读取文件中的测试用例（case）
            start_time = time.clock()
            case = cases[key]
            url = conf.get_conf('module', case['module']) + case['url']
            data = case['data']
            data['Platform'] = conf.get_conf('params', 'Platform')
            data['Terminal'] = conf.get_conf('params', 'Terminal')
            data['UserIP'] = conf.get_conf('params', 'UserIP')
            data['Version'] = conf.get_conf('params', 'Version')
            if "UserToken" in data and data['UserToken'] == '':
                data['UserToken'] = userinfo.get_token()
            hope_result = case['assert']
            method = case['method']
            test_report = {
                "case_id": case['id'],
                "t_name": case['name'],
                "method": method,
                "url": url,
                "params": data,
                "hope_result": hope_result,
                "actual_result": [],
                "test_result": ""
            }
            try:
                if method == 'post':
                    addsign_data = sign(data, conf.get_conf('sign', 'api_key'))
                    r = requests.post(url, data=json.dumps(addsign_data), headers=conf.header)
                    response = r.json()
                    s = True
                    for k in hope_result:
                        ar = str(k) + ":" + str(response[k])
                        test_report["actual_result"].append(ar)
                        if type(hope_result[k]) == type(''):
                            if hope_result[k] in response[k]:
                                s = s & True
                            else:
                                s = s & False
                        else:
                            if hope_result[k] == response[k]:
                                s = s & True
                            else:
                                s = s & False
                    if s:
                        test_report["test_result"] = "PASS"
                    else:
                        test_report["test_result"] = "Fail"

                elif method == 'get':
                    addsign_data = sign(data, conf.get_conf('sign', 'api_key'))
                    r = requests.get(url, params=addsign_data, headers=conf.header)
                    response = r.json()
                    s = True
                    for k in hope_result:
                        ar = str(k) + ":" + str(response[k])
                        test_report["actual_result"].append(ar)
                        if type(hope_result[k]) == type(''):
                            if hope_result[k] in response[k]:
                                s = s & True
                            else:
                                s = s & False
                        else:
                            if hope_result[k] == response[k]:
                                s = s & True
                            else:
                                s = s & False
                    if s:
                        test_report["test_result"] = "PASS"
                    else:
                        test_report["test_result"] = "Fail"

                else:
                    print(u'暂不支持该请求方式')
                test_reports.append(test_report)
                end_time = time.clock()
                str_time = '当前执行的用例：' + key + '_' * 4 + '用例执行所用时间：' + str(end_time - start_time) + 's'
                logger.info(str_time)
            except:
                error_msg = sys.exc_info()
                logger.error(error_msg)
                continue
    except:
        error_msg = sys.exc_info()
        logger.error(error_msg)
        continue

excelaction.creat_report(
    test_reports)  # 生成测试报告
sendreport()  # 发送测试报告