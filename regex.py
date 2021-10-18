import re
import os
import unittest


def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    source_dir = os.path.dirname(__file__)  # <-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path, 'r', encoding='utf-8')

    lines = infile.readlines()

    infile.close()

    return lines


def find_word(string_list):
    """ Return a list of words that contain three digit numbers in the middle. """

    three_digit_list = []

    three_digit_regex = re.compile("[0-9] + [0-9] + [0-9]")

    for line in lines:

        line_list = re.findall(three_digit_regex, line)

        for item in line_list:
            three_digit_list.append(item)
        line_list = []
        # return the list of all words that start with the letter B, E, or T
    return three_digit_list


def find_days(string_list):
    """ Return a list of days from the list of strings the dates format in the text are MM/DD/YYYY. """

    # initialize an empty list
    date_list = []
    # define the regular expression

    # loop through each line of the string list
    for item in string_list:
        # find full date then splice date out
        date_finder = re.findall(r'(\d+/\d+/\d+)', item)
        for date in date_finder:
            item = item[3:5]
            date_list.append(item)
        date_finder = []
    # find all the dates that match the regular expression in each line

    # loop through the found dates and only add the days to your empty list

    # return the list of days
    return date_list


def find_domains(string_list):
    """ Return a list of web address domains from the list of strings the domains of a wbsite are after www. """

    # initialize an empty list
    domain_list = []
    # define the regular expression
    for item in string_list:
        # find full date then splice date out
        domain_finder = re.findall(
            r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', item)
        for domain in domain_finder:

            domain_list.append(item)
        domain_finder = []

    return domain_list


class TestAllMethods(unittest.TestCase):

    def test_find_word(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        word_list = find_word(string_list)
        self.assertEqual(len(word_list), 4)

    def test_find_days(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        days_list = find_days(string_list)
        self.assertEqual(days_list, ['23', '12', '31', '4', '1', '4'])

    def test_domains(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        domain_list = find_domains(string_list)
        self.assertEqual(domain_list, ['pythex.org', 'si.umich.edu', 'sabapivot.com',
                         'stars.chromeexperiments.com', 'theofficestaremachine.com', 'regex101.com'])


def main():
    # Use main to test your function.
    # Run unit tests, but feel free to run any additional functions you need
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
