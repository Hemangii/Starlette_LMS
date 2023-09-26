# Starlette LMS (LEARNING MANAGEMENT SYSTEM)




## Table of Contents

1. [Overview & Requirements](#overview-&-requirements)
1. [Running Locally](#running-the-app-locally)
1. [Tech Stack](#tech-stack)
1. [Schema](#schema)

## Overview & Requirements

This is a learning management system where teachers can manage student and students can see their courses.

- Teachers can perform CRUD operations on students.
- Teachers can create courses.
- Teachers can assign courses to students.
- Students can interact view their courses.
- Students are able to see their progress for each course.

## Running the App Locally

1. Make sure Python>=3.8.X is installed. 
2. Create a virtual environment: `python -m venv venv`
3. Install packages: `pip install -r requirements.txt`
4. Run the development server: `uvicorn main:app --reload`

## Tech Stack

- Starlette
- Python 3.9+
- Pip
- Sqlite
- SQL Alchemy 1.4+
- Pydantic
- Black
- Pre-commit

## Schema

**User**

- email: str
- role: (student, teacher, fk)
- first_name: str
- last_name: str
- bio: str (TextField)



**Course**

- title: str
- description: str (TextField)
- user_id: fk


**StudentCourse**

*This model is used for teachers to assign courses to students. The 'completed' boolean is False until the student has completed the whole course.*

- student_id
- course_id
- completed

**TobeImplemented**

**CompletedContentBlock**

*Every time the student completes a content block, a row is created in this table. The teacher can then go and edit this information when they grade the content block and provide feedback.*

- student_id
- course_id
- feedback
- grade