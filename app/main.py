from fastapi import FastAPI
from app.api.v1.routes import health, items
from app.core.exceptions import register_exception_handlers
from app.middleware.logging import LoggingMiddleware

app = FastAPI(title="Backend Server", version="1.0.0")

app.add_middleware(LoggingMiddleware)
register_exception_handlers(app)

app.include_router(health.router, tags=["health"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
