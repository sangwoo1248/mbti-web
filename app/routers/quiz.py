from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List

from app.services.mbti_calculator import calculate_mbti

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def quiz_page(request: Request):
    """퀴즈 시작 페이지"""
    from app.data.questions import QUESTIONS
    return templates.TemplateResponse(
        "quiz.html",
        {"request": request, "questions": QUESTIONS}
    )


@router.post("/result", response_class=HTMLResponse)
async def quiz_result(request: Request):
    """퀴즈 결과 처리"""
    form_data = await request.form()
    
    # 답변 수집 (q1, q2, ... 형태)
    answers = []
    for key, value in form_data.items():
        if key.startswith("q"):
            answers.append(value)
    
    # MBTI 계산
    mbti_type = calculate_mbti(answers)
    
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "mbti_type": mbti_type,
        }
    )
