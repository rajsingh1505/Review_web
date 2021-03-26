from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg


# Create your views here.
def home(request):
    allMovies = Movie.objects.all()  # select * from movie

    context = {
        "movies": allMovies,
    }

    return render(request, 'main/index.html', context)

def detail(request, id):
    movie = Movie.objects.get(id=id) # select * from movie where id=id
    reviews = Review.objects.filter(movie=id).order_by("-comment")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)
    context = {
        "movie": movie,
        "reviews": reviews,
        "average": average
    }
    return render(request, 'main/details.html', context)







def add_review(request, id):
        movie = Movie.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("main:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', {"form": form})




#