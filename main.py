username = ""
password = ""
new_repositorie_name = 'easyGigHubRepositorie'
new_repositorie_description = 'none'

import urllib 
import urllib2 
from bs4 import BeautifulSoup

url = 'https://github.com/login'
login_post_url = 'https://github.com/session'
create_url = 'https://github.com/new'
create_post_url = 'https://github.com/repositories'

cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)

request = urllib2.Request(url)
response = opener.open(request)

soup = BeautifulSoup(response, "html.parser")
login_html = soup.form

utf8 = login_html.select('input[name="utf8"]')[0].attrs['value']
authenticity_token = login_html.select('input[name="authenticity_token"]')[0].attrs['value']

values = {
    'utf8': utf8.encode('utf8'),
    'authenticity_token': authenticity_token.encode('utf8'),
    'login': username.encode('utf8'),
    'password': password.encode('utf8')
}

data = urllib.urlencode(values)

request = urllib2.Request(login_post_url, data)

response = opener.open(request)

request = urllib2.Request(create_url)
response = opener.open(request)

soup = BeautifulSoup(response, "html.parser")
create_html = soup.select('form[action="/repositories"]')[0]

utf8 = create_html.select('input[name="utf8"]')[0].attrs['value']
authenticity_token = create_html.select('input[name="authenticity_token"]')[0].attrs['value']
owner = create_html.select('input[id="owner_droomo"]')[0].attrs['value']

values = {
    'utf8': utf8.encode('utf8'),
    'authenticity_token': authenticity_token.encode('utf8'),
    'owner': owner.encode('utf8'),
    'repository[name]': new_repositorie_name,
    'repository[description]': new_repositorie_description,
    'repository[public]': 'true',
    'repository[auto_init]': 0,   
}

data = urllib.urlencode(values)

request = urllib2.Request(create_post_url, data)

response = opener.open(request)

soup = BeautifulSoup(response, "html.parser")
result = soup.select('title')[0].text

if (result == username + '/' + new_repositorie_name):
    print result + ' create succes'
else:
    print 'mission faild.'