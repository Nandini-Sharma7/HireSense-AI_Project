def generate_suggestions(
    speech,
    face,
    nlp,
    resume
):

    suggestions = []

    if speech < 70:
        suggestions.append(
            "Improve communication clarity and reduce filler words."
        )

    if face < 70:
        suggestions.append(
            "Maintain better facial confidence and eye contact."
        )

    if nlp < 70:
        suggestions.append(
            "Answer lacks technical relevance to the job description."
        )

    if resume < 70:
        suggestions.append(
            "Resume can be improved by adding more relevant skills."
        )

    if len(suggestions) == 0:
        suggestions.append(
            "Excellent overall interview performance."
        )

    return suggestions