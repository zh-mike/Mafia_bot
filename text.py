count_user = int(input("Введите количество игроков за столом: "))
count_mafia = int(input("Введите количество мафии: "))
doctor = 1
sherif = 1
user_str = ""
user_str += "мафия " * count_mafia
user_str += "доктор " * doctor
user_str += "шериф " * sherif
user_str += "мирный " * (count_user - count_mafia - doctor - sherif)

print(user_str.split())


