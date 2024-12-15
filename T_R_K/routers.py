from aiogram import Router

from FSM_Calories import router as calories_router
from Common import router as common_router
from menu import router as main_menu_router
from menu_buy import router as catalog_router

main_router = Router(name=__name__)

main_router.include_routers(
    calories_router,
    main_menu_router,
    catalog_router
)

# this one has to be the last!
main_router.include_router(common_router)