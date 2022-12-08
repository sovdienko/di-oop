from abc import ABC, abstractmethod


class MailProvider(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, message: str):
        pass


class MailgunProvider(MailProvider):
    def send(self, to: str, subject: str, message: str):
        print(f'Sending {to} via Mailgun')


class UnioneProvider(MailProvider):
    def send(self, to: str, subject: str, message: str):
        print(f'Sending {to} via Unione')


class Mail:
    def __init__(self, provider: MailProvider):
        self._provider = provider
        print("Use provider {}".format(provider.__class__))

    def send(self, to: str, subject: str, message: str):
        self._provider.send(to, subject, message)


# def send_mail():
#     Mail(provider=UnioneProvider()).send(
#         to='boss@office.com',
#         subject='salary',
#         message='I want my money'
#         )


