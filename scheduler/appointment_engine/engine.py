from backend.db.database import SessionLocal
from sqlalchemy import text


def check_availability(doctor_id, date):

    db = SessionLocal()

    result = db.execute(
        text("""
        SELECT time_slot FROM availability
        WHERE doctor_id = :doctor_id
        AND date = :date
        """),
        {"doctor_id": doctor_id, "date": date}
    )

    return [r[0] for r in result]


def book_appointment(patient_id, doctor_id, date, time):

    db = SessionLocal()

    conflict = db.execute(
        text("""
        SELECT * FROM appointments
        WHERE doctor_id=:doctor_id
        AND appointment_date=:date
        AND appointment_time=:time
        """),
        {"doctor_id": doctor_id, "date": date, "time": time}
    ).fetchone()

    if conflict:
        return {"error": "Slot already booked"}

    db.execute(
        text("""
        INSERT INTO appointments
        (patient_id, doctor_id, appointment_date, appointment_time, status)
        VALUES (:patient_id, :doctor_id, :date, :time, 'confirmed')
        """),
        {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date,
            "time": time
        }
    )

    db.commit()

    return {"message": "Appointment confirmed"}

def suggest_alternatives(doctor_id, date):

    available = check_availability(doctor_id, date)

    return {
        "message": "Requested slot unavailable",
        "available_slots": available
    }