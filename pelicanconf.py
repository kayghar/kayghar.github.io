#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kaveh Gharavi'
SITENAME = 'Conferment of the Thirty Birds'
SITEURL = ''

PATH = 'content'

#THEME = "/home/kaveh/kayghar.github/kayghar.github.io/theme"

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu Items at the top

MENUITEMS = (('Home', '/'),
            ('Blog', '/category/blog.html'),
            ('About Me', '/aboutme.html'),
            ('CV', '/cv.html'),
            ('GitHub', 'https://github.com/kayghar'),
            )

# Blogroll, i.e. 'links' in the footer
LINKS = (('GitHub', 'https://github.com/kayghar'),
        )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/kayghar'),)

DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False