names1 = ('Стейк , Отбивная , Карбанара, Фаршированые перцы'  )
names2 = ('Жареный лосось , Жареная треска , Жареный карась')
names3 = ('Варенная капуста , Марковка по-корейски, Жареные баклажаны')
names4 = ('Мороженое, пудинг, чизкейк')

print("Виды блюд")
print("1.Мясные")
print("2.Рыбные")
print("3.Овощные")
print("4.Сладкие")

choice = input("Выбрать вид(1/2/3): ")
if  choice in ("1", "2", "3"):
        if choice == "1":
            print(names1)
        elif choice == "2":
            print(names2)
        elif choice == "3":
            print(names3)  
        elif choice == "4" :
             print(names4)
else:
    print("Такого блюда нет")
        
