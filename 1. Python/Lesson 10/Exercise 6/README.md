Напишите endpoint GET /user/{id}/feed, GET /post/{id}/feed, использующие ORM и возвращающие pydantic модель из ORM. Каждый endpoint должен принимать необязательный query-параметр limit, по умолчанию равный 10 - это количество записей, которое надо вернуть.

GET /user/{id}/feed должен вернуть все действия из feed для пользователя с id = {id} (из запроса).

GET /post/{id}/feed должен вернуть все действия из feed для поста с id = {id} (из запроса).

Оба endpoint должны возвращать действия в порядке убывания их времени (т.е. самые свежие действия первыми). Если список действий будет пустым, то возвращайте 200 и пустой список (а не 404, как в случае с пользователем). Оба endpoint должны учитывать лимит (параметр limit).
