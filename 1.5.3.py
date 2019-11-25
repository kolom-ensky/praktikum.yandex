# Получите доступ к библиотеке Pandas, используйте имя переменной pd.
import pandas as pd

# Создайте список music с 5 парами «имя вашего любимого исполнителя - название его песни».
music = [
    ['Alekseev', 'Мечта-подруга'],
    ['Michael Jackson', 'Human Nature'],
    ['George Michael', 'Jesus to a Child'],
    ['Земфира', 'Деньги'],
    ['Сплин', 'Дочь самурая']
]

# Создайте список entries с названиями для двух столбцов — artist и track.
entries = ['artist', 'track']

# Используя конструктор DataFrame(), создайте таблицу
# из списка ваших любимых исполнителей music и списка столбцов entries.
# Сохраните таблицу в переменной playlist и выведите эту сборную таблицу на экран.
playlist = pd.DataFrame(data = music, columns = entries)
print(playlist)
