from dishka import Provider, Scope, provide

from bootstrap.configs import config, Config


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def get_config(self) -> Config:
        return config
