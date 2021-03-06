#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""Primary configuration file for DesertPy Pelican Site"""

AUTHOR = u'DesertPy Pythonistas'
SITENAME = u'DesertPy'
SITEURL = 'http://desertpy.com'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
         ('Python.org', 'http://python.org'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/desertpy'),
          ('Github', 'https://github.com/desertpy'),
          ('Google+',
              'https://plus.google.com/communities/103511724147602323431'),
          ('Meetup', 'http://www.meetup.com/Phoenix-Python-Meetup-Group'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
PAGE_DIR = 'pages'

# Add page titles here if you don't want them linked to automatically
EXCLUDED_PAGES = ('Web Chat')

# this should be true for dev purposes otherwise you don't see your specified
# css, uh, I think
RELATIVE_URLS = True
GOOGLE_ANALYTICS = 'UA-39513587-1'
DISQUS_SITENAME = "desertpy"
THEME = "themes/subtle"

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
