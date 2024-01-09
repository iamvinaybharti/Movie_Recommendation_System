from django.shortcuts import render,redirect
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.forms import ModelForm
from django.contrib import messages
from django import forms
from .models import User

logstatus = None

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

class RegisterForm(forms.ModelForm):
    g = [("1", "Male"), ("2", "Female")]
    year = [str(i) for i in range(1980, 2010)]
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter Email"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Number"}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter Password"}))
    gender = forms.ChoiceField(label="Gender :", choices=g)
    dob = forms.DateField(label="Select Date :", widget=forms.SelectDateWidget(years=year))
    class Meta:
        model = User
        fields = ['name', 'email', 'number', 'password','gender', 'dob']

def welcome(request, template_name="RecEngine/welcome.html"):
    return render(request, template_name)

def home(request, template_name="RecEngine/home.html"):
    login_status = request.session['login_status']
    if (login_status == "1"):
        return render(request, template_name)
    else:
        return redirect('login')

def about(request, template_name="RecEngine/about.html"):
    return render(request, template_name, {"logstatus": logstatus})

def login(request, template_name="RecEngine/login.html"):
    global logstatus

    request.session['login_status'] = "0"
    form = LoginForm(request.POST)
    if (form.is_valid()):
        email = request.POST['email']
        password = request.POST['password']

        try:
            b = User.objects.get(email=email, password=password)
        except:
            b = False
            messages.error(request, "Your Email & Password is Incorrect")
        if (b):
            request.session['login_status'] = "1"
            logstatus = request.session['login_status']
            return render(request, "RecEngine/home.html", {"logstatus":logstatus,"b":b})
        else:
            return redirect('login')

    return render(request, template_name)

def register(request, template_name="RecEngine/register.html"):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your Account Has Been Created Successfully !")
        return render(request, template_name, {"form": form})
    return render(request, template_name, {"form": form})

def logout(request):
    # clear the session here...
    request.session['login_status'] = None
    return redirect('login')

def result(request):
    if request.method == "POST":
        value = request.POST['srh']
        value = value.title()

        def get_title_from_index(index):
            return df[df.index == index]["title"].values[0]

        def get_index_from_title(title):
            try:
                return df[df.title == title]["index"].values[0]
            except:
                return render(request, "RecEngine/error.html" , {"logstatus": logstatus})


        ##################################################

        ##Step 1: Read CSV File
        df = pd.read_csv("RecEngine/movie_dataset.csv")
        
        # print df.columns
        ##Step 2: Select Features

        features = ['keywords', 'cast', 'genres', 'director']
        ##Step 3: Create a column in DF which combines all selected features
        for feature in features:
            df[feature] = df[feature].fillna('')

        def combine_features(row):
            try:
                return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
            except:
                print("Error:", row)
                return render(request, "RecEngine/error.html", {"logstatus": logstatus})


        df["combined_features"] = df.apply(combine_features,axis=1)

        # print "Combined Features:", df["combined_features"].head()

        ##Step 4: Create count matrix from this new combined column
        cv = CountVectorizer()

        count_matrix = cv.fit_transform(df["combined_features"])

        ##Step 5: Compute the Cosine Similarity based on the count_matrix
        cosine_sim = cosine_similarity(count_matrix)
        # movie_user_likes = "Aliens"
        movie_user_likes = value
        ## Step 6: Get index of this movie from its title
        movie_index = get_index_from_title(movie_user_likes)

        try:
            similar_movies = list(enumerate(cosine_sim[movie_index]))
        except:
            return render(request, "RecEngine/error.html", {"logstatus": logstatus})

        ## Step 7: Get a list of similar movies in descending order of similarity score
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

        ## Step 8: Print titles of first 50 movies
        i = 0
        movies = []
        
        for element in sorted_similar_movies:
            movies.append(get_title_from_index(element[0]))
            i = i + 1
            if i > 10:
                maxee=max(movies)
                break
    return render(request, "RecEngine/result.html", {'movies':movies, "logstatus":logstatus,'maxee':maxee})



def detail(request, movie_id):
    def get_title_from_index(index):
        return df[df.index == index]["title"].values[0]

    def get_genre_from_index(index):
        return df[df.index == index]["genres"].values[0]

    def get_release_from_index(index):
        return df[df.index == index]["release_date"].values[0]

    def get_budget_from_index(index):
        return df[df.index == index]["budget"].values[0]

    def get_director_from_index(index):
        return df[df.index == index]["director"].values[0]

    def get_popularity_from_index(index):
        return df[df.index == index]["popularity"].values[0]

    def get_revenue_from_index(index):
        return df[df.index == index]["revenue"].values[0]

    def get_runtime_from_index(index):
        return df[df.index == index]["runtime"].values[0]

    def get_tagline_from_index(index):
        return df[df.index == index]["tagline"].values[0]

    def get_vote_from_index(index):
        return df[df.index == index]["vote_count"].values[0]

    def get_average_from_index(index):
        return df[df.index == index]["vote_average"].values[0]
    
    def get_cast_from_index(index):
        return df[df.index == index]["cast"].values[0]

    def get_overview_from_index(index):
        return df[df.index == index]["overview"].values[0]

    def get_index_from_title(title):
        return df[df.title == title]["index"].values[0]

    ##################################################

    ##Step 1: Read CSV File
    df = pd.read_csv("RecEngine/movie_dataset.csv")
    # print df.columns
    ##Step 2: Select Features

    features = ['keywords', 'cast', 'genres', 'director']
    ##Step 3: Create a column in DF which combines all selected features
    for feature in features:
        df[feature] = df[feature].fillna('')

    def combine_features(row):
        try:
            return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
        except:
            print("Error:", row)

    df["combined_features"] = df.apply(combine_features, axis=1)

    # print "Combined Features:", df["combined_features"].head()

    ##Step 4: Create count matrix from this new combined column
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df["combined_features"])

    ##Step 5: Compute the Cosine Similarity based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix)
    # movie_user_likes = "Aliens"
    movie_user_likes = movie_id

    ## Step 6: Get index of this movie from its title
    movie_index = get_index_from_title(movie_user_likes)

    similar_movies = list(enumerate(cosine_sim[movie_index]))

    ## Step 7: Get a list of similar movies in descending order of similarity score
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    ## Step 8: Print titles of first 50 movies
    i = 0
    movies = {}
    for element in sorted_similar_movies:
        title = get_title_from_index(element[0])
        movies['title'] = title

        genre = get_genre_from_index(element[0])
        movies['genre'] = genre

        release = get_release_from_index(element[0])
        movies['release'] = release

        budget = get_budget_from_index(element[0])
        movies['budget'] = budget

        director = get_director_from_index(element[0])
        movies['director'] = director

        popularity = get_popularity_from_index(element[0])
        movies['popularity'] = popularity

        revenue = get_revenue_from_index(element[0])
        movies['revenue'] = revenue

        runtime = get_runtime_from_index(element[0])
        movies['runtime'] = runtime

        tagline = get_tagline_from_index(element[0])
        movies['tagline'] = tagline

        vote = get_vote_from_index(element[0])
        movies['vote'] = vote

        cast = get_cast_from_index(element[0])
        movies['cast'] = cast

        average = get_average_from_index(element[0])
        movies['average'] = average

        overview = get_overview_from_index(element[0])
        movies['overview'] = overview
        movies['logstatus'] = logstatus
        i = i + 1
        if i >= 1:
            break

    return render(request, 'RecEngine/detail.html', movies)