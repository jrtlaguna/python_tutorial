from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


from .forms import PostModelForm
from .models import PostModel

# Create your views here.

def post_model_create_view(request):

    # if request.method == 'POST':
    #     form = PostModelForm(request.POST)
        
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data['title'])
    # if form.is_valid():
    #     obj = form.save()

    #     messages.success(request, "Created a new blog post.")

    #     return HttpResponseRedirect("/blog/{id}".format(id=obj.id))

    form = PostModelForm(request.POST or None)

    context ={
        'form': form
    }
    template = "blog/create_view.html"

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Created a new blog post!")
        context = {
            'form': PostModelForm()
        }

    return render(request, template, context)


def post_model_update_view(request, pk=None):
    obj = get_object_or_404(PostModel, id=pk)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        'obj': obj,
        'form': form
    }   
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated Post!")
        return HttpResponseRedirect("/blog/{id}".format(id=obj.id))

    template = "blog/update_view.html"

    return render(request, template, context)

def post_model_delete_view(request, pk=None):
    obj = get_object_or_404(PostModel, id=pk)
    template = 'blog/delete_view.html'  
    context = {
        'object': obj
    }

    print(request)

    if request.method == 'POST':
        obj.delete()
        messages.success(request, "POST deleted!")
        print('post deleted')
        return redirect('home')

    return render(request, template, context)

    

# @login_required()
def post_model_list_view(request):

    query = request.GET.get("q")
    qs = PostModel.objects.all()

    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) 
            )

    template_path = 'blog/list_view.html'
    context = {
        'posts': qs
    }

    return render(request, template_path, context)

def post_model_detail_view(request, pk):

    qs = PostModel.objects.filter(id=pk)
    
    context = {
        'posts': qs
    }

    return render(request, 'blog/detail_view.html', context)

def login_view(request):

    return render(request, 'blog/login.html')


# def post_model_robust_view(request, pk=None):
  
#     obj = None
#     context = {}
#     success_message = 'A new post was created.'

#     if pk is None:
#         template = "blog/create_view.html"

#     if id is not None:
#         obj = get_object_or_404(PostModel, id=pk)
#         success_message = 'A new post was created.'
#         context['object'] = obj
#         template = "blog/detail_view.html"
#         if "edit" in request.get_full_path():
#             template = "blog/update_view.html"

#     if "delete" in request.get_full_path():
#         template = "blog/delete_view.html"
#         if request.method == "POST":
#             obj.delete()
#             messages.success(request, "Post deleted.")
#             return HttpResponseRedirect('/blog/')
        
#     if "edit" in request.get_full_path() or "create" in request.get_full_path:
#         form = PostModelForm(request.POST or None, instance=obj)
#         context['form'] = form
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#             messages.success(request, success_message)
#             if obj is not None:
#                 return HttpResponseRedirect("blog/{id}".format(obj.id))
#             context['form'] = PostModelForm()

#     return render(request, template, context)