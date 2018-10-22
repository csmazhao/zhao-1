# -*- coding:utf-8 -*-

# A simple example using the HTTP plugin that shows the retrieval of a
# single page via HTTP.
#
# This script is automatically generated by ngrinder.
#
# @author admin
from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from net.grinder.plugin.http import HTTPPluginControl
from HTTPClient import Cookie, CookieModule, CookiePolicyHandler, NVPair
from org.json import JSONObject
import PTS #自定义的库，后续大家可扩充。

control = HTTPPluginControl.getConnectionDefaults()
# if you don't want that HTTPRequest follows the redirection, please modify the following option 0.
# control.followRedirects = 1
# if you want to increase the timeout, please modify the following option.
control.timeout = 600000 #超时时间10分钟

def tenant():
    statusCode = [0L, 0L, 0L, 0L]
    headers = [NVPair('Content-Type', 'application/json'),NVPair('Accept', 'application/json'),NVPair('Origin', '10.1.11.254')]
    data = '{"filterType": "all"}'
    result7 = HTTPRequest().POST('http://10.1.11.254/itsm/api/v2/ticket/getAllTicket', data, headers)
    code = result7.getStatusCode()
    data = result7.getText()
   # grinder.logger.info(data)
    json = JSONObject(data)
    grinder.logger.info(json.getString("errCode"))
    status = json.getString("errCode")
    if status == 'null':
        code = 300
    if status != 'null':
        code = int(status)
    PTS.addHttpCode(code, statusCode)
    return statusCode
    

# Make any method call on request1 increase TPS
Test(1,'test').record(tenant)

class TestRunner:
    # initlialize a thread
    def __init__(self):
        grinder.statistics.delayReports=True
        headers = [NVPair('Content-Type', 'application/json'),NVPair('Accept', 'application/json'),]
        #data = '{"email": "admin@uyun.cn","passwd": "0e7517141fb53f21ee439b355b5a1d0a"}'
        login_msg=PTS.get_tenant()
        lenth=len(login_msg)
        i=0
        #grinder.logger.info(login_msg[i][0])
        #grinder.logger.info(login_msg[i][1])
        data= '{"email": "%s", "passwd": "%s", "code": "uyun", "authCode": "fd9552d74e7113c7970226443dd4efd4181dd5aa068a8917c6357b6606b6994b"}' % (login_msg[i][0], login_msg[i][1])
        #grinder.logger.info(data)
        if i >= lenth-1:
            i=0
        i+=1
        result = HTTPRequest().POST('http://10.1.11.254/tenant/api/v1/user/login', data, headers)
        self.threadContext = HTTPPluginControl.getThreadHTTPClientContext()
        self.login_cookies = CookieModule.listAllCookies(self.threadContext)

    # test method
    def __call__(self):
        sumStatusCode = [0L,0L,0L,0L]
        #因为每次执行测试cookie会被清空，所以这里需要每次重新设置cookie
        for c in self.login_cookies:
           CookieModule.addCookie(c, self.threadContext)        
        PTS.sumHttpCode(tenant(),sumStatusCode)

        # if you want to print out log.. Don't use print keyword. Instead, use following.
        #grinder.logger.info(str(sumStatusCode))

        # statusCode[0]代表http code < 300 个数,    statusCode[1] 代表 300<=http code<400 个数
        # statusCode[2]代表400<=http code<500个数，  statusCode[3] 代表 http code >=500个数
        # 如果http code 300 到 400 之间是正常的
        # 那么判断事务失败，请将statusCode[1:4] 改为   statusCode[2:4] 即可
        if sum(sumStatusCode[1:4]) > 0:
            grinder.statistics.forLastTest.success = 0
            grinder.logger.error(u'事务请求中http 返回状态大于300，请检查请求是否正确!')
        else:
            grinder.statistics.forLastTest.success = 1