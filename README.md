# qa-web

Автоматизация тестирования UI приложения [OpenCart](https://docs.opencart.com/en-gb/introduction/).


# Настройка .env
После скачивания репозитория задать значение для переменных в файле `.env`. 

Для переменных `LOCAL_IP` и `BASE_URL` заменить значение на текущий локальный ip-адрес (команда для macOS`ipconfig getifaddr en0`)

Если тесты будут выполняться с помощью [selenoid](https://aerokube.com/selenoid/latest/) - установить `IS_LOCAL=False`, в противном случае `IS_LOCAL=True`.

# Запуск
1. Установить зависимости командой `poetry install`.
2. Установить и запустить [selenoid](https://aerokube.com/selenoid/latest/).
3. Запустить тесты с помощью `docker-compose up`.