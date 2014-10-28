# -*- coding: utf-8 -*-

from github3 import login
mytoken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
gh = login('xxxxx', token=mytoken)

user = gh.user()

print(user.name)
print(user.login)
print(user.followers)

for f in gh.iter_followers():
    print(str(f))

print(gh.zen())
