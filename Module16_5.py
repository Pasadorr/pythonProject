from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from contextlib import asynccontextmanager
templates = Jinja2Templates(directory="templates")
# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int
# Список пользователей
users: List[User] = []
# Создаем экземпляр FastAPI
app = FastAPI()
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Инициализация пользователей
    users.append(User(id=1, username="UrbanUser", age=24))
    users.append(User(id=2, username="UrbanTest", age=22))
    users.append(User(id=3, username="Capybara", age=60))
    yield  # Приложение будет работать в этом состоянии
    # Завершение
    users.clear()  # Очистка данных при завершении
# Привязываем lifespan
app.lifespan = lifespan
# GET запрос для получения списка всех пользователей через HTML-шаблон
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    try:
        return templates.TemplateResponse("users.html", {"request": request, "users": users})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении пользователей: {e}")
# GET запрос для получения информации о пользователе через HTML-шаблон
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("user.html", {"request": request, "user": user})
# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user