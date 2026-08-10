from fastapi import APIRouter

from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.leads import router as leads_router
from app.api.v1.routes.dashboard import router as dashboard_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(leads_router)
router.include_router(dashboard_router)