from typing import List
from observers.base import Observer

class EventDispatcher:
    def __init__(self):
        self._observers: List[Observer] = []

    def register(self, observer: Observer) -> None:
        """
        Register an observer to receive events.

        :param observer: An instance of Observer to be registered.
        """
        self._observers.append(observer)

    def notify(self, event_data: dict) -> None:
        """
        Notify all registered observers with the event data.

        :param event_data: A message or data that the observers need to process.
        """
        for observer in self._observers:
            observer.update(event_data)