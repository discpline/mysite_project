from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseCategory, Teacher, CompanyHead, Comment
from django.http import HttpResponse
from main_app.models import Footer
from .forms import SendMessageForm, CommentForm
from django.contrib import messages
from account.forms import UserRegistrationForm
from django.contrib.auth import login


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = CourseCategory.objects.filter(is_visible=True)
        courses = Course.objects.prefetch_related('instructor').filter(is_visible=True)
        teachers = Teacher.objects.filter(is_visible=True)
        company_head = CompanyHead.objects.filter(is_active=True).first()
        footer = Footer.objects.first()
        context['categories'] = categories
        context['courses'] = courses
        context['teachers'] = teachers
        context['company_head'] = company_head
        context['footer'] = footer
        context['send_message_form'] = SendMessageForm()
        context['user_registration_form'] = UserRegistrationForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        send_message_form = SendMessageForm(request.POST or None)
        user_registration_form = UserRegistrationForm(request.POST or None)

        if request.user.is_authenticated and 'signup' in request.POST:
            messages.info(request,
                          'You are already logged in. If you want to create a new account, please logout first.')
            return redirect('/')

        if 'send_message' in request.POST:
            context['send_message_form'] = send_message_form
            if send_message_form.is_valid():
                send_message_form.save()
                messages.success(request, 'Send Message done')
                return redirect('/')
            else:
                messages.error(request, 'There was an error with the message form.')

        elif 'signup' in request.POST:
            context['user_registration_form'] = user_registration_form
            if user_registration_form.is_valid():
                user = user_registration_form.save()
                login(request, user)
                messages.success(request, 'Account created successfully.')
                return redirect('/')
            else:
                messages.error(request, 'There was an error with the registration form.')

        return render(request, self.template_name, context=context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    other_courses = Course.objects.all
    context = {
        'course': course,
        'courses': other_courses,
        'user': request.user
    }
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.course = course
            comment.user = request.user
            comment.save()
            return redirect('course_detail', slug=slug)
    else:
        comment_form = CommentForm()
    comments = Comment.objects.filter(course=course)
    context['comments'] = comments
    context['comment_form'] = comment_form
    return render(request, 'course-single.html', context)

