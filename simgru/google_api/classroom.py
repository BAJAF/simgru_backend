import requests

COURSES_URL = "https://classroom.googleapis.com/v1/courses"

COURSEWORK_INFO_URL = "https://classroom.googleapis.com/v1/courses/{courseId}/courseWork/{id}"

def get_course_list(token: str):
    params = {
        "access_token": token,
        "courseStates": "ACTIVE",
    }
    res = requests.get(url=COURSES_URL, params=params)
    resDict = res.json()
    coursesList = []
    if resDict:
        for c in resDict["courses"]:
            coursesList.append({
                'name': c['name'],
                'id': c['id'],
                'description': c['descriptionHeading'],
                'link': c['alternateLink'],
            })

    return coursesList

def get_coursework(token: str, courseId: str, coursworkId: str):
    url = f'{COURSES_URL}/{courseId}/courseWork/{coursworkId}'

    params = {
        "access_token": token
    }

    res = requests.get(url=url, params=params)
    res_dict = res.json()
    coursework = dict()

    if res_dict:
        coursework = {
            'title': res_dict["title"],
            'link': res_dict["alternateLink"],
            'due_date':res_dict["dueDate"],
            'max_points': res_dict["maxPoints"]
        }

    return coursework

def get_course_information(token: str, courseId: str):
    course_url = f'{COURSES_URL}/{courseId}'
    students_url = f'{COURSES_URL}/{courseId}/students'
    courseworks_url = f'{COURSES_URL}/{courseId}/courseWork'

    course_params = { "access_token": token }
    students_params = {
        "access_token": token,
        "courseId": courseId
    }

    course_req = requests.get(url=course_url, params=course_params).json()
    students_req = requests.get(url=students_url, params=students_params).json()
    courseworks_req = requests.get(url=courseworks_url, params=students_params).json()

    course_information = dict()

    if course_req and students_req and courseworks_req:
        course_information = {
          "students": students_req,
          "coursework": courseworks_req,
          "course": course_req
        }

    return course_information
