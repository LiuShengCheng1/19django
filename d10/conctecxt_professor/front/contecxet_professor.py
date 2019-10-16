from .models import User


def front_user(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:
            user = User.object.get(pk=user_id)
            context['front_user'] = user
        except:
            pass
    return context