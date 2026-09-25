import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

# ============================================================
# SETUP
# ============================================================

fake = Faker("en_IN")
Faker.seed(42)
np.random.seed(42)
random.seed(42)

N_PATIENTS = 5000
N_DOCTORS = 50
N_APPOINTMENTS = 20000
N_ADMISSIONS = 5000
N_TREATMENTS = 10000
N_BILLS = 15000
N_FEEDBACK = 8000

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 9, 1)

# ============================================================
# 1. DEPARTMENTS
# ============================================================

departments_data = [
    [1, "Cardiology", "Block A - 1st Floor"],
    [2, "Orthopedics", "Block A - 2nd Floor"],
    [3, "Pediatrics", "Block B - 1st Floor"],
    [4, "General Medicine", "Block B - 2nd Floor"],
    [5, "Gynecology", "Block C - 1st Floor"],
    [6, "Neurology", "Block C - 2nd Floor"],
    [7, "Dermatology", "Block D - 1st Floor"],
    [8, "ENT", "Block D - 2nd Floor"],
    [9, "Oncology", "Block E - 1st Floor"],
    [10, "General Surgery", "Block E - 2nd Floor"]
]

departments = pd.DataFrame(
    departments_data,
    columns=[
        "Department_ID",
        "Department_Name",
        "Location"
    ]
)

# ============================================================
# 2. DOCTORS
# ============================================================

doctor_names = [
    fake.name() for _ in range(N_DOCTORS)
]

doctors_data = []

for i in range(1, N_DOCTORS + 1):

    department_id = ((i - 1) % 10) + 1
    experience = random.randint(3, 25)

    fee = random.choice([
        400, 500, 600, 700, 800, 1000, 1200, 1500
    ])

    doctors_data.append([
        i,
        doctor_names[i - 1],
        department_id,
        experience,
        fee
    ])

doctors = pd.DataFrame(
    doctors_data,
    columns=[
        "Doctor_ID",
        "Doctor_Name",
        "Department_ID",
        "Experience_Years",
        "Consultation_Fee"
    ]
)

# ============================================================
# 3. PATIENTS
# ============================================================

cities = [
    "Mumbai",
    "Pune",
    "Nashik",
    "Jalgaon",
    "Aurangabad",
    "Nagpur",
    "Ahmednagar",
    "Dhule",
    "Nandurbar",
    "Thane"
]

insurance_types = [
    "Private Insurance",
    "Government Scheme",
    "Corporate Insurance",
    "Self Pay"
]

patients_data = []

for i in range(1, N_PATIENTS + 1):

    gender = random.choice([
        "Male",
        "Female",
        "Other"
    ])

    age = random.randint(1, 85)

    registration_date = fake.date_between(
        start_date=START_DATE,
        end_date=END_DATE
    )

    patients_data.append([
        i,
        fake.name(),
        age,
        gender,
        random.choice(cities),
        registration_date,
        random.choice(insurance_types)
    ])

patients = pd.DataFrame(
    patients_data,
    columns=[
        "Patient_ID",
        "Patient_Name",
        "Age",
        "Gender",
        "City",
        "Registration_Date",
        "Insurance_Type"
    ]
)

# ============================================================
# HELPER FUNCTION
# ============================================================

def random_date(start, end):

    delta = end - start

    random_days = random.randint(
        0,
        delta.days
    )

    return start + timedelta(days=random_days)


# ============================================================
# 4. APPOINTMENTS
# ============================================================

appointment_types = [
    "Consultation",
    "Follow-up",
    "Routine Checkup",
    "Emergency Consultation"
]

appointment_statuses = [
    "Completed",
    "Completed",
    "Completed",
    "Completed",
    "Cancelled",
    "No-show"
]

appointments_data = []

for i in range(1, N_APPOINTMENTS + 1):

    patient_id = random.randint(
        1,
        N_PATIENTS
    )

    doctor_id = random.randint(
        1,
        N_DOCTORS
    )

    appointment_date = random_date(
        START_DATE,
        END_DATE
    )

    booking_date = appointment_date - timedelta(
        days=random.randint(1, 30)
    )

    status = random.choice(
        appointment_statuses
    )

    waiting_time = (
        random.randint(5, 90)
        if status == "Completed"
        else 0
    )

    appointments_data.append([
        i,
        patient_id,
        doctor_id,
        appointment_date,
        random.choice(appointment_types),
        status,
        booking_date,
        waiting_time
    ])

appointments = pd.DataFrame(
    appointments_data,
    columns=[
        "Appointment_ID",
        "Patient_ID",
        "Doctor_ID",
        "Appointment_Date",
        "Appointment_Type",
        "Appointment_Status",
        "Booking_Date",
        "Waiting_Time_Min"
    ]
)

# ============================================================
# 5. ADMISSIONS
# ============================================================

bed_types = [
    "General",
    "Semi-Private",
    "Private",
    "ICU"
]

admission_types = [
    "Emergency",
    "Planned"
]

discharge_statuses = [
    "Recovered",
    "Improved",
    "Transferred",
    "Discharged on Request"
]

admissions_data = []

for i in range(1, N_ADMISSIONS + 1):

    patient_id = random.randint(
        1,
        N_PATIENTS
    )

    doctor_id = random.randint(
        1,
        N_DOCTORS
    )

    doctor_department = doctors.loc[
        doctors["Doctor_ID"] == doctor_id,
        "Department_ID"
    ].iloc[0]

    admission_date = random_date(
        START_DATE,
        END_DATE - timedelta(days=5)
    )

    length_of_stay = random.randint(
        1,
        15
    )

    discharge_date = admission_date + timedelta(
        days=length_of_stay
    )

    admissions_data.append([
        i,
        patient_id,
        doctor_id,
        doctor_department,
        admission_date,
        discharge_date,
        random.choice(bed_types),
        length_of_stay,
        random.choice(admission_types),
        random.choice(discharge_statuses)
    ])

admissions = pd.DataFrame(
    admissions_data,
    columns=[
        "Admission_ID",
        "Patient_ID",
        "Doctor_ID",
        "Department_ID",
        "Admission_Date",
        "Discharge_Date",
        "Bed_Type",
        "Length_of_Stay",
        "Admission_Type",
        "Discharge_Status"
    ]
)

# ============================================================
# 6. TREATMENTS
# ============================================================

treatment_types = [
    "Consultation",
    "Diagnostic Procedure",
    "Minor Surgery",
    "Major Surgery",
    "Therapy",
    "Emergency Treatment",
    "Routine Procedure"
]

treatments_data = []

for i in range(1, N_TREATMENTS + 1):

    patient_id = random.randint(
        1,
        N_PATIENTS
    )

    doctor_id = random.randint(
        1,
        N_DOCTORS
    )

    department_id = doctors.loc[
        doctors["Doctor_ID"] == doctor_id,
        "Department_ID"
    ].iloc[0]

    treatment_date = random_date(
        START_DATE,
        END_DATE
    )

    admission_id = random.choice(
        admissions["Admission_ID"].tolist()
        + [None] * 3
    )

    treatment_type = random.choice(
        treatment_types
    )

    cost_ranges = {
        "Consultation": (500, 2000),
        "Diagnostic Procedure": (1000, 8000),
        "Minor Surgery": (10000, 30000),
        "Major Surgery": (40000, 200000),
        "Therapy": (2000, 15000),
        "Emergency Treatment": (5000, 50000),
        "Routine Procedure": (1000, 10000)
    }

    low, high = cost_ranges[treatment_type]

    treatment_cost = random.randint(
        low,
        high
    )

    treatments_data.append([
        i,
        patient_id,
        doctor_id,
        department_id,
        admission_id,
        treatment_date,
        treatment_type,
        treatment_cost
    ])

treatments = pd.DataFrame(
    treatments_data,
    columns=[
        "Treatment_ID",
        "Patient_ID",
        "Doctor_ID",
        "Department_ID",
        "Admission_ID",
        "Treatment_Date",
        "Treatment_Type",
        "Treatment_Cost"
    ]
)

# ============================================================
# 7. BILLING
# ============================================================

payment_statuses = [
    "Paid",
    "Paid",
    "Paid",
    "Partial",
    "Pending"
]

payment_methods = [
    "Cash",
    "Card",
    "UPI",
    "Insurance"
]

billing_data = []

for i in range(1, N_BILLS + 1):

    patient_id = random.randint(
        1,
        N_PATIENTS
    )

    treatment_id = random.randint(
        1,
        N_TREATMENTS
    )

    treatment_amount = treatments.loc[
        treatments["Treatment_ID"] == treatment_id,
        "Treatment_Cost"
    ].iloc[0]

    consultation_amount = random.choice([
        0,
        500,
        700,
        1000,
        1200
    ])

    medicine_amount = random.randint(
        0,
        10000
    )

    diagnostic_amount = random.randint(
        0,
        15000
    )

    discount = random.randint(
        0,
        int(treatment_amount * 0.15)
    )

    gross_amount = (
        consultation_amount
        + treatment_amount
        + medicine_amount
        + diagnostic_amount
    )

    insurance_coverage = random.choice([
        0,
        0,
        int(gross_amount * 0.25),
        int(gross_amount * 0.50),
        int(gross_amount * 0.75)
    ])

    final_amount = max(
        0,
        gross_amount
        - discount
        - insurance_coverage
    )

    bill_date = random_date(
        START_DATE,
        END_DATE
    )

    billing_data.append([
        i,
        patient_id,
        treatment_id,
        bill_date,
        consultation_amount,
        treatment_amount,
        medicine_amount,
        diagnostic_amount,
        discount,
        insurance_coverage,
        final_amount,
        random.choice(payment_statuses),
        random.choice(payment_methods)
    ])

billing = pd.DataFrame(
    billing_data,
    columns=[
        "Bill_ID",
        "Patient_ID",
        "Treatment_ID",
        "Bill_Date",
        "Consultation_Amount",
        "Treatment_Amount",
        "Medicine_Amount",
        "Diagnostic_Amount",
        "Discount",
        "Insurance_Coverage",
        "Final_Amount",
        "Payment_Status",
        "Payment_Method"
    ]
)

# ============================================================
# 8. PATIENT FEEDBACK
# ============================================================

feedback_data = []

for i in range(1, N_FEEDBACK + 1):

    patient_id = random.randint(
        1,
        N_PATIENTS
    )

    appointment_id = random.randint(
        1,
        N_APPOINTMENTS
    )

    feedback_date = random_date(
        START_DATE,
        END_DATE
    )

    satisfaction = random.randint(
        1,
        5
    )

    waiting_score = max(
        1,
        min(
            5,
            satisfaction + random.choice([-1, 0, 0, 1])
        )
    )

    doctor_score = max(
        1,
        min(
            5,
            satisfaction + random.choice([-1, 0, 1])
        )
    )

    hospital_score = max(
        1,
        min(
            5,
            satisfaction + random.choice([-1, 0, 1])
        )
    )

    comments = [
        "Good experience",
        "Very helpful doctor",
        "Waiting time was high",
        "Staff was cooperative",
        "Good hospital service",
        "Satisfied with treatment",
        "Could improve waiting time",
        "Excellent service"
    ]

    feedback_data.append([
        i,
        patient_id,
        appointment_id,
        feedback_date,
        satisfaction,
        waiting_score,
        doctor_score,
        hospital_score,
        random.choice(comments)
    ])

feedback = pd.DataFrame(
    feedback_data,
    columns=[
        "Feedback_ID",
        "Patient_ID",
        "Appointment_ID",
        "Feedback_Date",
        "Satisfaction_Score",
        "Waiting_Score",
        "Doctor_Score",
        "Hospital_Score",
        "Feedback_Text"
    ]
)

# ============================================================
# SAVE CSV FILES
# ============================================================

datasets = {
    "departments.csv": departments,
    "doctors.csv": doctors,
    "patients.csv": patients,
    "appointments.csv": appointments,
    "admissions.csv": admissions,
    "treatments.csv": treatments,
    "billing.csv": billing,
    "patient_feedback.csv": feedback
}

for filename, dataframe in datasets.items():

    dataframe.to_csv(
        filename,
        index=False
    )

    print(
        f"{filename}: {len(dataframe)} records created"
    )

print("\nDataset generation completed successfully!")