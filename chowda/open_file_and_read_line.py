from chowda.load import get_header
from chowda.parsing import parse_experiment_time

test_file = "/Users/christine/Documents/chowda/test/data/CTL1 wk3 exp1 RAW data.txt"

# this gives me the header- next I need to read each line in the header, run it through the parse function i wrote for it, call this whole thing "parse header" and this will return a dictionary of the header parsed

 
 

def parse_header(header):
    parse_line1 = parse_experiment_time(header[1])
    return parse_experiment_time(header[1])


header = get_header(test_file)
print header[1]
print parse_header(header)
#print "christine"
#print '"christine"'














    

