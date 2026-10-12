# MBTI Website

FastAPI 기반 MBTI 성격유형 테스트 웹사이트입니다.

## 기술 스택
- Python 3.10+
- FastAPI
- Jinja2 (템플릿)
- Uvicorn

## 프로젝트 구조

```
mbti-website/
├── app/
│   ├── main.py              # FastAPI 앱 진입점
│   ├── routers/             # 라우터
│   │   ├── quiz.py          # 퀴즈 관련
│   │   └── types.py         # 유형 목록/상세
│   ├── services/            # 비즈니스 로직
│   │   └── mbti_calculator.py
│   ├── data/                # 데이터
│   │   ├── questions.py     # 퀴즈 문항
│   │   └── types_data.py    # 16유형 설명
│   └── static/              # CSS, JS, 이미지
├── templates/               # Jinja2 템플릿
├── requirements.txt
└── README.md
```

## 시작하기

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 서버 실행 (프로젝트 루트에서)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

브라우저에서 http://localhost:8000 접속

## 주요 기능
- 12문항 MBTI 테스트
- 16가지 유형 상세 설명 (특징, 강점, 약점, 추천 직업)
- 반응형 UI

## 배포
GitHub에 올린 후 Render / Railway 등으로 배포 가능합니다.
