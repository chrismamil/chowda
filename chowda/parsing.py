#Split strip funciton
#use this to get rid of the n\r and "" junk on the title text of each experiment

import datetime

def split_strip(title_text):
	return title_text.replace('"', '').strip('\r\n').split(": ")

#Parse date
#FYI this will give the wrong date after 2068 b/c values 0-68 are mapped to 2000-2068 in POISX or X/open standard 
#http://docs.python.org/2/library/time.html
def date_parse(x):
	return(datetime.datetime.strptime(x, '%H:%M:%S %m-%d-%y'))


## Combines experiment time parsing
def parse_experiment_time(line):
	split_line = split_strip(line)
	parse_date = date_parse(split_line[1])
	parse_dict = {split_line[0] : parse_date}
	return parse_dict

#parse subject line

def split(line):
	return line.split(": ")

def parse_subject(line1):
	split_line = split_strip(line1)
	parse_line1 = {split_line[0] : split_line[1]}
	return parse_line1



#parse subject mass line
def split_strip2(line):
	return line.replace(' g', '').replace('"', '').split(": ")
print split_strip2("Subject Mass: 35.44 g")

def parse_mass(line):
	split_line = split_strip2(line)
	print split_line
	mass_as_float = float(split_line[1]) 
	parse_line = {split_line[0] : mass_as_float}
	return parse_line

#formally open_file_and_read_line- this parses the whole header together
def parse_header(header):
    parse_line1 = parse_experiment_time(header[1])
    parse_line2 = parse_subject(header[2])
    parse_line3 = parse_mass(header[3])
    dict_parse = dict(parse_line1.items() + parse_line2.items() + parse_line3.items())
    return dict_parse


















