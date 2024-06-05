from aiogram import Router

from filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import help, echo, scrape
    from .errors import error_handler

    router = Router()

    router.include_routers(help.router, echo.router, error_handler.router)

    return router
