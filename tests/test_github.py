from turnin.github import GitHub


def test_exists(github: GitHub):
    assert github is not None


def test_should_authenticate(github: GitHub):
    access_token = github.authenticate()
    assert access_token is not None
