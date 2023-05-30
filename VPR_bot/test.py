import pandas as pd
data = pd.read_csv("Book.csv")
def get_scores(code):
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

