class university:
    def __init__(self, univercity_name, building_body, region, city, street, building):
        self.univercity_name = univercity_name
        self.building_body = building_body
        self.region = region
        self.city = city
        self.street = street
        self.building = building

    def __str__(self):
        return f'Университет: {self.univercity_name} \n' +\
               f'Корпус: {self.building_body} \n' + \
               f'Регион: {self.region} \n' + \
               f'Город: {self.city} \n' + \
               f'Улица: {self.street} \n' + \
               f'Дом №: {self.building} \n'

class subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __str__(self):
        return f'Предмет: {self.subject_name}'

class teacher:
    def __init__(self, teacher_name, gender, height, weight, experience, category, specialties, faculty, department):
        self.teacher_name = teacher_name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.experience = experience
        self.category = category
        self.specialties = specialties
        self.faculty = faculty
        self.department = department

    def __str__(self):
        return f'Преподаватель: {self.teacher_name} \n' +\
               f'Пол: {self.gender} \n' +\
               f'Рост: {self.height} \n' +\
               f'Вес: {self.weight} \n' +\
               f'Стаж: {self.experience} \n' +\
               f'Категория: {self.category} \n' +\
               f'Специальность: {self.specialties} \n' +\
               f'Факультет: {self.faculty} \n' +\
               f'Кафедра: {self.department}'

class student:
    def __init__(self, student_name, gender, height, weight, faculty, department, specialties, course, group, performance, period_of_study):
        self.student_name = student_name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.faculty = faculty
        self.department = department
        self.specialties = specialties
        self.course = course
        self.group = group
        self.performance = performance
        self.period_of_study = period_of_study

    def __str__(self):
        return f'Студент: {self.student_name} \n' +\
               f'Пол: {self.gender} \n' +\
               f'Рост: {self.height} \n' +\
               f'Вес: {self.weight} \n' +\
               f'Факультет: {self.faculty} \n' +\
               f'Кафедра: {self.department} \n' +\
               f'Специальность: {self.specialties} \n' +\
               f'Курс: { self.course} \n' +\
               f'Группа: {self.group} \n' +\
               f'Успеваемсоть: {self.performance} \n' +\
               f'Период обучения: {self.period_of_study} '

University = university('ДГТУ', 'новый', 'Республика Дагенстан', 'Махачкала', 'пр. Шамиля', '56')
Subject = subject('ООП')
Teacher = teacher('Андрей', 'муж', '186', '68', '20 лет', 'вторая', 'Программная инженерия', 'ФКТВТиЭ', 'ПОВТиАС')
Student = student('Дмитрий', 'муж', '175', '60', 'ФКТВТиЭ', 'ПОВТиАС', 'Программная инженерия', '2', 'У933', 'Высокая', '2019 - 2022')
print(University, Subject, Teacher, Student, sep=('\n\n'))