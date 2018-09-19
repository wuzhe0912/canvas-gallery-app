# if 判斷式

weight_Pitt = 85
weight_Kara = 82

# 人一天喝水量公式為，個人體重*30
water_Pitt = weight_Pitt * 30   # cc
water_Kara = weight_Kara * 30

print('Pitt needs to drink {} cc in a day.'.format(water_Pitt))
print('Kara needs to drink {} cc in a day.'.format(water_Kara))

# use if else 判斷誰需要喝更多的水
if water_Pitt > water_Kara:
    print('Pitt needs to drink more water than Kara')
elif water_Pitt == water_Kara:
    print('Pitt and Kara need to drink some amount of water')
else:
    print('Kara needs to drink more water than Pitt')