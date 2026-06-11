# DANG-AI-AGENT

Production-ready AI mobile agent architecture with Flutter, FastAPI, PostgreSQL, OpenAI provider adapters, voice, chat, image generation, memory, dashboard, analytics, notifications, and authentication.

## Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Mobile

```bash
cd mobile_app
flutter pub get
flutter run
```

## Preview

Open `mobile_app/preview/index.html` to see the Thai dark mobile UI reference preview.

## Secrets

Do not commit real API keys. Copy `.env.example` to `.env` locally and set secrets there.
