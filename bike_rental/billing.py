"""Billing module for bike rental."""
import math
import enum
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
