from turnin import config


valid_config = {
    "provider": "GitHub",
    "user_email": "example@example.com",
    "instructor_email_addresses": ["example@example.com"],
}
provider, email, instructor = valid_config.values()


def test_exists(configuration: config.Configuration):
    assert configuration is not None


def test_should_retry_with_invalid_provider(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "1")
    selected_provider = config.Configuration.prompt_provider("some provider idk")
    assert provider == selected_provider


def test_should_retry_with_invalid_email(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: email)
    selected_email = config.Configuration.prompt_email("miss", "matched")
    assert email == selected_email


def test_should_allow_valid_instructor(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: email)
    instructors = config.Configuration.prompt_instructors()
    assert instructors[0] == email


def test_should_not_overwrite_unless_explicit(monkeypatch):
    config.Configuration(**valid_config).write()
    monkeypatch.setattr("builtins.input", lambda x: "n")
    assert config.Configuration.initialize() is not None