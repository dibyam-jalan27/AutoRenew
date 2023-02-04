from new import *
from test import *


def Auto_renew(self):
    username = USERNAME.get()
    password = PASSWORD.get()
    url = "http://117.239.204.229:8380/opac/myaccount/myAccount.html"

    startbot(username, password, url)


def Reset():
    print('Hello')
