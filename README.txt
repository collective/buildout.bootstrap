
Introduction
============

``buildout.bootstrap`` (formerly collective.recipe.bootstrap) is a zc.buildout extension 
that adds a (zc.buildout) ``bootstrap.py`` file to your buildout.

It satisfies the use case of::

    "I want to keep my buildout's bootstrap.py file up to date without having to manually download it from svn.zope.org." 

It also makes it possible (and easy) to add a bootstrap.py file to a buildout created
via the command: ``buildout init``. 

If at this point you still don't understand, consider the following. With this extension
you can avoid having to type::

    $ wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py

You mostly use this when you have initialized a new buildout (e.g. with
``buildout init``) and you want to: 

    - Check in the buildout to a version control system
    - Check out the buildout elsewhere and bootstrap it

See ``docs/INSTALL.txt`` for installation instructions.

