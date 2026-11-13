<<<<<<< HEAD
from fastapi import FastAPI
from routes.employee_routes import router as employee_router
from routes import auth
=======

from fastapi import FastAPI
from routes.employee_routes import router as employee_router
>>>>>>> 147883357cd62047c9454715a473cd5ae90caf9f

app = FastAPI(
    title="Employee Management API",
    description="Employee management using FastAPI and PostgreSQL",
    version="1.0.0"
)

<<<<<<< HEAD

app.include_router(auth.router)
=======
# Register employee routes
>>>>>>> 147883357cd62047c9454715a473cd5ae90caf9f
app.include_router(employee_router)


@app.get("/")
def home():
    return {
        "message": "Employee Management API is running"
    }