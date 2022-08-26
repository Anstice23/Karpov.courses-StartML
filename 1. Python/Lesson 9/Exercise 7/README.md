Напишите endpoint POST /user/validate, который будет принимать JSON в формате из прошлого задания и валидировать его. Для валидации укажите в функции, что она принимает аргумент типа User (возьмите этот класс из прошлого пункта). Наконец, верните в endpoint строку "Will add user: <имя> <фамилия> with age <возраст>"

Пример запроса: POST /user/validate с телом

{
  "name": "Aleksei",
  "surname": "Kozharin",
  "age": 77,
  "registration_date": "2022-01-01"
}

должно вернуть status code 200 и текст "Will add user: Aleksei Kozharin with age 77"

При этом запрос

{
  "name": "Aleksei",
  "surname": "Another"
}

Должен вернуть ошибку валидации: status code 422 и JSON с подробным текстом (оставьте тот, что FastAPI выдает по умолчанию). Отправьте app.py с реализацией endpoint и класса User.
