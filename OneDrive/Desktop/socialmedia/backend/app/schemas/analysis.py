from typing import List

from pydantic import BaseModel


class ScoreBreakdown(BaseModel):
    hook: int
    readability: int
    call_to_action: int
    hashtags: int
    engagement: int


class AnalysisResponse(BaseModel):
    filename: str
    file_type: str
    extracted_text: str
    word_count: int
    character_count: int
    engagement_score: int
    tone: str
    score_breakdown: ScoreBreakdown
    strengths: List[str]
    suggestions: List[str]