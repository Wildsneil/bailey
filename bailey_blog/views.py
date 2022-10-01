from django.shortcuts import render


def post_list(request):
    return render(request, 'bailey_blog/post_list.html', {})
