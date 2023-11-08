from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Article
from django.utils.encoding import uri_to_iri
from django.views.generic import TemplateView

class WeblogView(TemplateView):
    template_name = 'weblog/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(WeblogView,self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context
    
class ArticleView(View):
    
    def get(self,request,slug):
        article = get_object_or_404(Article,slug=uri_to_iri(slug))
        article.views += 1
        article.save()
        return render(request,'weblog/article.html',{'article':article})