#!/usr/bin/python
#Author: Jay Gurnani

from sys import exit, argv
import os,re

def main (arg):
    if len(arg) < 1:
        print "Wrong syntax. Required format = ./comment_parser.py argument.java"
        exit(0)
    else:
        checker(arg)

def checker (file_entered):
    fileName, fileExt = os.path.splitext(file_entered)
    if (fileExt == ".java"):
        java_comment(file_entered)
    elif (fileExt == ".c" or fileExt == ".cpp"):
        c_comment(file_entered)
    elif (fileExt == ".php"):
        php_comment(file_entered)
    else:
        print "No recognized syntax. Only Java/C/PHP allowed"
        exit(0)

def java_comment(file_entered):
    f = open(file_entered, 'r')
    for line in f:
        if (re.search('\/*.*\/', line) or re.search('\/\/', line)):
            line = line.strip()
            print line  
    f.close()

def c_comment(file_entered):
    f = open(file_entered, 'r')
    for line in f:
        if (re.search('\/*.*\/', line) or re.search('\/*', line) or re.search('\/\/', line)):
            line = line.strip()
            print line
    f.close()

def php_comment(file_entered):
    f = open(file_entered, 'r')
    for line in f:
        if (re.search('\/*.*\/', line) or re.search('\/\/', line) or re.search('#', line)):
            line = line.strip()
            print line
    f.close()

