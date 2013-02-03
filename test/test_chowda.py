import unittest
import os
import chowda.parsing as parse
import datetime
import pandas as pd
from chowda.load import load_file, get_data, load_dataframe


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TEST_FILE = "CTL1 wk3 exp1 RAW data.txt"


class TestChowda(unittest.TestCase):

    def setup(self):
        test_file = os.path.join(DATA_DIR, TEST_FILE)
        with open(test_file) as in_handle:
            self.in_data = in_handle.readlines()

    def test_parse_experiment_time(self):
        result = parse.parse_experiment_time(self.in_data[0])
        self.assertEquals(result.keys()[0], "Experiment Started")

    def test_parse_subject(self):
        result = parse.parse_subject(self.in_data[1])
        self.assertEquals(result["Subject"], "CNS1")

    def test_parse_mass(self):
        result = parse.parse_subject_mass(self.in_data[2])
        self.assertEquals(result["Subject Mass"], 34.26)

    def test_parse_header(self):
        result = parse.parse_header(self.in_data[0:9])
        WANT_KEYS = ["Experiment Started", "Subject", "Subject Mass"]
        self.assertEquals(result.keys(), WANT_KEYS)

    def test_load_file(self):
        result = load_file(TEST_FILE)
        self.assertEquals(result[0].strip(),
                          "Experiment Started: 13:46:23 11-14-11")

    def test_get_data(self):
        result = get_data(self.in_data)
        self.assertEquals(result.split(",", 1)[0], "Interval")

    def test_load_dataframe(self):
        result = load_dataframe(parse.get_data(self.in_data))
        self.assertEquals(result["Interval"].ix[0], "001")
