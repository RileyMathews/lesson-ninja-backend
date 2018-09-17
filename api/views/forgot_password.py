import json
from django.http import HttpResponse
from api.models import User, PasswordResetCode

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail

@csrf_exempt
def forgot_password(request):
    """a view that takes an email address
    and sends the user a reset code that allows them
    to reset their password
    
    Arguments:
        request {http} -- the full http request object
    """
    errors_found = False
    errors = dict()

    req_body = json.loads(request.body.decode())

    # get email address from request
    user_email = req_body['email']
    
    # find the user who's email matches the one sent
    current_user = [user for user in User.objects.all() if user.email == user_email]

    if len(current_user) != 0:
        current_user = current_user[0]
    else:
        errors_found = True
        errors['email'] = 'that email address was not found'

    

    if not errors_found:
        # generate a reset code that is attached to that user
        if current_user.reset_code:
            current_user.reset_code.delete()
            reset_code = PasswordResetCode.objects.create(user=current_user)
        else:
            reset_code = PasswordResetCode.objects.create(user=current_user)

        # generate an email body with the code in it and instructions on how to reset it.
        email_body = f"This password was sen't because a user requested a reset of the password for the account attached to this email. If you did not request this reset please ignore this email. Otherwise you can visit https://lesson.ninja/reset and follow the instructions to reset your password. Your password reset key is {reset_code}"

        send_mail("password reset at lesson ninja", email_body, "noreply@lesson.ninja", [current_user.email])

        response = json.dumps({"sucsess": "email sent"})
    else:
        response = json.dumps(errors)

    return HttpResponse(response, content_type='application/json')

    