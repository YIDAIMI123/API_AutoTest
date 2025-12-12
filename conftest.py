import pytest
from common.yaml_util import clean_yaml

@pytest.fixture(scope="session", autouse=True)
def clean_ex():
    clean_yaml()