
# class User:
#     name = 'Mike'
#
# user_1 = User()
# print(user_1)
# print(user_1.name)



# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# gentra = Car('Chevrolet', 'Black', 2022)



# class Comments:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
# action = Comments('Mirjahon', 'dkjfkdjfkd')
# print(action.username, action.text)





# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print("Машина остановись")
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# gentra = Car('Gentra', 'Black', 2022)
#
#
# gentra.stop()
# gentra.change_color('White')
# print(gentra.color)




# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, add_deposit):
#         self.balance += add_deposit
#
#     def cash(self, send_cash):
#         self.balance -= send_cash
#
#     def my_bal(self, my_bal_activity):
#         return self.balance
#
# my_wallet = BankAccount('Mirjahon', 50)
#
# while True:
#     action = input("Что хотите сделать? (Баланс/Пополнить/Вывести): ")
#     if action.lower() == 'баланс':
#         print(my_wallet.my_bal())
#
#     elif action.lower() == 'пополнить':
#         add_action = int(input("Сколько хотите добавить?: "))
#         my_wallet.deposit(add_action)
#         print('Успешно пополнено!')
#
#     elif action.lower() == 'вывести':
#         send_action = int(input("Сколько вывести?: "))
#         my_wallet.cash(send_action)
#         print("Успешно выведено!")
#     else:
#         print("Error!!!!!")





# class User:
#     def __init__(self, name, mail, age, number):
#         self.name = name
#         self.mail = mail
#         self.age = age
#         self.number = number
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def change_mail(self, new_mail):
#         self.mail = new_mail
#
#     def change_number(self, new_number):
#         self.number = new_number
#
# my_account = User('Mirjahon', 'jkdjfk', 20, '9989889898899')
#
#
# action = input("Что хотите сделать? (Изменить/Просмотреть): ")
# if action.lower() == 'изменить':
#     add_action = input("Что хотите изменить? (Имя/Мейл/Номер)")
#     if add_action.lower() == 'имя':













