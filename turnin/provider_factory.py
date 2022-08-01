from turnin.provider import Provider
from turnin.github import GitHub
from turnin.config import Configuration


def create_provider(configuration: Configuration) -> Provider:
    providers = {"GitHub": GitHub(configuration)}
    if (provider := providers.get(configuration.provider)) is None:
        raise NotImplementedError(
            f"{configuration.provider} is not an implmented provider"
        )
    return provider
