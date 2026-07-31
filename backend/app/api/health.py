from fastapi import APIRouter

from app.dependencies import SettingsDep

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check(settings: SettingsDep) -> dict:

    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }
