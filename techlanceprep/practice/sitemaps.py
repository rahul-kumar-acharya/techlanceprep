from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Topic, Question

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact', 'faq', 'pricing', 'privacy_policy', 'terms_of_service', 'all_topics']

    def location(self, item):
        return reverse(item)


class TopicSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return Topic.objects.all().order_by('name')

class QuestionSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Question.objects.all().select_related('topic').order_by('title')
