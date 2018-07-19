#!/usr/bin/env bash
pylint bike_rental
py.test --cov=bike_rental -v
