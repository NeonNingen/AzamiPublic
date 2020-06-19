[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://forthebadge.com)
[<img src="https://img.shields.io/badge/discord.py-rewrite-blue.svg?style=flat-square">](https://github.com/Rapptz/discord.py/tree/rewrite)
[<img src="https://img.shields.io/badge/python-3.8.2-brightgreen.svg?style=flat-square">](https://www.python.org/downloads/release/python-382/)
[![](https://img.shields.io/discord/711685458714689616.svg?style=flat-square&label=Support%20Guild&colorB=D896FF)](https://discord.com/invite/rRb23dt)
[![Build Status](https://travis-ci.org/pawbot-discord/Pawbot.svg?branch=master)](https://travis-ci.org/pawbot-discord/Pawbot)

Azami Public Release
-------------------------

**Azami was developed in python under the rewrite branch. Made by NeonNingen**\
**This bot is open source! So play with it to your heart contents!**\
**You can rename this bot or change anything you like! Go to events.py to do so**

##### Use a!help for Azami's commands

<ins> __Update log:__ </ins>

```python
Update #1 (19/06/2020) V1.0 Public Release
```

##### [Api Wrapper from Rapptz](https://github.com/Rapptz/discord.py)

##### [Current Azami V2.1 invite link](https://discord.com/oauth2/authorize?client_id=639574438794231818&permissions=8&scope=bot)

Running
---------------------------

#### These steps are for Windows users only!

Installation steps are:

1) ##### When downloading make sure to check which type of Azami you want. Look at the branches, you can either choose master (With webdriver) or non-webdriver

2) ##### Make sure to get Python 3.6 or higher, to run the bot!

3) ##### Set up a venv so do `python -m venv venv`

4) ##### Install dependencies `pip install -U -r requirements.txt`

5) ##### You can run this bot locally or with Heroku. Either follow step 5 to run locally or scroll down to Heroku to run 24/7.

6) ##### Create a discord bot at the Discord Developer Portal and make a token.txt in the Azami directory and paste the token there!

7) ##### Note: Google chrome webdriver needs to be installed from [GC webdriver](https://chromedriver.chromium.org/downloads). Place the webdriver in your Azami directory. You can use other webdrivers if you know how to. E.g. Firefox webdriver. 

8) ##### Go to the directory where you installed download Azami to and write cmd in the address bar

9) ##### Finally write `python -m main` and press enter, and the bot will run


**Super important note: Make sure to go to events.py and change line 8 owner id to your user id. More detailed explanation in events.py. Allows for owner commands Also make sure you have pip to do step 3**

#### That's it successful running locally!

Heroku
---------------------------

### You can run Azami on Heroku so she can be hosted 24/7

Steps are:

1) ##### You will need to create a public or private repository on Github and put the bot's directory onto that repo. [How to create a repo](https://www.youtube.com/watch?v=hMfi_ONvGEs) 

2) ##### You then need to make a Heroku account and create an app. Make sure to pick your region. Do not add a pipeline

3) ##### Go to settings and make sure to add buildpack python

4) ##### Then reveal config vars and set KEY to DISCORD_TOKEN

5) ##### Then set VALUE to your token which can be found in the discord developer portal

6) ##### Press Add and then go to Deploy. And select GitHub and add your Github repo

7) ##### From experience, some times it may fail when entering your Github repo so do step 6 over and over again. In terms of trying to connect to your Github repo

8) ##### Scroll down a little and there should be an option called automatic deployment press on it.

9) ##### Go to overview and press Configure Dynos and turn on the dyno.

10) ##### I'll leave a tutorial on how to get google chrome webdriver to work on Heroku. Doing this step allows you to remove webdriver from your directory on GitHub. If you want to. [Here is the tutorial, click me!](https://www.youtube.com/watch?v=Ven-pqwk3ec)

11) ##### Finally, after all that. Just push a new build of your Azami repo and walla. 24/7 Azami. 

### Last Note: Check out main.py it gives some explanation about this bot

#### That it for me, Thanks for using Azami! 

## The GNU General Public License v3.0

