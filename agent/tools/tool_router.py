from scheduler.appointment_engine.engine import book_appointment

def execute_tool(intent_data):

    intent = intent_data["intent"]

    if intent == "book_appointment":

        return book_appointment(
            patient_id=1,
            doctor_id=101,
            date=intent_data["date"],
            time=intent_data.get("time", "10:00")
        )

    if intent == "cancel_appointment":

        return {"message": "Appointment cancelled"}

    return {"message": "Unknown request"}