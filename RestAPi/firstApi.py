import requests
url = 'http://www.ibm.com/'
# r = requests.get(url)
# print(r.status_code)
# print(r.request.body)

# headers = r.headers
# print(headers)

# print(headers['date'])
# print(headers['Content-Type'])
# print(r.encoding)
# print(r.text[0:100])


url_get = 'http://httpbin.org/get'
payload = {"name":"Joseph", "ID":"123"}

r=requests.get(url_get,params=payload)
# print(r.url)
# # print(r.text)
# print(r.json())
url_post= 'http://httpbin.org/post'
payload= {"name":"Joseph", "ID":"123"}
r_post=requests.post(url_post,data=payload)
print("POST request URL: ",r_post.url)
print("GET request URL: ",r.url)

print("POST request BODY: ",r_post.request.body)
print("GET request BODY: ",r.request.body)
