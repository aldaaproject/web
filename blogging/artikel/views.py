from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from artikel.models import Kategori, ArtikelBlog
from artikel.forms import KategoriForms, ArtikelForms


def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user == 0:
        return False
    else:
        return True

####################### user biasa #########################
@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = ArtikelBlog.objects.filter(created_by=request.user)
    context = {
        "artikel":artikel,
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Tambah Artikel')
            return redirect('artikel_list')
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id_artikel, created_by=request.user)
    except:
        messages.warning(request, "Halaman yang di Minta Tidak Ditemukan")
        return redirect('/dashboard')

    if request.method == "POST":
        forms = ArtikelForms(request.POST, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Update Artikel')
            return redirect('artikel_list')

    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

    

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel, created_by=request.user).delete()
        messages.success(request, 'Berhasil Delete Artikel')
    except:
        messages.error(request, 'Gagal Delete Artikel')

    return redirect('artikel_list')

########################### admin ############################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori":kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":

        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Tambah Kategori')
            return redirect('admin_kategori_list')
    forms = KategoriForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)

    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Update Kategori')
            return redirect('admin_kategori_list')
    forms = KategoriForms(instance=kategori)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
    try:
        kategori = Kategori.objects.get(id=id_kategori).delete()
        messages.success(request, 'Berhasil Delete Kategori')
    except:
        messages.error(request, 'Gagal Delete Kategori')

    return redirect('admin_kategori_list')

##################### Artikel Blog #########################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        "artikel":artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Tambah Artikel')
            return redirect('admin_artikel_list')
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = ArtikelBlog.objects.get(id=id_artikel)

    if request.method == "POST":
        forms = ArtikelForms(request.POST, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Update Artikel')
            return redirect('admin_artikel_list')

    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

    

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
        messages.success(request, 'Berhasil Delete Artikel')
    except:
        messages.error(request, 'Gagal Delete Artikel')

    return redirect('admin_artikel_list')