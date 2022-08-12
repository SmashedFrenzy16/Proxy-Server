import urllib

URL = input("Enter the URL you want to have anonymous access to: ")

PROXY_ADDRESS = input("Enter proxy address: ")

if __name__ == __main__:
  
  response = urllib.urlopen(URL, proxies = {"http" : PROXY_ADDRESS})
  
  print("Proxy server returns response headers: %s ", %response.headers)
