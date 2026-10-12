from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.routers import quiz, types

app = FastAPI(
    title="MBTI Website",
    description="FastAPI 기반 MBTI 성격유형 테스트",
    version="1.0.0"
)

# 정적 파일 & 템플릿 설정
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="templates")

# 라우터 등록
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(types.router, prefix="/types", tags=["Types"])


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """메인 페이지"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
async def health_check():
    """헬스 체크"""
    return {"status": "ok"}
