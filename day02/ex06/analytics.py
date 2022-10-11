import os
from random import randint
import logging
import json
import requests

class Research:
    def __init__(self, path):
        self.path = path
        logging.info("Research class is created")

    def file_reader(self):
        header = True
        logging.info('Started reading the file')
        if not os.access(self.path, os.R_OK):
            raise ValueError("420 times check before using input")
        with open(self.path, "r") as f:
            lines = []
            for line in f:
                lines += line.rstrip().split('\n') 
        if (len(lines) < 2):
            raise ValueError("We need more or equal than 1 lines")
        if lines[0] == "0,1" or lines[0] == "1,0":
            header = False
        if header and len(lines[0].split(',')) != 2:
            raise ValueError("wrong header")
        line_s = []
        if header:
            line_s = lines[1:]
        else:
            line_s = lines
        for line in line_s:
            if line != "0,1" and line != "1,0":
                raise ValueError("ooops, only 0,1 or 1,0 should be inside starting from first line")
        res = []
        for line in line_s:
            strs = line.split(',')
            numbers = []
            for number in strs:
                numbers.append(int(number))
            res.append(list(numbers))
        logging.debug("File is ok")
        return res

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info("Calculations class is created")

        def counts(self):
            heads = 0
            tails = 0
            for pair in self.data:
                heads += pair[0]
                tails += pair[1]
            logging.debug("Heads and tails are calculated")
            return heads, tails

        def fractions(self, ran):
            first = ran[0] * 100 / (ran[0] + ran[1])
            second = ran[1] * 100 / (ran[0] + ran[1])
            logging.debug("Fractions of heads and tails are calculated")
            return first, second

    class Analytics(Calculations):
        def predict_random(self, num):
            res = []
            for i in range(num):
                first = randint(0, 1)
                if first == 1:
                    second = 0
                else:
                    second = 1
                res.append([first, second])
            logging.debug("Random predictions are made")
            return res

        def predict_last(self, res):
            logging.debug("Returning last pair of predictions")
            return res[-1]

        def calc_random(self, res):
            heads = 0
            tails = 0
            for pair in res:
                heads += pair[0]
                tails += pair[1]
            logging.debug("Random heads and tails are calculated")
            return heads, tails

        def save_file(self, data, name_of_file, extension):
            f = open(name_of_file + '.' + extension, "w")
            f.write(data)
            logging.debug("Saving report to the file")
            f.close()

    def send_slack_message(self, payload, webhook):
        return requests.post(webhook, json.dumps(payload))
