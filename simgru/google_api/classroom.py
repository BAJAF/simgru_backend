import requests

COURSES_LIST_URL = "https://classroom.googleapis.com/v1/courses"

COURSEWORK_INFO_URL = "https://classroom.googleapis.com/v1/courses/{courseId}/courseWork/{id}"

def get_course_list(token: str):
    params = {
        "access_token": token,
        "courseStates": "ACTIVE",
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

def get_coursework(token: str, courseId: str, coursworkId: str):
    url = f'{COURSES_LIST_URL}/{courseId}/courseWork/{coursworkId}'
    
    params = {
        "access_token": token
    }

    res = requests.get(url=url, params=params)
    res_dict = res.json()
    print(res_dict)
    coursework = dict()

    if res_dict:
        coursework = {
            'title': res_dict["title"],
            'link': res_dict["alternateLink"],
            'due_date':res_dict["dueDate"],
            'max_points': res_dict["maxPoints"]
        }
    
    return coursework

if __name__ == "__main__":
    get_course_list("ya29.a0Ael9sCO5vJADc9nOU7L1XqP7HLfa1W6GKxOh-TQbhnAH06FKJZDB_nheb9hsN1so87aS95goZ8qp0GYO8WEGX-Y_BcWdeQU5FHvK7vs_ODmST_H6-cuT3KBiBgpuTXXqsY82KfTRzOGJh8S4hkjPtb5DhKHgaCgYKAT0SARISFQF4udJhpAVtZT3hkh_xdgihoob1SQ0163")


'''
{
  "courseId": "542173537982",
  "id": "608160172596",
  "title": "Práctica 6 - Threads",
  "materials": [
    {
      "driveFile": {
        "driveFile": {
          "id": "1ZFDkbyVmdSPdwo-6OipktJLxk6DhhBQc",
          "title": "Práctica 6 - Threads.docx",
          "alternateLink": "https://drive.google.com/file/d/1ZFDkbyVmdSPdwo-6OipktJLxk6DhhBQc/view?usp=drive_web",
          "thumbnailUrl": "https://lh3.googleusercontent.com/s0xqYEntH01PQEmwTt1xXYrvauWLq8Gv4EQqy5Lg76_LiPaAVNV7ghzNw22vo7LI3Qn6JDds6e4ksL0=s200"
        },
        "shareMode": "VIEW"
      }
    },
    {
      "driveFile": {
        "driveFile": {
          "id": "1eSLildWpwODy5gaf6TLA2-Ma7pFasBpv",
          "title": "trn_set.csv",
          "alternateLink": "https://drive.google.com/file/d/1eSLildWpwODy5gaf6TLA2-Ma7pFasBpv/view?usp=drive_web"
        },
        "shareMode": "VIEW"
      }
    },
    {
      "driveFile": {
        "driveFile": {
          "id": "1sMxlQ-mCNNplJ3WHyOtnOFBYOGZBC-gb",
          "title": "tst_set.csv",
          "alternateLink": "https://drive.google.com/file/d/1sMxlQ-mCNNplJ3WHyOtnOFBYOGZBC-gb/view?usp=drive_web"
        },
        "shareMode": "VIEW"
      }
    },
    {
      "driveFile": {
        "driveFile": {
          "id": "1LwMnXpidcPrbzjAW4MlfUCqi4HV1EUb5",
          "title": "knn.py",
          "alternateLink": "https://drive.google.com/file/d/1LwMnXpidcPrbzjAW4MlfUCqi4HV1EUb5/view?usp=drive_web"
        },
        "shareMode": "VIEW"
      }
    }
  ],
  "state": "PUBLISHED",
  "alternateLink": "https://classroom.google.com/c/NTQyMTczNTM3OTgy/a/NjA4MTYwMTcyNTk2/details",
  "creationTime": "2023-05-05T23:33:22.781Z",
  "updateTime": "2023-05-06T02:13:23.162Z",
  "dueDate": {
    "year": 2023,
    "month": 6,
    "day": 2
  },
  "dueTime": {
    "hours": 7,
    "minutes": 59
  },
  "maxPoints": 100,
  "workType": "ASSIGNMENT",
  "submissionModificationMode": "MODIFIABLE_UNTIL_TURNED_IN",
  "creatorUserId": "107733051004990211741"
}


'''