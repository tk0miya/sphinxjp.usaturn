# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

html_use_modindex = False
html_use_index = False
extensions = ['sphinxjp.usaturn']
source_suffix = '.rst'
master_doc = 'index'

project = u'sphinxjp.usaturn quick reference'
copyright = u'2014, Takeshi KOMIYA'


def setup(app):
    app.add_character_admonition('debian',
                                 'https://www.debian.org/logos/openlogo-nd-100.jpg',
                                 'Debian')
