================
sphinxjp.usaturn
================

`sphinxjp.usaturn` is sphinx extension to add `usaturn` admonition.
This extension enable you to add wonderful admonition notaiton.

Example::

  .. usaturn:: Hello world!

  .. usaturn:: Hello world!
     :align: right


Who's usaturn?
================

Go Yamada (@usaturn) is Sphinx evangelist in Japan.
He is a chairman of `SphinxCon JP 2014`_ .

.. _SphinxCon JP 2014: http://sphinx-users.jp/event/20141026_sphinxconjp/index.html

With gratitude.

Setting
=======

You can see available package at `PyPI <http://pypi.python.org/pypi/sphinxjp.shibukawa>`_.

You can get source code at http://bitbucket.org/tk0miya/

Install
-------

Use pip::

   $ pip install sphinxjp.usaturn


Configure Sphinx
----------------

To enable this extension, add ``sphinxjp.usaturn`` module to extensions
option at :file:`conf.py`.

.. code-block:: python

   # Enabled extensions
   extensions = ['sphinxjp.usaturn']


Directive
=========

.. describe:: .. usaturn::

   This directive insert a `usaturn` admonition into the document.

   Example::

     .. usaturn:: Hello world!

     .. usaturn:: Hello world!
        :align: right

   .. usaturn:: Hello world!

   .. usaturn:: Hello world!
      :align: right


Internal API
=============

`sphinxjp.usaturn` adds `add_character_admonition()` as sphinx API.

.. describe:: add_character_admonition(character_name, image_url, label)

   Define new admonition directive.

   Example::

     def setup(app):
         app.add_character_admonition('debian',
                                      'https://www.debian.org/logos/openlogo-nd-100.jpg',
                                      'Debian')

   After that, `sphinxjp.usaturn` defines `debian` admonition directive.
   It has 'Debian' label and specified logo as its image.

   Example::

     .. usaturn:: Hello world!

     .. debian:: Hello debian world!
        :align: right

   .. usaturn:: Hello world!

   .. debian:: Hello debian world!
      :align: right


Repository
==========

This code is hosted by Bitbucket.

  https://bitbucket.org/tk0miya/sphinxjp.usaturn


License
=======
Apache License 2.0
