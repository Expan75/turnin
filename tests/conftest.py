import pytest
from turnin.config import Configuration
from turnin.github import GitHub


@pytest.fixture
def configuration() -> Configuration:
    return Configuration("GitHub", "test@testing.com", ["instructor@instructorson.com"])


@pytest.fixture
def github(configuration: Configuration) -> GitHub:
    return GitHub(configuration)