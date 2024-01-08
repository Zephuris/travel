from django.contrib.auth.models import User,AnonymousUser
from core.models import ProfilePic
def user_pic_context(request):
    try:
        pic_qs = ProfilePic.objects.get(user = request.user)
        return {'photo':pic_qs}
    except:
        return {'photo':'/profile/default.png'}