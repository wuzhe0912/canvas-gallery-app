# 猜炸彈數字遊戲

# 假設炸彈為87
# 最大可猜範圍~最小可猜範圍

bomb = 87
max_num = 200
min_num = 0

while True:
    print('炸彈範圍介於{}~{}之間。'.format(min_num, max_num))
    playerNum = int(input('請輸入一個炸彈數字：'))
    if playerNum == bomb:
        print('BooM! Game Over!')
        break
    elif playerNum < bomb:
        min_num = playerNum
    else:
        max_num = playerNum
