from django.shortcuts import render

posts = [
    {
        'author': 'Iggy',
        'title': 'Blog post #1',
        'content': 'First post content',
        'date_posted': 'October 11, 2023'
    },
    {
        'author': 'Naty',
        'title': 'Blog post #2',
        'content': 'Second post content',
        'date_posted': 'October 12, 2023'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})