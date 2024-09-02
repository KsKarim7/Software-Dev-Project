from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.

# @login_required
# def add_post(req):
#     if(req.method == 'POST'):  #user post request
#         post_form = forms.PostForm(req.POST)  # capturing the post request data of the user
#         if(post_form.is_valid()):  # validation of the posted data
#             # post_form.cleaned_data['author'] = req.user
#             post_form.instance.author = req.user
#             post_form.save()  # if the data valid then it is set in the database
#             return redirect('add_post')  #then sending data to add_post url if everything is good
#     else:  #or else user will get blank form 
#         post_form = forms.PostForm(req.POST)

#     return render(req,'add_post.html',{'form':post_form})



# add post using class based view:
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# @login_required
# def edit_post(req,id):
#     post = models.Post.objects.get(pk=id)  #getting the post with the id
#     post_form = forms.PostForm(instance=post) #getting the post
#     if(req.method == 'POST'):  #user post request
#         post_form = forms.PostForm(req.POST,instance=post)  # capturing the post request data of the user
#         if(post_form.is_valid()):  # validation of the posted data
#             post_form.instance.author = req.user
#             post_form.save()  # if the data valid then it is set in the database
#             return redirect('homepage')  #then sending data to add_post url if everything is good

#     return render(req,'add_post.html',{'form':post_form})


# Class based view
@method_decorator(login_required, name = 'dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwargs = 'id'
    success_url = reverse_lazy('profile')

# @login_required
# def delete_post(req,id):
#     post = models.Post.objects.get(pk=id)
#     post.delete()
#     return redirect('homepage')

# Class based view
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class DetailPostView(DetailView):
    model = models.Post
    template_name = 'post_details.html'