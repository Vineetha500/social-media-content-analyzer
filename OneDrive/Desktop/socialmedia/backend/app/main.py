from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.analyze import router as analyze_router


app = FastAPI(
    title="Social Media Content Analyzer",
    description=(
        "Extract text from PDFs/images and analyze "
        "social media content for engagement."
    ),
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(analyze_router)


@app.get("/")
def root():
    return {
        "message": "Social Media Content Analyzer API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }