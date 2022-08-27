BranchingOperator - это оператор, который по некоторому условию определяет, в какое ответвление пойдет выполнение DAG. Один из способов определить это "некоторое условие" - это задать python функцию, которая будет возвращать task_id, куда надо перейти после ветвления.

Создайте DAG, имеющий BranchPythonOperator. Логика ветвления должна быть следующая: если значение Variable is_startml равно "True", то перейти в таску с task_id="startml_desc", иначе перейти в таску с task_id="not_startml_desc". Затем объявите две задачи с task_id="startml_desc" и task_id="not_startml_desc".

NB: класс Variable возвращает строку!

В первой таске распечатайте "StartML is a starter course for ambitious people", во второй "Not a startML course, sorry".

Перед BranchPythonOperator можете поставить DummyOperator - он ничего не делает, но зато задает красивую "стартовую точку" на графе. Точно так же можете поставить DummyOperator в конце DAG.

По итогу у вас получится следующий граф (с DummyOperator):
