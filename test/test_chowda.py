import unittest
import os
import chowda.parsing as parse
import datetime
import pandas as pd
from chowda.load import load_file

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TEST_FILE = "CTL1 wk3 exp1 RAW data.txt"
TEST_1 = os.path.join(DATA_DIR, TEST_FILE)


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

    def test_load_file(self):
        from chowda.load import load_file
        result = load_file(TEST_1)
        self.assertEquals(result[0].strip(),
                          '"Oxymax Windows  V 2.30 Data File"')

    def test_get_header(self):
        from chowda.load import get_header
        result = get_header(TEST_1)
        self.assertEquals(result[0].strip(),
                          '"Oxymax Windows  V 2.30 Data File"')
        self.assertEquals(result[-1].split(",")[0].strip(), '"========"')

    def test_get_data(self):
        from chowda.load import get_data
        result = get_data(TEST_1)
        self.assertEquals(result[0].split(",", 1)[0], "Interval")

    def test_partition_file(self):
        from chowda.load import partition_file
        header, data = partition_file(TEST_1)
        self.assertEquals(header[0].strip(),
                          '"Oxymax Windows  V 2.30 Data File"')
        self.assertEquals(header[-1].split(",")[0].strip(), '"========"')
        self.assertEquals(data[0].split(",", 1)[0], "Interval")

    def test_load_dataframe(self):
        from chowda.load import load_dataframe
        result = load_dataframe(parse.get_data(self.in_data))
        self.assertEquals(result["Interval"].ix[0], "001")
