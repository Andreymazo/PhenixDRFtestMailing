###########################################
Расссылка по списку телефонов клиентов (через оператор Мегафон),
+
Апи реквест о рассылке (отправляем если...)

##########################################

командные файлы:

    create_super_user1.py - создает суперпользователя
    create_mailings2.py - создаем рассылки
    create_clientts3.py - создаем клиентов
    mailing_sms.py - запускается рассылка по списку клиентов + апи рекввест

###################### Redis, Celery, Flower, Celery beat#####################
systemctl start redis
celery -A config worker -l info
celery -A config flower --port=5001
###############################Cron##################
python manage.py crontab add
python manage.py crontab show
python manage.py crontab remove
+ log.log пишется
########################################################
можно работать из админки (это Селери бит дает сделать)