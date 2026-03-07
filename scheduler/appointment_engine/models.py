from pydantic import BaseModel
from datetime import date

class Appointment(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: str
    status: str