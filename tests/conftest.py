import pytest
from matrix_output import app as output_app
from matrix_processing import app as processing_app


@pytest.fixture
def processing_client():
    processing_app.config["TESTING"] = True
    with processing_app.test_client() as client:
        yield client


@pytest.fixture
def output_client():
    output_app.config["TESTING"] = True
    with output_app.test_client() as client:
        yield client
