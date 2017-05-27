# coding:utf-8

from random import choice
from django.core.mail import send_mail

from my_users.models import EmailVerifyRecord
from LeDian.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = u'LeDian点菜系统注册激活链接'
        email_body = u'请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/%s'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    if send_type == 'forget':
        email_title = u'LeDian点菜系统密码重置链接'
        email_body = u'请点击下面的链接重置密码：http://127.0.0.1:8000/reset/%s'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(randomlength=8):
    str = []
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for _ in xrange(randomlength):
        str.append(choice(chars))
    return ''.join(str)

