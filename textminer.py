import urllib.request

response = urllib.request.urlopen('http://www.google.com')
html = response.read()

print(html)





