from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.data.types_data import MBTI_TYPES

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def types_list(request: Request):
    """16가지 유형 목록"""
    return templates.TemplateResponse(
        "types.html",
        {"request": request, "types": MBTI_TYPES}
    )


@router.get("/{type_code}", response_class=HTMLResponse)
async def type_detail(request: Request, type_code: str):
    """특정 유형 상세 페이지"""
    type_code = type_code.upper()
    
    if type_code not in MBTI_TYPES:
        raise HTTPException(status_code=404, detail="존재하지 않는 MBTI 유형입니다.")
    
    return templates.TemplateResponse(
        "type_detail.html",
        {
            "request": request,
            "mbti_type": type_code,
            "type_info": MBTI_TYPES[type_code]
        }
    )
