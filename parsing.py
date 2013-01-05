#Split strip funciton
#use this to get rid of the n\r and "" junk on the title text of each experiment



def split_strip(title_text):
	return title_text.strip('"').strip('n\r').split(" :")

print split_strip('"Experiment Started: 13:46:31 11-07-11 n\r"')
