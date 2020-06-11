from api.httpbin0 import HttpBin


class TestDemo():
    def __init__(self,base_url,**kwargs):
        self.api_base_url=base_url
        self.https=HttpBin(self.api_base_url,**kwargs)


# if __name__=='__main__':
#     rs=TestDemo('http://192.168.0.103')
#     print rs.l
#     print rs.text
#     print 'success'