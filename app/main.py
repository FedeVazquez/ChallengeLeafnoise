from fastapi import FastAPI

from app.api.employee_controller import router as employee_router
from app.api.auth_controller import router as auth_router


app = FastAPI(
    title="PeopleFlow Employees API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(employee_router)


@app.get("/")
def health():
    return {"status": "ok"}
    