from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from  .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
import os
from django.conf import settings
from django.http import Http404, HttpResponse
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>. html
    context_object_name = 'posts'
    paginate_by = 7

   

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
     


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['NOM','PRENOM','POSTNOM','UNIVERSITE','PROGRAMME','FACULTE','DEPARTEMENT','LOGEMENT','NOM_DU_PERE','NOM_DE_LA_MERE','PHOTO','DIPLOMES','COPIE_DU_PASSPORT','NIVEAU_EN_ANGLAIS','PAYS','NUMERO_DE_TEL']
 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['NOM','PRENOM','POSTNOM','UNIVERSITE','PROGRAMME','FACULTE','DEPARTEMENT','LOGEMENT','NOM_DU_PERE','NOM_DE_LA_MERE','PHOTO','DIPLOMES','COPIE_DU_PASSPORT','NIVEAU_EN_ANGLAIS','PAYS','NUMERO_DE_TEL']
 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def download_file(request, pk):
    post = get_object_or_404(Post, pk=pk)
    file_path = post.PHOTO.path if request.GET.get('type') == 'photo' else post.DIPLOMES.path if request.GET.get('type') == 'diplome' else post.COPIE_DU_PASSPORT.path if request.GET.get('type') == 'passport' else post.NIVEAU_EN_ANGLAIS.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404    
  


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def head(request):

    return render(request, 'blog/header.html')

 
def homes(request):

    return render(request,'blog/Homes.html')


def ciu(request):
    return render(request, 'blog/Ciuuniversity.html')

def neu(request):
    return render(request, 'blog/Near eastuniversity.html')

def gau(request):
    return render(request, 'blog/Gauuniversity.html')


def emu(request):
    return render(request, 'blog/EMUuniversity.html')


def bau(request):
    return render(request, 'blog/Bauuniversity.html')

def underciu(request):
    return render( request, 'blog/undergraduate.html')

 
def underbau(request):
    return render( request, 'blog/undergraduateBAU.html')

def underneu(request):
    return render( request, 'blog/undergraduateNEU.html')

def undergau(request):
    return render( request, 'blog/undergraduateGAU.html')

def underemu(request):
    return render( request, 'blog/undergraduateEMU.html')

 
def admi(request):
    return render( request, 'blog/admissionP.html')

 
def ser(request):
    return render( request, 'blog/services.html')

 
def chy(request):
    return render( request, 'blog/chypre.html')



def masterciu(request):
    return render( request, 'blog/MasterProgram.html')


def masterneu(request):
    return render( request, 'blog/MasterProgramNEU.html')

def masterbau(request):
    return render( request, 'blog/MasterProgramBAU.html')


def mastergau(request):
    return render( request, 'blog/MasterProgramGAU.html')

def masteremu(request):
    return render( request, 'blog/MasterProgramEMU.html')


def doctoratgau(request):
     return render( request, 'blog/DoctoratGAU.html')


def doctoratneu(request):
     return render( request, 'blog/DoctoratNEU.html')


def doctoratemu(request):
     return render( request, 'blog/DoctoratEMU.html')


def doctoratemu(request):
     return render( request, 'blog/DoctoratEMU.html')

def doctoratciu(request):
     return render( request, 'blog/Doctorat.html')
 
def doctoratbau(request):
     return render( request, 'blog/Doctorat.html')

