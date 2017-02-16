import re
from bs4 import BeautifulSoup

#soup = BeautifulSoup(html_doc, 'html.parser')
soup = BeautifulSoup(open("input.txt"), 'html.parser')

#get only the text; removes all the tags.
str = soup.get_text()

#RegEx to get the content between two strings; "going." and "Share"
#re.DOTALL: consider "." to match with everything including whitespaces
sub_str = re.search('going\.(.*)Share', str, re.DOTALL)

#get the required group
sub_str = sub_str.group(1)

#split lines in order to read data line by line
lines = sub_str.split('\n')

#Read data line by line, remove extra whitespace "\s" and join the data
final_str = ""
for line in lines:
    if line != "\n":
        final_str += line.strip() + "\n"

#RegEx to replace multiple newline "\n" with one newline"\n"
final_str = re.sub('\n+', '\n', final_str)

opfile = open("output.txt", "w")
opfile.write(final_str)
opfile.close()

print final_str
