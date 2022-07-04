# Отправка письма
Скрипт отправляет письма по указанным адресам.

**Подготовка Linux:**<br>

Скачать git:
```
sudo apt-get install git
```
Сделать fork репозитория:
```
git clone https://github.com/NankuF/send_email.git
```
Перейти в директорию со скриптом:
```
cd ~ && cd send_email/
```
Создать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
. ./venv/bin/activate
```
Установить зависимости:
```
pip install -r requirements.txt 
```
Создать файл .env и указать в нем переменные:
```
EMAIL_LOGIN=your_login
EMAIL_PASSWORD=пароль_для_приложений.(это не пароль от почты)
SENDER_MAIL=your_login@yandex.ru
RECEIVERS_MAIL=your_login@yandex.ru (получатель - вы сами)
```


**Запуск:** <br>

Ввести в консоли код:
```
python send_email.py
```
