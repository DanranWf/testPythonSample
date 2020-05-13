import requests,json

class RestClient():
	"""common methods for RestClient"""
	def __init__(self, api_base_url):
		# super(RestClient, self).__init__()
		self.api_root_url = api_base_url
		self.session=requests.session()

	def get(self,url,**kwargs):
		return self.request(url,'get',**kwargs)

	def post(self,url,data=None,json=None,**kwargs):
		return self.request(url,'post',data,json,**kwargs)

	def options(self,url,**kwargs):
		return self.request(url,'options',**kwargs)

	def head(self,url,**kwargs):
		return self.request(url,'head',**kwargs)
	
	def put(self,url,data=None,**kwargs):
		return self.request(url,'put',data,**kwargs)

	def patch(self,url,data=None,**kwargs):
		return self.request(url,'patch',data,**kwargs)

	def delete(self,url,**kwargs):
		return self.request(url,'delete',**kwargs)

	def request(self,url,method_name,data=None,json=None,**kwargs):
		url=self.api_base_url+url
		if method_name=='get':
			return self.session.get(url,**kwargs)
		if method_name=='post':
			return self.session.post(url,**kwargs)
		if method_name==''

if __name__=='__main__':
	r=RestClient("http://httpbin.org")
	x=r.post('/post',json={'a':'b'})
	print(x.url)
	print(x.text)
	# print(x.session)

