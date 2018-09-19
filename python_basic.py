print('Hello World!')

name = 'Pitt'
job = 'developer'

print(name + ' is a ' + job)

age = 30

print(name + ' is a ' + str(age) + ' year old ' + job)

# 另一種寫法
print('{} is a {} year old {}'.format(name, age, job))

# 對變數進行運算
print('{} will be {} in a year'.format(name, age+1))

# 建立一個問候
print('What is your name?')
yourName = input()
print('Nice to meet you ' + yourName)

# 詢問年齡
print('what us your age?')
yourAge = input()
# 這邊需注意，使用者輸入實為字符串，無法進行運算，須再轉回整數型
print('You will be {} in a year'.format(int(yourAge) + 1))
