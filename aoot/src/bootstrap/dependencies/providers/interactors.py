from dishka import Provider, Scope, provide_all

from application.token import BuyTokens, AddTokens


class InteractorProvider(Provider):
    scope = Scope.REQUEST

    get_interactors = provide_all(BuyTokens, AddTokens)
