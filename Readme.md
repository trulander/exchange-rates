#Python
Python Backend Level: Junior и Middle/Senior

Требования к junior-to-middle уровню такие: http://crm.kt-team.de/~YRk3d (внутренняя ссылка).


Писать можно на 2ух стеках (Django + Celery или Flask/aiohttp/Starlette + сервис воркер).
Нужно написать сервис/сервисы (в зависимости от стека) которые делают

    сервис ходит по API раз в 5-10-15 мин (задать через env) и забирают данные о криптовалюте BTC (например curl -H "X-CMC_PRO_API_KEY: d61bca4c-e9d3-40b9-8d82-abf9b057ffbd" -H "Accept: application/json" -d "id=1" -G https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest) и сохраняют в базу курс, время когда сходили и то что посчитаешь нужным
    сервис который отдает информацию из базы о курсе (последнюю и список)
        по возможности обновляет таймер (типа я захотел свежак, дернул endpoint и воркер обновил данные)*
    завернуть все это в Docker + docker-compose**
    само собой выложить на github
    круто будет если это будет асинхронно (если не django)***
