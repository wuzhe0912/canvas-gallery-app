friends = [
    'pitt, pitt@gmail.com',
    'daisy, daisy@gmail.com',
    'nancy, nancy@gmail.com'
]


print(friends[0])
print(friends[0].split(','))
# title()將第一個字轉成大寫
print(friends[0].split(',')[0].title())
# strip()清除多餘空白
print(friends[0].split(',')[1].strip())

for friendList in friends:
    print(friendList)

for friendList in friends:
    name = friendList.split(',')[0].title()
    email = friendList.split(',')[1].strip()
    print("{}'s email address： {}".format(name, email))
