patients = {}

def save_patient_history(patient_id, appointment):

    if patient_id not in patients:
        patients[patient_id] = []

    patients[patient_id].append(appointment)


def get_patient_history(patient_id):

    return patients.get(patient_id, [])