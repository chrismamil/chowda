#Split strip funciton
#use this to get rid of the n\r and "" junk on the title text of each experiment

import datetime

def split_strip(title_text):
	return title_text.strip('"').strip('n\r').split(" :")

print split_strip('"Experiment Started: 13:46:31 11-07-11 n\r"')

#Parse date
#FYI this will give the wrong date after 2068 b/c values 0-68 are mapped to 2000-2068 in POISX or X/open standard 
#http://docs.python.org/2/library/time.html

def date_parse(x):
	return(datetime.datetime.strptime(x, '%H:%M:%S %d-%m-%y'))

print date_parse('13:46:31 11-07-11')

#split lines of text into strings
def split(line):
	return line.split(" :")

print split('Subject: CSN1')
print split ("subject mass: 35.4g")
print split("measure time: 60 seconds")
print split("settle time: 144 seconds")

dictionary = {'Experiment started' : '13:46:31 11-07-11', 'Subject': 'CSN1' , 'Subject mass':'35.4g', 'measure time': '60seconds', 'settle time': '144 seconds'}

dictionary['Experiment started']










