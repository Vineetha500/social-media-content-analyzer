import re
from typing import List, Dict


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def count_characters(text: str) -> int:
    return len(text)


def detect_hashtags(text: str) -> List[str]:
    return re.findall(r"#\w+", text)


def detect_questions(text: str) -> bool:
    return "?" in text


def detect_call_to_action(text: str) -> bool:
    cta_patterns = [
        r"\bcomment\b",
        r"\bshare\b",
        r"\blike\b",
        r"\bfollow\b",
        r"\bsubscribe\b",
        r"\blearn more\b",
        r"\bclick\b",
        r"\btell us\b",
        r"\blet me know\b",
        r"\bjoin\b",
        r"\btry\b",
        r"\bdownload\b",
    ]

    text_lower = text.lower()

    return any(
        re.search(pattern, text_lower)
        for pattern in cta_patterns
    )


def calculate_hook_score(text: str) -> int:
    """
    Estimate hook quality using simple heuristics.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return 20

    first_line = lines[0]

    score = 40

    if len(first_line) <= 120:
        score += 15

    if "?" in first_line:
        score += 15

    attention_words = [
        "how",
        "why",
        "what",
        "secret",
        "mistake",
        "guide",
        "tips",
        "important",
        "new",
        "learn",
        "discover",
    ]

    if any(word in first_line.lower() for word in attention_words):
        score += 15

    if any(char.isdigit() for char in first_line):
        score += 10

    return min(score, 100)


def calculate_readability_score(text: str) -> int:
    """
    Lightweight readability heuristic.
    """

    words = count_words(text)

    if words == 0:
        return 0

    sentences = re.split(r"[.!?]+", text)
    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    sentence_count = max(len(sentences), 1)

    average_words_per_sentence = words / sentence_count

    if average_words_per_sentence <= 12:
        return 95

    if average_words_per_sentence <= 18:
        return 85

    if average_words_per_sentence <= 25:
        return 70

    if average_words_per_sentence <= 35:
        return 55

    return 40


def calculate_cta_score(text: str) -> int:
    if detect_call_to_action(text):
        return 100

    if detect_questions(text):
        return 65

    return 25


def calculate_hashtag_score(text: str) -> int:
    hashtags = detect_hashtags(text)

    if 2 <= len(hashtags) <= 5:
        return 100

    if len(hashtags) == 1:
        return 60

    if len(hashtags) == 0:
        return 30

    return 55


def calculate_engagement_score(
    hook: int,
    readability: int,
    cta: int,
    hashtags: int,
    engagement: int,
) -> int:

    score = (
        hook * 0.25
        + readability * 0.20
        + cta * 0.20
        + hashtags * 0.10
        + engagement * 0.25
    )

    return round(score)


def calculate_engagement_potential(text: str) -> int:
    score = 40

    if detect_questions(text):
        score += 20

    if detect_call_to_action(text):
        score += 20

    engagement_words = [
        "you",
        "your",
        "we",
        "community",
        "experience",
        "opinion",
        "think",
        "agree",
    ]

    matches = sum(
        1
        for word in engagement_words
        if re.search(rf"\b{word}\b", text.lower())
    )

    score += min(matches * 5, 20)

    return min(score, 100)


def detect_tone(text: str) -> str:
    text_lower = text.lower()

    professional_words = [
        "business",
        "strategy",
        "company",
        "industry",
        "professional",
        "career",
        "technology",
    ]

    positive_words = [
        "great",
        "excellent",
        "success",
        "amazing",
        "happy",
        "excited",
        "love",
        "best",
    ]

    casual_words = [
        "hey",
        "awesome",
        "cool",
        "wow",
        "lol",
        "fun",
    ]

    professional_score = sum(
        word in text_lower for word in professional_words
    )

    positive_score = sum(
        word in text_lower for word in positive_words
    )

    casual_score = sum(
        word in text_lower for word in casual_words
    )

    if professional_score >= 2:
        return "Professional"

    if casual_score >= 2:
        return "Casual"

    if positive_score >= 2:
        return "Positive"

    return "Neutral"


def generate_strengths(
    text: str,
    hook: int,
    readability: int,
    cta: int,
    hashtags: int,
    engagement: int,
) -> List[str]:

    strengths = []

    if hook >= 75:
        strengths.append(
            "The opening has a strong attention-grabbing structure."
        )

    if readability >= 80:
        strengths.append(
            "The content is easy to read and understand."
        )

    if cta >= 75:
        strengths.append(
            "The post includes a clear call to action."
        )

    if hashtags >= 75:
        strengths.append(
            "The post uses a reasonable number of hashtags."
        )

    if engagement >= 75:
        strengths.append(
            "The content encourages audience interaction."
        )

    if detect_questions(text):
        strengths.append(
            "The post uses a question to encourage responses."
        )

    if not strengths:
        strengths.append(
            "The post has a clear central topic."
        )

    return strengths


def generate_suggestions(
    text: str,
    hook: int,
    readability: int,
    cta: int,
    hashtags: int,
    engagement: int,
) -> List[str]:

    suggestions = []

    if hook < 70:
        suggestions.append(
            "Strengthen the opening with a question, statistic, "
            "benefit, or curiosity-driven statement."
        )

    if readability < 70:
        suggestions.append(
            "Break long sentences and paragraphs into shorter, "
            "easier-to-scan sections."
        )

    if cta < 70:
        suggestions.append(
            "Add a clear call to action such as asking readers "
            "to comment, share an opinion, or try something."
        )

    hashtag_count = len(detect_hashtags(text))

    if hashtag_count == 0:
        suggestions.append(
            "Consider adding 2–4 highly relevant hashtags."
        )
    elif hashtag_count > 8:
        suggestions.append(
            "Reduce the number of hashtags and keep only the "
            "most relevant ones."
        )

    if engagement < 70:
        suggestions.append(
            "Make the post more interactive by asking a specific "
            "question or inviting readers to share an experience."
        )

    word_count = count_words(text)

    if word_count > 300:
        suggestions.append(
            "Consider shortening the post or adding headings/bullets "
            "to make it easier to scan."
        )

    if word_count < 30:
        suggestions.append(
            "Add useful context, examples, or a stronger explanation "
            "to provide more value."
        )

    if not suggestions:
        suggestions.append(
            "The post is already well structured. Test different "
            "hooks and calls to action to optimize further."
        )

    return suggestions


def analyze_text(text: str) -> Dict:

    text = text.strip()

    word_count = count_words(text)
    character_count = count_characters(text)

    hook = calculate_hook_score(text)
    readability = calculate_readability_score(text)
    cta = calculate_cta_score(text)
    hashtags = calculate_hashtag_score(text)
    engagement = calculate_engagement_potential(text)

    final_score = calculate_engagement_score(
        hook,
        readability,
        cta,
        hashtags,
        engagement,
    )

    return {
        "word_count": word_count,
        "character_count": character_count,
        "engagement_score": final_score,
        "tone": detect_tone(text),
        "score_breakdown": {
            "hook": hook,
            "readability": readability,
            "call_to_action": cta,
            "hashtags": hashtags,
            "engagement": engagement,
        },
        "strengths": generate_strengths(
            text,
            hook,
            readability,
            cta,
            hashtags,
            engagement,
        ),
        "suggestions": generate_suggestions(
            text,
            hook,
            readability,
            cta,
            hashtags,
            engagement,
        ),
    }