"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

block = False

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def singleHeader(line):
  line = re.sub(r'#\s*(.*)\s*',r'<h1>\1</h1>',line)
  return line

def doubleHeader(line):
  line = re.sub(r'##\s*(.*)\s*',r'<h2>\1</h2>',line)
  return line

def tripleHeader(line):
  line = re.sub(r'###\s*(.*)\s*',r'<h3>\1</h3>',line)
  return line

def startBlockQuote(line):
  line = re.sub(r'^>\s*(.*)\s*',r'\1',line)
  block = True
  line.lstrip()
  line.rstrip()
  if '#' in line:
    line = tripleHeader(line)
    line = doubleHeader(line)
    line = singleHeader(line)
  return line        
    
if __name__ == "__main__":
  
  first = True
  inBlock = False
  
  for line in fileinput.input():
    line = line.rstrip() 
    line = convertStrong(line)
    line = convertEm(line)
    line = tripleHeader(line)
    line = doubleHeader(line)
    line = singleHeader(line)
    if line[0] == '>' and first:
      block = True
    line = startBlockQuote(line)    
    
    if len(line) == 0:
      block = True
      inBlock = True

    if not block:
      if '<' in line and inBlock:
        print '\n' + line + '\n</blockquote>',
      else:
        print '<p>' + line + '</p>'
    else:
      if first:
        print '<blockquote>\n\t<p>' + line + '</p>\n\n',
        first = False
      elif len(line) == 0:
        print '',
      
      block = False
