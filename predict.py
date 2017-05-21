# coding:utf-8
# 預測可能消耗的卡路里
import math


def get_data():
    # 體重
    weight = 90  # input('請輸入您的體重(Kg): ')
    # 身高
    height = 180  # input('請輸入您的身高(Cm): ')
    # 性別
    gender = 1  # input('請輸入您的性別(男:1 女:0): ')
    # 年齡
    age = 21  # input('請輸入您的年齡(歲): ')
    # BMI值
    BMI = float(weight) / math.pow(float(height) / 100, 2)

    # 訓練的項目
    train_project = 'arm'  # input('請輸入訓練項目(chest, back, belly, leg, arm, aerobic): ')
    # 訓練物的重量
    bar_kg = 100  # input('請輸入訓練物的重量(kg，若沒有則輸入0): ')
    # 訓練時間或組數
    train_time = float(720) / 60  # float(input('請輸入訓練時間(min): ')) / 60

    # 不同體重每做1000克.米的功所消耗的能量(千卡、大卡)
    if weight <= 52:
        P_per_kg_meter = 0.048
    elif 52 < weight <= 60:
        P_per_kg_meter = 0.053
    elif 60 < weight <= 67.5:
        P_per_kg_meter = 0.058
    elif 67.5 < weight <= 75:
        P_per_kg_meter = 0.063
    elif 75 < weight <= 82.5:
        P_per_kg_meter = 0.068
    elif 82.5 < weight <= 90:
        P_per_kg_meter = 0.073
    elif 90 < weight <= 100:
        P_per_kg_meter = 0.078
    elif 100 < weight <= 110:
        P_per_kg_meter = 0.082
    else:  # 110 < weight
        P_per_kg_meter = 0.085

    return int(weight), int(height), int(gender), int(age), BMI, P_per_kg_meter, str(train_project), float(train_time), int(bar_kg)


# 胸肌(俯立挺身)
def chest(gender, weight, train_time, age):
    cal = 0
    max_rhythm = max_heart_rate(age)
    print 'max_heart_rate ' + str(max_rhythm)
    # 男:((-55.0969+(0.6309*HR)+(0.1988*W)+(0.2017*A)) / 4.184) * 60 * T
    # 女:((-20.4022+(0.4472*HR)+(0.1263*W)+(0.074*A)) / 4.184) * 60 * T
    if gender == 1:
        cal = ((-55.0969 + (0.6309 * max_rhythm) + (0.1988 * weight) + (0.2017 * age)) / 4.184) * 60 * train_time
    elif gender == 0:
        cal = ((-20.4022 + (0.4472 * max_rhythm) + (0.1263 * weight) + (0.074 * age)) / 4.184) * 60 * train_time
    return cal


# 背肌(槓鈴上舉)
def back(height, bar_kg, P_per_kg_meter, train_time):
    high = float(height)/5*2
    cal = (bar_kg * float(high) / 100 * 0.919 * P_per_kg_meter)*train_time
    return cal


# 腹肌(仰臥起坐)
def belly(gender, weight, train_time, age):
    cal = 0
    max_rhythm = max_heart_rate(age)
    print 'max_heart_rate ' + str(max_rhythm)
    # 男:((-55.0969+(0.6309*HR)+(0.1988*W)+(0.2017*A)) / 4.184) * 60 * T
    # 女:((-20.4022+(0.4472*HR)+(0.1263*W)+(0.074*A)) / 4.184) * 60 * T
    if gender == 1:
        cal = ((-55.0969 + (0.6309 * max_rhythm) + (0.1988 * weight) + (0.2017 * age)) / 4.184) * 60 * train_time / 1000
    elif gender == 0:
        cal = ((-20.4022 + (0.4472 * max_rhythm) + (0.1263 * weight) + (0.074 * age)) / 4.184) * 60 * train_time / 1000
    return cal


# 小腿肌(深蹲，可加槓鈴)
def leg():
    return 0


# 臂肌(啞鈴)
def arm(height, bar_kg, P_per_kg_meter, train_time):
    high = float(height) / 5
    cal = (bar_kg * float(high) / 100 * 0.919 * P_per_kg_meter) * train_time
    return cal


# 有氧
def aerobic(gender, weight, train_time, age):
    cal = 0
    max_rhythm = max_heart_rate(age)
    print 'max_heart_rate ' + str(max_rhythm)
    # 男:((-55.0969+(0.6309*HR)+(0.1988*W)+(0.2017*A)) / 4.184) * 60 * T
    # 女:((-20.4022+(0.4472*HR)+(0.1263*W)+(0.074*A)) / 4.184) * 60 * T
    if gender == 1:
        cal = ((-55.0969 + (0.6309 * max_rhythm) + (0.1988 * weight) + (0.2017 * age)) / 4.184) * 60 * train_time / 1000
    elif gender == 0:
        cal = ((-20.4022 + (0.4472 * max_rhythm) + (0.1263 * weight) + (0.074 * age)) / 4.184) * 60 * train_time / 1000
    return cal


# 最大心律
def max_heart_rate(age):
    return 208 - 0.7 * age


if __name__ == '__main__':

    # 使用者基本資訊
    weight, height, gender, age, BMI, P_per_kg_meter, train_project, train_time, bar_kg = get_data()

    # 訓練種類
    if train_project == 'chest':
        cal = chest(gender, weight, train_time, age)
    elif train_project == 'back':
        cal = back(height, bar_kg, P_per_kg_meter, train_time)
    elif train_project == 'belly':
        cal = belly(gender, weight, train_time, age)
    elif train_project == 'leg':
        cal = leg()
    elif train_project == 'arm':
        cal = arm(height, bar_kg, P_per_kg_meter, train_time)
    elif train_project == 'aerobic':
        cal = aerobic(gender, weight, train_time, age)

    print '預計消耗' + str(cal) + '千卡'
    # 存入資料庫

    # print "您的BMI值為: " + str(BMI)
    # print "您完成一次" + str(bar_kg) + "KG上舉所消耗的卡路里為：" + str(bar_kg*float(height)/100*0.919*P_per_kg_meter) + "千卡"
