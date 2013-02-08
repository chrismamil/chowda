#Split strip funciton
#use this to get rid of the n\r and "" junk on the title text of each experiment

import datetime

def split_strip(title_text):
	return title_text.strip('"').strip('n\r').split(": ")

#Parse date
#FYI this will give the wrong date after 2068 b/c values 0-68 are mapped to 2000-2068 in POISX or X/open standard 
#http://docs.python.org/2/library/time.html
def date_parse(x):
	return(datetime.datetime.strptime(x, '%H:%M:%S %d-%m-%y'))


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





















