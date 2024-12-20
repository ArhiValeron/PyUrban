from aiogram import Router

from T_R_K.handlers.FSM_Calories import router as calories_router
from T_R_K.handlers.common import router as common_router
from T_R_K.handlers.menu import router as main_menu_router
from T_R_K.handlers.menu_catalog import router as catalog_router
from T_R_K.handlers.FSM_RegistrationState import router as user_add_router

main_router = Router(name=__name__)

main_router.include_routers(
    calories_router,
    main_menu_router,
    catalog_router,
    user_add_router
)

# this one has to be the last!
main_router.include_router(common_router)