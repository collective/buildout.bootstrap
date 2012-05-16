Introduction
============

*Formerly collective.recipe.bootstrap*

``buildout.bootstrap`` is a buildout extension that adds a buildout *bootstrap.py* file to your buildout.

It satisfies the use case of::

    "I want to keep my buildout's bootstrap.py file up to date without having to manually download it" 

It also makes it easy to add a *bootstrap.py* file to a buildout created via::

    $ buildout init

If you still don't understand consider the following: with this extension you can avoid having to type::

    $ curl -O https://raw.github.com/buildout/buildout/master/bootstrap/bootstrap.py

You typically use this extension when you have created a new buildout and want to

    - Check it in to version control
    - Check it out somewhere else

See ``docs/INSTALL.txt`` for installation instructions.

