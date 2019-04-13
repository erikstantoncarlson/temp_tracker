#!/usr/bin/env python

class TempTracker(object):
    """
    Records temperatures and processes the stored values.
    """

    coldest_temp = 0
    hottest_temp = 110

    def __init__(self):
        super(TempTracker, self).__init__()

        self._temperatures = []
    
    def insert(self, temp):
        """
        Records a new temperature.

        :param temp: The temperature to insert.
        :raises: `ValueError` if the temperature is not in the range of
            `self.coldest_temp` to `self.hottest_temp` inclusive, or if
            temp is not an `int`.
        """

        if not isinstance(temp, int):
            raise ValueError("Temperature must be an integer.")

        if temp < self.coldest_temp or temp > self.hottest_temp:
            message = "Temperature should be a value between "
            message += "{coldest} and {hottest}. Temperature: {temp}".format(
                coldest=self.coldest_temp,
                hottest=self.hottest_temp,
                temp=temp)
            raise ValueError(message)

        self._temperatures.append(temp)

    def get_max(self):
        """
        Get the maximum temperature recorded.

        :returns: The maximum temperature.
        :raises: `ValueError` if there are no recorded temperatures.
        """

        try:
            return max(self._temperatures)
        except ValueError:
            message = "Cannot get the maximum because there are no temperatures recorded."
            raise ValueError(message)

    def get_min(self):
        """
        Get the minimum temperature recorded.

        :returns: The minimum temperature.
        :raises: `ValueError` if there are no recorded temperatures.
        """

        try:
            return min(self._temperatures)
        except ValueError:
            raise ValueError("Cannot get the minimum because there are no temperatures recorded.")

    def get_mean(self):
        """
        Get the mean temperature of all recorded temperatures.

        :returns: The mean of all temperatures.
        :raises: `ValueError` if there are no recorded temperatures.
        """

        if len(self._temperatures) == 0:
            message = ("Cannot get the mean because there are no "
                "temperatures recorded.")
            raise ValueError(message)

        total = sum(self._temperatures)
        return total / float(len(self._temperatures))


class TempTrackerFast(TempTracker):
    """
    The same as TempTracker, but has much better performance
    for `get_max`, `get_min`, and `get_mean` by keeping track
    of max, min, and mean when inserts happen.
    """

    def __init__(self):
        super(TempTrackerFast, self).__init__()
        
        # Use -1 value to mean the value has not been set yet.
        self._min_temp = -1
        self._max_temp = -1
        self._total_temp = 0

    def insert(self, temp):
        super(TempTrackerFast, self).insert(temp)

        # Set the minimum temperature if it hasn't been set or
        # the newly inserted temperature is lower
        if self._min_temp == -1 or temp < self._min_temp:
            self._min_temp = temp

        # Set the maximum temperature if it hasn't been set or
        # the newly inserted temperature is higher
        if self._max_temp == -1 or temp > self._max_temp:
            self._max_temp = temp

        self._total_temp += temp

    def get_max(self):
        if self._max_temp == -1:
            message = "Cannot get the maximum because there are no temperatures recorded."
            raise ValueError(message)

        return self._max_temp

    def get_min(self):
        if self._min_temp == -1:
            message = "Cannot get the minimum because there are no temperatures recorded."
            raise ValueError(message)

        return self._min_temp

    def get_mean(self):
        if len(self._temperatures) == 0:
            message = ("Cannot get the mean because there are no "
                "temperatures recorded.")
            raise ValueError(message)

        return self._total_temp / float(len(self._temperatures))