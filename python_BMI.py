# BMI 計算實作

name_P = 'Pitt'
height_p = 1.82  # meter
weight_p = 85    # kg

name_J = 'Jack'
height_j = 1.71  # meter
weight_j = 72    # kg


def bmi_calculator(name, weight, height):
    # BMI公式 體重/身高(m)
    bmi = weight / height ** 2
    # round語法 取小數點後特定幾位數
    # print('Pitt\'s BMI: {}'.format(round(BMI, 2)))
    print("{}'s BMI: {}".format(name, round(bmi, 2)))

    # 判斷並陳述體重是否過重
    if bmi < 18.5:
        print('{} is underweight.'.format(name))
    elif 18.5 <= bmi < 25:  # BMI >= 18.5 and BMI < 25:
        print('{} is normal weight.'.format(name))
    else:
        print('{} is overweight.'.format(name))


bmi_calculator(name_P, weight_p, height_p)
bmi_calculator(name_J, weight_j, height_j)
