import json
from django.http import HttpResponse
from api.models import User, PasswordResetCode

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, is_password_usable

@csrf_exempt
def reset_password(request):
    """function that accepts a request with a 
    password reset code, and resets the corresponding
    users password.
    
    Arguments:
        request {http} -- the full http request object
    """

    errors_found = False
    errors = dict()

    req_body = json.loads(request.body.decode())

    # get request data
    email = req_body['email']
    code = req_body['code']
    new_password = req_body['password']

    # find user who's email matches
    current_user = [user for user in User.objects.all() if user.email == email]

    if len(current_user) != 0:
        current_user = current_user[0]
    else:
        errors_found = True
        errors['email'] = 'email address not found'


    

    # make sure code matches their code
    if not errors_found:
        # check for code
        user_code = [code for code in PasswordResetCode.objects.all() if code.user == current_user]
        if len(user_code) != 0:
            if str(current_user.reset_code) == str(code):
                # reset password to new password
                if is_password_usable(new_password):
                    hashed = make_password(new_password)
                    current_user.password = hashed
                    current_user.save()
                    current_user.reset_code.delete()
                else:
                    errors_found = True
                    errors['password'] = "that password is not usable"
            else:
                errors_found = True
                errors['whoops'] = "something went wrong"
        else:
            errors_found = True
            errors['whoops'] = "something went wrong"

    if not errors_found:
        response = json.dumps({"sucsess": "password reset"})
    else:
        response = json.dumps(errors)


    return HttpResponse(response, content_type='application/json')
