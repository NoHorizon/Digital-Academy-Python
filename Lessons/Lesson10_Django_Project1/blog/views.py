from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404
from blog.models import Post


# Create your views here.
def home_view(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name='home.html',
        context={
            'title': 'Glory to Ukraine',
            'posts': Post.objects.order_by('-create_time').all()
        }
    )


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    # try:
    #     post: Post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404('Request post does not exist!')
    # else:
    #     return HttpResponse(f'You chose post: {post}')

    # post: Post = get_object_or_404(Post, pk=pk)
    # return HttpResponse(f'You chose post: {post}')
    return render(request, 'post_detail.html', {
        'post': get_object_or_404(Post, pk=pk)
    })
