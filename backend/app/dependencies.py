from typing import Annotated

from fastapi import Depends

from app.core.config import Settings, get_settings

# SettingsDep is a reusable, typed dependency. Any route can declare a
# parameter like `settings: SettingsDep` and FastAPI will call get_settings()
# and inject the result -- the route function never constructs Settings
# itself.
#
# This file is intentionally small right now. Starting in Phase 2/3, this is
# where a `DbSessionDep` (a database session per request) and a
# `CurrentUserDep` (the authenticated user, derived from a JWT) will be
# added, following this exact same pattern.
SettingsDep = Annotated[Settings, Depends(get_settings)]