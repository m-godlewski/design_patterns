"""
Example of Abstract Factory design pattern implementation.


Pros:
- Tight connection between creator and concrete products is avoided.
- Implementation new subclasses don't mess with the previous implemented code.
- SRP (Single Responsibility Principle).

Cons:
- Code becomes more complicated with increasing number of subclasses.

"""

from __future__ import annotations
from abc import ABC, abstractmethod


# Base Creator


class ShoesCreator(ABC):
    """
    Main creator (abstract) class. Each subclass that inherits from this class
    should implement its own factory method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Creator may also have its own, default implementation of this method.
        """
        pass

    def some_operation(self) -> str:
        """
        Creator itself is not returning any product, despite of his name.
        It may have contained basic business logic, that subclasses override.
        """

        # calling factory method to create product
        shoes = self.factory_method()

        # Now, use the product.
        result = (
            f"ShoesCreator works with: {shoes.operation()}"
        )

        return result


# Concrete Creators


class SneakersCreator(ShoesCreator):
    """
    Concrete product creator, overwrites factory method from its base class
    and returns concrete product.
    """

    def factory_method(self) -> Shoes:
        return Sneakers()


class CrocksCreator(ShoesCreator):
    """
    Concrete product creator, overwrites factory method from its base class
    and returns concrete product.
    """

    def factory_method(self) -> Shoes:
        return Crocks()


class Shoes(ABC):
    """
    Product interface declares operation that each concrete product has to implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


# Concrete Products


class Sneakers(Shoes):
    def operation(self) -> str:
        return "Sneakers shoes!"


class Crocks(Shoes):
    def operation(self) -> str:
        return "Crocks shoes!"


def client_side_method(creator: ShoesCreator) -> None:
    """
    Client side code works with instances of concrete creator through its base interface.
    Any type of creator subclass can be passed by this method argument.
    """

    print(f"{creator.some_operation()}")


if __name__ == "__main__":
    print("SneakersCreator:")
    client_side_method(SneakersCreator())
    print()
    print("CrocksCreator:")
    client_side_method(CrocksCreator())
