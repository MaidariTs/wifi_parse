# wifi_parse
Этот код отправляет в телеграм сообщение с паролем от Wi-Fi, к которому Вы были подключены.

# Установка
1. Клонируйте репозиторий
git clone https://github.com/MaidariTs/wifi_parse

2. Установите вирутальное окружение
python -m venv venv

3. Активируйте виртуальное окружение
source venv/Scripts/activate

4. Установите requirements.txt
pip install -r requirements.txt

5. Создайте файл .env и впишите следующие переменные:
BOT_TOKEN = 'Токен бота'
USER_ID = 'ID пользователя'
WIFI_NAME = 'Имя WIFI, к которому Вы были подключены'
