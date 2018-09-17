import json
from django.http import HttpResponse
from api.models import User

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, is_password_usable, make_password

@csrf_exempt
def change_password(request):
    """Handles the creation of a new user for authentication
    Method args:
        request -- the full HTTP request object
    """
    errors_found = False
    errors = dict()

    req_body = json.loads(request.body.decode())

    all_users = User.objects.all()
    # get user from auth token
    token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
    current_user = User.objects.get(auth_token=token)

    # get old password from request
    old_password = req_body['old_password']
    new_password = req_body['new_password']

    # confirm that users old password is correct
    if not check_password(old_password, current_user.password):
        errors_found = True
        errors['old_password'] = "password is not correct"

    # confirm that new password is usable
    if not is_password_usable(new_password):
        errors_found = True
        errors['new_password'] = "That password is not usable"

    # change the password
    if not errors:
        new_hash = make_password(new_password)
        current_user.password = new_hash
        # save the user
        current_user.save()
        # return sucsess or error
        response = json.dumps({"sucsess": "password changed"})
    else:
        response = json.dumps(errors)

    return HttpResponse(response, content_type='application/json')






# username_check = [user for user in all_users if user.username == req_body['username']]
#     email_check = [user for user in all_users if user.email == req_body['email']]

#     errors = dict()
#     if username_check:
#         errors["username"] = "This username is already in use"
#         errors_found = True
    
#     if email_check:
#         errors["email"] = "This email is already in use"
#         errors_found = True
    

#     if errors_found:
#         response = json.dumps(errors)
#     else:
#         # make new user
#         new_user = User.objects.create_user(
#             username=req_body['username'],
#             password=req_body['password'],
#             email=req_body['email'],
#             first_name=req_body['first_name'],
#             last_name=req_body['last_name'],
#             is_student=req_body['is_student'],
#             is_teacher=req_body['is_teacher']
#         )
#         token = Token.objects.create(user=new_user)

#         response = json.dumps({"token": token.key})

#         send_mail(
#             f"Welcome {req_body['first_name']}", 
#             "Welcome to Lesson Ninja.",
#             "Welcome to lesson Ninja! And thank you for trying this out. If you have any questions, concerns, or comments feel free to reach out to me at contact@lesson.ninja. Happy Learning!",
#             [new_user.email],
#             fail_silently=False
#         )
