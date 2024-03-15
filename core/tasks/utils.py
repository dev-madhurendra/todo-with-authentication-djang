from rest_framework.exceptions import AuthenticationFailed
import jwt

def check_authentication(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    
    return payload

STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]