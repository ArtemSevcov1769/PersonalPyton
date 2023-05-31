import pandas as pd
data_test = pd.read_csv("Book.csv")
data_math = pd.read_csv("math_8.csv")
data_rus = pd.read_csv('rus_8.csv')
def get_scores(data, code):
    string = data.loc[data['Код'] == code].copy()
    string.loc[:, 'Код'] = string.loc[:, 'Код'].astype(float)
    string.loc[:, 'Итого баллов'] = string.loc[:, 'Итого баллов'].astype(float)
    string.loc[:, 'Оценка ВПР'] = string.loc[:, 'Оценка ВПР'].astype(float)
    try:
        code_2 = round(string['Код'].values[0])
        sum_balls = round(string['Итого баллов'].values[0])
        estimation = round(string['Оценка ВПР'].values[0])
        return f'Код: {code}\nКоличество баллов: {sum_balls}\nОценка: {estimation}'
    except:
        return 'Ваш код отсутствует, либо вы отсутствовали на экзамене'

