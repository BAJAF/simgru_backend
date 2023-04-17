import requests

COURSES_LIST_URL = "https://classroom.googleapis.com/v1/courses"

def get_course_list(token: str):
    params = {
        "access_token": token,
        "courseStates": "ACTIVE"
    }
    res = requests.get(url=COURSES_LIST_URL, params=params)
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


if __name__ == "__main__":
    get_course_list("ya29.a0Ael9sCO5vJADc9nOU7L1XqP7HLfa1W6GKxOh-TQbhnAH06FKJZDB_nheb9hsN1so87aS95goZ8qp0GYO8WEGX-Y_BcWdeQU5FHvK7vs_ODmST_H6-cuT3KBiBgpuTXXqsY82KfTRzOGJh8S4hkjPtb5DhKHgaCgYKAT0SARISFQF4udJhpAVtZT3hkh_xdgihoob1SQ0163")