from scheduler.appointment_engine.engine import book_appointment

def book_tool(patient_id, doctor_id, date, time):
    return book_appointment(patient_id, doctor_id, date, time)