# coding:utf-8
# 訓練後分析，因最大心律可能有改變
import math

def get_data():

    # 體重
    weight = input('請輸入您的體重(Kg): ')
    # 身高
    height = input('請輸入您的身高(Cm): ')
    # 性別
    gender = input('請輸入您的性別(男:1 女:0)')
    # 年齡
    age = input('請輸入您的年齡(歲)')
    # BMI值
    BMI = float(weight) / math.pow(float(height) / 100, 2)


    # 訓練物的重量
    bar_kg = input('請輸入訓練物的重量(kg): ')
    # 訓練時間
    train_time = float(input('請輸入訓練時間(min): ')) / 60

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
    else: # 110 < weight
        P_per_kg_meter = 0.085

    # 訓練的項目
    train_project = 'chest'

    return weight, height, gender, age, BMI, P_per_kg_meter, train_project, train_time, bar_kg

# 胸肌(俯立挺身)
def chest():
    return 0

# 背肌(槓鈴上舉)
def back():
    return 0

# 腹肌(仰臥起坐)
def belly():
    return 0

# 小腿肌(深蹲，可加槓鈴)
def leg():
    return 0

# 臂肌(啞鈴)
def arm():
    return 0

# 有氧
def aerobic():
    return 0

# 最大心律
def max_heart_rate(age):
    return 208 - 0.7*age



if __name__ == '__main__':

    # 使用者基本資訊
    weight, height, gender, age, BMI, P_per_kg_meter, train_project, train_time, bar_kg = get_data()


    # 訓練種類
    if train_project == 'chest':
        chest()
    elif train_project == 'back':
        back()
    elif train_project == 'belly':
        belly()
    elif train_project == 'leg':
        leg()
    elif train_project == 'arm':
        arm()
    elif train_project == 'aerobic':
        aerobic()

    # 存入資料庫

    # print "您的BMI值為: " + str(BMI)
    # print "您完成一次" + str(bar_kg) + "KG上舉所消耗的卡路里為：" + str(bar_kg*float(height)/100*0.919*P_per_kg_meter) + "千卡"