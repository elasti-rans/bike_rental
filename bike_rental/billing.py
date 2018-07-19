"""Billing module for bike rental."""
import abc
import math
import enum
import typing
import datetime


class InvalidDuration(Exception):
    """An Exception for invalid durations - zero or negative."""


class BikeRate(enum.Enum):
    """An enum that represent the different renting plans."""
    # rate value is (price per time unit, time unit)
    ByHour = (5, datetime.timedelta(hours=1))
    ByDay = (20, datetime.timedelta(days=1))
    ByWeek = (60, datetime.timedelta(weeks=1))

    @property
    def base_price(self) -> int:
        """Return the price per relevant time unit for current plan."""
        price, _ = self.value  # pylint: disable=E0633
        return price

    def cost(self, duration: datetime.timedelta) -> int:
        """Return the cost of a duration under this plan."""
        if duration <= datetime.timedelta():
            raise InvalidDuration('duration={} is not legal'.format(duration))

        price, time_unit = self.value  # pylint: disable=E0633
        return math.ceil(duration / time_unit) * price


class _Rental(abc.ABC):  # pylint: disable=R0903
    """Abstract interface for get the best price for renting."""

    @abc.abstractmethod
    def best_price(self) -> typing.Union[int, float]:
        """Abstract method that return rental best price"""


class BikeRental(_Rental):
    """Implement _Rental interface for a single bike."""

    def __init__(self, duration: datetime.timedelta) -> None:
        if duration <= datetime.timedelta():
            raise InvalidDuration('duration={} is not legal'.format(duration))

        self._duration = duration

    def __repr__(self):
        return '{}(duration={})'.format(type(self).__name__, self._duration)

    def best_price(self) -> int:
        return min(rate.cost(self._duration) for rate in BikeRate)


class GroupRental(_Rental):
    """Implement _Rental for a list of bikes."""

    _NO_DISCOUNT = 1.0
    _FAMILY_DISCOUNT = 0.7

    def __init__(self, rentals: typing.List[BikeRental]) -> None:
        self._rentals = rentals

    def __repr__(self):
        return '{}(rentals={})'.format(type(self).__name__, self._rentals)

    def best_price(self) -> float:
        price = sum(rental.best_price() for rental in self._rentals)
        return price * self._discount

    @property
    def _discount(self) -> float:
        family_discount = 3 <= len(self._rentals) <= 5
        return self._FAMILY_DISCOUNT if family_discount else self._NO_DISCOUNT
