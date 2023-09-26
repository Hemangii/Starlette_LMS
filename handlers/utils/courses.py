from sqlalchemy.orm import Session
from handlers.utils.models.courses import Course
from pydantic_schemas.course import CourseCreate


def get_course(db: Session, course_id: int):
    course=db.query(Course).filter(Course.id == course_id).first()
    return course.as_json()


def get_courses(db: Session):
    courses= db.query(Course).all()
    return [ course.as_json() for course in courses]


def get_user_courses(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return [ course.as_json() for course in courses]


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course.as_json()