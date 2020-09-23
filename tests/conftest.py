import os

import pytest
from flask.wrappers import Response
from werkzeug.utils import cached_property


class TestResponse(Response):

    @cached_property
    def text(self):
        if self.mimetype.startswith('text'):
            return self.data.decode(self.charset)
        return self.data


@pytest.fixture()
def app():
    os.environ['FLASK_ENV'] = 'test'
    from miniq.main import app
    app.response_class = TestResponse
    with app.app_context():
        yield app
