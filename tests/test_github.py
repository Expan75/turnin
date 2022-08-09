from turnin.github import GitHub


def test_exists(github: GitHub):
    assert github is not None