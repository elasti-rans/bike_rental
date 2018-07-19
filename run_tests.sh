#!/usr/bin/env bash
pylint bike_rental
mypy bike_rental/
py.test --cov=bike_rental -v
