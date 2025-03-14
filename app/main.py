from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_tables, delete_tables
from app.router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очишена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Выключение')


    

app = FastAPI(lifespan=lifespan,)


tasks = []

app.include_router(task_router)