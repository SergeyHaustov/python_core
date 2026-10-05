class Doctor:
    def treat(self):
        pass


class Surgeon(Doctor):
    def treat(self):
        print("Операционное вмешательство.")


class Dentist(Doctor):
    def treat(self):
        print("Лечение зубов.")


class Therapist(Doctor):

    def treat(self):
        print("Первичный приём.")

    def appointment(self, patient):
        if patient.treatment_plan == 1:
            print("Назначен хирург.")
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            print("Назначен дантист.")
            patient.doctor = Dentist()
        else:
            print("Назначен терапевт.")
            patient.doctor = Therapist()
        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan, doctor):
        self.treatment_plan = treatment_plan
        self.doctor = doctor


patient1 = Patient(1, None)
therapist = Therapist()
therapist.appointment(patient1)
