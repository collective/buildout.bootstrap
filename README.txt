
Introduction
============

``buildout.bootstrap`` (formerly collective.recipe.bootstrap) is a zc.buildout extension 
that adds a (zc.buildout) ``bootstrap.py`` file to your buildout.

It satisfies the use case of::

    "I want to keep my buildout's bootstrap.py file up to date 
    without having to manually download it from svn.zope.org." 

It also makes it possible (and easy) to add a bootstrap.py file to a buildout created
via the command: ``buildout init``. 

If at this point you still don't understand, consider the following. With this extension
you can avoid having to type::

    % wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/bootstrap.py


Installation
============

To use this zc.buildout extension, just add a new extension called ``buildout.bootstrap``
to the buildout section of your ``buildout.cfg``::

    [buildout]
    extensions = 
        ...
        buildout.bootstrap

Now whenever you run Buildout this extension will add or update your
buildout's bootstrap.py file, leaving you free to do other more important
things: like write, test, and deploy your code!
