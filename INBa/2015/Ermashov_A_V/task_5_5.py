import random
start = "Один из соборов Московского кремля является: "
choice = random.randint(1,8)
 if choice == 1:
     print(start+"Колокольня Ивана Великого")
 elif choice == 2: 
     print(start+"Успенский собор")
 elif choice == 3: 
 	print(start +"Благовещенский собор")
 elif choice == 4: 
 	print(start +"Архангельский собор")
 elif choice == 5: 
 	print(start +"Храм Положения ризы Божией Матери во Влахерне")
 elif choice == 6: 
 	print(start +"Патриарший дворец и собор Двенадцати апостолов")
 elif choice == 7: 
 	print(start +"Верхоспасский собор")
 elif choice == 8: 
 	print(start +"Церковь Рождества Богородицы на Сенях")
input("Нажмите ENTER для продолжения")