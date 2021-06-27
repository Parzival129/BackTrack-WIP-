# import all modules
print ("loading modules")
# ! SORRY might only work on Russells laptop

import os
import random
import time

import playsound
import wikipediaapi
from autocorrect import Speller
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask.globals import g
from rich.console import Console

app = Flask(__name__)
app.secret_key = "for-gods-sake-get-a-hobby!"
console = Console()

# SONGS and playlists
sad_songs = ['sad1', 'sad2', 'sad3']
happy_songs = ['happy1', 'happy2', 'happy3']
romantic_songs = ['roman1', 'roman2', 'roman3']
epic_songs = ['epic1', 'epic2', 'epic3']
suspenseful_songs = ['suspense1', 'suspense2', 'suspense3']

FINAL_PLAYLIST = []
LIST_OF_KEYWORDS = []
SPACES_between_FINAL_PLAYLIST = []

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
  print         ("                 -Server Edition-")
  print ("")

# set language
wiki_wiki = wikipediaapi.Wikipedia('en')
title()

def Convert(string):

    li = list(string.split(" "))
    return li

@app.route("/plot_input", methods=['GET', 'POST'])
def plot_input():

    if request.method == 'POST':  #this block is only entered when the form is submitted
        
        book_plot = request.form.get('plot')
        # strip punctuation
        book_plot_stripped = book_plot.strip(',')
        book_plot_stripped2 = book_plot_stripped.strip('.' and '!' and ',')
        array_book_plot = Convert(book_plot_stripped2)
        
        def keyword(song_type, comment, song_type_short):
            song_to_play = random.choice(song_type)
            FINAL_PLAYLIST.append(song_to_play)

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

        FINAL_PLAYLIST.pop()

        count = 0
        

        for i in FINAL_PLAYLIST:

          if i == 'empty':
            dummy_variable = 234344

          else:
            print (f"Playing song: {i}")
            il = i
            return '''

          <audio controls>
            <source class="player" src="static/music/{}.mp3" type="audio/mpeg">
            <source class="player" src="static/music/{}.mp3" type="audio/mpeg">
          Your browser does not support the audio element.
          </audio>
            '''.format(i, il);


        return '''<h1>The array book plot value is: {}</h1>
                  <h2>The keywords are: {}</h2>'''.format(array_book_plot, LIST_OF_KEYWORDS)

    return '''
                  <style>
              
              body {
                background-image: linear-gradient(to right, #000F29, #000F4B);
              }

              .title-text {
                text-align: center;
                display: block;
                font-family: Verdana;
                color: white;
                font-size: 60px;
                margin-right: auto;
                margin-left: auto;
                padding-bottom: 30px;
              }

              .center-block1 {
                display: block;
                margin-left: auto;
                margin-right: auto;
                color: white;
                font-family: Verdana;
              }
              .a-thing {
                text-align: center;
              }
              .center-block2 {
                margin-top: 50px;
                text-align: center;
                display: block;
                margin-right: auto;
                margin-left: auto;
                font-family: Verdana;
              }
              </style>
              <body>
    <form class="a-thing" method="POST">
                  <h class="title-text">Input book Plot:</h>
                  <textarea class="center-block" name="plot" cols="50" rows="10"></textarea>

                  <input class="center-block2" type="submit" value="Submit"><br>
              </form>
              </body>'''
 
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@app.route('/start', methods=['GET', 'POST']) 
def start():
  return '''
  
    <!-- Based on http://codepen.io/lbebber/pen/ypgql -->
  <link href="http://necolas.github.io/normalize.css/3.0.2/normalize.css" rel='stylesheet'/>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js"></script>
  <title>BackTrack</title>
  <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
  <style>
    /* Just colors and font sizes */
    * {
      font-family: Blippo, fantasy;
      font-style: italic;
      text-align: center;
    }

    body {
      background-color: black;  
      text-align: center;
    }
    
    .glitch {
      text-align: center;
      color: white;
      font-size: 100px;
      margin: 0 auto;
      width: 400px;
    }
    
    /* Real glitch effect */
    .glitch {
      text-align: center;
      position: relative;
      background: transparent;
    }
    
    .glitch:after {
      text-align: center;
      animation: glitch-animation 2s infinite linear alternate-reverse;
      background: black;
      clip: rect( 0, 900px, 0, 0 );
      color: white;
      content: attr( data-text );
      left: 2px;
      overflow: hidden;
      position: absolute;
      text-shadow: -1px 0 red;
      top: 0;
    }

    .glitch:before {
      text-align: center;
      animation: glitch-animation-2 3s infinite linear alternate-reverse;
      background black;
      clip: rect( 0, 900px, 0, 0 );
      color: white;
      content: attr( data-text );
      left: -2px;
      overflow: hidden;
      position: absolute;
      text-shadow: 1px 0 blue;
      top: 0;
    }

    /* Expanded Animations */
    @keyframes glitch-animation {
      0% {
        clip: rect(42px, 9999px, 44px, 0);
      }
      5% {
        clip: rect(12px, 9999px, 59px, 0);
      }
      10% {
        clip: rect(48px, 9999px, 29px, 0);
      }
      15.0% {
        clip: rect(42px, 9999px, 73px, 0);
      }
      20% {
        clip: rect(63px, 9999px, 27px, 0);
      }
      25% {
        clip: rect(34px, 9999px, 55px, 0);
      }
      30.0% {
        clip: rect(86px, 9999px, 73px, 0);
      }
      35% {
        clip: rect(20px, 9999px, 20px, 0);
      }
      40% {
        clip: rect(26px, 9999px, 60px, 0);
      }
      45% {
        clip: rect(25px, 9999px, 66px, 0);
      }
      50% {
        clip: rect(57px, 9999px, 98px, 0);
      }
      55.0% {
        clip: rect(5px, 9999px, 46px, 0);
      }
      60.0% {
        clip: rect(82px, 9999px, 31px, 0);
      }
      65% {
        clip: rect(54px, 9999px, 27px, 0);
      }
      70% {
        clip: rect(28px, 9999px, 99px, 0);
      }
      75% {
        clip: rect(45px, 9999px, 69px, 0);
      }
      80% {
        clip: rect(23px, 9999px, 85px, 0);
      }
      85.0% {
        clip: rect(54px, 9999px, 84px, 0);
      }
      90% {
        clip: rect(45px, 9999px, 47px, 0);
      }
      95% {
        clip: rect(37px, 9999px, 20px, 0);
      }
      100% {
        clip: rect(4px, 9999px, 91px, 0);
      }
    }

    @keyframes glitch-animation-2 {
      0% {
        clip: rect(65px, 9999px, 100px, 0);
      }
      5% {
        clip: rect(52px, 9999px, 74px, 0);
      }
      10% {
        clip: rect(79px, 9999px, 85px, 0);
      }
      15.0% {
        clip: rect(75px, 9999px, 5px, 0);
      }
      20% {
        clip: rect(67px, 9999px, 61px, 0);
      }
      25% {
        clip: rect(14px, 9999px, 79px, 0);
      }
      30.0% {
        clip: rect(1px, 9999px, 66px, 0);
      }
      35% {
        clip: rect(86px, 9999px, 30px, 0);
      }
      40% {
        clip: rect(23px, 9999px, 98px, 0);
      }
      45% {
        clip: rect(85px, 9999px, 72px, 0);
      }
      50% {
        clip: rect(71px, 9999px, 75px, 0);
      }
      55.0% {
        clip: rect(2px, 9999px, 48px, 0);
      }
      60.0% {
        clip: rect(30px, 9999px, 16px, 0);
      }
      65% {
        clip: rect(59px, 9999px, 50px, 0);
      }
      70% {
        clip: rect(41px, 9999px, 62px, 0);
      }
      75% {
        clip: rect(2px, 9999px, 82px, 0);
      }
      80% {
        clip: rect(47px, 9999px, 73px, 0);
      }
      85.0% {
        clip: rect(3px, 9999px, 27px, 0);
      }
      90% {
        clip: rect(26px, 9999px, 55px, 0);
      }
      95% {
        clip: rect(42px, 9999px, 97px, 0);
      }
      100% {
        clip: rect(38px, 9999px, 49px, 0);
      }
    }
  </style>

  <div class="glitch" data-text="BackTrack">BackTrack</div>
            <p class="center-texts">Programmed by: Russell Tabata</p>

            <style>

            .body {
              background: url("static/background.jpg") no-repeat fixed center;
              background-position: center;
              background-size: cover;
            }

            .center-texts {
              text-align: center;
              font-size: 20px;
              color: white;
              font-family: Verdana;
            }
            .center {
              display: block;
              margin-left: auto;
              margin-right: auto;
              width: 50%;
            }
            .myButton {
              margin-left: auto;
              margin-right: auto;
              display: block;
              background-color:#FF5453;
              border-radius:13px;
              border:1px solid #D65453;
              cursor:pointer;
              color:#ffffff;
              font-family: Verdana;
              font-size:17px;
              padding:16px 31px;
              text-decoration:none;
              text-shadow:0px 1px 0px #282d66;
            }
            .myButton:hover {
              background-color:#C15453;
            }
            .myButton:active {
              top:1px;
            }
            </style>
            
            <body class="body">
            <p> </p>
            <p> </p>
            <h2> </h2>

            <style>

* {
  margin: 0;
  padding: 0;
}

html,
body {

}

body {
  background: #FFF;
  font-family: 'Noto Sans JP', sans-serif;
  font-weight: 400;
}

.buttons {
  display: flex;
  flex-direction: row;
      flex-wrap: wrap;
  justify-content: center;
  text-align: center;
  width: 100%;
  height: 80%;
  margin: 0 auto;
/*   padding: 2em 0em; */
}

.container {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  background-color: transparent;

  width: 240px;
}

h1 {
  text-align: left;
  color: #444;
  letter-spacing: 0.05em;
  margin: 0 0 0.4em;
  font-size: 1em;
}

p {
  text-align: left;
  color: #444;
  letter-spacing: 0.05em;
  font-size: 0.8em;
  margin: 0 0 2em;
}


.btn {
  letter-spacing: 0.1em;
  cursor: pointer;
  font-size: 14px;
  font-weight: 400;
  line-height: 45px;
  max-width: 160px;
  position: relative;
  text-decoration: none;
  text-transform: uppercase;
  width: 100%;
}
.btn:hover {
  text-decoration: none;
}

/*btn_background*/
.effect04 {
  --uismLinkDisplay: var(--smLinkDisplay, inline-flex);
  display: var(--uismLinkDisplay);
  color: #000;
  outline: solid  2px #000;
  position: relative;
  transition-duration: 0.4s;
  overflow: hidden;
}

.effect04::before,
.effect04 span{
    margin: 0 auto;
  transition-timing-function: cubic-bezier(0.86, 0, 0.07, 1);
  transition-duration: 0.4s;
}

/* 文字1を上に */
.effect04:hover{

  background-color: transparent;
  backdrop-filter: blur(5px);
}

/* HOVERしたら文字1を上に */
.effect04:hover span{
  -webkit-transform: translateY(-400%) scale(-0.1,20);
          transform: translateY(-400%) scale(-0.1,20);
}

/*文字2*/

.effect04::before{
  content: attr(data-sm-link-text);
  /* color of the after text*/
  color:  #FFFFFF;
  position: absolute;
  left: 0;
  right: 0;
  -webkit-transform: translateY(500%) scale(-0.1,20);
          transform: translateY(500%) scale(-0.1,20);
}

/* HOVERしたら文字2を上に */
.effect04:hover::before{
  letter-spacing: 0.05em;
  -webkit-transform: translateY(0) scale(1,1);
          transform: translateY(0) scale(1,1);
}


            </style>
            <div class="buttons">
              <div class="container">
                  <button onclick="location.href='/book'" class="btn effect04" data-sm-link-text="Create new Track" target="_blank"><span>Start</span></button>      
              </div>


            </div>
          
            </body>
        '''

# ? INPUT book title, maybe make the 
# ? UI alittle nicer
# book = input("Input a book (only the title)> ")

@app.route('/book', methods=['GET', 'POST']) #allow both GET and POST requests
def book():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        book = request.form.get('book')
        page_py = wiki_wiki.page(book)

        # print("Page - Exists: %s" % page_py.exists())
        
        if page_py.exists() == True:
            print ("THE BOOK EXISTS!")
            return redirect(url_for("plot_input"))


        # ! If the book does not exist:
        else:
            return "that book doesn't exist"


    # form for submitting the book name
    return '''
              <style>

              .title-text {
                color: white;
                text-align: center;
                display: block;
                font-size: 60px;
                margin-right: auto;
                padding-bottom: 50px;
                margin-left: auto;
                font-family: Verdana;
              }

              .center-block {
                font-size: 35px;
                text-align: center;
                display: block;
                margin-right: auto;
                margin-left: auto;
                background-color: transparent; 
                font-family: Verdana;
                outline: none;
                color: white;
                border-style: none none solid none;
              }

              .center-submit {
                font-size: 35px;
                text-align: center;
                display: block;
                margin-right: auto;
                margin-left: auto;
                font-family: Verdana;
              }

              body {
                background-image: linear-gradient(to right, #000F29, #000F4B);
              }

              </style>
    
              <form method="POST">
              <body>
                  <h class="title-text">Input your Book:</h>
                  <input class="center-block" type="text" name="book" required><br>
                  <input class="center-submit" type="submit" value="Submit"><br>
              </form>
              </body>'''
            

if __name__ == "__main__":
    print ("were runnin it!")
    app.debug=True
  
    app.run()
