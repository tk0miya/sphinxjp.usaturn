================
sphinxjp.usaturn
================

`sphinxjp.usaturn` is sphinx extension to add `usaturn` admonition.
This extension enable you to add wonderful admonition notaiton.

Example::

  .. usaturn:: Hello world!



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


Repository
==========

This code is hosted by Bitbucket.

  https://bitbucket.org/tk0miya/sphinxjp.usaturn


License
=======
Apache License 2.0
