from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse

from posts.models import Post

class PostsListView(ListView):
	def get_queryset(self):
		try:
			category = self.kwargs['category']
			print(category)
			queryset = Post.objects.filter(status="published").filter(category__title=category)
			return queryset, category
		except:
			queryset = Post.objects.filter(status="published")
			category = ''
			return queryset, category
	#context_object_name = "posts"
	template_name = "posts/list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = self.get_queryset()[1]
		context['posts'] = self.get_queryset()[0]
		return context
    #context_object_name = "posts"
    #template = "posts/list.html"

def take_posts_by_category(request):
	if request.method == "POST":
			categories = request.POST["take"]
			print(categories)
			posts = TodoItem.objects.filter(category=categories)
			return render(request, "posts/post_list.html", {"posts": posts})
			#queryset = categories
			#return queryset

def json_list_published_posts(request):
    posts = Post.objects.filter(status="published")
    1 / 0
    return JsonResponse(
        {
            "posts": [
                {
                    "title": p.title,
                    "slug": p.slug,
                    "id": p.id,
                    "published": p.when_published,
                }
                for p in posts
            ]
        }
    )

# Create your views here.
