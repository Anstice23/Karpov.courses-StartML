Оберните в ORM таблицу post из базы данных для финального проекта. У вас должен получиться класс, который использует declarative_base() (заготовка будет ниже) и объявляет все колонки. Этим классом будем пользоваться, чтобы потом доставать объекты.

Учтите, что при создании класса необходимо правильно указать имя таблицы (это __tablename__) и схему таблицы (для финального проекта используется стандартная public, поэтому не обязательно явно задавать).

Отправьте файл под названием table_post.py, содержащий реализацию класса Post, который описывает таблицу post на языке ORM. Обратите внимание, что table_post.py должен импортировать Base из файла database