# import all modules
print ("loading modules")
# ! SORRY might only work on Russells laptop

from flask import render_template, flash, redirect, url_for
import flask
import playsound
import random
import os
import time
import wikipediaapi
from rich.console import Console
from autocorrect import Speller

app = flask(__name__)
app.secret_key = "for-gods-sake-get-a-hobby!"
console = Console()

check = Speller(lang='en')
# ? cool looking title function

def title():
  '''
   Displays the cool looking title when called 
  '''
  # TODO: fix the colors so that they look cool later
  print ("")
  console.print ("    ____             __  ______                __  ", style="bold red")
  console.print ("   / __ )____ ______/ /_/_  __/________ ______/ /__", style="bold yellow")
  console.print ("  / __  / __ `/ ___/ //_// / / ___/ __ `/ ___/ //_/", style="bold green")
  console.print (" / /_/ / /_/ / /__/ ,<  / / / /  / /_/ / /__/ ,<   ", style="bold blue")
  console.print ("/_____/\__,_/\___/_/|_|/_/ /_/   \__,_/\___/_/|_|  ", style="bold purple")
  print ("")

# set language
wiki_wiki = wikipediaapi.Wikipedia('en')
title()

# ? INPUT book title, maybe make the 
# ? UI alittle nicer
book = input("Input a book (only the title)> ")

# clear da screan
os.system("cls")

# Checks to make sure if the book exists or not by
# cross referecing wiki database

page_py = wiki_wiki.page(book)
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True
def backtrack():
  title()
  # convert the string into a list
  def Convert(string):

    li = list(string.split(" "))
    return li
  
  # SONGS and playlists
  sad_songs = ['sad1', 'sad2', 'sad3']
  happy_songs = ['happy1', 'happy2', 'happy3']
  romantic_songs = ['roman1', 'roman2', 'roman3']
  epic_songs = ['epic1', 'epic2', 'epic3']
  suspenseful_songs = ['suspense1', 'suspense2', 'suspense3']

  # ? define key lists
  FINAL_PLAYLIST = []
  LIST_OF_KEYWORDS = []
  SPACES_between_FINAL_PLAYLIST = []

  # TODO change this input to scraping wikipedia for the plot
  # ? use setcions?

  book_plot = input("PLOT >> ")
  # strip punctuation
  book_plot_stripped = book_plot.strip(',')
  book_plot_stripped2 = book_plot_stripped.strip('.' and '!' and ',')
  array_book_plot = Convert(book_plot_stripped2)
  print (array_book_plot)
  print ("")

  # ? Keyword finder function

  def keyword(song_type, comment, song_type_short):
    song_to_play = random.choice(song_type)
    FINAL_PLAYLIST.append(song_to_play)
    print (comment)
    print (f"play {song_type_short} song: {song_to_play}")

  for i in array_book_plot:
    
    word = check(i)
    i = word
    #  creates series of if statements to check for keywords  
    # TODO: add more keywords for backtrack plot recognition

    # all key word finders
    if i == "died" or i == "killing" or i == "dies" or i == 'killed' or i == 'kills' or i == 'dead' or i == 'death':
      keyword(sad_songs, "A person died", "sad")
      LIST_OF_KEYWORDS.append(i)

    if i == 'kissed' or i == 'kisses' or i == 'love':
      keyword(romantic_songs, "romance be happenin", "romantic")
      LIST_OF_KEYWORDS.append(i)

    if i == 'battle' or i == 'battled' or i == 'battles' or i == 'fights' or i == 'war' or i == 'chase':
      keyword(epic_songs, "A BATTLE IS GOIN DOWWWWWWWWN!!!", "epic")
      LIST_OF_KEYWORDS.append(i)

    if i == 'sunny' or i == 'bright' or i == 'happy' or i == 'celebrate' or i == 'glad' or i == 'glee':
      keyword(happy_songs, "HAPPINESS IS HAPPENIN", "happy")
      LIST_OF_KEYWORDS.append(i)

    if i == 'suspense' or i == 'dark' or i == 'rickety' or i == 'broken' or i == 'scary':
      keyword(suspenseful_songs, "(0o0) *Ghost noises here*", "suspenseful")
      LIST_OF_KEYWORDS.append(i)

    if i == 'lost' or i == 'taken':
      keyword(sad_songs, "sadness", "sad")
      LIST_OF_KEYWORDS.append(i)
    else:
      # uselesssssssssssssss
      FINAL_PLAYLIST.append('empty')

  print ("")
  # removes final element
  FINAL_PLAYLIST.pop()

  print (f"The final playlist is: {FINAL_PLAYLIST}")
  keywords = 0
  amount_between_key = 0
  for i in FINAL_PLAYLIST:
    if i == 'empty':

      amount_between_key += 1

    else:
      # calculating amount of 'empty's between keywords

      SPACES_between_FINAL_PLAYLIST.append(amount_between_key)
      amount_between_key = 0
      keywords += 1

  print (f"All keywords detected: {LIST_OF_KEYWORDS}")
  print (f"Spaces list: {SPACES_between_FINAL_PLAYLIST}")

  print (f"Amount of keywords: {keywords}")
 # ? random code and stuff

  count = 0

  for i in FINAL_PLAYLIST:

    # playing music playlist

    if i == 'empty':

      # ? There is noti  to sseee here fvogr=dsf

      Dummy_variable = 3274
      # playsound.playsound('music/neutral.mp3', True)
    else:
      print ("")
      print (f"playing song: {i}")
      playsound.playsound(('music/' + i + '.mp3'), True)

      # TODO: set up some sort of neutral music player or time.sleep funtion
      time.sleep(SPACES_between_FINAL_PLAYLIST[count])
      count += 1

  print ("")
  console.print ("playlist is over :(", style="bold red")
  time.sleep(100)

# ? THE REST...

if page_py.exists() == True:
  print ("THE BOOK EXISTS!")
  # backtrack( --put the plot from wikipedia here-- )
  backtrack()

# ! If the book does not exist:
if page_py.exists() == False:
  print ("THE BOOK DOESN'T EXIT")
  os.system("python backtrack_testing.py")
  exit()
  quit()