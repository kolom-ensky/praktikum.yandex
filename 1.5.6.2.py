# Посчитайте число прослушанных треков в жанре поп.
# Для этого лучше всего использовать логическое условие genre_fight['genre'] == 'pop'.
# Сохраните результат в переменной genre_pop. Напечатайте ответ на экране в таком виде:
# Число прослушанных треков в жанре поп равно ...

import pandas as pd
df = pd.read_csv('music_log.csv')
genre_fight = df.loc[:, ['genre', 'Artist']]
# genre_pop = genre_fight.loc[genre_fight.loc[:, 'genre'] == 'pop']['genre'].count()
genre_pop = genre_fight[genre_fight['genre'] == 'pop']['genre'].count()
print('Число прослушанных треков в жанре поп равно', genre_pop)
