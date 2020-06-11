import sys
a=sys.path.append('..')
# from common.common import Common
from common.switch import Switch

def lpost(testdemo,statuscode=100):
    '''
    payload paramn info
    :param testdemo:
    :param statuscode:
    :return:
    '''

    rs = testdemo.https.post_data(statuscode)
    # print (rs)
    Switch().success=False
    if rs.status_code==200:
        Switch.success=True
    else:
        Switch.error='post error code {}'.format(rs.status_code)
    return rs,Switch()
def ppost(testdemo,query='lwj',payload=None):
    '''
    freeform query:
    :param testdemo:
    :param query:
    :return:
    '''
    payload={
        'freeform':query
    }
    rs=testdemo.https.post_query(query,json=payload)
    print(rs.url)
    # print(rs)
    return rs




