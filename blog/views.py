from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'About Me',
        'content': 'Hello! My Name is John Doe',
        'date_posted': 'Jan 23, 2008'
    },
    {
        'author': 'Jane Smith',
        'title': 'My Travel Adventures',
        'content': 'Exploring the world, one city at a time!',
        'date_posted': 'Feb 15, 2010'
    },
    {
        'author': 'Mike Johnson',
        'title': 'Tech Trends 2023',
        'content': 'Discussing the latest in technology and innovation.',
        'date_posted': 'Dec 5, 2023'
    },
    {
        'author': 'Emma Watson',
        'title': 'Book Club Highlights',
        'content': 'Sharing thoughts on my favorite reads this month.',
        'date_posted': 'Mar 10, 2021'
    },
    {
        'author': 'Liam Brown',
        'title': 'Fitness Journey',
        'content': 'Tips and tricks for staying healthy and active.',
        'date_posted': 'Sep 8, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})



