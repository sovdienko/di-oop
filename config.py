import punq

from mail import MailProvider, UnioneProvider

container = punq.Container()
container.register(MailProvider, UnioneProvider)