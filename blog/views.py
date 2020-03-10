from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



#function view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


#class list 
class PostListView(ListView):
  	model = Post
  	template_name = 'blog/home.html'
  	context_object_name = 'posts'
  	ordering = '-date_posted'
  	paginate_by = 10   


class UserPostListView(ListView):
  	model = Post
  	template_name = 'blog/user_posts.html'
  	context_object_name = 'posts'
  	paginate_by = 10


  	def get_queryset(self):
  		user = get_object_or_404(User, username = self.kwargs.get('username'))
  		return Post.objects.filter(author=user).order_by('-date_posted')

  	
#Detailed view
class PostDetailView(DetailView):
  	model = Post
 

class PostCreateView(LoginRequiredMixin,CreateView):
  	model = Post
  	fields = ['title','content']

  	def form_valid(self,form):
  		form.instance.author = self.request.user
  		return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  	model = Post
  	success_url ='/'
  	fields = ['title','content']

  	def form_valid(self,form):
  		form.instance.author = self.request.user
  		return super().form_valid(form)


  			# put catch 403 exception here to handle error and redirect home 
  	def test_func(self):
  		post = self.get_object()
  		if self.request.user == post.author:
  			return True



def about(request):
    return render (request,'blog/about.html', {'title': 'About'} )


def announcement(request):
  return render (request,'blog/announcement.html', {'title': 'Announcement'})


def gallery(request):
  return render (request, 'blog/gallery.html', {'title':'Gallery'})




#delet function done but wont implement it till requested 
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
 	model = Post
 	success_url ='/'

 	def test_func(self):
 		post = self.get_object()
 		if self.request.user == post.author:
 			return True
 		return False







