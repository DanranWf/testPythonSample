import requests,json

class common_api():
    def __init__(self,base_url):
        self.url=base_url
        self.session=requests.session()

    def get(self,url,**kwargs):
        return self.request('get',url,**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return self.request('post',url,data,json,**kwargs)
    def request(self,method_name,url,data=None,json=None,**kwargs):
        url=self.url+url
        print(method_name)
        if method_name=='get':
            return self.session.get(url,**kwargs)
        if method_name=='post':
            return self.session.post(url,data,json,**kwargs)
class lwj():
    pass
if __name__=='__main__':
    rq=common_api('http://192.168.0.103')
    rs1=rq.get('/anything')
    # print(rs1.text)
    rs2=rq.post('/anything',json={'a':'b'})
    # print(rs2.text)
    # c=requests.get('http://baidu.com')
    # c1 = requests.get('http://baidu.com')
    # cc=requests.request('get','http://baidu.com')
    d=lwj()
    d1=lwj()
    if d==d1:
        print('two equals') 
    else:
        print('two not eaual')


