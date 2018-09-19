# Lesson Ninja Api
This is the api for the online app lesson ninja. You can view the current live product at lesson.ninja

# API overview
This api is built using django with django rest framework. The serializers used are django rest's hyperlinked model serializer which generates url's as well as primary keys for the objects it creates. In most places in this project as well as the frontend the url is treated as the unique identifier. 

# Development setup
To setup this api locally follow these steps.
1. create a virtual environment using `virtualenv environmentname`
1. activate that environment using `source environmentname/bin/activate`
1. clone down this repo and cd into it
1. install pip dependencies using `pip install -r requirements.txt`

# Environment setup
This repo uses a json settings file that is outside of source control to change settings and keep sensitive information hidden. The settings file should live in the settings directory. The formatting of that file should look like this. With the words in all caps being replaced with the nessesary information.

```
{
    "environment": "development",
    "secret_key": "SECRET_KEY",
    "production_database_name": "DATABASE_NAME",
    "production_database_user": "DATABASE_USER",
    "production_database_password": "DATABASE_PASSWORD",
    "production_database_host": "DATABASE_HOST"
}
```

This file has a counterpart that lives on the production virtual machine where the environment value is changed to "production". The json file is then read by the init file of the settings directory and settings are loaded and changed as nessesary. Setting that apply to both development and production environments live in base.py. With settings that differ between development in production living in development.py and production.py respectively. This setup allows seamless integration of new code into the virtual machine running the production code without needing to change any settings every time it needs to be pulled into the virtal machine. 

# Deployment
To deploy changes to this code into production. Merge changes into the master branch and push those changes up to github. Then ssh into the virtual machine. It has a bash function written named 'update' that goes through all the nessesary steps to update the machine and restart nginx to refresh the changes. So simply ssh in and run `update`. 

# API endpoints
The following is information about the various api endpoints available here. 

### A note on api errors
Many of the endpoints will return errors if the data passed to them is invalid. The format of that data will follow like this example error.
```
{
    "password": "That password is not secure enough",
    "username": "That username is already in use"
}
```
Handeling these errors on the frontend can be done by looping through the keys of the object. And then somehow presenting the errors to the user.

### A note on authorization
If an endpoint here is marked as 'auth required'. The endpoint expects a user jwt to be in the headers. 
```
{
    "Authorization": "Token dasifiwenf..."
}
```

### notes on detail view
Many of the endpoints allow get and post on the base endpoint (such as lesson/), but have a detail view when an id is appended to the url (lesson/1/). The detail view allows put and delete requests on that particular object. Whenever you see put and delete as available methods here. those are only available on the detail view.

# Post only endpoints
The following endpoints are post only.

## auth/register/
Expected input data
```
{
    "username": "myusername",
    "password": "supersafepassword",
    "email": "email@fakewebsite.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_student": "false",
    "is_teacher": "true"
}
```

Sucsessful response
```
{
    "token": "adsfidhihifa..."
}
```

## auth/login/
Expected input data
```
{
    "username": "myusername"
    "password": "supersafepassword"
}
```

Sucsessful response
```
{
    "token": "asdflhdsf..."
}
```

## auth/change_password/
auth required
Epected input
```
{
    "old_password": "superunsafepassword",
    "new_password": "newsupersafepassword"
}
```

Sucsessful response
```
{
    "sucsess": "password changed"
}
```

## auth/forgot_password/
Expected input
```
{
    "email": "email@fakewebsite.com"
}
```

Sucsessful response
```
{
    "sucsess": "email sent"
}
```

## auth/reset_password/
Expected input
```
{
    "email": "email@fakewebsite.com",
    "code": "123jisjfh89h...",
    "password": "passwordidefinitelywontforget"
}
```

Sucsessful response
```
{
    "sucsess": "password reset"
}
```

## connect/
auth required
Expected input
```
{
    "connection_key": "teacher#1234"
}
```

Sucsessful response
```
{
    "sucsess": "It worked!"
}
```

# Other endpoints

## user/
auth required
available query parameters
1. get_single_user -- boolean: If query is true the endpoint will only return the user who's auth token was sent to it. otherwise a list of users will be returned. However the single user option will still be returned as a one item long array.

available methods
- get
- post
- put

Example get
```
[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/user/1/",
        "username": "username",
        "first_name": "name",
        "last_name": "name",
        "email": "email@website.com",
        "is_student": false,
        "is_teacher": true
    }
]
```

This endpoint should not be posted to. User registration should be sent to the auth/register/ endpoint.

## student/
auth required
available query parameters
1. get_single_user -- boolean: If query is true the endpoint will only return the user who's auth token was sent to it. otherwise a list of users will be returned. However the single user option will still be returned as a one item long array.
1. username -- string: If query is present students will be filtered by usernames that contain the substring passed in the parameter.

available methods
- get
- post
- put

Example get
```
{
    "id": 1,
    "url": "http://127.0.0.1:8000/student/1/",
    "user": {
        "id": 1,
        "url": "http://127.0.0.1:8000/user/1/",
        "username": "rileymathews",
        "first_name": "",
        "last_name": "",
        "email": "rileymathews80@gmail.com",
        "is_student": true,
        "is_teacher": false
    }
}
```

Example post
```
{

}
```
Posting to this endpoint automatically takes the users auth token from headers and creates a student profile for them. We are not currently saving any extra information about students past their base user information. This endpoint was still created to allow for easy scalibility in the future if student unique information is found as needed in the future.

## teacher/
auth required
available query parameters
1. get_single_user -- boolean: If query is true the endpoint will only return the user who's auth token was sent to it. otherwise a list of users will be returned. However the single user option will still be returned as a one item long array.

available methods
- get
- post
- put

example get
```
[
    {
        "id": 1,
        "connection_key": "username#1596",
        "s3_user_key": "1ca9c5ec-80b9-4ee0-90bc-d68783a3fa39",
        "url": "http://127.0.0.1:8000/teacher/1/",
        "bio": "",
        "street": "",
        "city": "",
        "region": "",
        "country": "",
        "zip_code": "",
        "user": {
            "id": 1,
            "url": "http://127.0.0.1:8000/user/1/",
            "username": "username",
            "first_name": "name",
            "last_name": "name",
            "email": "email@fakewebsite.com",
            "is_student": false,
            "is_teacher": true
        },
        "students": []
    }
]
```

example post
```
{
    "bio": "",
    "street": "",
    "city": "",
    "region": "",
    "country": "",
    "zip_code": "",
}
```
None of these fields are required. Other keys such as connection_key and s3_user_key are automatically generated and should not be included in a post request to create a new teacher profile.

## teacher_student/
auth required
available query parmeters
1. teacher -- pk: primary key for a teacher
1. student -- pk: primary key for a student

If both of the query parameters are present. The api will return the particular object that intersects that student and that teacher. otherwise all intersections are returned. 

available methods
- get
- post
- delete

example get
```
[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/teacher_student/1/",
        "teacher": "http://127.0.0.1:8000/teacher/1/",
        "student": "http://127.0.0.1:8000/student/1/",
        "confirmed": false
    }
]
```

example post
```
{
    "teacher": "http://127.0.0.1:8000/teacher/1/",
    "student": "http://127.0.0.1:8000/student/1/",
    "confirmed": false
}
```

## subject/
available methods

- get
- post
- put
- delete

example get
```
[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/subject/1/",
        "name": "Music",
        "description": "everything music"
    }
]
```

example post
```
{
    "name": "Music",
    "description": "everything music"
}
```

## lesson/
quth required
available query parameters
1. filter_by_auth -- boolean: if true only current users lessons will be returned

available methods
- get
- post
- put
- delete

example get
```
[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/lesson/1/",
        "name": "music theory",
        "description": "all things music theory",
        "content": "see documents",
        "teacher": {
            "id": 1,
            "connection_key": "rileymathews#1596",
            "s3_user_key": "1ca9c5ec-80b9-4ee0-90bc-d68783a3fa39",
            "url": "http://127.0.0.1:8000/teacher/1/",
            "bio": "",
            "street": "",
            "city": "",
            "region": "",
            "country": "",
            "zip_code": "",
            "user": {
                "id": 1,
                "url": "http://127.0.0.1:8000/user/1/",
                "username": "rileymathews",
                "first_name": "",
                "last_name": "",
                "email": "rileymathews80@gmail.com",
                "is_student": false,
                "is_teacher": false
            },
            "students": [
                {
                    "id": 1,
                    "url": "http://127.0.0.1:8000/student/1/",
                    "user": {
                        "id": 1,
                        "url": "http://127.0.0.1:8000/user/1/",
                        "username": "rileymathews",
                        "first_name": "",
                        "last_name": "",
                        "email": "rileymathews80@gmail.com",
                        "is_student": false,
                        "is_teacher": false
                    }
                }
            ]
        },
        "documents": []
    }
]
```

example post
```
{
    "name": "",
    "description": "",
    "content": ""
}
```

## student_lesson/
auth required
available query params
1. users -- boolean: if present this endpoint will only return assignments in which the current user is somehow linked. for a teacher that means its their lesson. for a student it means they are on that lesson.

available methods 
- get
- post
- put
- delete

example get
```
[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/student_lesson/1/",
        "lesson": {
            "url": "http://127.0.0.1:8000/lesson/1/",
            "name": "music theory",
            "description": "all things music theory",
            "content": "see documents",
            "teacher": {
                "url": "http://127.0.0.1:8000/teacher/1/",
                "connection_key": "rileymathews#1596",
                "s3_user_key": "1ca9c5ec-80b9-4ee0-90bc-d68783a3fa39",
                "bio": "",
                "street": "",
                "city": "",
                "region": "",
                "country": "",
                "zip_code": "",
                "user": "http://127.0.0.1:8000/user/1/",
                "students": [
                    "http://127.0.0.1:8000/student/1/"
                ]
            },
            "documents": []
        },
        "student": {
            "url": "http://127.0.0.1:8000/student/1/",
            "user": {
                "url": "http://127.0.0.1:8000/user/1/",
                "password": "pbkdf2_sha256$120000$APNSPKPMei3j$6q2k9GtSohAj99BYcf+haIhtfPGJakcvV+mA/MjCTDY=",
                "last_login": "2018-09-19T14:50:32.586028Z",
                "is_superuser": true,
                "username": "rileymathews",
                "first_name": "",
                "last_name": "",
                "email": "rileymathews80@gmail.com",
                "is_staff": true,
                "is_active": true,
                "date_joined": "2018-09-19T14:48:23.689755Z",
                "is_teacher": false,
                "is_student": false,
                "groups": [],
                "user_permissions": []
            }
        },
        "has_opened": false,
        "finished_on": null
    }
]
```

example post
```
{
    "student": "http://127.0.0.1:8000/student/1/",
    "lesson": "http://127.0.0.1:8000/lesson/1/",
    "has_opened": false,
    "finished_on": null
}
```

## document/
auth required

available methods
- get
- post
- put
- delete

example get
```
[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/document/1/",
        "s3_url": "https://lesson-ninja-files-dev.s3.us-east-2.amazonaws.com/1d31aed0-e53a-43fd-b4b1-93a649afa34c/Circle%20of%20Fifths.pdf",
        "s3_key": "1d31aed0-e53a-43fd-b4b1-93a649afa34c/Circle of Fifths.pdf",
        "file_extension": "pdf",
        "name": "circle of fifths",
        "notes": "pdf doc"
    }
]
```

example post
```
{
    "s3_url": "https://lesson-ninja-files-dev.s3.us-east-2.amazonaws.com/1d31aed0-e53a-43fd-b4b1-93a649afa34c/Circle%20of%20Fifths.pdf",
    "s3_key": "1d31aed0-e53a-43fd-b4b1-93a649afa34c/Circle of Fifths.pdf",
    "file_extension": "pdf",
    "name": "circle of fifths",
    "notes": "pdf doc"
}
```

## lesson_document/
auth required
available query params
1. lesson -- pk: id pk for a lesson
1. document -- pk: id pk for a document

if both params are present the api will return the intersection object between that lesson and that document

available methods

- get
- post
- delete

example get
```
[
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/lesson_document/1/",
        "lesson": "http://127.0.0.1:8000/lesson/1/",
        "document": "http://127.0.0.1:8000/document/1/"
    }
]
```

example post
```
{
    "lesson": "http://127.0.0.1:8000/lesson/1/",
    "document": "http://127.0.0.1:8000/document/1/"
}
```