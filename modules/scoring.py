def final_score(speech, face, nlp):

    final = (
        0.3 * speech +
        0.3 * face +
        0.4 * nlp
    ) / 10

    return round(final, 2)