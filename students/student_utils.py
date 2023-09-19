# EXTRACT CREATE ATTENDANCE RECORDS LOGIC TO FUNCTION
from typing import List
from students.models.student import Student
from students.models.student_attendence_model import StudentAttendance


def create_attendance_records(
        students: List[Student], 
        class_id: int, 
        date: str, 
        author_id: int
        ) -> List[StudentAttendance]:
    # CREATE HOLDER FOR ATTENDANCE RECORDS
    attendance_records = []

    # TO PREVENT BULK_CREATE ERRORS, EXCLUDE STUDENT IF ATTENDANCE RECORD EXISTS
    for student in students:
        if not student['attendance_for_day']:
            attendance_record = {
                "student_id_id": student['id'],
                "class_id_id": class_id,
                "date": date,
                "status": 0,
                "reason": None,
                "author_id_id": author_id,
            }
            attendance_records.append(attendance_record)
            
    return StudentAttendance.objects.bulk_create(
        [StudentAttendance(**record) for record in attendance_records])