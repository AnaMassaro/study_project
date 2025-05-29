from abc import ABC, abstractmethod

class Observer(ABC):
   @abstractmethod
   def update(self, event_data: dict) -> None:
      """
      Update method to be called when the observed object changes.
      
      :param event_data: A message or data that the observer needs to process.
      """
      pass