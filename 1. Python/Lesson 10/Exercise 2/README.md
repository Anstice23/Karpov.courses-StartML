Оберните таблицу user в ORM по аналогии с тем, как делали с таблицей post. Точно так же берите Base из database (from database import Base) и используйте следующий файл database.py
Используя класс User из прошлого пункта, магию ORM и немного чтения документации, отберите всех пользователей, у которых экспериментальная группа равна 3, сгруппируйте их по парам (country, os) и выведите для каждой группы (country, os, count(*)), отсортированные по убыванию COUNT(*) и имеющие COUNT(*) > 100 (т.е. те группы, в которых более 100 записей). Результат сохраните в список из кортежей, например, [("Germany", "Android", 100), ("Russia", "iOS", 10033)], и распечатайте его.

Дополните файл с классом User соответствующим кодом, отгородив его от определения класса конструкцией if __name__ == "__main__"