import pytest
from turnin import provider_factory
from turnin.config import Configuration


def test_should_allow_valid(configuration: Configuration):
    configuration.provider = "GitHub"
    provider = provider_factory.create_provider(configuration)


def test_should_reject_invalid(configuration: Configuration):
    configuration.provider = "Blah"
    with pytest.raises(NotImplementedError):
        provider_factory.create_provider(configuration)
