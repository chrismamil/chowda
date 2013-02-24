import os
import fnmatch
from chowda.log import logger
from chowda.utils import file_exists, partition


def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)


def load_file(filename):
    if not file_exists(filename):
        logger.warning("%s does not exist or is a zero length file, skipping."
                       % (filename))
        return None
    logger.info("Loading %s." % (filename))
    with open(filename) as in_handle:
        return in_handle.readlines()


def _is_not_data_header(line):
    return not line.split(",")[0] == '"Interval"'


def partition_header_and_data(lines):
    return partition(_is_not_data_header, lines)


def get_data(filename):
    lines = load_file(filename)
    header, data = partition_header_and_data(lines)
    stripped = [x.strip().replace('"', '') for x in data]
    return stripped


def get_header(filename):
    lines = load_file(filename)
    header, data = partition_header_and_data(lines)
    return list(header)


def partition_file(filename):
    lines = load_file(filename)
    header, data = partition_header_and_data(lines)
    #unquoted_data = [x.strip().replace('"', '') for x in data]
    return list(header), list(data)


def process_directory(data_dir):
    #partitioned_files = map(partition_file, locate("*.txt", data_dir))
    header, raw_data = partition_file(list(locate("*.txt", data_dir))[0])
    units = get_units(raw_data)
    colnames = get_colnames(raw_data)
    data_points = get_data_points(raw_data)
    return units, colnames, data_points
    """
    do analayis a on big table
    do the b
    make graphs
    summarize
    output

    TODO:
    drop final column
    drop feed,acc
    """


def get_units(data):
    return data[1].split(",")[:-1]


def get_colnames(data):
    return data[0].split(",")[:-1]


def get_data_points(data):
    return [x.split(",")[:-1] for x in data[3:]]
