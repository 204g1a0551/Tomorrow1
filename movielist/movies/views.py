from django.shortcuts import render
def fun1(request):
    movies={'movies':[{'name': 'Kanchana', 'Hero': 'Raghava Lawrence', 'Director': 'Raghava Lawrence', 'Imdb': '5.8', 'ReleaseYear': '2011'},
    {'name': 'Inception', 'Hero': 'Leonardo DiCaprio', 'Director': 'Christopher Nolan', 'Imdb': '8.8', 'ReleaseYear': '2010'},
    {'name': 'The Dark Knight', 'Hero': 'Christian Bale', 'Director': 'Christopher Nolan', 'Imdb': '9.0', 'ReleaseYear': '2008'},
    {'name': 'Interstellar', 'Hero': 'Matthew McConaughey', 'Director': 'Christopher Nolan', 'Imdb': '8.6', 'ReleaseYear': '2014'},
    {'name': 'The Matrix', 'Hero': 'Keanu Reeves', 'Director': 'Lana Wachowski', 'Imdb': '8.7', 'ReleaseYear': '1999'},
    {'name': 'The Godfather', 'Hero': 'Marlon Brando', 'Director': 'Francis Ford Coppola', 'Imdb': '9.2', 'ReleaseYear': '1972'},
    {'name': 'The Shawshank Redemption', 'Hero': 'Tim Robbins', 'Director': 'Frank Darabont', 'Imdb': '9.3', 'ReleaseYear': '1994'}]}
    return render(request,'index.html',movies)
