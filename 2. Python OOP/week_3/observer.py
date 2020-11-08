from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribe = set()

    def subscribe(self, subscriber):
        self.__subscribe.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribe.remove(subscriber)

    def notify(self, messages):
        for subscriber in self.__subscribe:
            subscriber.update(messages)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, messages):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, messages):
        self.achievements.add(messages['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)
