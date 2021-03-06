buildout.bootstrap
==================

Buildout extension to download https://bootstrap.pypa.io/bootstrap-buildout.py automatically.

Introduction
------------

Formerly `collective.recipe.bootstrap <https://pypi.python.org/pypi/collective.recipe.bootstrap>`_

``buildout.bootstrap`` is a Buildout extension that adds a Buildout ``bootstrap.py`` file to your buildout.

It satisfies the use case:

    "I want to keep my buildout's bootstrap.py file up to date without having to download it manually."

It also makes it easy to add a ``bootstrap.py`` file to a buildout created via ``buildout init`` e.g.::

    $ buildout init

After running this command, you have a ``buildout.cfg`` that looks like this::

    [buildout]
    parts =

And you can now add the extension like so::

    [buildout]
    extensions = buildout.bootstrap
    parts =

Run buildout again and afterward you should have a ``bootstrap.py`` file. Once you have a ``bootstrap.py`` file you can bootstrap the buildout via::

    $ python bootstrap.py 

If you still don't understand, consider the following: with this extension you can avoid having to type::

    $ curl -O https://bootstrap.pypa.io/bootstrap-buildout.py

You typically use this extension when you have created a new buildout and want to:

- Check it in to version control
- Check it out somewhere else and bootstrap it with python only (i.e. no setuptools available)

Installation
------------

Add ``buildout.bootstrap`` to the ``extensions`` parameter in the buildout section of your ``buildout.cfg`` e.g.::

    [buildout]
    extensions = buildout.bootstrap
    parts =

Contributors
------------

- Alex Clark
- David Beitey
- Sean "nutjob" Kelly
