from random import randint


roles_list = ['Мафия', 'Мафия', 'Шериф', 'Шериф', 'Мирный', 'Мирный', 'Мирный', 'Мирный']

print(randint(0, len(roles_list)-1))
user_role = roles_list.pop(randint(0, len(roles_list)-1))
print(user_role)
print(roles_list)
