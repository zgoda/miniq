MiniQ
=====

Minimal template for Flask application. And I say minimal - no blueprints, no application factory, just couple views and some configuration but modularized for easier maintenance.

This is implemented as follow-up to `Charles Leifer blog post <https://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/>`_ on structuring simple Flask applications. This post has been written in 2013 and although Flask did not change much since, other parts of Flask (and Python) environment did. Many things now look different, and many tasks that seemed not worth the hassle now are much more approachable.

So this is 2020 version of simplest Flask application *done right*:

* application is installable with simple ``pip install -U -e .``
* application loads configuration from both shared ``.flaskenv`` and private ``.env`` files
* test-ready configuration in ``setup.cfg``
* code layout that requires installation before test, and tests installed code
* proper version configuration (``setup.py`` does not execute any application code)

This should be enough for simplest cases like personal blog or single purpose app.

This code is licensed under terms of 3-clause BSD licence but I do not require any attribution nor even mentioning the source if you use it as your own project boilerplate. However I do require full licence application if you intend to distribute it as template or other kind of starting point.
