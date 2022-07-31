import os
import pytest
import tempfile
from turnin import config

valid_provider = { 1: "GitHub" }
valid_email = "example@example.com" 


def test_exists(configuration: config.Configuration):
    assert configuration is not None


def test_should_retry_with_invalid_provider(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "1")
    provider = config.Configuration.prompt_provider("some provider idk")
    assert provider == valid_provider[1]    


def test_should_retry_with_invalid_email(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: valid_email)
    email = config.Configuration.prompt_email("miss", "matched")
    assert email == valid_email


def test_should_allow_valid_instructor(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: valid_email)
    instructors = config.Configuration.prompt_instructors()
    assert instructors[0] == valid_email


def test_should_not_overwrite_unless_explicit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "n") 
    assert config.Configuration.initialize() is None