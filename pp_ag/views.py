from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView,DetailView,TemplateView, UpdateView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django .urls import reverse_lazy, reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.http import HttpResponseRedirect
from django.contrib.auth import login

# Create your views here.

# home page
def index(request):
    return render(request, 'index.html')

# user signup
def signup(request):
    if request.method=="POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            email_subject = "Activate Your Account"
            message = render_to_string('activate_account.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': str(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.content_subtype = "html"
            email.send(fail_silently=False)

            return render(request, 'send_email_confirmation.html')
    else:
        form=UserSignUpForm()
        
    return render(request,'registration.html', {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = auth.models.User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, auth.models.User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        url = reverse('ag:home')
        return HttpResponseRedirect(url)
    else:
        return render(request, 'invalid_link.html')


# upload project
class PostCreateView(CreateView, LoginRequiredMixin):
    login_url = '/signup/'
    redirect_field_name = 'registration.html'

    model = Case
    form = CaseForm
    fields = ['project_name','description', 'goal', 'cover_image', 'image1', 'image2', 'image3', 'image4', 'audio', 'video','document']
    template_name = "case_form.html"


# project list
class PostListView(ListView):
    model = Case
    select_related=('first_name', 'last_name', 'cover_image')
    template_name='case_list.html'


# Detail information for each project
class CaseDetail(DetailView):
    model = Case
    template_name='case_detail.html'


# about me page
class AboutView(TemplateView):
    template_name = 'about.html'

# 
class CaseUpdateView(UpdateView):
    form_class=CaseForm
    model = Case
    template_name = "case_update.html"
