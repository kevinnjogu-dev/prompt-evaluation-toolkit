"""
Prompt scoring functions.
"""


def instruction_score(prompt):
    length = len(prompt.split())

    if length >= 20:
        return 5
    elif length >= 12:
        return 4
    elif length >= 8:
        return 3
    elif length >= 4:
        return 2
    return 1


def clarity_score(prompt):
    prompt = prompt.lower()

    keywords = [
        "explain",
        "summarize",
        "compare",
        "list",
        "describe",
        "analyze",
    ]

    score = sum(keyword in prompt for keyword in keywords)

    return min(score + 2, 5)


def overall_score(prompt):
    instruction = instruction_score(prompt)
    clarity = clarity_score(prompt)

    return round((instruction + clarity) / 2, 2)