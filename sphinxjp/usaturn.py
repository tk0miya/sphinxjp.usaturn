# -*- coding: utf-8 -*-

import os
from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.util.osutil import copyfile

USATURN_CSS = 'usaturn.css'


def html_visit_usaturn(self, node):
    url = "https://pbs.twimg.com/profile_images/1365715199/md_400x400.png"

    self.body.append(self.starttag(node, 'div', CLASS='admonition usaturn'))
    self.body.append(self.starttag(node, 'div', CLASS='icon'))
    self.body.append(self.starttag(node, 'img', src=url, empty=True))
    self.body.append('<br />')
    self.body.append(self.starttag(node, 'div', CLASS='name'))
    self.body.append(u'うさたーん')
    self.body.append('</div>\n')
    self.body.append('</div>\n')
    self.body.append(self.starttag(node, 'div', CLASS='message'))


def html_depart_usaturn(self, node):
    self.body.append('</div>\n')
    self.body.append('</div>\n')


class usaturn(nodes.Admonition, nodes.Element):
    pass


class UsaturnAdmonition(BaseAdmonition):
    node_class = usaturn


def on_builder_inited(app):
    app.add_stylesheet(USATURN_CSS)


def on_build_finished(app, exception):
    if app.builder.name != 'html' or exception:
        return

    app.info('Copying requirements stylesheet... ', nonl=True)
    dest = os.path.join(app.builder.outdir, '_static', USATURN_CSS)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), USATURN_CSS)
    copyfile(source, dest)
    app.info('done')


def setup(app):
    app.add_node(usaturn,
                 html=(html_visit_usaturn, html_depart_usaturn))
    app.add_directive('usaturn', UsaturnAdmonition)
    app.connect('builder-inited', on_builder_inited)
    app.connect('build-finished', on_build_finished)
