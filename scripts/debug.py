import sys
a=sys.path.append('..')
from testdemo import TestDemo
# print sys.path
from params.operations import *

if __name__=="__main__":
    rs=TestDemo('http://192.168.0.103:83')
    #case lpost
    # post_result,ttt=lpost(rs,'200')
    # print('cccccccccc',post_result,ttt)
    # print(post_result.url)
    # # print(ttt.error)
    # print('tttt',type(post_result))

    # case ppost
    ppost_rs=ppost(rs,query='wf')
    print('wfffff',ppost_rs.headers)
    assert ppost_rs.status_code==100,'code status is {}, rs value is {}'.format(ppost_rs.status_code,ppost_rs.json())
    print('ppost',ppost_rs.json())
    # print(ppost_rs.)






    # assert post_result.status_code==200,'status_code is not expeted 200'
    # assert post_result.status_code == 100, 'status_code is {}, not expeted 100'.format(post_result.status_code)
    # assert post_result.status_code == 100, 'status_code is %s, not expeted 100'%(post_result.status_code)


    # print post_result.url
    # print post_result.content
    # if(''==post_result.content):
    #     print('it is none')


    # assert post_result.status_code==200
