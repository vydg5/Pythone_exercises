# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 23:15:01 2016

@author: virea_000
"""

"""
# import the requests Python library for programmatically making HTTP requests
# after installing it according to these instructions: 
# http://docs.python-requests.org/en/latest/user/install/#install
"""
import requests

"""
# import the BeautifulSoup Python library according to these instructions: 
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
# use this syntax as described on the documentation page: 
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
"""
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'

"""
# the syntax (according to the documentation) for how to 
# "load" a webpage through Python
"""
r =requests.get(base_url)

"""
# how to decode the text of the HTML of the NY Times homepage
# website. r comes from the requests request above
"""
soup = BeautifulSoup(r.text)

"""
# find and loop through all elements on the page with the 
# class name "story-heading"
"""
for story_heading in soup.find_all(class_="story-heading"):
    """
    # for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely
    """
    if story_heading.a:
        print(story_heading.a.text.replace("/","").strip())
    else:
        print(story_heading.contents[0].strip())

