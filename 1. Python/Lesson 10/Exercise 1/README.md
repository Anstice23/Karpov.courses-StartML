Оберните в ORM таблицу post из базы данных для финального проекта. У вас должен получиться класс, который использует declarative_base() (заготовка будет ниже) и объявляет все колонки. Этим классом будем пользоваться, чтобы потом доставать объекты.

Учтите, что при создании класса необходимо правильно указать имя таблицы (это __tablename__) и схему таблицы (для финального проекта используется стандартная public, поэтому не обязательно явно задавать).

Отправьте файл под названием table_post.py, содержащий реализацию класса Post, который описывает таблицу post на языке ORM. Обратите внимание, что table_post.py должен импортировать Base из файла database

Используя класс Post из предыдущего степа, отберите все посты с topic = "business", отсортируйте их по убыванию их id и возьмите первые 10 id. Сделайте это все через ORM и sqlalchemy и распечатайте результат в виде списка из чисел. Например, [1, 2, 3, 4, 5]

Дополните файл с классом Post соответствующим кодом, отгородив его от определения класса конструкцией if __name__ == "__main__", и отправьте итоговый python-скрипт в форму ниже.
