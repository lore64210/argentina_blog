from django.shortcuts import render
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math

def categories(request):
    categories = Category.objects.all().order_by('start_date')
    print(categories[0].start_date)
    return render(request, "categories.html", {
        "categories": categories
    })

def filteredPosts(request, category = None):
    objects_per_page = 9
    if not category:
        list_of_objects = Post.objects.all()
        main_content = list(filter(lambda post: post.is_main_content, list_of_objects))[:10]
    else:
        category_id = Category.objects.get(label=category)
        list_of_objects = Post.objects.filter(category=category_id).all()
        main_content = []
    p = Paginator(list_of_objects, objects_per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'current_page': page_number,
        'page_obj': page_obj,
        'show_pagination': list_of_objects.count() > objects_per_page,
        'range': range(0, math.ceil(list_of_objects.count() / objects_per_page)),
        'main_content': main_content,
        'show_main_content': len(main_content) != 0
    }
    return render(request, 'list.html', context)

def post(request, post):
    blog_post = Post.objects.get(id = post)
    for category in blog_post.category.all():
        print(category)
    recomendations = Post.objects.filter(category=blog_post.category.all()[0].id).all()
    recomendations = list(filter(lambda post: post.id != blog_post.id, recomendations))[:3]
    return render(request, "post.html", {
        "post": blog_post,
        "recomendations": recomendations
    })

def biographies(request):
    objects_per_page = 9
    list_of_objects = Post.objects.filter(is_biography=True).all()
    p = Paginator(list_of_objects, objects_per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'current_page': page_number,
        'page_obj': page_obj,
        'show_pagination': list_of_objects.count() > objects_per_page,
        'range': range(0, math.ceil(list_of_objects.count() / objects_per_page)),
    }
    return render(request, 'biographies.html', context)

def summary(request):
    return render(request, "summary.html")
