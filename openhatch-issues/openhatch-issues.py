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

issue = gh.issue('openhatch', 'oh-mainline', 1403)
print(issue)
print(issue.title)
print(issue.state)
for l in issue.iter_labels():
	print(str(l))
	if 'stat' in l.name:
		print("this is a status label")
		if issue.is_closed() and 'resolved' not in l.name:
			print("This issue should be marked resolved.")
			print("Removing old status")
			issue.remove_label(l)
			issue.add_labels('stat:resolved')
