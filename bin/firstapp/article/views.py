# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator

# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</html></body>" %view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('myview.html') 
    html = t.render(Context({'name': view})) 
    return HttpResponse(html)

def template_three_simple(request):
    view = 'template_three'
    return render_to_response('myview.html',{'name': view})

def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 3    )
    return render_to_response('articles.html',{'articles': current_page.page(page_number), 'username': auth.get_user(request).username})

def article(request, article_id=1):
#    return render_to_response('article.html',{'article': Article.objects.get(id=article_id),'comments': Comments.objects.filter(comments_article_id=article_id)})
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    try:
        args['article'] = Article.objects.get(id=article_id)
        args['comments'] = Comments.objects.filter(comments_article=article_id)
        args['form'] = comment_form
        args['username'] = auth.get_user(request).username #получение имени пользователя из request если существует
    except Exception as ex:
        print "err:{}".format(ex)
    return render_to_response('article.html', args) 

def addlike(request, article_id, page_number):
    try:
        if article_id in request.COOKIES:
            redirect("/page/"+page_number+'/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/page/'+page_number+"/")
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/page/'+page_number+'/')
    
def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST) #из брауз.отправились в commentform и присвоились в form
        if form.is_valid():
            comment = form.save(commit=False) #commit=False для того что бы form.save не сохранял данные в базу пока не получить comments_article
            comment.comments_article = Article.objects.get(id=article_id) #
            comment.comments_user = auth.get_user(request).username
            form.save() #
            request.session.set_expiry(60) #создает объект сессии который живет в течении 60 сек
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)

