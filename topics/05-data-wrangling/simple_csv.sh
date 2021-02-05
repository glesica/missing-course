#!/bin/sh

set -e

cat kc_house_data.csv \
    | csvcut -c price,zipcode,bedrooms,bathrooms,condition \
    | tee house_data_simple.csv

cat tax-stats-2014.csv \
    | sed 's/a02650/total_income/' \
    | sed 's/n02650/total_income_count/' \
    | sed 's/numdep/dependent_count/' \
    | csvcut -c total_income,total_income_count,dependent_count,zipcode \
    | tee tax_data_simple.csv

csvjoin -c zipcode tax_data_simple.csv house_data_simple.csv \
    | tee house_tax_data.csv

