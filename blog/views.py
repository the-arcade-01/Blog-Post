from django.shortcuts import render

posts = [
	{
		'author': 'Aashish',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'Nov 11, 2019'
	},
	{
		'author': 'John Jones',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'Nov 15, 2019'
	}
	
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})