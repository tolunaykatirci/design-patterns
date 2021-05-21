from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: AbstractHandler) -> AbstractHandler:
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _successor: AbstractHandler = None

    def set_next(self, handler: AbstractHandler) -> AbstractHandler:
        self._successor = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._successor:
            return self._successor.handle(request)

        return None


class MonkeyHandler(AbstractHandler):

    def handle(self, request: Any) -> Optional[str]:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)
