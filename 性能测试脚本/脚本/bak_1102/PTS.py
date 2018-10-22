# -*- coding:utf-8 -*-

#    created by LiBin 2016-5-31

#   Licensed under the MIT licence:
#
#   Permission is hereby granted, free of charge, to any person
#   obtaining a copy of this software and associated documentation
#   files (the "Software"), to deal in the Software without
#   restriction, including without limitation the rights to use,
#   copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following
#   conditions:
#
#   The above copyright notice and this permission notice shall be
#   included in all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#   HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#   OTHER DEALINGS IN THE SOFTWARE.
import random

def addHttpCode(statuscode, code_list):
    if statuscode < 300:
        code_list[0] += 1
    elif 300 <= statuscode < 400:
        code_list[1] += 1
    elif 400 <= statuscode < 500:
        code_list[2] += 1
    elif statuscode >= 500:
        code_list[3] += 1
		
		
def addHttpCode1(errcode, code_list):
    if errcode < 300:
        code_list[0] += 1
    elif 300 <= errcode < 400:
        code_list[1] += 1
    elif 400 <= errcode < 500:
        code_list[2] += 1
    elif errcode >= 500:
        code_list[3] += 1


def sumHttpCode(StatusCode, sumStatusCode):
    for i in xrange(4):
        sumStatusCode[i] += StatusCode[i]
		
def sumHttpCode1(ErrCode, sumErrCode):
    for i in xrange(4):
        sumErrCode[i] += ErrCode[i]
        

def random_num(num):
    number = ''
    for i in random.sample(range(10), int(num)):
        number += ''.join(str(i))

    return number
def get_tenant():
	tenant_list = [('admin@uyun.cn':'0e7517141fb53f21ee439b355b5a1d0a'),]