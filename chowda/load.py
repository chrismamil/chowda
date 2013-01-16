import os
import fnmatch
from chowda.log import logger


def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)


def load_file(filename):
    logger.info("Processing %s." % (filename))
    """
    open file
    header = christine_function(filedata)
    body = rorys_function(filedata)
    combine_that_stuff = comin
    agiowngoangowngo
    return the big table of data
    """
    logger.info("Finished processing %s." % (filename))


def process_directory(dir):
    map(load_file, locate("*.txt", dir))
    """
    do analayis a on big table
    do the b
    make graphs
    summarize
    output
    """
