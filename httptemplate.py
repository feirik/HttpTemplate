import base64
import requests

url = "url"

# Initiate persistent session object
session = requests.Session()


# Pass in user/pw if needed
session.auth = ('username', 'password')


# Pass in user-agent in header
user_agent = "user_agent 1.0"
session.headers.update({'User-Agent': user_agent})


# Print header we sent to the server
response = session.get(url)
print(response.request.headers)


# Print headers we received
print(response.headers)


# Status code of request we sent
print(response.status_code)


# Pass in referer in header
referer = "referer"
session.headers.update({'referer': referer})

response = session.get(url)


# Pass in modified cookie value
cookies = {'cookieParameter': 'value'}

response = session.get(url, cookies=cookies)


# Store cookie in cookiejar for use over multiple domains or paths
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='url1', path='/cookies')
jar.set('gross_cookie', 'blech', domain='url2', path='/elsewhere')
response = requests.get(url, cookies=jar)


# Pass in data in GET request
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(url, params=payload)


# Pass in data in POST request
payload = {'key1': 'value1', 'key2': 'value2'}

response = requests.post(url, data=payload)


# Pass in file in POST request
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
response = requests.post(url, files=files)


#Disable redirect
response = requests.get(url, allow_redirects=False)


# Decode content
content = response.content.decode('utf-8')


# Decoding encoding
encoded = "hex"
encoded = bytes.fromhex(encoded)
# Reverse if needed
encoded = encoded[::-1]
# b64 decode if needed
decoded = base64.decodebytes(encoded)
