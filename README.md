# Exam Seating Arrangement System

A simple web application that solves exam seating arrangement using CSP (Constraint Satisfaction Problem) with Backtracking algorithm.

## Concept

**Problem:** Arrange students in an exam hall such that no two students from the same branch sit adjacent to each other (left, right, top, bottom).

**Solution Approach:**
- **CSP Formulation**
  - Variables: Seat positions (row, col)
  - Domain: Set of students
  - Constraint: Adjacent seats cannot have same branch students

- **Algorithm:** Backtracking
  - Assigns students to seats one by one
  - Checks constraint after each assignment
  - Backtracks if constraint violated


## Setup Instructions

### 1. Install Python

Download and install from https://www.python.org/downloads/

**Important:** Check "Add Python to PATH" during installation.

### 2. Install Flask

Open terminal/command prompt in project folder:

```bash
python -m pip install flask

### 3. Run the Application
python app.py
```
