#!/bin/sh

set -e

cat kc_house_data.csv \
    | csvcut -c price,zipcode,bedrooms,bathrooms,condition \
    | tee kc_house_data_simple.csv

