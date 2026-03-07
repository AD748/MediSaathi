def interpret(text: str):

    text = text.lower()

    if "book" in text:
        return {
            "intent": "book_appointment"
        }

    if "cancel" in text:
        return {
            "intent": "cancel_appointment"
        }

    return {"intent": "unknown"}