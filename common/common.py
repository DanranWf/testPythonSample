#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

class Common(object):
    """docstring for Common"""
    def __init__(self, base_url,username=None,password=None,token=None):
        # super(Common, self).__init__()
        self.base_url = base_url
        self.session=requests.session()
        self.username=username
        self.password=password
        # self.to
        # if username and password:
        #     self.session.auth=(self.username,self.password)
        # elif token:
        #     a="token {}".format(token)
        #     a=self.session.headers["Authorization"] = a
        #     print(a)

            # pass

    def request(self,method_name,url,data=None,json=None,verify=False,**kwargs):
        url=self.base_url+url
        if method_name=='get':
            return self.session.get(url,**kwargs)
        if method_name=='post':
            print('post method',url)
            return self.session.post(url,data,json,**kwargs)
        if method_name=='options':
            return self.session.options(url,**kwargs)
        if method_name=="head":
            return self.session.head(url,**kwargs)
            #attentin
            # return self.session.head(self,url,**kwargs)
        if method_name=='put':
            return self.session.put(url,data,**kwargs)
            #attentin
            # return self.session.head(self,url,**kwargs)
        if method_name=='patch':
            return self.session.patch(url,data,**kwargs)
            #attentin
            # return self.session.head(self,url,**kwargs)
        if method_name=='delete':
            return self.session.delete(url,**kwargs)
            #attentin
            # return self.session.head(self,url,**kwargs)



    def get(self,url,**kwargs):
        return self.request('get',url,**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return self.request('post',url,data,json,**kwargs)
    def options(self,url,**kwargs):
        return self.request('options',url,**kwargs)
    def head(self,url,**kwargs):
        return self.request('head',url,**kwargs)
    def put(self,url,data=None,**kwargs):
        return self.request('put',url,data,**kwargs)
    def patch(self,url,data=None,**kwargs):
        return self.request('patch',url,data,**kwargs)
    def delete(self,url,**kwargs):
        return self.request('delete',url,**kwargs)


        
if __name__ == '__main__':
    # token=''
    # headers=
    rq=Common("http://192.168.0.103/basic-auth/1/2")
    rs=rq.get('')
    print rs.status_code
    print(rs.text)
    print(rs.headers)

   