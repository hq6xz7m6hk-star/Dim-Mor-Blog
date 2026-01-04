from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная": "/", "рецензии": "/catalog", "о сайте": "/about", "отзывы": "/comment"}

def main_page(request):
   title = "Главная страница"
   data = {"menu": MENU, "title": title}
   return render(request, "./index.html", context=data)

def catalog_page(request):
   title = "рецензии"
   data = {"menu": MENU, "title": title}
   return render(request, "./catalog.html", context=data)

def about_page(request):
   title = "о сайте"
   data = {"menu": MENU, "title": title}
   return render(request, "./about.html", context=data)

def comment_page(request):
   title = "отзывы"
   data = {"menu": MENU, "title": title}
   return render(request, "./comment.html", context=data)