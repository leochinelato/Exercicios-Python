import urllib.request

try:
    site = urllib.request.urlopen("http://instagram.com/")
except urllib.error.URLError:
    print("Deu erro")
else:
    print("Conexão estabelecida com sucesso!")
