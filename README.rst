MiniQ
=====

Minimal template for Flask application. And I say minimal - no blueprints, no application factory, just couple views and some configuration but modularised for easier maintenance.

This is implemented as follow-up to `Charles Leifer blog post <https://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/>`_ on structuring simple Flask applications. This post has been written in 2013 and although Flask did not change itself much since, other parts of Flask and Python environment did. Many things now look different, and many tasks that seemed not worth the hassle in 2013 now are much more approachable. Yes, I'm looking at you, packaging. This code is ready to be properly packaged.

So this is 2020 version of simplest Flask application *done right*:

* application is installable with simple ``pip install -U -e .``
* install ``wheel`` package and it becomes *packageable* into ``whl`` with ``python setup.py bdist_wheel``
* application loads configuration from both shared ``.flaskenv`` and private ``.env`` files
* test-ready configuration in ``setup.cfg``
* code layout that requires installation before test, and tests installed code
* proper version configuration (``setup.py`` does not execute any application code)

This should be enough for simplest cases like personal blog or single purpose app.

The reason
----------

There are a plenty of Flask tutorials and most of them uses single module approach - everything lands in single Python file, and this is perfectly valid for a tutorial. On the other end are documents on how to structure large Flask applications, like `the Digital Ocean one <https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications>`_ or even `hints in official Flask docs <https://flask.palletsprojects.com/en/1.1.x/patterns/packages/>`_. But what if your app is small and you want it to be easy to maintain and open to extend? Go read the above mentioned post from Charles Leifer and use this repo as a starting point.

Testing
-------

This code includes testing setup for pytest. To run tests 1st install test dependencies.

.. code:: shell-session

    $ pip install -U -r requirements.test.txt --upgrade-strategy eager

Your code should be properly installed in virtual environment, with basic ``venv`` that's included in Python distribution this looks like ``pip install -U -e . --upgrade-strategy eager``. The last part (``--upgrade-strategy eager``) simulates fresh install on new system where no previous versions exist. This should be included in all CI test configurations.

And then you may run full test suite with coverage report.

.. code:: shell-session

    $ python -m pytest -sx --cov-branch --cov-report term-missing:skip-covered --cov=miniq tests

Modding
-------

If you don't need to display anything, you may safely remove ``templates`` directory from application source tree. Flask has a direct dependency of Jinja2 templating engine but it's not initialised until any code calls for rendering a template. Other than that it's just a Flask application object. Go and abuse it.

That strange ORM
----------------

It's just one of the options. A no-brainer choice is `Flask-SQLAlchemy <https://pypi.org/project/Flask-SQLAlchemy/>`_ which is made by the same team that brings Flask, but you are not limited to it. There's also `Peewee <https://pypi.org/project/peewee/>`_ and `Pony <https://pypi.org/project/pony/>`_ and any of them is worth checking - Pony is fastest, Peewee has lowest memory footprint, SQLAlchemy has the best community around it. Choose your poison. Detailed instructions on Flask integration are available in their docs.

Licence compliance
------------------

This code is licensed under terms of 3-clause BSD licence but I do not require any attribution nor even mentioning the source if you use it as your own project boilerplate. However I do require full licence application if you intend to distribute it as template or other kind of starting point.
