#!/bin/bash

head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n +2 ../ex02/hh_sorted.csv | \
awk 'BEGIN {FS = OFS = "," } 
    {
        STR = ""

        if (index(tolower($3), "junior"))
            STR = STR"Junior/"
        if (index(tolower($3), "middle"))
            STR = STR"Middle/"
        if (index(tolower($3), "senior"))
            STR = STR"Senior"
        if (STR == "")
            STR = "-"

        gsub(/[\/ ]*$/, "", STR) 
        
        $3 = "\""STR"\""
        print
    }' \
    >> hh_positions.csv

    #awk печатает линии, в которых встречается заданное слово, поданное аргументом перед словом '/slovo/{print}' filename
    #awk '/slovo/{print}' filename
    #tail -n 2 после флага -n печатает последние две
     #tail -n +2 после флага -n кроме последних двух
    #head -n 1 печатает с начала заданное количество линий после флга -n 

    #FS: FS command contains the field separator character which is used to divide 
    #fields on the input line. The default is “white space”, meaning space and tab characters.
    #FS can be reassigned to another character (typically in BEGIN) to change the field separator.

    #OFS: OFS command stores the output field separator, which separates the fields when Awk prints them. 
    #The default is a blank space. Whenever print has several parameters separated with commas,
    # it will print the value of OFS in between each parameter. 
    #gsub(/[\/ ]*$/, "", STR) если встретится /[\/ ]*$/, то заменит в STR это на "" https://www.programmingr.com/tutorial/gsub-in-r/
    