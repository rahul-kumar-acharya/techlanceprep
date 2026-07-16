from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from practice.models import Topic, Question
from accounts.models import User


def home(request):
    topics = Topic.objects.all()
    total_questions = Question.objects.count()
    total_users = User.objects.count()
    return render(request, 'core/home.html', {
        'topics': topics,
        'total_questions': total_questions,
        'total_users': total_users
    })


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def terms_of_service(request):
    return render(request, 'core/terms_of_service.html')


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /tech-admin/",
        "Disallow: /accounts/",
        "Disallow: /dashboard/",
        "Disallow: /practice/bookmarks/",
        "Disallow: /practice/api/",
        "",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def google_verify(request, code):
    content = f"google-site-verification: google{code}.html"
    return HttpResponse(content, content_type="text/plain")



