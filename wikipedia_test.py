# import all modules
import wikipediaapi
import time
# set language
wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Ready Player One')
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

if page_py.exists() == True:
  print ("THE BOOK EXISTS!")

elif page_py.exists() == False:
  print ("THE BOOK DOESN'T EXIT")

def print_sections(sections, level=0):
        for s in sections:
                print ("")
                if s == 'Plot':
                  print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text))
                  print ("")
                  print ("")
                  print ("######################################################################################")
                  print ("")
                  print ("")
                print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
                print_sections(s.sections, level + 1)

print_sections(page_py.sections)
# *: History - Python was conceived in the late 1980s,
# *: Features and philosophy - Python is a multi-paradigm programming l
# *: Syntax and semantics - Python is meant to be an easily readable
# **: Indentation - Python uses whitespace indentation, rath
# **: Statements and control flow - Python's statements include (among other
# **: Expressions - Some Python expressions are similar to l
time.sleep(2300)
