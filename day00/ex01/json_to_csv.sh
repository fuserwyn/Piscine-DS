#/bin/sh

OUTPUT_FILE=hh.csv

FILTER_FILE=filter.jq

jq '.items' ../ex00/hh.json  | jq -r -f $FILTER_FILE > $OUTPUT_FILE