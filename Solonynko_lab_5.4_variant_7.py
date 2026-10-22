students = {
    "КБ10000001": {"first_name": "Олександр", "last_name": "Солонинко", "year": 1, "grades": [90, 85, 92, 88]},
    "КБ10000002": {"first_name": "Анастасія", "last_name": "Ковальчук", "year": 1, "grades": [75, 80, 88, 82]},
    "КБ10000003": {"first_name": "Максим", "last_name": "Бондаренко", "year": 2, "grades": [95, 98, 92, 100]},
    "КБ10000004": {"first_name": "Олена", "last_name": "Ткаченко", "year": 2, "grades": [65, 70, 72, 68]},
    "КБ10000005": {"first_name": "Дмитро", "last_name": "Шевченко", "year": 3, "grades": [88, 90, 85, 91]},
    "КБ10000006": {"first_name": "Ірина", "last_name": "Мороз", "year": 3, "grades": [78, 82, 80, 85]},
    "КБ10000007": {"first_name": "Артем", "last_name": "Кравченко", "year": 4, "grades": [92, 94, 96, 90]},
    "КБ10000008": {"first_name": "Софія", "last_name": "Лисенко", "year": 4, "grades": [60, 65, 70, 68]},
    "КБ10000009": {"first_name": "Денис", "last_name": "Мельник", "year": 1, "grades": [82, 88, 90, 84]},
    "КБ10000010": {"first_name": "Марія", "last_name": "Бойко", "year": 2, "grades": [90, 91, 89, 93]}
}

course_data = {}

for ticket, info in students.items():
    year = info["year"]
    
    student_avg = sum(info["grades"]) / len(info["grades"])

    if year not in course_data:
        course_data[year] = []
    
    course_data[year].append(student_avg)

print("=== СЕРЕДНЯ УСПІШНІСТЬ НА КОЖНОМУ КУРСІ ===")
for year in sorted(course_data.keys()):
    course_avg = sum(course_data[year]) / len(course_data[year])
    students_count = len(course_data[year])
    print(f"{year}-й курс: {course_avg:.2f} балів (студентів: {students_count})")
    


