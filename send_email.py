import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
login = os.getenv('EMAIL_LOGIN')
password = os.getenv('EMAIL_PASSWORD')
sender = os.getenv('SENDER_MAIL')
receivers = os.getenv('RECEIVERS_MAIL')

website = 'dvmn.org'
link = 'https://dvmn.org/referrals/svPQW6zRN1ZjPHofEYOQbsC3YQ2HV9RyR4mpUWBb/'
friend_name = 'Иван'
my_name = 'Валерий'
text = f"""
Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на {website}?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → {link}
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.

"""
letter = f"""\
From: {sender}
To: {receivers}
Subject: Курсы со скидкой 30% на dvmn.org
Content-Type: text/plain; charset="UTF-8";
{text}
"""
letter = letter.encode('utf-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(sender, [receivers], letter)
server.quit()
