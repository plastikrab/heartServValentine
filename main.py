from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Указываем, где лежат наши HTML файлы
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Открываем index.html по корневой ссылке
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    # Запуск сервера на порту 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)