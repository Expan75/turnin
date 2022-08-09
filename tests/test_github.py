import pytest
from turnin.github import (
    GitHub, 
    OauthChallengeResponse,
    DeviceAccessTokenResponse
)


@pytest.fixture
def oauth_response() -> OauthChallengeResponse:
    return OauthChallengeResponse(**{
        "device_code": "",
        "user_code": "",
        "verification_uri": "",
        "expires_in": 5,
        "interval": 5,
    })

@pytest.fixture
def access_token_response() -> DeviceAccessTokenResponse:
    return OauthChallengeResponse(**{
        "device_code": "",
        "user_code": "",
        "verification_uri": "",
        "expires_in": 5,
        "interval": 5,
    })


def test_exists(github: GitHub):
    assert github is not None