# MBTI Website

FastAPI 기반 MBTI 성격유형 테스트 웹사이트입니다.

## 기술 스택
- Python
- FastAPI
- Jinja2 (템플릿)

## 시작하기

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload
```

## 배포
GitHub에 올린 후 Render / Railway 등으로 배포 예정입니다.
