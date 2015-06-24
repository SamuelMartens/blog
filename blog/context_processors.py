from blog.forms import LoginForm
from content.models import UserImage


def log_form_proc(request):
    user_images=UserImage.objects.all()
    return {'log_form':LoginForm(),'user_images':user_images,}

