from scheduler.appointment_engine.engine import book_appointment


def book_tool(data):

    return book_appointment(
        patient_id=1,
        doctor_id=101,
        date=data["date"],
        time=data.get("time", "10:00")
    )
