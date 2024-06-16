# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания нового заказа в системе
# содержат имя, фамилию, адрес заказчика, ближайшую к заказчику станцию метро, телефон заказчика,
# количество дней аренды,дату доставки,комментарий от заказчика, предпочитаемые цвета
order_body = {
    "firstName": "Maria",
    "lastName": ",Bashenina",
    "address": "Opochinina, 9",
    "metroStation": 24,
    "phone": "+7 800 588 58 58",
    "rentTime": 1,
    "deliveryDate": "2024-07-09",
    "comment": "None",
    "color": [
        "BLACK"
    ]
}

params_get = {
    "t": ""
}