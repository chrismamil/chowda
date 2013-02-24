#Split strip funciton
#use this to get rid of the n\r and "" junk on the title text of each experiment

import datetime

def split_strip(title_text):
	return title_text.strip('"').strip('n\r').split(": ")

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
	split_line = split(line1)
	parse_line1 = {split_line[0] : split_line[1]}
	return parse_line1

print parse_subject("Subject: CSN1")

#parse subject mass line
def split_strip2(line):
	return line.strip(' g').split(": ")
print split_strip2("Subject Mass: 35.44 g")

def parse_mass(line):
	split_line = split_strip2(line)
	print split_line

	parse_line = {split_line[0] : split_line[1]}
	float = split_line[1]
	return parse_line

print parse_mass("Subject Mass: 35.44 g")

print type(35.44)


##want to look like Subject mass: 35.4 (where 35.4 is a float...not a string)

##next step- bring raw data subject lines into my parsing...the data is a LIST...figure out how to get the items in the list i want (ie: 1,2,3, not 0, and not past 3)
## to get raw data
# filename = "/Users/christine/Documents/chowda/test/data/CTL1 wk3 exp1 RAW data.txt"
#>>> filename:'/Users/christine/Documents/chowda/test/data/CTL1 wk3 exp1 RAW data#.txt'
#>>> from chowda.load_file import get_header
#>>> from chowda.load import get_header
#>>> get_header(filename)
# this will give me all the header stuff

#want to parse lines 2,3,4,5


























