# KahootFlooder
A simple working Kahoot flooder written in Python using Selenium.

# Warning
Each bot uses ~50 Mb's of ram, thus using too many bots may make your machine unresponsive.

# Usage
 
## Install Selenium 
 
1. Open a command prompt as admin
2. run ``python -m pip install selenium`` (`python3` on Linux)
    
## Install ChromeDriver (Windows)
 
1. Download the relevant Windows version of the ChromeDriver from (http://chromedriver.chromium.org/downloads)
2. Extract `chromedriver.exe` from the zip file
3. Move the file to `C:\Program Files (x86)\Python`
    
## Setting up the bot
 
1. Download the kahoot_flooder.py file from this repository
2. Run the file from the command line with the relevant game pin, bot count and bot prefix
3. ``python kahoot_flooder.py --pin 3803477 --count 5 --prefix "bot_gba"``
    
# File arguments
```commandline
usage: kahoot_flooder.py [-h] --pin PIN --count COUNT --prefix PREFIX

Simple script to flood kahoot games

options:
  -h, --help       show this help message and exit
  --pin PIN        Kahoot game pin
  --count COUNT    Amount of bots
  --prefix PREFIX  Prefix for bots (name=prefix{botNumber})
```

# Todo
   - Re-implement everything properly (direct requests with websockets as opposed to spinning up a new browser tab/process per bot)
   - Add option to bypass 2 factor joining
