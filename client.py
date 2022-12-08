from typing import cast

from config import container
from mail import Mail, MailProvider


def run():
    mail_provider = cast(MailProvider,container.resolve(MailProvider))
    Mail(mail_provider).send(
        to='boss@office.com',
        subject='Salary',
        message='Give me m money'
    )
