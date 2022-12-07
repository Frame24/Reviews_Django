from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView

from reviews.forms import TextForm
    
def createArticle(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.save()
            form.save_m2m()
            # textobj = form.save()
            # textobj2 = form.save_m2m()
            # textsclassesobj = textobj.entry_set.create(
            #     text_id = textobj['id_text']
            # )
            return HttpResponseRedirect('/index/')
    else:
        form = TextForm()
    return render(request, 'createArticle.html', {'form': form})