from chowda.load import get_header
from chowda.parsing import parse_experiment_time, parse_subject, parse_mass

test_file = "/Users/christine/Documents/chowda/test/data/CTL1 wk3 exp1 RAW data.txt"

# this gives me the header- next I need to read each line in the header, run it through the parse function i wrote for it, call this whole thing "parse header" and this will return a dictionary of the header parsed

 
 

def parse_header(header):
    parse_line1 = parse_experiment_time(header[1])
    parse_line2 = parse_subject(header[2])
    parse_line3 = parse_mass(header[3])
    dict_parse = dict(parse_line1.items() + parse_line2.items() + parse_line3.items())
    return dict_parse



header = get_header(test_file)
print parse_header(header)


















    

