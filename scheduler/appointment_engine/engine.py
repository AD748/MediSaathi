appointments = []

def book_appointment(patient_id, doctor_id, date, time):

    for a in appointments:
        if a["doctor_id"] == doctor_id and a["date"] == date and a["time"] == time:
            return {"error": "Slot already booked"}

    appointment = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "status": "confirmed"
    }

    appointments.append(appointment)

    return {"message": "Appointment confirmed", "appointment": appointment}