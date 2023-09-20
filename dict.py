
# x = {'name': 'Pasha'}
# print(x['name'])



# data = {'name': ['Jordan', 'Mike'],
#         'age': 21,
#         'job': 'Programmers'}
# print(data['name'][0], data['job'][-1])



# data = {'name': ['Jordan', 'Mike'],
#         'age': 21,
#         'job': 'Programmers'}
# print(data.items())



# my_dict = {'song': 'M', 'singer': 'Q'}
# my_dict.pop('song')
# print(my_dict)
# print(my_dict.clear())


# my_dict = {'song': 'M', 'singer': 'Q'}
# my_dict.popitem()
# print(my_dict)



# my = ['2', '33', '33', 2, 'k']
# my2 = set(my)
# print(my2)



# instructor = dict(name='Jordan', age=32, job='programmer')
# for i in instructor.keys():
#     print(i)
# for v in instructor.values():
#     print(v)
# for i, v in instructor.items():
#     print(f'{i} : {v}')



# names_and_dates = {'Mirjahon': 20,
#                    'Mike': 30}
# while True:
#     name = input("What name?: ")
#     print(names_and_dates.get(name))



all_products = {'Весь склад': {}}

while True:
    admin = input("Что вы хотите сделать?(Добавить продукт/Весь продукт/Завершить): ")


    if admin.lower() == "добавить продукт":
        name_of_product = input("Какой продукт?: ")
        quantity_of_product = int(input("Какое количество?: "))
        all_products['Весь склад'][name_of_product] = quantity_of_product
        print("Всё добавлено!")
        
    elif admin.lower() == "весь продукт":
        print(all_products)

    elif admin.lower() == "завершить":
        end = input("Показать весь склад?: ")
        if end.lower() == "да":
            print(all_products)
        elif end.lower() == "нет":
            break











