У нас осталась таблица feed_action. С ней есть тонкость: в ней присутствуют ключи из других таблиц (ForeignKey).

Оберните таблицу feed_action в ORM. Используйте названия user_id и post_id для соответствующих колонок и укажите, что они являются ForeignKey. Пока не делайте relationship (если уже хочется) - их оставим на следующие примеры.

Как обычно, используйте Base из database.py, который был в прошлых степах, и импортируйте Base точно так же из database