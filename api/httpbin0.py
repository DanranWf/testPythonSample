import sys
a=sys.path.append('..')
print (a)
# import os
# print os.path.abspath('..')
# ccc=os.path.abspath('..')
# print(ccc)
import time
# time.sleep(30)

from common.common import Common

class HttpBin(Common):
    def __init__(self,base_url,**kwargs):
        super(HttpBin, self).__init__(base_url,**kwargs)


    def list_base_page(self,**kwargs):
        '''

        :param kwargs:
        :return:
        '''

        return self.get('/',**kwargs)

    def list_request_ip(self,**kwargs):
        '''

        :param kwargs:
        :return:
        '''
        return self.get('/ip',**kwargs)
    def post_data(self,status_code,**kwargs):
        '''

        :param kwargs:
        :return:
        '''
        print('status_code is', status_code)
        return self.post('/status/{}'.format(status_code),**kwargs)

    def post_query(self,query,**kwargs):
        '''

        :param kwargs:
        :return:
        '''
        print('status_code is', query)
        return self.post('/response-headers?freeform={}'.format(query),**kwargs)

if __name__=="__main__":
    ins=HttpBin('http://192.168.0.103')
    rs=ins.list_request_ip()
    print type(rs.json())
    print rs.json()['origin']
    print rs.status_code

