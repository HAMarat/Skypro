import functions


def get_student_by_pk(pk):
    """
    Получаем список со словарями из данных студетнов
    """
    student_list = functions.load_students('students.json')
    for student in student_list:
        if student['pk'] == pk:
            return student


def get_profession_by_title(title):
    """
    Получаем список со словарями из данных профессий
    """
    profession_list = functions.load_students('professions.json')
    for profession in profession_list:
        if profession['title'] == title:
            return profession


def check_fitness(student, profession):
    """
    Получаем словарь с результатом
    """
    has_profession = list(set(profession).intersection(set(student)))
    need_profession = list(set(profession).difference(set(student)))
    fit_percent = round(len(has_profession) / len(profession) * 100)
    return {
        "has": has_profession,
        "lacks": need_profession,
        "fit_percent": fit_percent
    }


# Получаем номер студента
student_pk = int(input('Введите номер студента: '))

# Выводим данные о студенте, если есть в списке
if get_student_by_pk(student_pk) is not None:
    student_dict = get_student_by_pk(student_pk)
    name_student = student_dict["full_name"]
    student_skills_list = student_dict["skills"]
    print(f'Студент {name_student}\n'
          f'Знает {", ".join(student_skills_list)}')
else:
    print('Информация не найдена')
    quit()

print()

# Получаем профессию по которой проверить студента
profession_title = input(f'Выберите специальность для оценки студента {name_student} ').title()

# Проверяем есть ли профессия в списке профессий
if get_profession_by_title(profession_title) is not None:
    profession_skills_list = get_profession_by_title(profession_title)["skills"]
    abilities_dict = check_fitness(student_skills_list, profession_skills_list)
else:
    print('Информация не найдена')
    quit()

print()

# Выводим результат
print(f'Пригодность {abilities_dict["fit_percent"]}%\n'
      f'{name_student} знает {", ".join(abilities_dict["has"])}\n'
      f'{name_student} не знает {", ".join(abilities_dict["lacks"])}')
