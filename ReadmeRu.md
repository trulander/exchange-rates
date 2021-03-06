# django(DRF) + celery + unit tests + docker + docker-compose
Описание задачи для проекта:
```team foundation
сервис ходит по API раз в 5-10-15 мин (задать через env) и забирают данные о криптовалюте BTC (например curl -H "X-CMC_PRO_API_KEY: d61bca4c-e9d3-40b9-8d82-abf9b057ffbd" -H "Accept: application/json" -d "id=1" -G https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest) и сохраняют в базу курс, время когда сходили и то что посчитаешь нужным
    сервис который отдает информацию из базы о курсе (последнюю и список)
        по возможности обновляет таймер (типа я захотел свежак, дернул endpoint и воркер обновил данные)*
    завернуть все это в Docker + docker-compose**
    само собой выложить на github
    круто будет если это будет асинхронно (если не django)***
```


## Список эндпоинтов API:
```team foundation
/api/ratecurrency/all/    - Выводит список всех записей с курсами валют
/api/ratecurrency/all/{id}/  - Выводит список курсов с сортировкой по id валюты

/api/ratecurrency/{id}/  - Выводит 1 запись курса по ее id в таблице

/api/ratecurrency/last/{id}/    - Выводит последнюю запись курса валюты из DB по ее id

/api/ratecurrency/latest/{id}/   - Создает task для celery для запроса свежего курса валюты по ее id через сервис к стороннему api.
                    Ожидает выполнения задачи celery и возвращает результат в ответ.
                    
/api/currency/     - Выводит список валют сохраненных в DB
/api/currency/{id}/  - Выводит детально информацию о валюте из DB по ее id
```

## Список эндпоинтов у services:
```team foundation
/services/requestcurrency/{id}/ - 
        Делает запрос напрямую на сторонний api курса валюты по id на стороннем сервисе.
        Результат сохраняет в бд и в ответ отдает модель валюты.
        Доступно только по авторизации
```


В проекте содержится модуль Core которых содержит в себе общие классы для всех приложений

Приложение api отвечает за представление API для конечного пользователя проекта, предоставляет эндпоинты
для работой с данными находящимися в базе данных.

Приложение services отвечает за бизнесслогику, содержит 1 сервисный эндпоинт для прямого запроса к стороннему api без celery
В папке BusinessLogic содержится класс бизнес логики сервиса который отвечает за запросы к стороннему api

Проект базово работает с базой данный sqlite, но рассчитан и на работу с postgreSQL, для переключения на работу с ним есть 
специальная переменная окружения DATABASE_TYPE которая в случае присвоения ей значения sqlite работает с этой базой, в противном случае с postgresql.


Для первого запуска приложения требуется наличие установленного docker и docker-compose на компьютере.
комманды для развертывания приложения:
```shell
    git clone https://github.com/trulander/exchange-rates
    cd exchange-rates
    docker-compose up
```

Докер сам соберет нужные зависимости, установит требуемые пакеты и запустит сразу работающий проект из коробки.

## Некоторые полезные комманды
### Запуск django тестов
```shell
  docker-compose exec web python manage.py test
```

Асинхронная реализация этого же проекта: [https://github.com/trulander/exchange-rates-async](https://github.com/trulander/exchange-rates-async)
