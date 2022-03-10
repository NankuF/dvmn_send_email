# Отправка письма
Скрипт отправляет письма по указанным адресам.

**Подготовка Linux:**<br>

Скачать git:
```
sudo apt-get install git
```
Сделать fork репозитория:
```
git clone https://github.com/NankuF/dvmn_send_email.git
```
Перейти в директорию со скриптом:
```
cd ~ && cd dvmn_send_email/
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

**Запуск:** <br>

Ввести в консоли код:
```
python send_email.py
```