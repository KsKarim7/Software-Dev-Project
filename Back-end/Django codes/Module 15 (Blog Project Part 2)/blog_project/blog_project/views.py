from django.shortcuts import render
from posts.models import Post


def home(req):
    data = Post.objects.all()
        # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(req,'home.html',{'data':data})