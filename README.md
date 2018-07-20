# bike_rental

[![Build Status](https://travis-ci.com/elasti-rans/bike_rental.svg?branch=master)](https://travis-ci.com/elasti-rans/bike_rental)

### Assumptions
    Only python 3.5 or newer versions are supported.
    This due to usage of typing module that require python >3.5, and enum module =>3.4.

### How to run the tests
    # Enter into python virtual environment#
    python3.6 -m venv </path/to/new/virtual/environment>
    source </path/to/new/virtual/environment>/bin/activate

    pip install -r requirements.txt  # Install tests requirements
    ./run_tests.sh  # this will run pylint and mypy checkers and then will execute the unit tests

### The design
    BikeRate object - represent the various rental plans - by hour, by day, by week
        as such it encasulate the plan details - the minimal time period and the price for the period.
        It also allow calculating that cost for a given duration in a desigered palan.

    BikeRental - represent a bike rental and as such it contain the rental duration.
        It also allow getting the best price for that duration.
        It Just calculate each plan cost for that duration and return the minimal.

    GroupRental - this object is another representation of a rental but it represent a rental of several bikes >=1.
        The constructor of this object get list of BikeRental, as each bike in the rental can have different duration.
        So each bike in the group rental could be rental using different rent plan.
        This object calculate the price by summing the cost of each bike and then apply a discount if such is given.

    GroupRental and BikeRental implement the _Rental interface so a user of the objects
        can use polymorphisem and treat them the same way.
        e.g: calculate the rent cost of all rentals done in the last month.

### The development practices
    Basically I applied TDD.
    First I added the requirments for static analysis tools unit tests framework.
    Added travis ci intergration.
    Then I tried to provide small commits (each focus on ceratin functionality)
    each commit was provided with its relevant unit tests, to make sure eachcommit is fully functional by it self.
    The reason for the small commits is ease of review, and easier bug find using bisect.
