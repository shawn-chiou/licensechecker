#!/usr/bin/python

import extractor #Importing extractor Class
import comment_parser
from sys import argv #Importing argv support 

(script, argument) = argv

comment_parser.main(argument)

