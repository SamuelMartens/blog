from blog.forms import LoginForm


def log_form_proc(request):
    return {'log_form':LoginForm()}

