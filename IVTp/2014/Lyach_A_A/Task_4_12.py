# Задача 4. Вариант 12.
# Напишите программу, которая выводит имя, под которым скрывается Лариса Петровна Косач-Квитка


# Лях.А.А.
# 22.05.2016

real_name = 'Лариса Петровна Косач-Квитка'
p_name = 'Леся Украинка '
interests = ('поэзия, лирика, эпос, драма')
born_place = 'Новоград-Волынский '
born_year = 1871
death_year = 1913
death_oldness = death_year - born_year

print(real_name +', ' + ' \nболее известна под псевдонимом '
              + p_name + ',')
print('родилась в ' + born_place  +
      ' в ' + str(born_year) + ' году.')
print(str (interests) + ' сопровождали её всю сознательную жизнь.')
print('В честь писательницы именем Леси Украинки названы : Бульвар , улицы , театр , швейная фабрика и много всего другого. Умерла в  ' + str (death_year) + ' году,')
print('прожив ' + str (death_oldness ) + ' лет.')

input('\nНажмите Enter для выхода.')
