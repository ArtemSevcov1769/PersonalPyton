import pandas as pd
data_math = pd.read_csv("math.csv")
data_rus = pd.read_csv('rus.csv')
data_bio = pd.ExcelFile('bio.xlsx', engine='openpyxl')
data_geo = pd.ExcelFile('geo.xlsx', engine='openpyxl')
data_obsh = pd.read_excel('obsh.xlsx')
data_hist = pd.read_excel('hist.xlsx')
data_him = pd.read_excel('him.xlsx')
data_phiz = pd.read_excel('phiz.xlsx')
def get_scores(data, code):
    string = data.loc[data['Код'] == code].copy()
    string.loc[:, 'Код'] = string.loc[:, 'Код'].astype(float)
    string.loc[:, 'Итого баллов'] = string.loc[:, 'Итого баллов'].astype(float)
    string.loc[:, 'Оценка ВПР'] = string.loc[:, 'Оценка ВПР'].astype(float)
    try:
        code_2 = round(string['Код'].values[0])
        sum_balls = round(string['Итого баллов'].values[0])
        estimation = round(string['Оценка ВПР'].values[0])
        return f'Код: {code_2}\nКоличество баллов: {sum_balls}\nОценка: {estimation}'
    except:
        return 'Ваш код отсутствует, либо вы отсутствовали на экзамене'

