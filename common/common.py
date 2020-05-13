import requests

class Common(object):
    """docstring for Common"""
    def __init__(self, base_url):
        # super(Common, self).__init__()
        self.base_url = base_url
        self.session=requests.session()

    def request(self,method_name,url,data=None,json=None,**kwargs):
        url=self.base_url+url
        if method_name=='get':
            return self.session.get(url,**kwargs)
        if method_name=='post':
            return self.session.post(url,data=None,json=None,**kwargs)
    def get(self,url,**kwargs):
        return self.request('get',url,**kwargs)
    def post(self,url,data=None,json=None,**kwargs):
        return self.request('post',url,**kwargs)
if __name__ == '__main__':
    rq=Common("http://httpbin.org")
    rs=rq.get('/anything')
    print(rs.text)