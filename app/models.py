from itertools import count
from tkinter import N
from typing_extensions import runtime
from sqlalchemy import null, text, desc, asc, and_, or_, nullslast
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc
from datetime import date
import random
import math
import datetime
from datetime import datetime, timedelta
from sqlalchemy.sql import column
from babel.dates import format_date, format_datetime, format_time
import statistics
import math
import re
import json
import pytz
'''
This file defines data models and related business logics
'''

db = SQLAlchemy(app)

class Movie(db.Model):
    """A class to represent a movie."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rewatch = db.Column(db.Boolean, nullable=True)
    rewatchScore = db.Column(db.Integer, nullable=False)
    rewatchCount = db.Column(db.Integer, nullable=False)
    rewatchCountList = db.Column(db.Integer, nullable=False)
    cinematicScore = db.Column(db.Integer, nullable=False)
    cinematicCount = db.Column(db.Integer, nullable=False)
    poster = db.Column(db.String(100), nullable=True)
    rank = db.Column(db.Integer, nullable=True)
    unwatched = db.Column(db.Boolean, nullable=True)
    director = db.Column(db.String(120), nullable=True)
    runtime = db.Column(db.Integer, nullable=True)
    lastWatchedDate = db.Column(db.Date, nullable=True)
    notes = db.Column(db.String(1000), nullable=True)
    stars = db.Column(db.Integer, nullable=True)
    recommend = db.Column(db.String(120), nullable=True)
    genres = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(500), nullable=True)
    rankingPercentage = db.Column(db.Integer, nullable=True)
    rankingPercentageList = db.Column(db.Integer, nullable=True)
    rankingWinCount = db.Column(db.Integer, nullable=True)
    rankingWinCountList = db.Column(db.Integer, nullable=True)
    pointsGained = db.Column(db.Integer, nullable=True)
    winsGained = db.Column(db.Integer, nullable=True)
    faveQuote = db.Column(db.String(500), nullable=True)
    timesWatched = db.Column(db.Integer, nullable=True)
    currentlyWatching = db.Column(db.Boolean, nullable=True)
    beatBelow = db.Column(db.Boolean, nullable=True)
    liked = db.Column(db.Integer, nullable=True)
    winnerUpsetCount = db.Column(db.Integer, nullable=True)
    loserUpsetCount = db.Column(db.Integer, nullable=True)
    onComputer = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return "<Movie %r>" % self.title
    

class Genre(db.Model):
    """A class to represent a movie genre."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    count = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return "<Genre %r>" % self.name

class MovieGenre(db.Model):
    """A class to represent the link between movies and genres."""
    id = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.Integer, nullable=False)
    genreId = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Movie_Genre %r>" % self.movieId

class Ranking(db.Model):
    """A class to record the ranking."""
    id = db.Column(db.Integer, primary_key=True)
    winnerMovieId = db.Column(db.Integer, nullable=False)
    loserMovieId = db.Column(db.Integer, nullable=False)
    modifiedDate = db.Column(db.DateTime, nullable=False)
    winnerStartingPoints = db.Column(db.Integer, nullable=False)
    loserStartingPoints = db.Column(db.Integer, nullable=False)
    winnerPointsGained = db.Column(db.Integer, nullable=False)
    loserPointsLossed = db.Column(db.Integer, nullable=False)
    winnerEndingPoints = db.Column(db.Integer, nullable=False)
    losserEndingPoints = db.Column(db.Integer, nullable=False)
    winnerCount = db.Column(db.Integer, nullable=False)
    loserCount = db.Column(db.Integer, nullable=False)
    winnerTitle = db.Column(db.String(250), nullable=True)
    winnerPoster = db.Column(db.String(250), nullable=True)
    loserTitle = db.Column(db.String(250), nullable=True)
    loserPoster = db.Column(db.String(250), nullable=True)
    overwriteDate = db.Column(db.DateTime, nullable=True)
    overwriteRankingId = db.Column(db.Integer, nullable=True)
    saved = db.Column(db.Boolean, nullable=True)
    sessionId = db.Column(db.Integer, nullable=True)
    flagged = db.Column(db.Boolean, nullable=True)
    loserRank = db.Column(db.Integer, nullable=True)
    winnerRank = db.Column(db.Integer, nullable=True)
    loserYear = db.Column(db.Integer, nullable=True)
    winnerYear = db.Column(db.Integer, nullable=True)
    rankingDate = db.Column(db.String(120), nullable=True)
    confirmed = db.Column(db.DateTime, nullable=True)
    rankingDifference = db.Column(db.Integer, nullable=True)
    reversed = db.Column(db.Boolean, nullable=True)
    generated = db.Column(db.Boolean, nullable=True)
    generatedNotes = db.Column(db.String(200), nullable=True)
    likeUpset = db.Column(db.Boolean, nullable=True)
    winnerLiked = db.Column(db.Integer, nullable=True)
    loserLiked = db.Column(db.Integer, nullable=True)
    winnerStars = db.Column(db.Integer, nullable=True)
    loserStars = db.Column(db.Integer, nullable=True)
    listId = db.Column(db.Integer, nullable=True)


    def __repr__(self):
        return "<Ranking %r>" % self.id
    
class SharedRanking(db.Model):
    """A class to record the ranking."""
    id = db.Column(db.Integer, primary_key=True)
    winnerMovieId = db.Column(db.Integer, nullable=False)
    loserMovieId = db.Column(db.Integer, nullable=False)
    modifiedDate = db.Column(db.DateTime, nullable=False)
    winnerStartingPoints = db.Column(db.Integer, nullable=False)
    loserStartingPoints = db.Column(db.Integer, nullable=False)
    winnerPointsGained = db.Column(db.Integer, nullable=False)
    loserPointsLossed = db.Column(db.Integer, nullable=False)
    winnerEndingPoints = db.Column(db.Integer, nullable=False)
    losserEndingPoints = db.Column(db.Integer, nullable=False)
    winnerCount = db.Column(db.Integer, nullable=False)
    loserCount = db.Column(db.Integer, nullable=False)
    winnerTitle = db.Column(db.String(250), nullable=True)
    winnerPoster = db.Column(db.String(250), nullable=True)
    loserTitle = db.Column(db.String(250), nullable=True)
    loserPoster = db.Column(db.String(250), nullable=True)
    overwriteDate = db.Column(db.DateTime, nullable=True)
    overwriteRankingId = db.Column(db.Integer, nullable=True)
    saved = db.Column(db.Boolean, nullable=True)
    sessionId = db.Column(db.Integer, nullable=True)
    flagged = db.Column(db.Boolean, nullable=True)
    loserRank = db.Column(db.Integer, nullable=True)
    winnerRank = db.Column(db.Integer, nullable=True)
    loserYear = db.Column(db.Integer, nullable=True)
    winnerYear = db.Column(db.Integer, nullable=True)
    rankingDate = db.Column(db.String(120), nullable=True)
    confirmed = db.Column(db.DateTime, nullable=True)
    rankingDifference = db.Column(db.Integer, nullable=True)
    reversed = db.Column(db.Boolean, nullable=True)
    newColumn = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return "<Ranking %r>" % self.id
    

class MovieWatch(db.Model):
    """A class to represent the link between movies and watch instances."""
    id = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(500), nullable=True)
    watchDate = db.Column(db.Date, nullable=True)
    people = db.Column(db.String(500), nullable=True)
    moviePoster = db.Column(db.String(500), nullable=True)
    movieTitle = db.Column(db.String(500), nullable=True)
    notes = db.Column(db.String(500), nullable=True)
    movieRecommendation = db.Column(db.String(500), nullable=True)
    movieStars = db.Column(db.String(500), nullable=True)
    movieOverallNotes = db.Column(db.String(1000), nullable=True)
    firstWatch = db.Column(db.Boolean, nullable=True)
    movieLiked = db.Column(db.Integer, nullable=True)
    confirmedStars = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return "<Movie_Watch %r>" % self.movieId
    
class List(db.Model):
    """A class to represent the link between movies and watch instances."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    count = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return "<List %r>" % self.name
    
class ListMovie(db.Model):
    """A class to represent the link between movies and lists instances."""
    id = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.Integer, nullable=False)
    listId = db.Column(db.Integer, nullable=False)
    movieName = db.Column(db.String(500), nullable=True)
    moviePoster = db.Column(db.String(500), nullable=True)
    listName = db.Column(db.String(500), nullable=True)


    def __repr__(self):
        return "<List %r>" % self.movieName

class SavedRanking(db.Model):
    """A class to represent savedRankings."""
    id = db.Column(db.Integer, primary_key=True)
    firstMovieId = db.Column(db.Integer, nullable=False)
    secondMovieId = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Saved Ranking %r>" % self.id
    
class Session(db.Model):
    """A class to represent the link between movies."""
    id = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DateTime, nullable=True)
    endDate = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "<Sessions %r>" % self.id


# create all tables
db.create_all()

def getListDetailsFromNAme(name, title):
    if len(name) < 1: 
        return []
    search = '%' + name + '%' 
    records = MovieWatch.query.filter(MovieWatch.people.like(search)).order_by(desc(MovieWatch.watchDate)).all()

    for x in records:
        movie = Movie.query.filter(Movie.id == x.movieId).all()[0]
        x.movieTitle = movie.title
        x.movieLiked = movie.liked
        x.movieRecommendation = movie.recommend
        x.movieStars = movie.stars
        x.movieOverallNotes = movie.notes

    results = []
    if len(title) > 0:
        for x in records:
            if title.upper() in x.movieTitle.upper():
                results.append(x) 
        return results 
        
    return records


def getListDetails(id):
    list = List.query.filter(List.id == id).all()[0]
    
    return list

def getListPeople():
    sql = text('SELECT DISTINCT people From movie_watch \
            WHERE people is not null and length(people) > 1;')
    people = db.engine.execute(sql)
    records = []
    for row in people:
        records.append(row[0]) #ids
    
    names = []
    for record in records:
        commaCount = record.count(',')
        andCount = record.upper().count('and'.upper())
        if commaCount == 0 and andCount ==0:
            name = record.strip()
            found = False
            for n in names:
                if n.upper() == name.upper():
                    found = True
                    break
            if not found:
                names.append(name)
        seperatedNames = []
        if commaCount > 0:
            seperatedNames = record.split(',')
            for seperatedName in seperatedNames:
                name = seperatedName.strip()
                name = name.replace('and ', ',')
                if name.upper() != 'AND':
                    found = False
                    for n in names:
                        if n.upper() == name.upper():
                            found = True
                            break
                    if not found:
                        names.append(name)

    return names

def getPerson(name):
    search = '%' + name + '%' 
    records = MovieWatch.query.filter(MovieWatch.people.like(search)).all()

    movies = []
    for log in records: 
        movie = Movie.query.filter(Movie.id == log.movieId).all()[0]
        movie.genres = getMovieGenreNames(movie.id)
        found = False
        for mov in movies:
            if mov.id == movie.id:
                found = True
        if not found:
            movies.append(movie)
    
    return movies
    

def getAllLists():
    list = List.query.filter(text("id <> 20 and id <> 21 and id <> 22 and id <> 23 and id <> 24 and id <> 25 and id <> 16 and id <> 28 and id <> 32")).order_by(List.name).all()
    
    return list

def getListsOfPeople():
   list = List.query.filter(text("id = 20 or id = 21 or id = 22 or id = 23 or id = 24 or id = 25")).order_by(List.name).all()
   return list

def getListOfYears():
    list = List.query.filter(text("id = 16 or id = 28 or id = 32")).order_by(List.name).all()
    return list

def getUnwatchedMoviesFromList(listId):
    movieIds = ListMovie.query.filter(ListMovie.listId == listId).all()
    movies = []
    for x in movieIds:
        movie = Movie.query.filter(and_(Movie.id == x.movieId, Movie.unwatched == 1)).all()
        if len(movie) > 0:
            movie = movie[0]
            movie.genres = getMovieGenreNames(movie.id)
            movies.append(movie)

    movies.sort(key=lambda x: x.title, reverse=False)
    
    # return getOverallRanks(movies)
    return movies

def checkNotLastRanked(first, second):
    rankings = Ranking.query.filter(and_(text('overwriteRankingId IS NULL') , or_
                                    (and_
                                     (Ranking.winnerMovieId == first, Ranking.loserMovieId == second), 
                                     and_
                                     (Ranking.winnerMovieId == second, Ranking.loserMovieId == first)
                                ))).order_by(desc(Ranking.modifiedDate)).limit(1).all()
    if len(rankings) < 1:
        return True
    
    if rankings[0].modifiedDate - datetime.now() > timedelta(days=1):
        return True

    return False

def getMoviesFromList(listId):
    movieIds = ListMovie.query.filter(ListMovie.listId == listId).all()

    movieIdString = "("
    for x in movieIds:
        movieIdString = movieIdString + str(x.movieId) + ","
    movieIdString = movieIdString + "0)"
    movies = []
    textStr1 = 'loserMovieId IN ' + movieIdString
    textStr2 = 'winnerMovieId IN ' + movieIdString
    for x in movieIds:
        movie = Movie.query.filter(and_(Movie.id == x.movieId, Movie.unwatched != 1)).all()
        if len(movie) > 0:
            movie = movie[0]
            movie.genres = getMovieGenreNames(movie.id)
            movie.rankingWinCountList = len(Ranking.query.filter(and_(Ranking.winnerMovieId == movie.id, text('overwriteRankingId IS NULL'), text(textStr1))).all())
            movie.rewatchCountList = len(Ranking.query.filter(and_(or_(Ranking.winnerMovieId == movie.id, Ranking.loserMovieId == movie.id), text(textStr1),text(textStr2), text('overwriteRankingId IS NULL'))).all())
            if movie.rewatchCountList > 0:
                movie.rankingPercentageList = int(movie.rankingWinCountList / movie.rewatchCountList * 100)
            else:
                movie.rankingPercentageList = 0
            movies.append(movie)

    movies.sort(key=lambda x: (x.rankingPercentageList, x.rankingWinCountList, -x.rewatchCountList, x.rewatchScore), reverse=True) 
    
    return rankingAlgorithm(getOverallRanks(movies))
    #return movies

def misLikedUosetLoserss():
    sqlText = text(""" 
            SELECT m_loser.id AS WinnerTitle, COUNT(*) AS WinsAgainstLiked1
FROM ranking r
JOIN movie m_winner ON r.winnerMovieId = m_winner.id
JOIN movie m_loser ON r.loserMovieId = m_loser.id
WHERE ((m_winner.liked = 3 AND m_loser.liked = 1) or (m_winner.liked = 2 AND m_loser.liked = 1) or ((m_winner.liked = 3 AND m_loser.liked = 2)))  AND r.overwriteRankingId is NULL
GROUP BY m_loser.title 
HAVING WinsAgainstLiked1 > 3
ORDER by WinsAgainstLiked1 desc


""")
    
    movies = db.engine.execute(sqlText)
    names = []
    liked_counts = []
    for row in movies:
        names.append(row[0])
        liked_counts.append(row[1])
    
    moviesList = []
    counter = 0
    for x in names:
        movie = Movie.query.filter(Movie.id == x).all()[0]
        movie.cinematicCount = liked_counts[counter]
        moviesList.append(movie)
        counter = counter + 1

    return moviesList


def misLikedUosets():
    sqlText = text(""" 
            SELECT m_winner.id AS WinnerTitle, COUNT(*) AS WinsAgainstLiked1
FROM ranking r
JOIN movie m_winner ON r.winnerMovieId = m_winner.id
JOIN movie m_loser ON r.loserMovieId = m_loser.id
WHERE ((m_winner.liked = 3 AND m_loser.liked = 1) or (m_winner.liked = 2 AND m_loser.liked = 1) or ((m_winner.liked = 3 AND m_loser.liked = 2)))  AND r.overwriteRankingId is NULL
GROUP BY m_winner.title
                   HAVING WinsAgainstLiked1 > 3
ORDER by WinsAgainstLiked1 desc


""")
    
    movies = db.engine.execute(sqlText)
    names = []
    liked_counts = []
    for row in movies:
        names.append(row[0])
        liked_counts.append(row[1])
    
    moviesList = []
    counter = 0
    for x in names:
        movie = Movie.query.filter(Movie.id == x).all()[0]
        movie.cinematicCount = liked_counts[counter]
        moviesList.append(movie)
        counter = counter + 1

    return moviesList


def top_directors():
    sqlText = text("""
    WITH LikedMoviesCount AS (
        SELECT director, COALESCE(COUNT(*), 0) as liked_movies_count
        FROM movie
        WHERE unwatched <> 1 AND liked = 1
        GROUP BY director
    ),
    DecentMoviesCount AS (
        SELECT director, COALESCE(COUNT(*), 0) as decent_movies_count
        FROM movie
        WHERE unwatched <> 1 AND liked = 2
        GROUP BY director
    ),
    BadMoviesCount AS (
        SELECT director, COALESCE(COUNT(*), 0) as bad_movies_count
        FROM movie
        WHERE unwatched <> 1 AND liked = 3
        GROUP BY director
    ),
    TopMovies AS (
        SELECT director, id, title, rewatchScore,
               ROW_NUMBER() OVER (PARTITION BY director ORDER BY rewatchScore DESC) as rn
        FROM movie
        WHERE unwatched <> 1
    ),
    DirectorMovieCount AS (
        SELECT director, COUNT(*) as total_movies
        FROM movie
        WHERE unwatched <> 1
        GROUP BY director
    )
    SELECT 
        tm.director, 
        ROUND(AVG(tm.rewatchScore)) as average_rewatchScore, 
        dmc.total_movies as movie_count,
        lmc.liked_movies_count as liked_movie_count,
        dmc2.decent_movies_count as decent_movie_count,
        bmc.bad_movies_count as bad_movie_count,
        MAX(CASE WHEN tm.rn = 1 THEN tm.id END) as top_movie_id_1, 
        MAX(CASE WHEN tm.rn = 1 THEN tm.title END) as top_movie_poster_1,
        MAX(CASE WHEN tm.rn = 2 THEN tm.id END) as top_movie_id_2, 
        MAX(CASE WHEN tm.rn = 2 THEN tm.title END) as top_movie_poster_2,
        MAX(CASE WHEN tm.rn = 3 THEN tm.id END) as top_movie_id_3, 
        MAX(CASE WHEN tm.rn = 3 THEN tm.title END) as top_movie_poster_3
    FROM TopMovies tm
    JOIN DirectorMovieCount dmc ON tm.director = dmc.director
    LEFT JOIN LikedMoviesCount lmc ON tm.director = lmc.director
    LEFT JOIN DecentMoviesCount dmc2 ON tm.director = dmc2.director
    LEFT JOIN BadMoviesCount bmc ON tm.director = bmc.director
    WHERE tm.rn <= 3
    GROUP BY tm.director, dmc.total_movies, lmc.liked_movies_count, dmc2.decent_movies_count, bmc.bad_movies_count
    HAVING movie_count > 2
    ORDER BY lmc.liked_movies_count DESC, (lmc.liked_movies_count / dmc.total_movies) DESC, dmc2.decent_movies_count DESC, bmc.bad_movies_count ASC, average_rewatchScore DESC
                   LIMIT 10;
    """)
    movies = db.engine.execute(sqlText)
    names = []
    liked_counts = []
    decent_counts = []
    bad_counts = []
    scores = []
    counts = []
    firsts  = []
    firsts1  = []
    seconds = []
    seconds1 = []
    thirds = []
    thirds1 = []
    for row in movies:
        names.append(row[0])
        liked_counts.append(row[3])
        decent_counts.append(row[4])
        bad_counts.append(row[5])
        scores.append(row[1])
        counts.append(row[2])
        firsts.append(row[6])
        firsts1.append(row[7])
        seconds.append(row[8])
        seconds1.append(row[9])
        thirds.append(row[10])
        thirds1.append(row[11])

    result = []
    result.append(names)
    result.append(liked_counts)
    result.append(decent_counts)
    result.append(bad_counts)
    result.append(scores)
    result.append(counts)
    result.append(firsts)
    result.append(firsts1)
    result.append(seconds)
    result.append(seconds1)
    result.append(thirds)
    result.append(thirds1)
    return result


def top_movie_from_year():
    sqlText = text("""
     WITH LikedMoviesCount AS (
    SELECT m.year, COALESCE(COUNT(*), 0) as liked_movies_count
    FROM movie m
    WHERE m.unwatched <> 1 AND m.liked = 1
    GROUP BY m.year
),
DecentMoviesCount AS (
    SELECT m.year, COALESCE(COUNT(*), 0) as decent_movies_count
    FROM movie m
    WHERE m.unwatched <> 1 AND m.liked = 2
    GROUP BY m.year
),
BadMoviesCount AS (
    SELECT m.year, COALESCE(COUNT(*), 0) as bad_movies_count
    FROM movie m
    WHERE m.unwatched <> 1 AND m.liked = 3
    GROUP BY m.year
),
    TopMovies AS (
        SELECT year, id, title, rewatchScore,
               ROW_NUMBER() OVER (PARTITION BY year ORDER BY rewatchScore DESC) as rn
        FROM movie
        WHERE unwatched <> 1
    ),
    DirectorMovieCount AS (
        SELECT year, COUNT(*) as total_movies
        FROM movie
        WHERE unwatched <> 1
        GROUP BY year
    )
    SELECT 
        tm.year, 
        ROUND(AVG(tm.rewatchScore)) as average_rewatchScore, 
        dmc.total_movies as movie_count,
        lmc.liked_movies_count as liked_movie_count,
        dmc2.decent_movies_count as decent_movie_count,
        bmc.bad_movies_count as bad_movie_count,
        MAX(CASE WHEN tm.rn = 1 THEN tm.id END) as top_movie_id_1, 
        MAX(CASE WHEN tm.rn = 1 THEN tm.title END) as top_movie_poster_1,
        MAX(CASE WHEN tm.rn = 2 THEN tm.id END) as top_movie_id_2, 
        MAX(CASE WHEN tm.rn = 2 THEN tm.title END) as top_movie_poster_2,
        MAX(CASE WHEN tm.rn = 3 THEN tm.id END) as top_movie_id_3, 
        MAX(CASE WHEN tm.rn = 3 THEN tm.title END) as top_movie_poster_3
    FROM TopMovies tm
    JOIN DirectorMovieCount dmc ON tm.year = dmc.year
    LEFT JOIN LikedMoviesCount lmc ON tm.year = lmc.year
    LEFT JOIN DecentMoviesCount dmc2 ON tm.year = dmc2.year
    LEFT JOIN BadMoviesCount bmc ON tm.year = bmc.year
    WHERE tm.rn <= 3
    GROUP BY tm.year, dmc.total_movies, lmc.liked_movies_count, dmc2.decent_movies_count, bmc.bad_movies_count
    HAVING movie_count > 2
    ORDER BY (lmc.liked_movies_count / dmc.total_movies) DESC, lmc.liked_movies_count DESC, dmc2.decent_movies_count DESC, bmc.bad_movies_count ASC, average_rewatchScore DESC;    
    """)

    movies = db.engine.execute(sqlText)
    years = []
    scores = []
    watchedCounts = []
    likedCounts = []
    decentCounts = []
    badCounts = []
    firstIds = []
    firstPosters = []
    secondIds = []
    secondPosters = []
    thirdIds = []
    thirdPosters = []
    for row in movies:
        years.append(row[0])
        scores.append(row[1])
        watchedCounts.append(row[2])
        likedCounts.append(row[3])
        decentCounts.append(row[4])
        badCounts.append(row[5])
        firstIds.append(row[6])
        firstPosters.append(row[7])
        secondIds.append(row[8])
        secondPosters.append(row[9])
        thirdIds.append(row[10])
        thirdPosters.append(row[11])

    result = []
    result.append(years)
    result.append(scores)
    result.append(watchedCounts)
    result.append(likedCounts)
    result.append(decentCounts)
    result.append(badCounts)
    result.append(firstIds)
    result.append(firstPosters)
    result.append(secondIds)
    result.append(secondPosters)
    result.append(thirdIds)
    result.append(thirdPosters)
    return result

def updatePoster(id, poster):
    movie = getMovie(id)
    movie.poster = poster
    db.session.commit()

def getMovie(id):
    movie = Movie.query.filter(Movie.id == id).first()
    return movie

def top_movie_from_year_ordered():
    sqlText = text("""
     WITH LikedMoviesCount AS (
    SELECT m.year, COALESCE(COUNT(*), 0) as liked_movies_count
    FROM movie m
    WHERE m.unwatched <> 1 AND m.liked = 1
    GROUP BY m.year
),
DecentMoviesCount AS (
    SELECT m.year, COALESCE(COUNT(*), 0) as decent_movies_count
    FROM movie m
    WHERE m.unwatched <> 1 AND m.liked = 2
    GROUP BY m.year
),
BadMoviesCount AS (
    SELECT m.year, COALESCE(COUNT(*), 0) as bad_movies_count
    FROM movie m
    WHERE m.unwatched <> 1 AND m.liked = 3
    GROUP BY m.year
),
    TopMovies AS (
        SELECT year, id, title, rewatchScore,
               ROW_NUMBER() OVER (PARTITION BY year ORDER BY rewatchScore DESC) as rn
        FROM movie
        WHERE unwatched <> 1
    ),
    DirectorMovieCount AS (
        SELECT year, COUNT(*) as total_movies
        FROM movie
        WHERE unwatched <> 1
        GROUP BY year
    )
    SELECT 
        tm.year, 
        ROUND(AVG(tm.rewatchScore)) as average_rewatchScore, 
        dmc.total_movies as movie_count,
        lmc.liked_movies_count as liked_movie_count,
        dmc2.decent_movies_count as decent_movie_count,
        bmc.bad_movies_count as bad_movie_count,
        MAX(CASE WHEN tm.rn = 1 THEN tm.id END) as top_movie_id_1, 
        MAX(CASE WHEN tm.rn = 1 THEN tm.title END) as top_movie_poster_1,
        MAX(CASE WHEN tm.rn = 2 THEN tm.id END) as top_movie_id_2, 
        MAX(CASE WHEN tm.rn = 2 THEN tm.title END) as top_movie_poster_2,
        MAX(CASE WHEN tm.rn = 3 THEN tm.id END) as top_movie_id_3, 
        MAX(CASE WHEN tm.rn = 3 THEN tm.title END) as top_movie_poster_3
    FROM TopMovies tm
    JOIN DirectorMovieCount dmc ON tm.year = dmc.year
    LEFT JOIN LikedMoviesCount lmc ON tm.year = lmc.year
    LEFT JOIN DecentMoviesCount dmc2 ON tm.year = dmc2.year
    LEFT JOIN BadMoviesCount bmc ON tm.year = bmc.year
    WHERE tm.rn <= 3
    GROUP BY tm.year, dmc.total_movies, lmc.liked_movies_count, dmc2.decent_movies_count, bmc.bad_movies_count
    HAVING movie_count > 2
    ORDER BY tm.year desc;    
    """)

    movies = db.engine.execute(sqlText)
    years = []
    scores = []
    watchedCounts = []
    likedCounts = []
    decentCounts = []
    badCounts = []
    firstIds = []
    firstPosters = []
    secondIds = []
    secondPosters = []
    thirdIds = []
    thirdPosters = []
    for row in movies:
        years.append(row[0])
        scores.append(row[1])
        watchedCounts.append(row[2])
        likedCounts.append(row[3])
        decentCounts.append(row[4])
        badCounts.append(row[5])
        firstIds.append(row[6])
        firstPosters.append(row[7])
        secondIds.append(row[8])
        secondPosters.append(row[9])
        thirdIds.append(row[10])
        thirdPosters.append(row[11])

    result = []
    result.append(years)
    result.append(scores)
    result.append(watchedCounts)
    result.append(likedCounts)
    result.append(decentCounts)
    result.append(badCounts)
    result.append(firstIds)
    result.append(firstPosters)
    result.append(secondIds)
    result.append(secondPosters)
    result.append(thirdIds)
    result.append(thirdPosters)
    return result



def find_best_movies_by_win_percentage():
    movies = Movie.query.filter(
                                and_(
                                        Movie.unwatched != 1
                                    )
                                ).order_by(text("rankingPercentage desc, rankingWinCount desc,  rewatchCount asc")).all()    
    return set_ranks(movies)

def getOverallRanks(movies):
    AllMovies = Movie.query.filter(Movie.unwatched != 1).order_by(desc(Movie.rewatchScore)).all()

    ranked = set_ranks(AllMovies)

    for x in movies:
        for y in ranked:
            if y.id == x.id:
                x.rank = y.rank
    db.session.commit()

    return movies


def set_ranks(movies):
    for i in range(0, len(movies)):
        movies[i].rank = i + 1
    db.session.commit()
    return movies

def set_count(genres):
    for genre in genres:
        movies = MovieGenre.query.filter(MovieGenre.genreId == genre.id).count()
        genre.count = movies
    return genres

def find_best_movies():
    movies = Movie.query.filter(and_(Movie.unwatched != 1, text("stars is not NULL and stars <> 'None' and stars <> '' "))).order_by(text("(CASE  WHEN stars = '' THEN NULL WHEN stars= 'None' THEN NULL ELSE stars END) desc, rewatchScore desc")).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies) 

def get_genre_count(genre):
    movies = MovieGenre.query.filter(MovieGenre.genreId == genre.id).count()
    genre.count = movies
    return genre

def get_list_count(list):
    movies = ListMovie.query.filter(ListMovie.listId == list.id).count()
    list.count = movies
    return list

def find_top_unwatched_movies(num):
    if num == 0:
        num = Movie.query.count()
    movies = Movie.query.order_by(desc(Movie.rewatchScore)).limit(num).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_top_watched_movies(num):
    if num == 0:
        num = Movie.query.count()
    movies = Movie.query.filter(Movie.unwatched != 1).order_by(desc(Movie.rewatchScore)).limit(num).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_top_movies(num):
    if num == 0:
        num = Movie.query.count()
    movies = Movie.query.filter(Movie.unwatched != 1).order_by(desc(Movie.rewatchScore)).limit(num).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_movies_all():
    movies = Movie.query.filter(Movie.unwatched != 1).order_by(desc(Movie.rewatchScore)).all()
    return set_ranks(movies)

def find_all_movies():
    movies = Movie.query.order_by(asc(Movie.title)).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_all_watched_movies():
    movies = Movie.query.filter(Movie.unwatched != 1).order_by(asc(Movie.title)).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_all_unwatched_movies():
    movies = Movie.query.filter(Movie.unwatched == 1).order_by(asc(Movie.title)).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_all_movies_without(movies):
    allMovies = find_all_movies()

    for x in movies:
        for y in allMovies:
            if x.id ==y.id:
                allMovies.remove(y)

    return allMovies


def find_filtered_movies(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                        Movie.unwatched != 1, 
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max)
                                    )
                                ).order_by(desc(Movie.rewatchScore)).all()
    
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
                x.genres = getMovieGenreNamesWithCheck(x.id, genres)
                if len(x.genres) > 0:
                    result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)

    return set_ranks(result)

def rankingAlgorithm(moviesSortedByPoints):
    sortedMovies = []

    if len(moviesSortedByPoints) < 2:
        return moviesSortedByPoints

    firstMovie = moviesSortedByPoints[0]
    secondMovie = moviesSortedByPoints[1]
    while len(moviesSortedByPoints) > 2:
        rankings = Ranking.query.filter(or_(and_(Ranking.loserMovieId == firstMovie.id, Ranking.winnerMovieId == secondMovie.id), and_(Ranking.loserMovieId == secondMovie.id, Ranking.winnerMovieId == firstMovie.id))).order_by(desc(Ranking.id)).all()
        if len(rankings)  > 0:
            # the two have been ranked against each other
            mostRecent = rankings[0]
            if mostRecent.winnerMovieId == firstMovie.id:
                # the higher ranked won
                firstMovie.beatBelow = True
                sortedMovies.append(firstMovie)
                moviesSortedByPoints.remove(moviesSortedByPoints[0])
                firstMovie = moviesSortedByPoints[0]
                secondMovie = moviesSortedByPoints[1]
            else:
                # the lower ranked won
                secondMovie.beatBelow = True
                sortedMovies.append(secondMovie)
                moviesSortedByPoints.remove(moviesSortedByPoints[1])
                firstMovie = moviesSortedByPoints[0]
                secondMovie = moviesSortedByPoints[1]
        else:
            # they have not been ranked, instead we take the first
            firstMovie.beatBelow = False
            sortedMovies.append(firstMovie)
            moviesSortedByPoints.remove(moviesSortedByPoints[0])
            firstMovie = moviesSortedByPoints[0]
            secondMovie = moviesSortedByPoints[1]
    
    while len(moviesSortedByPoints) != 0:
        moviesSortedByPoints[0].beatBelow = False
        sortedMovies.append(moviesSortedByPoints[0])
        moviesSortedByPoints.remove(moviesSortedByPoints[0])

        
    return sortedMovies

def find_filtered_movies_forRanking(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                        Movie.unwatched != 1, 
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max)
                                    )
                                ).order_by(desc(Movie.rewatchScore)).all()
    
    result = [] 
    counter = 0
    moviesSortedByPoints = []
    for x in movies:
        if len(genreInput) > 1:
                x.genres = getMovieGenreNamesWithCheck(x.id, genres)
                if len(x.genres) > 0:
                    result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)
        x.rank = counter + 1
        counter = counter + 1
        moviesSortedByPoints.append(x)
    
    return rankingAlgorithm(moviesSortedByPoints)

def unloggedMovies():
    sqlText = text("SELECT * \
FROM movie m \
WHERE m.id NOT IN (SELECT movieId from movie_watch) \
and m.unwatched <> 1") 
    
    movies = db.engine.execute(sqlText)
    names = []
    for row in movies:
        names.append(row[0])

    result = findMoviesByIdList(names)

    return result
    

def find_filtered_movies_first_logged(location, people, notes, start, end, title):
    logs = []
    movies = []
    # start and end date
    if start is not None and start != '' and start != "" and end is not None and end != '' and end != "":
        start = str(start)
        start = datetime.strptime(start, '%Y-%m-%d')
        start = start - timedelta(days=1)
        end = str(end)
        end = datetime.strptime(end, '%Y-%m-%d')

        logs = MovieWatch.query.filter(and_(
                                        or_(location == "", location is None, MovieWatch.location.ilike('%' + location + '%')), 
                                        or_(people == "", people is None, MovieWatch.people.ilike('%' + people + '%')), 
                                        or_(notes == "", notes is None, MovieWatch.notes.ilike('%' + notes + '%')), 
                                        and_(MovieWatch.watchDate >= start, MovieWatch.watchDate <= end, MovieWatch.firstWatch == 1)
                                        )).order_by(text("watchDate desc, id desc")).all()
        
     # start date
    elif start is not None and start != '' and start != "":
        start = str(start)
        start = datetime.strptime(start, '%Y-%m-%d')
        start = start - timedelta(days=1)
        logs = MovieWatch.query.filter(and_(
                                        or_(location == "", location is None, MovieWatch.location.ilike('%' + location + '%')), 
                                        or_(people == "", people is None, MovieWatch.people.ilike('%' + people + '%')), 
                                        or_(notes == "", notes is None, MovieWatch.notes.ilike('%' + notes + '%')), 
                                        or_(MovieWatch.watchDate >= start)
                                        , MovieWatch.firstWatch == 1
                                        )).order_by(text("watchDate desc, id desc")).all()
    # end date
    elif end is not None and end != '' and end != "":
        end = str(end)
        end = datetime.strptime(end, '%Y-%m-%d')
        logs = MovieWatch.query.filter(and_(MovieWatch.watchDate <= end, MovieWatch.firstWatch == 1)).order_by(text("watchDate desc, id desc")).all()

    else:
        logs = MovieWatch.query.filter(and_(
                                        or_(location == "", location is None, MovieWatch.location.ilike('%' + location + '%')), 
                                        or_(people == "", people is None, MovieWatch.people.ilike('%' + people + '%')), 
                                        or_(notes == "", notes is None, MovieWatch.notes.ilike('%' + notes + '%'))
                                        , MovieWatch.firstWatch == 1
                                        )).order_by(text("watchDate desc, id desc")).all()

    for x in logs:
            movie = Movie.query.filter(Movie.id == x.movieId).all()[0]
            x.movieTitle = movie.title
            x.movieLiked = movie.liked
            x.movieRecommendation = movie.recommend
            x.movieStars = movie.stars
            x.movieOverallNotes = movie.notes
            movies.append(movie)

    results = []
    if len(title) > 0:
        for x in logs:
            if title.upper() in x.movieTitle.upper():
                results.append(x) 
        return results 
        
    return logs

def find_filtered_movies_logged(location, people, notes, start, end, title):
    logs = []
    movies = []
    # start and end date
    if start is not None and start != '' and start != "" and end is not None and end != '' and end != "":
        start = str(start)
        start = datetime.strptime(start, '%Y-%m-%d')
        start = start - timedelta(days=1)
        end = str(end)
        end = datetime.strptime(end, '%Y-%m-%d')

        logs = MovieWatch.query.filter(and_(
                                        or_(location == "", location is None, MovieWatch.location.ilike('%' + location + '%')), 
                                        or_(people == "", people is None, MovieWatch.people.ilike('%' + people + '%')), 
                                        or_(notes == "", notes is None, MovieWatch.notes.ilike('%' + notes + '%')), 
                                        and_(MovieWatch.watchDate >= start, MovieWatch.watchDate <= end)
                                        )).order_by(text("watchDate desc, id desc")).all()
        
     # start date
    elif start is not None and start != '' and start != "":
        start = str(start)
        start = datetime.strptime(start, '%Y-%m-%d')
        start = start - timedelta(days=1)
        logs = MovieWatch.query.filter(and_(
                                        or_(location == "", location is None, MovieWatch.location.ilike('%' + location + '%')), 
                                        or_(people == "", people is None, MovieWatch.people.ilike('%' + people + '%')), 
                                        or_(notes == "", notes is None, MovieWatch.notes.ilike('%' + notes + '%')), 
                                        or_(MovieWatch.watchDate >= start)
                                        )).order_by(text("watchDate desc, id desc")).all()
    # end date
    elif end is not None and end != '' and end != "":
        end = str(end)
        end = datetime.strptime(end, '%Y-%m-%d')
        logs = MovieWatch.query.filter(MovieWatch.watchDate <= end).order_by(text("watchDate desc, id desc")).all()

    else:
        logs = MovieWatch.query.filter(and_(
                                        or_(location == "", location is None, MovieWatch.location.ilike('%' + location + '%')), 
                                        or_(people == "", people is None, MovieWatch.people.ilike('%' + people + '%')), 
                                        or_(notes == "", notes is None, MovieWatch.notes.ilike('%' + notes + '%'))
                                        )).order_by(text("watchDate desc, id desc")).all()

    for x in logs:
            movie = Movie.query.filter(Movie.id == x.movieId).all()[0]
            x.movieTitle = movie.title
            x.movieLiked = movie.liked
            x.movieRecommendation = movie.recommend
            x.movieStars = movie.stars
            x.movieOverallNotes = movie.notes
            movies.append(movie)

    results = []
    if len(title) > 0:
        for x in logs:
            if title.upper() in x.movieTitle.upper():
                results.append(x) 
        return results 
        
    return logs


def uncofnrimtedLogs():
    logs = []

    logs = MovieWatch.query.filter(and_(
                                        MovieWatch.confirmedStars != 1
                                        )).order_by(text("watchDate desc, id desc")).all()

    for x in logs:
            movie = Movie.query.filter(Movie.id == x.movieId).all()[0]
            x.movieTitle = movie.title
            x.movieLiked = movie.liked
            x.movieRecommendation = movie.recommend
            x.movieStars = movie.stars
            x.movieOverallNotes = movie.notes     
            x.movieYear = movie.year 
            x.movieRank = movie.rank
            x.movieRecommendStars = getRankingForStars(x.movieId)[4]
             
    return logs

def find_filtered_unwatched_movies(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                        Movie.unwatched == 1, 
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max)
                                    )
                                ).order_by(desc(Movie.runtime)).all()
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)
    return set_ranks(result)

def find_filtered_rewatched_movies(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                        Movie.rewatch == 1, 
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max)
                                    )
                                ).order_by(desc(Movie.runtime)).all()
    
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)
    return set_ranks(result)


def find_filtered_currently_movies(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                        Movie.currentlyWatching == 1, 
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max)
                                    )
                                ).order_by(desc(Movie.runtime)).all()
    
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)
    return set_ranks(result)

def find_all_watched_filtered_movies(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max),
                                     Movie.unwatched != 1
                                    )
                                ).order_by(desc(Movie.rewatchScore)).all()
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)

    return set_ranks(result)

def find_all_filtered_movies(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max)
                                    )
                                ).order_by(desc(Movie.rewatchScore)).all()
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)

    return set_ranks(result)

def find_all_unwatched_filtered_movies(title, director, year, min, max, recommendation, genreInput):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max),
                                     Movie.unwatched == 1
                                    )
                                ).order_by(desc(Movie.rewatchScore)).all()
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)

    return set_ranks(result)


def find_all_movies_to_watch(title, director, year, min, max, recommendation, watchedBefore, genreInput, listView):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()


    result = []

    random_number = random.randint(1, 10)

    if (not listView) and watchedBefore and random_number < 8:
        movies = Movie.query.filter(
                                and_(
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max),
                                     or_(and_(watchedBefore == 0, Movie.unwatched != 0 ),  and_(watchedBefore == 1, Movie.unwatched == 0 )),
                                     text('movie.id not IN (SELECT movieId FROM movie_watch WHERE julianday(\'now\') - julianday(movie_watch.watchDate) <  150)')
                                    )
                                ).order_by(func.random()).all()
    elif (not listView) and watchedBefore:
        movies = Movie.query.filter(
                                    and_(
                                        or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                        or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                        or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                        or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                        or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                        or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max),
                                        or_(and_(watchedBefore == 0, Movie.unwatched != 0 ),  and_(watchedBefore == 1, Movie.unwatched == 0 )),
                                        text('movie.id not IN (SELECT movieId FROM movie_watch WHERE julianday(\'now\') - julianday(movie_watch.watchDate) <  60)')
                                        )
                                    ).order_by(func.random()).all()

    else:
        movies = Movie.query.filter(
                                    and_(
                                        or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                        or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                        or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                        or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                        or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                        or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max),
                                        or_(and_(watchedBefore == 0, Movie.unwatched != 0 ),  and_(watchedBefore == 1, Movie.unwatched == 0 ))
                                        )
                                    ).order_by(func.random()).all()
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)

    return result



def findHourCountAll():
    sql = text('SELECT (SELECT SUM(runtime)  FROM movie \
WHERE unwatched = 0 and id not in (SELECT movieId FROM movie_watch)) as countOfUnlogged, \
SUM(movie.runtime) as loggedCount \
FROM movie_watch \
JOIN movie on movie_watch.movieId = movie.id')
    rankings = db.engine.execute(sql)
    hours = []
    hours2 = []
    for row in rankings:
        hours.append(row[0])
        hours2.append(row[1])
    
    return hours[0] + hours2[0]

def findHourCountThisYear(days):
    # Calculate the date n days ago
    theDate = date.today() - timedelta(days=days)

    # Update the SQL query to include the condition for watchDate
    sql = text('''
        SELECT SUM(movie.runtime) as loggedCount
        FROM movie_watch
        JOIN movie ON movie_watch.movieId = movie.id
        WHERE movie_watch.watchDate >= :date
    ''')

    # Execute the query with theDate as a parameter
    rankings = db.engine.execute(sql, date=theDate)

    # Initialize hours
    hours = []

    # Iterate through the results and append to hours
    for row in rankings:
        hours.append(row[0])

    # Return the total hours or 0 if the list is empty
    return hours[0] if hours else 0



def find_all_filtered_movies_without(title, director, year, min, max, recommendation, movies, genres):
    allMovies = find_all_filtered_movies(title, director, year, min, max, recommendation, genres)

    for x in movies:
        for y in allMovies:
            if x.id ==y.id:
                allMovies.remove(y)

    return allMovies


def find_filtered_movies_by_stars(title, director, year, min, max, recommendation, genreInput, stars):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                        Movie.unwatched != 1, 
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max),
                                    or_(stars == 0, stars is None, stars == "", str(stars) == "0", Movie.stars == stars),
                                     text("stars is not NULL and stars <> 'None' and stars <> '' ")
                                    )
                                ).order_by(text("(CASE  WHEN stars = '' THEN NULL WHEN stars= 'None' THEN NULL ELSE stars END) desc, rewatchScore desc")).all()
    result = [] 
    for x in movies:
        if len(genreInput) > 1:
            x.genres = getMovieGenreNamesWithCheck(x.id, genres)
            if len(x.genres) > 0:
                result.append(x)
        else:
            x.genres = getMovieGenreNames(x.id)
            result.append(x)
    return set_ranks(result)

def find_filtered_movies_by_win_percentage(title, director, year, min, max, recommendation, genreInput, stars):
    genres = []
    if len(genreInput) > 0:
        genres = Genre.query.filter(text(' \' ' + genreInput + '\' LIKE \'%\' || genre.name ||\'%\'')).all()
    movies = Movie.query.filter(
                                and_(
                                        Movie.unwatched != 1, 
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max),
                                    or_(stars == 0, stars is None, stars == "", str(stars) == "0", Movie.stars == stars)
                                    )
                                ).order_by(text("rankingPercentage desc, rankingWinCount desc")).all()    
    return set_ranks(movies)


def find_recently_watched():
    logs = MovieWatch.query.order_by(desc(MovieWatch.watchDate)).all()
    movies = []
    for x in logs:
        movie = Movie.query.filter(Movie.id == x.movieId).all()
        if len(movie) > 0:
            m = movie[0]
        m.lastWatchedDate = x.watchDate
        m.genres = getMovieGenreNames(m.id)
        movies.append(m)
        
    return movies


def filterRecentWatched(start, end):
    if start is not None and start != '' and start != "" and len(start) > 4 and end is not None and end != '' and end != "" and len(end) > 4 :
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        start = start - timedelta(days=1)
        logs = MovieWatch.query.filter(and_(MovieWatch.watchDate >= start, MovieWatch.watchDate <= end)).order_by(desc(MovieWatch.watchDate)).all()
        movies = []
        for x in logs:
            movie = Movie.query.filter(Movie.id == x.movieId).all()
            movie[0].lastWatchedDate = x.watchDate
            movies.append(movie[0])
    elif start is not None and start != '' and start != "" and len(start) > 4:
        start = datetime.strptime(start, '%Y-%m-%d')
        logs = MovieWatch.query.filter(MovieWatch.watchDate >= start).order_by(desc(MovieWatch.watchDate)).all()
        movies = []
        for x in logs:
            movie = Movie.query.filter(Movie.id == x.movieId).all()
            movie[0].lastWatchedDate = x.watchDate
            movies.append(movie[0])
    elif end is not None and end != '' and end != "" and len(end) > 4:
        end = datetime.strptime(end, '%Y-%m-%d')
        logs = MovieWatch.query.filter(MovieWatch.watchDate <= end).order_by(desc(MovieWatch.watchDate)).all()
        movies = []
        for x in logs:
            movie = Movie.query.filter(Movie.id == x.movieId).all()
            movie[0].lastWatchedDate = x.watchDate
            movies.append(movie[0])
    else:
        logs = MovieWatch.query.order_by(desc(MovieWatch.watchDate)).all()
        movies = []
        for x in logs:
            movie = Movie.query.filter(Movie.id == x.movieId).all()
            movie[0].lastWatchedDate = x.watchDate
            movies.append(movie[0])
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return movies

def getRandomMovie():
    movies = Movie.query.filter(and_(Movie.unwatched != 1, Movie.rewatch != 1)).order_by(func.random()).all()
    # size = Movie.query.count()
    # while(True):
    #     index = random.randint(1, size)
    #     movie = Movie.query.filter(Movie.id == index).all()
    #     if len(movie) > 0:
    #         if movie[0].unwatched != 1 and movie[0].rewatch != 1:
    #             break
    # return movie[0]
    return movies[0]

def getRandomRankdeMovie(movieId):
    rankings = Ranking.query.filter(and_(or_(Ranking.winnerMovieId == movieId, Ranking.loserMovieId == movieId),  text("overwriteRankingId is null"))).all()
    size = len(rankings)
    while True:
        index = random.randint(0, size - 1)  # Corrected here
        ranking = rankings[index]
        newMovieId = ranking.loserMovieId if ranking.winnerMovieId == movieId else ranking.winnerMovieId
        movie = Movie.query.filter(Movie.id == newMovieId).all()
        if movie and movie[0].unwatched != 1:
            break
    return movie[0]


def getRankOfRecentMovies(inputSize):
    logs = MovieWatch.query.order_by(text("watchDate desc, id desc")).limit(inputSize).all()
    return logs

def getRecommendedMovies(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]
    moviesFromDirector = Movie.query.filter(and_(Movie.director == movie.director, Movie.id != movieId)).all()


    similarRankingMovies = []
    
    movie4 = Movie.query.filter(and_(Movie.id == movie.id,text("stars is not NULL and stars <> 'None' and stars <> '' "))).all()
    hasStars = len(movie4) > 0

    if hasStars: 
        similarRankingMovies = Movie.query.filter(
                                                and_(Movie.id != movieId, Movie.director != movie.director, Movie.unwatched != 1,
                                                     Movie.liked == movie.liked, text("stars is not NULL and stars <> 'None' and stars <> '' "), or_(and_(Movie.stars >= movie.stars, Movie.stars - movie.stars <= 1.5), and_(Movie.stars <= movie.stars, movie.stars - Movie.stars <= 1.5) ) )
                                                ).order_by(text("ABS(movie.rewatchScore - " + str(movie.rewatchScore) + ") asc, movie.rank asc")).all()
    else:
        similarRankingMovies = Movie.query.filter(and_(text("liked = 1 or liked = 2 or liked = 3"), Movie.liked == movie.liked)).order_by(text("ABS(movie.rewatchScore - " + str(movie.rewatchScore) + ") asc")).all()
    
    unwatchedMovies = Movie.query.filter(and_(Movie.unwatched == 1, Movie.director != movie.director)
                               ).all()
    

    # get movies with the same name (Harry Potter)
    sortedWords = []
    regex = re.compile('[^a-zA-Z ]')
    title = regex.sub("", movie.title)
    words = title.split(" ")
    for word in words:
        if not( word.lower() == "of" or word == "Is" or word == "is" or word == "X" or word == "F" or word == "with" or word=="Movie" or word=="La" or word=="Book" or word == "My"  or word =="From" or word =="from"  or  word == "to" or word == "II" or word == "III" or word == "On" or word == "on" or word == "Her" or word == "One" or word == "New" or word == "new" or word == "her" or word == "king" or word == "of" or word.lower() == "and" or word == "The" or  word.lower() == "the" or  word.lower() == "in" or  word.lower() == "for" or  word.lower() == "a" or  word.lower() == "an" ):
            sortedWords.append(word)  

    movieIdString = "("
    notFirst = False
    for x in sortedWords:
        if len(x.strip()) > 0:
            if notFirst:
                movieIdString = movieIdString + " or "
            else:
                notFirst = True
            movieIdString =  movieIdString + "(title LIKE '% " + x + ":%' or title LIKE '% " + x + "%' or title LIKE '%" + x + " %' or title LIKE '%" + x + ":%')" 
    movieIdString = movieIdString +  ")"


    similarNames = []
    if movieIdString != "()":
        similarNames = Movie.query.filter(and_(text(movieIdString),
                                                    Movie.id != movie.id, Movie.director != movie.director)
                                    ).order_by(asc(Movie.rewatchScore)).all()
    for movie in similarNames:
        movie.genres = getMovieGenreNames(movie.id)
    
    
    genres = MovieGenre.query.filter(MovieGenre.movieId == movie.id).all()

    result = []

    unwatched = []

    similar = []


    for movie in similarRankingMovies:
        movieGenres = MovieGenre.query.filter(movie.id == MovieGenre.movieId).all()
        found2 = False
        for genre in genres:
            for movieGenre in movieGenres:
                if genre.genreId == movieGenre.genreId:
                    movie.genres = getMovieGenreNames(movie.id)
                    similar.append(movie)
                    found2 = True
                    break
            if found2:
                break

    for x in moviesFromDirector:
        x.genres = getMovieGenreNames(x.id)

    for movie in unwatchedMovies:
        movieGenres = MovieGenre.query.filter(movie.id == MovieGenre.movieId).all()
        if len(movieGenres) == 2 and len(genres) == 2:
            if (movieGenres[0].genreId == genres[0].genreId and movieGenres[1].genreId == genres[1].genreId) or (movieGenres[1].genreId == genres[0].genreId and movieGenres[0].genreId == genres[1].genreId):
                movie.genres = getMovieGenreNames(movie.id)
                unwatched.append(movie)
        elif len(movieGenres) == 1 and len(genres) == 2:
            if (movieGenres[0].genreId == genres[0].genreId or movieGenres[0].genreId == genres[1].genreId):
                movie.genres = getMovieGenreNames(movie.id)
                unwatched.append(movie)
        elif len(movieGenres) == 2 and len(genres) == 1:
            if (movieGenres[0].genreId == genres[0].genreId or movieGenres[1].genreId == genres[0].genreId):
                movie.genres = getMovieGenreNames(movie.id)
                unwatched.append(movie)
        elif len(movieGenres) == 1 and len(genres) == 1:
            if (movieGenres[0].genreId == genres[0].genreId):
                movie.genres = getMovieGenreNames(movie.id)
                unwatched.append(movie)
    
    results = []
    results.append(result)
    results.append(unwatched)
    results.append(moviesFromDirector)
    results.append(similar)
    results.append(similarNames)

    return results


def getBestOfEachYear():
    sql = text("SELECT m1.id \
                FROM movie m1\
                WHERE rewatchScore = (SELECT MAX(rewatchScore) FROM movie m2 where m1.year = m2.year and m2.unwatched <> 1 and m1.unwatched <> 1) \
                ORDER by year desc")
    
    movies = db.engine.execute(sql)
    names = []
    for row in movies:
        names.append(row[0])

    result = findMoviesByIdList(names)

    return result


def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

def autoRank(movieId):
    autoRankLikes(movieId)
    autoRankLikes1(movieId)
    autoRankStars1(movieId)
    autoRankStars2(movieId)

def autoRankLikedCertain (movieId):
    ##### ALL liked movies beat all of the mid movies #######
     # Check if the given movie has a liked value of 1
    given_movie = Movie.query.filter(Movie.id == movieId).first()
    if not given_movie or given_movie.liked != 1:
        return 

    # Find all movies with a liked value of 2
    unliked_movies = Movie.query.filter(Movie.liked == 2).all()

    for movie in unliked_movies:
        # Skip if it's the same movie
        if movie.id == movieId:
            continue

        # Check if these two movies have been ranked against each other
        existing_ranking = Ranking.query.filter(
            (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == movie.id)  |
            (Ranking.winnerMovieId == movie.id) & (Ranking.loserMovieId == movieId) 
        ).first()

        # If not ranked, update rankings
        if not existing_ranking:
            updateRankings(movieId, movie.id, True)

def autoRankMidCertain (movieId):
    ##### ALL mid movies beat all of the disliked movies #######
     # Check if the given movie has a liked value of 2
    given_movie = Movie.query.filter(Movie.id == movieId).first()
    if not given_movie or given_movie.liked != 2:
        return 

    # Find all movies with a liked value of 3
    unliked_movies = Movie.query.filter(Movie.liked == 3).all()

    for movie in unliked_movies:
        # Skip if it's the same movie
        if movie.id == movieId:
            continue

        # Check if these two movies have been ranked against each other
        existing_ranking = Ranking.query.filter(
            (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == movie.id) |
            (Ranking.winnerMovieId == movie.id) & (Ranking.loserMovieId == movieId)
        ).first()

        # If not ranked, update rankings
        if not existing_ranking:
            updateRankings(movieId, movie.id, True)

def autoRankDisLikedCertain(movieId):
     ##### ALL disliked movies lose to all of the mid movies #######
    # Check if the given movie has a liked value of 3
    given_movie = Movie.query.filter(Movie.id == movieId).first()
    if not given_movie or given_movie.liked != 3:
        return 

    # Find all movies with a liked value of 2
    unliked_movies = Movie.query.filter(Movie.liked == 2).all()

    for movie in unliked_movies:
        # Skip if it's the same movie
        if movie.id == movieId:
            continue

        # Check if these two movies have been ranked against each other
        existing_ranking = Ranking.query.filter(
            (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == movie.id)  |
            (Ranking.winnerMovieId == movie.id) & (Ranking.loserMovieId == movieId) 
        ).first()

        # If not ranked, update rankings
        if not existing_ranking:
            updateRankings(movie.id, movieId, True)


def autoRankCertain(movieId):
    autoRankLikedCertain(movieId)
    autoRankMidCertain(movieId)
    autoRankDisLikedCertain(movieId)


def autoRankLikes(movieId):
    # Check if the given movie has a liked value of 1
    given_movie = Movie.query.filter(Movie.id == movieId).first()
    if not given_movie or given_movie.liked != 1:
        return 

    # Find all movies with a liked value of 3
    unliked_movies = Movie.query.filter(Movie.liked == 3).all()

    for movie in unliked_movies:
        # Skip if it's the same movie
        if movie.id == movieId:
            continue

        # Check if these two movies have been ranked against each other
        existing_ranking = Ranking.query.filter(
            (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == movie.id) |
            (Ranking.winnerMovieId == movie.id) & (Ranking.loserMovieId == movieId) 
        ).first()

        # If not ranked, update rankings
        if not existing_ranking:
            updateRankings(movieId, movie.id, True)


def autoRankLikes1(movieId):
    # Check if the given movie has a liked value of 3
    given_movie = Movie.query.filter(Movie.id == movieId).first()
    if not given_movie or given_movie.liked != 3:
        return 

    # Find all movies with a liked value of 1
    unliked_movies = Movie.query.filter(Movie.liked == 1).all()

    for movie in unliked_movies:
        # Skip if it's the same movie
        if movie.id == movieId:
            continue

        # Check if these two movies have been ranked against each other
        existing_ranking = Ranking.query.filter(
            (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == movie.id)  |
            (Ranking.winnerMovieId == movie.id) & (Ranking.loserMovieId == movieId)
        ).first()

        # If not ranked, update rankings
        if not existing_ranking:
            updateRankings(movie.id, movieId, True)


def autoRankStars1(movieId):
    # Check if the given movie has a liked value of 1
    given_movie = Movie.query.filter(Movie.id == movieId).first()
    if not given_movie or given_movie.liked != 1:
        return 

    # Find all movies with a liked value of 2
    liked_movies = Movie.query.filter(Movie.liked == 2).all()

    for movie in liked_movies:
        if movie.id == movieId:
            continue

        # Check if these two movies have been ranked against each other
        existing_ranking = Ranking.query.filter(
            (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == movie.id)  |
            (Ranking.winnerMovieId == movie.id) & (Ranking.loserMovieId == movieId) 
        ).first()

        if not existing_ranking:
            # Ensure both movies have a stars value
            if given_movie.stars is None or given_movie.stars == 'None' or movie.stars is None or  movie.stars == 'None':
                continue

            if len(str(given_movie.stars)) < 1 or len(str(movie.stars)) < 1:
                continue

            # Check if the given movie's stars are greater by 2 or more
            if int(given_movie.stars) >= int(movie.stars) + 2:
                # Update rankings with the given movie as the winner
                updateRankings(movieId, movie.id, True)      

def autoRankStars2(movieId):
    # Check if the given movie has a liked value of 2
    given_movie = Movie.query.filter(Movie.id == movieId).first()
    if not given_movie or given_movie.liked != 2:
        return 

    # Find all movies with a liked value of 2
    liked_movies = Movie.query.filter(Movie.liked == 3).all()

    for movie in liked_movies:
        if movie.id == movieId:
            continue

        # Check if these two movies have been ranked against each other
        existing_ranking = Ranking.query.filter(
            (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == movie.id)  |
            (Ranking.winnerMovieId == movie.id) & (Ranking.loserMovieId == movieId) 
        ).first()

        if not existing_ranking:
            # Ensure both movies have a stars value
            if given_movie.stars is None or given_movie.stars == 'None' or movie.stars is None or  movie.stars == 'None':
                continue

            if len(str(given_movie.stars)) < 1 or len(str(movie.stars)) < 1:
                continue

            # Check if the given movie's stars are greater by 2 or more
            if int(given_movie.stars) >= int(movie.stars) + 2:
                # Update rankings with the given movie as the winner
                updateRankings(movieId, movie.id, True)      



def autoRankList(listId):
    movieIds = ListMovie.query.filter(ListMovie.listId == listId).all()

    for movieId in movieIds:
        autoRank(movieId.movieId)

def getUpsets(movieId):
    result = []
    upsetOthers = Ranking.query.filter(and_(text('overwriteRankingId is NULL'), Ranking.winnerMovieId == movieId, Ranking.likeUpset)).all()
    beenUpset = Ranking.query.filter(and_(text('overwriteRankingId is NULL'), Ranking.loserMovieId == movieId, Ranking.likeUpset)).all()
    result.append(upsetOthers)
    result.append(beenUpset)
    return result


def updateRankings(winnerId, loserId, autoGenerated):
    ##print("find movies")
    winner = Movie.query.filter(Movie.id == winnerId).all()[0]
    loser = Movie.query.filter(Movie.id == loserId).all()[0]
    ##print("found movies")

    ##print("getting probability")
    Pb =  Probability(winner.rewatchScore, loser.rewatchScore)
    Pa =  Probability(loser.rewatchScore, winner.rewatchScore)
    Ra = int(winner.rewatchScore + 50 * (1 - Pa))
    Rb = int(loser.rewatchScore + 50 * (0 - Pb))

    isUniqueRanking = True
    isReversedRanking = False
    ##print("finding all rankings")
    # allRankings = Ranking.query.order_by(desc(Ranking.modifiedDate)).all()

    # lastRanked = allRankings[0]
    lastRanked = Ranking.query.order_by(desc(Ranking.modifiedDate)).first()

    ##print("mkaing query")
    text1 = 'overwriteRankingId is NULL AND ((winnerMovieId = ' + str(winnerId) + ' and loserMovieId = ' + str(loserId) + ') OR (winnerMovieId = ' + str(loserId) + ' AND loserMovieId = ' + str(winnerId) + ' ) ' + ')'
    rankings = Ranking.query.filter(text(text1)).all()
    if len(rankings) > 0:
        isUniqueRanking = False
    ##print("starting loop")
    for r in rankings:
        if (r.winnerMovieId == winnerId and r.loserMovieId == loserId):
            r.confirmed = func.now()
        if (r.winnerMovieId == loserId and r.loserMovieId == winnerId):
            r.reversed = True
            isReversedRanking = True
        if ((r.winnerMovieId == winnerId and r.loserMovieId == loserId) or (r.winnerMovieId == loserId and r.loserMovieId == winnerId))and r.overwriteRankingId is None:
            r.overwriteRankingId = lastRanked.id + 1

    ##print("hpdating rankinugs")
    ranking = Ranking(winnerMovieId=winner.id, loserMovieId=loser.id, modifiedDate=func.now(), winnerStartingPoints=winner.rewatchScore, loserStartingPoints=loser.rewatchScore, 
                      winnerPointsGained=50 * (1 - Pa), loserPointsLossed=50 * (1 - Pb), winnerEndingPoints=Ra, losserEndingPoints=Rb, winnerCount=winner.rewatchCount, loserCount=loser.rewatchCount, generated=autoGenerated)
    
    # 3 options:
    # 1) unique ranking, increase the win count and rewatch Count for winner, only increase rewatch Count for loser
    # 2) reverse of past Ranking, increase the win count for winner, decrease win Count for loser
    # 3) confirming of past Ranking, change nothing
    ##print("checking is unique")
    if isUniqueRanking:
        winner.rankingWinCount = len(Ranking.query.filter(and_(Ranking.winnerMovieId == winner.id, text('overwriteRankingId is NULL'))).all()) + 1
        winner.rewatchCount = len(Ranking.query.filter(and_(or_(Ranking.winnerMovieId == winner.id, Ranking.loserMovieId == winner.id), text('overwriteRankingId IS NULL'))).all()) + 1
        if winner.rewatchCount > 0:
            winner.rankingPercentage =int(winner.rankingWinCount / winner.rewatchCount * 100)
        else:
            winner.rankingPercentage = 0
        
        loser.rewatchCount = len(Ranking.query.filter(and_(or_(Ranking.winnerMovieId == loser.id, Ranking.loserMovieId == loser.id), text('overwriteRankingId IS NULL'))).all()) + 1
        if loser.rewatchCount > 0:
            loser.rankingPercentage =int(loser.rankingWinCount / loser.rewatchCount * 100)
        else:
            loser.rankingPercentage = 0
    elif isReversedRanking:
        winner.rankingWinCount = len(Ranking.query.filter(and_(Ranking.winnerMovieId == winner.id, text('overwriteRankingId is NULL'))).all()) + 1
        winner.rewatchCount = len(Ranking.query.filter(and_(or_(Ranking.winnerMovieId == winner.id, Ranking.loserMovieId == winner.id), text('overwriteRankingId IS NULL'))).all())
        if winner.rewatchCount > 0:
            winner.rankingPercentage =int(winner.rankingWinCount / winner.rewatchCount * 100)
        else:
            winner.rankingPercentage = 0
        loser.rankingWinCount = len(Ranking.query.filter(and_(Ranking.winnerMovieId == loser.id, text('overwriteRankingId is NULL'))).all()) - 1
        loser.rewatchCount = len(Ranking.query.filter(and_(or_(Ranking.winnerMovieId == loser.id, Ranking.loserMovieId == loser.id), text('overwriteRankingId IS NULL'))).all())
        if loser.rewatchCount > 0:
            loser.rankingPercentage =int(loser.rankingWinCount / loser.rewatchCount * 100)
        else:
            loser.rankingPercentage = 0
    winner.rewatchScore = Ra
    loser.rewatchScore = Rb
    ##print("checking flag")
    ranking = checkFlag(winner, loser, ranking)
    ##print("flag checked")
    ranking = checkLikedUpset(winner, loser, ranking)
    ##print("checked upsets")
    db.session.add(ranking)
    db.session.commit()

def checkLikedUpset(winner, loser, ranking):
    if winner.liked is not None and loser.liked is not None:
        if (winner.liked == 3 and loser.liked == 2) or (winner.liked == 2 and loser.liked == 1):
            ranking.likeUpset = 1
    return ranking


def getClosestRankings():
    flaggedRankings = Ranking.query.filter(and_(text('overwriteRankingId IS NULL  and  rankingDifference is not NULL and winnerRank is not NULL and loserRank is not NULL'), Ranking.modifiedDate >= date.today())).order_by(text('abs(winnerRank - loserRank) asc, winnerRank asc')).limit(25).all()
    for flaggedRanking in flaggedRankings:
        winner = Movie.query.filter(and_(Movie.id == flaggedRanking.winnerMovieId)).all()
        flaggedRanking.winnerTitle = winner[0].title
        
        loserMovie = Movie.query.filter(Movie.id == flaggedRanking.loserMovieId).all()
        flaggedRanking.loserTitle = loserMovie[0].title
        
        flaggedRanking.rankingDifference = abs(flaggedRanking.rankingDifference)
        flaggedRanking.rankingDate = format_datetime(flaggedRanking.modifiedDate - timedelta(hours=5), locale='en')

    return flaggedRankings

def getBiggestUpsets():
    flaggedRankings = Ranking.query.filter(and_(text('overwriteRankingId IS NULL and rankingDifference is not NULL and winnerRank is not NULL and loserRank is not NULL and winnerRank > loserRank'), Ranking.modifiedDate >= date.today() )).order_by(text('winnerRank - loserRank desc')).limit(25).all()
    for flaggedRanking in flaggedRankings:
        winner = Movie.query.filter(and_(Movie.id == flaggedRanking.winnerMovieId)).all()
        flaggedRanking.winnerTitle = winner[0].title
        
        loserMovie = Movie.query.filter(Movie.id == flaggedRanking.loserMovieId).all()
        flaggedRanking.loserTitle = loserMovie[0].title
        
        flaggedRanking.rankingDate = format_datetime(flaggedRanking.modifiedDate - timedelta(hours=5), locale='en')


    return flaggedRankings

def findNumOfReversedMovies():
    flaggedRankings = Ranking.query.filter(Ranking.reversed == 1).all()


    return len(flaggedRankings)


def checkFlag(winner, loser, ranking):
    sql = text("WITH RankedMovies AS ( \
                SELECT id, \
                    ROW_NUMBER() OVER (ORDER BY rewatchScore DESC) AS rank \
                FROM movie \
                WHERE movie.unwatched <> 1 \
            ) \
            SELECT  a.rank as winnerRank, b.rank as loserRank, a.rank - b.rank AS rank_difference \
            FROM RankedMovies a, RankedMovies b \
            WHERE a.id = " + str(winner.id) + " AND b.id = " + str(loser.id))
    
    ranks = db.engine.execute(sql)

    difference = 0

    for row in ranks:
        winnerRankNum = row[0] #winnerRank
        loserRankNum = row[1]  #loserRank 
        difference = row[2] #difference 

    ranking.winnerRank = winnerRankNum
    ranking.loserRank = loserRankNum
    ranking.winnerYear = winner.year
    ranking.loserYear = loser.year
    ranking.rankingDifference = ranking.winnerRank - ranking.loserRank

    flagChecker = get_or_calculate_average_value()
    if flagChecker is None or int(flagChecker) < 100:
        flagChecker = 100
    if difference > flagChecker and (winner.rewatchCount > 3 and loser.rewatchCount > 3):
        ranking.flagged = True
        return ranking

    ranking.flagged = False
    return ranking

def currentWatchStreak():
    sql = text(""" WITH DateDiffs AS (
    SELECT
        watchDate,
        julianday(watchDate) - julianday(LAG(watchDate) OVER (ORDER BY watchDate DESC)) AS Diff
    FROM (
        SELECT DISTINCT watchDate
        FROM movie_watch
        WHERE watchDate IS NOT NULL AND watchDate <= CURRENT_DATE
        ORDER BY watchDate DESC
    )
),
Streaks AS (
    SELECT
        watchDate,
        CASE 
            WHEN Diff = -1 THEN 0
            ELSE 1
        END AS StreakBreak
    FROM DateDiffs
),
GroupedStreaks AS (
    SELECT
        watchDate,
        SUM(StreakBreak) OVER (ORDER BY watchDate DESC) AS StreakGroup
    FROM Streaks
),
StreakLengths AS (
    SELECT
        StreakGroup,
        COUNT(*) AS Length,
        MIN(watchDate) AS StartDate,
        MAX(watchDate) AS EndDate
    FROM GroupedStreaks
    GROUP BY StreakGroup
)
SELECT
    CASE 
        WHEN (SELECT watchDate FROM movie_watch ORDER BY watchDate DESC LIMIT 1) = CURRENT_DATE THEN Length
        WHEN (julianday(CURRENT_DATE) - julianday((SELECT watchDate FROM movie_watch ORDER BY watchDate DESC LIMIT 1))) = 1 THEN Length
        ELSE 0
    END AS CurrentStreak
FROM StreakLengths
WHERE EndDate = (SELECT MAX(watchDate) FROM movie_watch)
ORDER BY StartDate DESC
LIMIT 1;
 """)
    
    calculatedAverageValue = 0
    rankings = db.engine.execute(sql)
    for row in rankings:
        calculatedAverageValue = row[0]
    result =[]
    result.append(calculatedAverageValue)

    result.append(calculatedAverageValue)
    result.append(0)

    return result  # Or appropriate response if no streak is found

def longestWatchStreak():
    sql = text("""WITH DateDiffs AS (
    SELECT
        watchDate,
        julianday(watchDate) - julianday(LAG(watchDate) OVER (ORDER BY watchDate)) AS Diff
    FROM (
        SELECT DISTINCT watchDate
        FROM movie_watch
        WHERE watchDate IS NOT NULL
        ORDER BY watchDate
    )
),
Streaks AS (
    SELECT
        watchDate,
        CASE WHEN Diff = 1 THEN 0 ELSE 1 END AS NewStreakStart
    FROM DateDiffs
),
GroupedStreaks AS (
    SELECT
        watchDate,
        SUM(NewStreakStart) OVER (ORDER BY watchDate) AS StreakGroup
    FROM Streaks
),
StreakLengths AS (
    SELECT
        StreakGroup,
        COUNT(*) AS Length,
        MIN(watchDate) AS StartDate,
        MAX(watchDate) AS EndDate
    FROM GroupedStreaks
    GROUP BY StreakGroup
)
SELECT StartDate, EndDate, Length
FROM StreakLengths
ORDER BY Length DESC
LIMIT 1;
"""
)
    calculatedAverageValue = 0
    start_date = 0
    end_date = 0
    rankings = db.engine.execute(sql)
    for row in rankings:
        start_date = row[0]
        end_date = row[1]
        calculatedAverageValue = row[2]
    result =[]
    result.append(calculatedAverageValue)

    if start_date is not None:
        est = pytz.timezone('US/Eastern')
        current_date_est = datetime.now(est).date()
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()  # Assuming watchDate is in 'YYYY-MM-DD' format
        end_date =  datetime.strptime(end_date, "%Y-%m-%d").date()  
        date_difference = (current_date_est - start_date).days
        result.append(date_difference)
        result.append((current_date_est - end_date).days)
        return result
    else:
        result.append(0)
        result.append(0)
        return result  # Or appropriate response if no streak is found

# Function to store data (average value and date)
def store_data(average_value):
    data = {
        'average_value': average_value,
        'date': datetime.now().isoformat()
    }
    with open('average_value_data.json', 'w') as file:
        json.dump(data, file)

# Function to get stored data
def get_stored_data():
    try:
        with open('average_value_data.json', 'r') as file:
            data = json.load(file)
            data['date'] = datetime.fromisoformat(data['date'])
            return data
    except FileNotFoundError:
        return None
    
def get_or_calculate_average_value():
    stored_data = get_stored_data()
    if stored_data and not is_week_passed(stored_data['date']):
        return stored_data['average_value']
    else:
        # Calculate the new average value
        # (Replace this with your actual SQL query and DB execution logic)
        average_value = calculate_average_value_from_db()

        # Store the new value along with the current date
        store_data(average_value)

        return average_value
    
def calculate_average_value_from_db():
    calculatedAverageValue = 100
    sql = text("WITH PercentileThreshold AS (\
                    SELECT \
                        rankingDifference,\
                        NTILE(10) OVER (ORDER BY rankingDifference DESC) AS percentile\
                    FROM ranking\
                    WHERE winnerRank IS NOT NULL AND loserRank IS NOT NULL\
                )\
                SELECT MIN(rankingDifference) as top10PercentThreshold\
                FROM PercentileThreshold\
                WHERE percentile = 1;")
    
    rankings = db.engine.execute(sql)
    for row in rankings:
        calculatedAverageValue = row[0]
    return calculatedAverageValue

# Function to check if a week has passed since last calculation
def is_week_passed(last_date):
    return last_date - datetime.now() >= timedelta(days=1)

def getMovieById(id):
    movie = Movie.query.filter(Movie.id == id).all()
    return movie[0]

def getRecentRankings():
    flaggedRankings = Ranking.query.filter(and_(text('overwriteRankingId IS NULL'), text('confirmed is NULL'))).order_by(desc(Ranking.modifiedDate)).limit(25).all()
    for flaggedRanking in flaggedRankings:
        winner = Movie.query.filter(and_(Movie.id == flaggedRanking.winnerMovieId)).all()
        flaggedRanking.winnerTitle = winner[0].title
        
        loserMovie = Movie.query.filter(Movie.id == flaggedRanking.loserMovieId).all()
        flaggedRanking.loserTitle = loserMovie[0].title
        
        flaggedRanking.rankingDate = format_datetime(flaggedRanking.modifiedDate - timedelta(hours=5), locale='en')


    return flaggedRankings

def getMovieLog(id):
    log = MovieWatch.query.filter(MovieWatch.id == id).all()[0]
    movie = Movie.query.filter(Movie.id == log.movieId).all()[0]
    log.movieTitle = movie.title
    log.movieLiked = movie.liked
    return log

def getPlusMinusMovies(id):
    movie = Movie.query.filter(Movie.id == id).all()[0]
    if movie.unwatched:
        result = []
        result.append([])
        result.append([])
        result.append([])
        return result

    movies = find_top_watched_movies(0)

    for x in movies:
        if x.id == id:
            movie = x

    movies.sort(key=lambda x: x.rank, reverse=False)
    rank = movie.rank
    result = []

    better = []
    actual = []
    worse = []

    endingRank = rank
    startingRank = rank - 3
    if startingRank < 0: 
        startingRank = 1 
    for i in range(startingRank,endingRank):
        if startingRank + i == len(movies):
            startingRank = 0 - i
        better.append(movies[startingRank -1 ])
        startingRank = startingRank + 1
    
    actual.append(movies[rank - 1])
    rank = rank + 1
    endingRank = rank + 3

    if (endingRank + (endingRank - rank))  >= len(movies) -1:
        endingRank = len(movies) + 1

    for i in range(rank,endingRank):
        if rank + i == len(movies) - 1:
            rank = 0 - i
        worse.append(movies[rank - 1])
        rank = rank + 1
    
    result.append(better)
    result.append(actual)
    result.append(worse)

    # for i in range(-4,3):
    #     if rank + i  == len(movies):
    #         rank = 0 - i
    #     result.append(movies[rank + i])
    return result

def get_rankings(movie_id):
    # Get winners and losers lists
    winners = Ranking.query.filter(and_(Ranking.winnerMovieId == movie_id, Ranking.overwriteRankingId.is_(None))).order_by(desc(Ranking.modifiedDate)).all()
    losers = Ranking.query.filter(and_(Ranking.loserMovieId == movie_id, Ranking.overwriteRankingId.is_(None))).order_by(desc(Ranking.modifiedDate)).all()

    # Fetch details for each opponent movie
    for ranking in winners + losers:
        opponent_id = ranking.loserMovieId if ranking.winnerMovieId == movie_id else ranking.winnerMovieId
        opponent_movie = Movie.query.filter(Movie.id == opponent_id).one_or_none()
        
        if opponent_movie:
            if ranking.winnerMovieId == movie_id:
                ranking.opponentTitle = opponent_movie.title
                ranking.opponentPoster = opponent_movie.poster
                ranking.opponentLiked = opponent_movie.liked
            else:
                ranking.opponentTitle = opponent_movie.title
                ranking.opponentPoster = opponent_movie.poster
                ranking.opponentLiked = opponent_movie.liked

    return winners, losers

def predictStars(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]

    movies = Movie.query.filter(and_(Movie.unwatched != 1, or_(text("stars is not NULL and stars <> 'None' and stars <> '' "), Movie.id == movieId))).all()

    movies = rankingAlgorithm((movies))

    try:
        movie_index = movies.index(movie)
    except ValueError:
        return None
    moviesBeat = []
    moviesLost = []
    for x in range(1, 6):
        if movie_index - x >= 0 :
            rankings = Ranking.query.filter(or_(and_(Ranking.winnerMovieId == movieId, Ranking.loserMovieId == movies[movie_index -1].id), and_(Ranking.loserMovieId == movieId, Ranking.winnerMovieId == movies[movie_index -1].id))).order_by(desc(Ranking.modifiedDate)).all()
            if len(rankings) > 0:
                movieWon = rankings[0].winnerMovieId == movieId
                if movieWon:
                    movie = Movie.query.filter(Movie.id == movies[movie_index -1].id).all()[0]
                    moviesBeat.append(movie.stars)
                else:
                    moviesLost.append(movie.stars)
    for x in range(1, 6):
        if movie_index + x < len(movies) :
            rankings = Ranking.query.filter(or_(and_(Ranking.winnerMovieId == movieId, Ranking.loserMovieId == movies[movie_index -1].id), and_(Ranking.loserMovieId == movieId, Ranking.winnerMovieId == movies[movie_index -1].id))).order_by(desc(Ranking.modifiedDate)).all()
            if len(rankings) > 0:
                movieWon = rankings[0].winnerMovieId == movieId
                if movieWon:
                    movie = Movie.query.filter(Movie.id == movies[movie_index -1].id).all()[0]
                    moviesBeat.append(movie.stars)
                else:
                    moviesLost.append(movie.stars)

def predict_stars(movie_id):
    winners, losers = get_rankings(movie_id)

    # Initialize variables for weighted rating calculation
    weighted_sum = 0
    total_weight = 0

    # Process winners - wins against high-rated movies are more significant
    for win in winners:
        opponent_movie = Movie.query.filter(Movie.id == win.loserMovieId).one_or_none()
        if opponent_movie and opponent_movie.stars:
            try:
                stars = float(opponent_movie.stars)  # Convert to float
                weighted_sum += stars * 1.5
                total_weight += 1.5
            except ValueError:
                # Handle the case where conversion to float fails
               print(f"Warning: Invalid star rating for movie ID {opponent_movie.id}")


    # Process losers - losses against low-rated movies are more significant
    for loss in losers:
        opponent_movie = Movie.query.filter(Movie.id == loss.winnerMovieId).one_or_none()
        if opponent_movie and opponent_movie.stars:
            try:
                stars = float(opponent_movie.stars)
                weighted_sum += stars * 0.5
                total_weight += 0.5
            except ValueError:
               print(f"Warning: Invalid star rating for movie ID {opponent_movie.id}")


    # Calculate the weighted average star rating
    if total_weight > 0:
        predicted_rating = weighted_sum / total_weight
        return max(0, min(predicted_rating, 10))  # Ensure rating is within valid range
    else:
        return None


def getRankings(id):
    result = []
    winners = Ranking.query.filter(and_(Ranking.winnerMovieId == id, text('overwriteRankingId IS NULL'))).order_by(desc(Ranking.modifiedDate)).all()
    losers = Ranking.query.filter(and_(Ranking.loserMovieId == id, text('overwriteRankingId IS NULL'))).order_by(desc(Ranking.modifiedDate)).all()


    for x in winners:
        winnerMovie = Movie.query.filter(Movie.id == x.loserMovieId).all()
        x.winnerTitle = winnerMovie[0].title
        x.winnerPoster = winnerMovie[0].poster
        x.winnerLiked = winnerMovie[0].liked

    for x in losers:
        loserMovie = Movie.query.filter(Movie.id == x.winnerMovieId).all()
        x.loserTitle = loserMovie[0].title
        x.loserPoster = loserMovie[0].poster
        x.loserLiked = loserMovie[0].liked


    result.append(winners)
    result.append(losers)

    return result


def getRankingForStars(id):
    result = []
    # Join the Movie table and filter where Ranking.winnerMovieId's Movie.stars is a number
    winners = Ranking.query.join(Movie, Ranking.loserMovieId == Movie.id)\
                        .filter(and_(Ranking.winnerMovieId == id, 
                                        Movie.stars.isnot(None),
                                         Movie.stars != 'None',
                                         Movie.stars != '',
                                        text('overwriteRankingId IS NULL')))\
                        .order_by(desc(Ranking.modifiedDate)).all()

    # Do the same for loserMovieId
    losers = Ranking.query.join(Movie, Ranking.winnerMovieId == Movie.id)\
                        .filter(and_(Ranking.loserMovieId == id, 
                                    Movie.stars.isnot(None),
                                    Movie.stars != 'None',
                                    Movie.stars != '',
                                    text('overwriteRankingId IS NULL')))\
                        .order_by(desc(Ranking.modifiedDate)).all()

    for x in winners:
        winnerMovie = Movie.query.filter(Movie.id == x.loserMovieId).first()
        if winnerMovie:
            x.winnerTitle = winnerMovie.title
            x.winnerPoster = winnerMovie.poster
            x.winnerLiked = winnerMovie.liked
            x.winnerStars = winnerMovie.stars

    for x in losers:
        loserMovie = Movie.query.filter(Movie.id == x.winnerMovieId).first()
        if loserMovie:
            x.loserTitle = loserMovie.title
            x.loserPoster = loserMovie.poster
            x.loserLiked = loserMovie.liked
            x.loserStars = loserMovie.stars

    winner_stars_set = set(x.loserStars for x in losers)
    loser_stars_set = set(x.winnerStars for x in winners)

    # Sort the sets in descending order for lower_bound and ascending order for upper_bound
    sorted_winner_stars = sorted(winner_stars_set, reverse=True)
    sorted_loser_stars = sorted(loser_stars_set)

    # Determine the lower bound
    # Start with the highest value in loserStars that is not in winnerStars
    lower_bound = None
    for star in sorted_loser_stars[::-1]:  # Iterate in reverse order (highest to lowest)
        if star not in winner_stars_set:
            lower_bound = star
            break

    upper_bound = None
    for star in sorted_winner_stars[::-1]:  # Iterate in reverse order (lowest to highest)
        if star not in sorted_loser_stars:
            upper_bound = star
            break
    
    suggestedStar = 0
    explainString = ""
    if lower_bound is not None:
        if upper_bound is None:
            upper_bound = 9.5
        if lower_bound > upper_bound:
            lower_bound = upper_bound - 2
        values = []
        tempLower = lower_bound
        tempUpper = upper_bound
        while tempLower < tempUpper:
            if 0.5 + tempLower < tempUpper:
                tempLower = tempLower + 0.5
                values.append(tempLower)
            else:
                break
        counts = []
        winCounts = []
        lossCounts = []
        if len(values) < 1:
            values.append(lower_bound + 0.5 - 0.5)
            suggestedStar = lower_bound

        if len(values) == 1:
                suggestedStar = values[0]
                values.insert(0, values[0] - 0.5)
                values.append(values[1] + 0.5)
                for val in values:
                    sqlTextWin = text(" \
        overwriteRankingId is NULL \
    and winnerMovieId = " + str(id) + " and loserMovieId IN (SELECT id from movie where movie.stars = " + str(val) + ") \
    ")
                    sqlTextLoss = text("""
        overwriteRankingId is NULL
    and loserMovieId = """ + str(id) + """ and winnerMovieId IN (SELECT id from movie where movie.stars = """ + str(val) + """)
    """)
                    wins = Ranking.query.filter((sqlTextWin)).all()
                    losses = Ranking.query.filter((sqlTextLoss)).all()

                    if len(wins) + len(losses) == 0:
                        counts.append(0)
                    else:
                        counts.append(round(100 * len(wins) / (len(wins) + len(losses)), 2) )

                    winCounts.append(len(wins))
                    lossCounts.append(len(losses))
                index = 0
                while len(values) > index:
                    if counts[index] > 60:
                        index = index + 1
                    else:
                        break
                for i in range(0, len(values)):
                    if i != 0:
                        explainString = explainString + "\n" +  str(values[i]) + "/10: " + str(counts[i]) + "% win rate (" + str(winCounts[i]) + "/" + str(winCounts[i] + lossCounts[i]) +  ")"
                    else:
                        explainString = explainString + "" +  str(values[i]) + "/10: " + str(counts[i]) + "% win rate (" + str(winCounts[i]) + "/" + str(winCounts[i] + lossCounts[i]) +  ")"

        else:
            for val in values:
                sqlTextWin = text(" \
    overwriteRankingId is NULL \
and winnerMovieId = " + str(id) + " and loserMovieId IN (SELECT id from movie where movie.stars = " + str(val) + ") \
")
                sqlTextLoss = text("""
    overwriteRankingId is NULL
and loserMovieId = """ + str(id) + """ and winnerMovieId IN (SELECT id from movie where movie.stars = """ + str(val) + """)
""")
                wins = Ranking.query.filter((sqlTextWin)).all()
                losses = Ranking.query.filter((sqlTextLoss)).all()

                if len(wins) + len(losses) == 0:
                    counts.append(0)
                else:
                    counts.append(round(100 * len(wins) / (len(wins) + len(losses)), 2) )
                winCounts.append(len(wins))
                lossCounts.append(len(losses))
            index = 0
            while len(values) > index:
                if counts[index] > 60:
                    if index + 1 == len(values):
                        break
                    index = index + 1
                else:
                    break
            suggestedStar = values[index]
            
            for i in range(0, len(values)):
                if i != 0:
                        explainString = explainString + "\n" +  str(values[i]) + "/10: " + str(counts[i]) + "% win rate (" + str(winCounts[i]) + "/" + str(winCounts[i] + lossCounts[i]) +  ")"
                else:
                    explainString = explainString + "" +  str(values[i]) + "/10: " + str(counts[i]) + "% win rate (" + str(winCounts[i]) + "/" + str(winCounts[i] + lossCounts[i]) +  ")"

            
    # Sorting (existing code)
    winners.sort(key=lambda x: x.winnerStars, reverse=True)
    losers.sort(key=lambda x: x.loserStars)

    # Append results
    result.append(winners)
    result.append(losers)
    result.append(upper_bound)
    result.append(lower_bound)
    result.append(suggestedStar)
    result.append(explainString)


    return result

def getUpsets(id):
    result = []
    winners = Ranking.query.filter(and_(Ranking.winnerMovieId == id, text('overwriteRankingId IS NULL'), Ranking.likeUpset == 1)).order_by(desc(Ranking.modifiedDate)).all()
    losers = Ranking.query.filter(and_(Ranking.loserMovieId == id, text('overwriteRankingId IS NULL'), Ranking.likeUpset == 1)).order_by(desc(Ranking.modifiedDate)).all()


    for x in winners:
        winnerMovie = Movie.query.filter(Movie.id == x.loserMovieId).all()
        x.winnerTitle = winnerMovie[0].title
        x.winnerPoster = winnerMovie[0].poster
        x.winnerLiked = winnerMovie[0].liked

    for x in losers:
        loserMovie = Movie.query.filter(Movie.id == x.winnerMovieId).all()
        x.loserTitle = loserMovie[0].title
        x.loserPoster = loserMovie[0].poster
        x.loserLiked = loserMovie[0].liked


    result.append(winners)
    result.append(losers)

    return result

def getFlaggedRankings():
    flaggedRankings = Ranking.query.filter(and_(Ranking.flagged == 1, text('overwriteRankingId IS NULL'))).order_by(text('winnerRank - loserRank desc')).all()
    for flaggedRanking in flaggedRankings:
        winner = Movie.query.filter(and_(Movie.id == flaggedRanking.winnerMovieId)).all()
        flaggedRanking.winnerTitle = winner[0].title
        
        flaggedRanking.winnerLiked = winner[0].liked
        loserMovie = Movie.query.filter(Movie.id == flaggedRanking.loserMovieId).all()
        flaggedRanking.loserTitle = loserMovie[0].title
        
        flaggedRanking.loserLiked = loserMovie[0].liked
        flaggedRanking.rankingDate = format_datetime(flaggedRanking.modifiedDate - timedelta(hours=5), locale='en')

        sql = text("WITH RankedMovies AS ( \
                SELECT id, \
                    ROW_NUMBER() OVER (ORDER BY rewatchScore DESC) AS rank \
                FROM movie \
                WHERE movie.unwatched <> 1 \
            ) \
            SELECT  a.rank as winnerRank, b.rank as loserRank, a.rank - b.rank AS rank_difference \
            FROM RankedMovies a, RankedMovies b \
            WHERE a.id = " + str(winner[0].id) + " AND b.id = " + str(loserMovie[0].id))
    
        ranks = db.engine.execute(sql)

        difference = 0

        for row in ranks:
            winnerRankNum = row[0] #winnerRank
            loserRankNum = row[1]  #loserRank 
            difference = row[2] #difference 

        flaggedRanking.winnerRank = winnerRankNum
        flaggedRanking.loserRank = loserRankNum
        flaggedRanking.winnerYear = winner[0].year
        flaggedRanking.loserYear = loserMovie[0].year
        flaggedRanking.rankingDifference = flaggedRanking.winnerRank - flaggedRanking.loserRank

        flagChecker = get_or_calculate_average_value()
        if flagChecker is None or int(flagChecker) < 100:
            flagChecker = 100
        if difference > flagChecker and (winner[0].rewatchCount > 3 and loserMovie[0].rewatchCount > 3):
            flaggedRanking.flagged = True
        else:
            flaggedRanking.flagged = False

    return flaggedRankings

def getUpsetsRankings():
    flaggedRankings = Ranking.query.filter(and_(Ranking.likeUpset == 1, text('overwriteRankingId IS NULL'), Ranking.confirmed != 1)).order_by(text('winnerRank - loserRank desc')).all()
    for flaggedRanking in flaggedRankings:
        winner = Movie.query.filter(and_(Movie.id == flaggedRanking.winnerMovieId)).all()
        flaggedRanking.winnerTitle = winner[0].title
        
        flaggedRanking.winnerLiked = winner[0].liked
        loserMovie = Movie.query.filter(Movie.id == flaggedRanking.loserMovieId).all()
        flaggedRanking.loserTitle = loserMovie[0].title
        
        flaggedRanking.loserLiked = loserMovie[0].liked
        flaggedRanking.rankingDate = format_datetime(flaggedRanking.modifiedDate - timedelta(hours=5), locale='en')


    return flaggedRankings

def getSharedRankings():
    flaggedRankings = SharedRanking.query.filter().order_by(desc(SharedRanking.id)).all()
    for flaggedRanking in flaggedRankings:
        winner = Movie.query.filter(and_(Movie.id == flaggedRanking.winnerMovieId)).all()
        flaggedRanking.winnerTitle = winner[0].title
        loserMovie = Movie.query.filter(Movie.id == flaggedRanking.loserMovieId).all()
        flaggedRanking.loserTitle = loserMovie[0].title
        
        flaggedRanking.rankingDate = format_datetime(flaggedRanking.modifiedDate - timedelta(hours=5), locale='en')

    return flaggedRankings


def removeFlagFromRanking(rankingId):
    ranking = Ranking.query.filter(Ranking.id == rankingId).all()[0]
    ranking.flagged = False
    ranking.confirmed = func.now()

    db.session.commit()



def removeSharedMovie(rankingId, movieId):
    shared = SharedRanking.query.filter(SharedRanking.id == rankingId).all()[0]
    winnerId = 0
    loserId = 0
    if movieId == shared.winnerMovieId:
        winnerId = movieId
        loserId = shared.loserMovieId
    else:
        winnerId = movieId
        loserId = shared.winnerMovieId

    SharedRanking.query.filter(SharedRanking.id == rankingId).delete()
    
    updateRankings(winnerId, loserId, False)
    db.session.commit()

def getRankingsInList(listId, movieId):
    result = []

    winnerSql = text('SELECT * FROM ranking where overwriteRankingId IS NULL and winnerMovieId = ' + str(movieId) + ' AND loserMovieId IN (SELECT movieId from list_movie WHERE overwriteRankingId IS NULL and listId = ' + str(listId) + ' )')
    loserSql = text('SELECT * FROM ranking where overwriteRankingId IS NULL and loserMovieId = ' + str(movieId) + ' AND winnerMovieId IN (SELECT movieId from list_movie WHERE overwriteRankingId IS NULL and listId = ' + str(listId) + ' )')
    rankings = db.engine.execute(winnerSql)
    rankings2 = db.engine.execute(loserSql)
    winners = []
    losers = []
    for x in rankings:
        ranking = Ranking.query.filter(Ranking.id == x.id).all()[0]
        winnerMovie = Movie.query.filter(Movie.id == x.loserMovieId).all()
        ranking.winnerTitle = winnerMovie[0].title
        ranking.winnerPoster = winnerMovie[0].poster
        winners.append(ranking)

    for x in rankings2:
        ranking = Ranking.query.filter(Ranking.id == x.id).all()[0]
        loserMovie = Movie.query.filter(Movie.id == x.winnerMovieId).all()
        ranking.loserTitle = loserMovie[0].title
        ranking.loserPoster = loserMovie[0].poster
        losers.append(ranking)


    # winners = Ranking.query.filter(and_(Ranking.winnerMovieId == id, text('overwriteRankingId IS NULL'))).order_by(desc(Ranking.modifiedDate)).all()
    # losers = Ranking.query.filter(and_(Ranking.loserMovieId == id, text('overwriteRankingId IS NULL'))).order_by(desc(Ranking.modifiedDate)).all()


    # for x in winners:
    #     winnerMovie = Movie.query.filter(Movie.id == x.loserMovieId).all()
    #     x.winnerTitle = winnerMovie[0].title
    #     x.winnerPoster = winnerMovie[0].poster

    # for x in losers:
    #     loserMovie = Movie.query.filter(Movie.id == x.winnerMovieId).all()
    #     x.loserTitle = loserMovie[0].title
    #     x.loserPoster = loserMovie[0].poster


    result.append(winners)
    result.append(losers)

    return result

def getTimesLogged(id):
    movies = MovieWatch.query.filter(MovieWatch.movieId == id).all()[0]
    return len(movies)

def getTimesWatched(id):
    count = MovieWatch.query.filter(MovieWatch.movieId == id).all()
    return len(count)

def getMovieDetails(id):
    movie = Movie.query.filter(Movie.id == id).all()[0]
    count = MovieWatch.query.filter(MovieWatch.movieId == movie.id).all()
    movie.timesWatched = len(count)
    movie.movieRecommendStars = getRankingForStars(movie.id)[4]
    movie.genres = getMovieGenreNames(movie.id)

    return movie

def find_rewatch_movies():
    movies = Movie.query.filter(and_(Movie.rewatch == 1, Movie.unwatched != 1)).order_by(desc(Movie.id)).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_current_watch_movies():
    movies = Movie.query.filter(Movie.currentlyWatching == 1).order_by(desc(Movie.runtime)).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_genres():
    genres = Genre.query.order_by(asc(Genre.name)).all()
    return set_count(genres)

def find_movies_by_genre(id):
    movies = []
    movieIds = MovieGenre.query.filter(MovieGenre.genreId == id).all()
    for movieId in movieIds:
        movie = Movie.query.filter(Movie.id == movieId.movieId).all()
        if len(movie) > 0 :
            # if movie[0].unwatched != 1:
            #     movies.append(movie[0])
            movies.append(movie[0])
    movies.sort(key=lambda x: x.rewatchScore, reverse=True)

    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(movies)

def find_movies_by_genre_filter(genreId, title, director, year, min, max, recommendation):
    movies = Movie.query.filter(
                                and_(
                                     or_(title == "", title is None, Movie.title.ilike('%' + title + '%')), 
                                     or_(director == "", director is None, Movie.director.ilike('%' + director + '%')), 
                                     or_(year == "", year is None, Movie.year.ilike('%' + year + '%')), 
                                     or_(recommendation == "", recommendation is None, Movie.recommend.ilike('%' + recommendation + '%')), 
                                     or_(min == 0, min == "", min is None, str(min) == "0", Movie.runtime > min),
                                     or_(max == 0, max is None, max == "", str(max) == "0", Movie.runtime < max)
                                    )
                                ).order_by(desc(Movie.rewatchScore)).all()
    
    result = []
    movieIds = MovieGenre.query.filter(MovieGenre.genreId == genreId).all()
    for movieId in movieIds:
        for movie in movies:
            if movieId.movieId == movie.id:
                result.append(movie)
    for x in result:
        x.genres = getMovieGenreNames(x.id)
    return set_ranks(result)

def find_movies_by_list(id):
    movies = []
    movieIds = ListMovie.query.filter(ListMovie.listId == id).all()
    for movieId in movieIds:
        movie = Movie.query.filter(Movie.id == movieId.movieId).all()
        if len(movie) > 0 :
            # if movie[0].unwatched != 1:
            #     movies.append(movie[0])
            movies.append(movie[0])
    movies.sort(key=lambda x: x.rewatchScore, reverse=True)
    return set_ranks(movies)


def find_genres_by_id(id):
    genre = Genre.query.filter(Genre.id == id).all()
    return get_genre_count(genre[0])

def find_list_by_id(id):
    list = List.query.filter(List.id == id).all()
    return get_list_count(list[0])

def getRandomMovieByGenre(id):
    while True:   
        movies = find_movies_by_genre(id)
        index = random.randint(0, len(movies) -1)
        movie = movies[index]
        if(movie.unwatched != 1):
            break
        if(len(movies) < 2):
            movie = []
            break
    return movie

def getRandomMovieByList(id):
    while True:   
        movies = find_movies_by_list(id)
        index = random.randint(0, len(movies) -1)
        movie = movies[index]
        if(movie.unwatched != 1):
            break
        if(len(movies) < 2):
            movie = []
            break
    return movie

def movieForMovieFromList(id, movieId):
    movies = []
    sql = text("SELECT * \
            FROM movie m1 \
            WHERE	\
                         m1.unwatched <> 1 AND   m1.id IN (SELECT movieId FROM list_movie lm1 where lm1.listId = " + str(id) + ") AND\
                                (SELECT COUNT(*) \
                                FROM ranking \
                                WHERE  ranking.overwriteRankingId is NULL and (\
                                                (winnerMovieId = m1.id and  loserMovieId IN (SELECT movieId FROM list_movie lm1 where lm1.listId = " + str(id) + ")) \
                                        or (loserMovieId = m1.id and  winnerMovieId IN (SELECT movieId FROM list_movie lm1 where lm1.listId = " + str(id) + "))) \
                                        ) < (SELECT COUNT(*) FROM list_movie lm2 WHERE listId = " + str(id) + " and movieId IN (SELECT id FROM movie WHERE lm2.movieId = movie.id and movie.unwatched <> 1)) - 1")

    rankings = db.engine.execute(sql)
    names = []
    for row in rankings:
        names.append(row[0]) #ids
    movies = findMoviesByIdList(names)
    if(len(movies)) < 2:
        return []

    found_movie = None
    for movie in movies:
        if movie.id == int(movieId):
            found_movie = movie
            break
    if found_movie is None:
        return []
    firstMovie = found_movie

    while True:
        secondMovie = random.choice(movies)
        if firstMovie.id != secondMovie.id: 
            ranking = Ranking.query.filter(or_
                                           (and_(Ranking.loserMovieId == firstMovie.id, Ranking.winnerMovieId == secondMovie.id), 
                                            and_(Ranking.loserMovieId == secondMovie.id, Ranking.winnerMovieId == firstMovie.id
                                                 )
                                            )
                                           ).all()
            if len(ranking) < 1:
                break
    return secondMovie


def getRandomRecentMovie():
    logs = getRankOfRecentMovies(15)
    log = random.choice(logs)
    movie = Movie.query.filter(log.movieId == Movie.id).all()[0]
    return movie

def getRandomUnrankedMovie():
    while True:
        movies = Movie.query.filter(Movie.unwatched != 1).order_by(asc(Movie.rewatchCount)).limit(50).all()
        index = random.randint(0, len(movies) - 1)
        movie = movies[index]
        if(movie.unwatched != 1):
            break
    return movie

def saveForLater(winnerId, loserId):
    winner = Movie.query.filter(Movie.id == winnerId).all()[0]
    loser = Movie.query.filter(Movie.id == loserId).all()[0]

    Pb =  0
    Pa =  0
    Ra = 0
    Rb = 0

    shared = SharedRanking.query.filter(or_(and_(SharedRanking.winnerMovieId == winnerId, SharedRanking.loserMovieId == loserId), 
                                            and_(SharedRanking.loserMovieId == winnerId, SharedRanking.winnerMovieId == loserId)
                                            )).all()
    
    if len(shared) > 0:
        return

    ranking = SharedRanking(winnerMovieId=winner.id, loserMovieId=loser.id, modifiedDate=func.now(), winnerStartingPoints=winner.rewatchScore, loserStartingPoints=loser.rewatchScore, 
                      winnerPointsGained=50 * (1 - Pa), loserPointsLossed=50 * (1 - Pb), winnerEndingPoints=Ra, losserEndingPoints=Rb, winnerCount=winner.rewatchCount, loserCount=loser.rewatchCount)
    
    ranking = checkFlag(winner, loser, ranking)

    db.session.add(ranking)
    db.session.commit()

def add_movie(new_title, new_year, people, new_director, new_runtime, rewatched, new_poster, newFirstGenre, newSecondGenre, notes, stars, recommend, date, location, faveQuote, watchNotes):
    if date is not None and date != '' and date != "":
        newDate = datetime.strptime(date, '%Y-%m-%d')
    else:
        newDate = None
    if len(people) > 0 or len (location) > 0 or (date != None and date != ""):
        unwateched = 0
    else:
        unwateched = 1
    movie = Movie(title=new_title, year=new_year, rewatch=rewatched, rewatchScore=1500, rewatchCount=0, cinematicScore=1500, cinematicCount=0, poster="",
     unwatched=unwateched, director=new_director, runtime=new_runtime, notes=notes, stars=stars, recommend=recommend, lastWatchedDate=newDate, location=location, rankingPercentage=0, rankingWinCount=0, faveQuote=faveQuote)
    db.session.add(movie)
    db.session.commit()

    movie = Movie.query.filter(Movie.title == new_title).all()[0]

    firstGenre = Genre.query.filter(Genre.name == newFirstGenre).all()
    if(firstGenre is not None and len(firstGenre) > 0):
        firstMovieGenre = MovieGenre(movieId=movie.id,genreId=firstGenre[0].id)
        db.session.add(firstMovieGenre)

    secondGenre = Genre.query.filter(Genre.name == newSecondGenre).all()
    if(secondGenre is not None and len(secondGenre) > 0):
        secondMovieGenre = MovieGenre(movieId=movie.id,genreId=secondGenre[0].id)
        db.session.add(secondMovieGenre)

    log_movie(movie.id, movie.notes, movie.stars, movie.recommend, movie.faveQuote, location, people, watchNotes, date)

    db.session.commit()


    return movie.id

def add_list(new_name, notes):
    list = List(name=new_name, notes=notes)
    db.session.add(list)
    db.session.commit()

    list = List.query.filter(List.name == new_name).order_by(desc(List.id)).all()[0]

    return list.id

def createListWithRandomMovies(size):
    list = List(name="Random List", notes= ("Random List with " + str(size) + " movies") )
    db.session.add(list)

    list = List.query.filter(List.name == "Random List").order_by(desc(List.id)).all()[0]

    for i in range(0,size):
        while True:
            movie = getRandomMovie()
            if movie.unwatched != 1:
                lists = ListMovie.query.filter(and_(ListMovie.listId == list.id, ListMovie.movieId == movie.id)).all()
                if len(lists) < 1:
                    listMovie = ListMovie(listId=list.id, movieId=movie.id)
                    db.session.add(listMovie)
                    break    
    db.session.commit()
    return list.id

def duplicateList(listId):
    oldList = List.query.filter(List.id == listId).order_by(desc(List.id)).all()[0]

    list = List(name=(str(oldList.id) + " (Duplicate)"), notes= ("Duplicated List:  " + str(oldList.notes)) )
    db.session.add(list)

    list = List.query.filter(List.name == (str(oldList.id) + " (Duplicate)")).order_by(desc(List.id)).all()[0]

    listMovies = ListMovie.query.filter(ListMovie.listId == listId).all()

    for oldListMovie in listMovies:
        listMovie = ListMovie(listId=list.id, movieId=oldListMovie.movieId)
        db.session.add(listMovie)   
    db.session.commit()
    return list.id



def addMoviesToListRandom(listId):
    list = List.query.filter(List.id == listId).order_by(desc(List.id)).all()[0]
    while True:
            movie = getRandomMovie()
            if movie.unwatched != 1:
                lists = ListMovie.query.filter(and_(ListMovie.listId == list.id, ListMovie.movieId == movie.id)).all()
                if len(lists) < 1:
                    listMovie = ListMovie(listId=list.id, movieId=movie.id)
                    db.session.add(listMovie)
                    break    
    db.session.commit()

def getTimesRankedString(listId):
    sql = text("SELECT COUNT(*)\
                FROM ranking  r\
                WHERE r.winnerMovieId IN (SELECT movieId from list_movie WHERE listId =  " + str(listId) + ")\
                and r.loserMovieId IN (SELECT movieId from list_movie WHERE listId =  " + str(listId) + ")\
                AND r.overwriteRankingId is null")
    rankings = db.engine.execute(sql)
    names = []
    for row in rankings:
        names.append(row[0]) #ids
    count = names[0]
    

    return count

def updateMovie(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]
    movie.unwatched = 0
    movie.rewatch = 0
    db.session.commit()

def updateLiked(movieId, liked):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]
    #1 = liked, 2 = decent, 3= trash
    movie.liked = liked
    db.session.commit()


    

# def getSavedMovies():
    # rankings = SavedRanking.query.filter().all()
    # if len(rankings) < 1:
    #     return []
    # for r in rankings:
        



def saveRanking(first, second):
    rankingsBefore = SavedRanking.query.filter(or_ ( and_(SavedRanking.firstMovieId == second, SavedRanking.secondMovie == first ) , and_(SavedRanking.firstMovieId == first, SavedRanking.secondMovie == second ) ) ).all()
    if len(rankingsBefore) > 0:
        return

    first = Movie.query.filter(Movie.id == first).all()[0]
    second = Movie.query.filter(Movie.id == second).all()[0]

    ranking = SavedRanking(firstMovieId=first.id, secondMovieId=second.id)

    db.session.add(ranking)
    db.session.commit()

def removeSavedRanking(first, second):
    SavedRanking.query.filter(or_ ( and_(SavedRanking.firstMovieId == second, SavedRanking.secondMovie == first ) , and_(SavedRanking.firstMovieId == first, SavedRanking.secondMovie == second ) ) ).delete()
    db.session.commit()

def rewatchMovie(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]
    movie.rewatch = 1
    db.session.commit()

def confirmLog(logId):
    log = MovieWatch.query.filter(and_(MovieWatch.id == logId)).all()
    if len(log) > 0:
        movieId = log[0].movieId
        logs = MovieWatch.query.filter(and_(MovieWatch.movieId == movieId, MovieWatch.confirmedStars != 1)).all()
        for log in logs:
            log.confirmedStars = 1
        db.session.commit()

def addMovieToList(listId, movieId):
    lists = ListMovie.query.filter(and_(ListMovie.listId == listId, ListMovie.movieId == movieId)).all()
    if len(lists) > 0:
        return
    listMovie = ListMovie(listId=listId, movieId=movieId)
    db.session.add(listMovie)
    db.session.commit()

def unRewatchMovie(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]
    movie.rewatch = 0
    db.session.commit()

def removeCurrentWatch(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]
    movie.currentlyWatching = 0
    db.session.commit()

def currentlyWatching(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]
    movie.currentlyWatching = 1
    db.session.commit()

def find_unwatched_movies():
    movies = Movie.query.filter(Movie.unwatched == 1).order_by(desc(Movie.id)).all()
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
    return movies

def getMovieWatches(id):
    watches = MovieWatch.query.filter(MovieWatch.movieId == id).order_by(desc(MovieWatch.watchDate), desc(MovieWatch.id)).all()
    return watches

def update_log(movie_id, location, newPeople, newNotes, date, faveQuote, recommend, stars, notes):
    
    
    log = MovieWatch.query.filter(MovieWatch.id == movie_id).all()[0]
    log.location = location
    log.people = newPeople
    log.notes = newNotes
    if date is not None and date != '' and date != "" and len(date) > 4:
        date = datetime.strptime(date, '%Y-%m-%d')
    else:
        date = None
    log.watchDate = date

    if date is not None:
        if date.year == datetime.now().year:
            addMovieToList(28, log.movieId)
            addMovieToList(32, log.movieId)

    if "Isabella" in newPeople:
        addMovieToList(20, log.movieId)
    if "Mom" in newPeople:
        addMovieToList(21, log.movieId)
    if "Sebby" in newPeople:
        addMovieToList(22, log.movieId)
    if "Lils" in newPeople:
        addMovieToList(23, log.movieId)
    if "Dad" in newPeople:
        addMovieToList(24, log.movieId)
    if "Charles" in newPeople:
        addMovieToList(25, log.movieId)

    db.session.commit()

    return log.movieId


def update_movie(movie_id, new_title, new_year, unwatched, rewatched, new_poster, new_firstGenre, new_secondGenre, new_director, new_runtime, notes, stars, recommend, date, location, faveQuote, liked, onComputer):
    movie = Movie.query.filter(Movie.id == movie_id).all()[0]
    movie.title = new_title
    movie.year = new_year
    movie.rewatch = rewatched
    movie.poster = new_poster
    movie.director = new_director
    movie.runtime = new_runtime
    movie.notes = notes
    movie.stars = stars
    movie.recommend = recommend
    movie.faveQuote = faveQuote
    movie.liked = liked
    movie.onComputer = onComputer
    if movie.onComputer == 1:
        addMovieToList(27, movie.id)

    if date is not None and date != '' and date != "" and len(date) > 4:
        movie.lastWatchedDate = datetime.strptime(date, '%Y-%m-%d')
    movie.location = location 
    
    movieGenres = MovieGenre.query.filter(MovieGenre.movieId == movie_id).all()
    
    for movieGenre in movieGenres:
        MovieGenre.query.filter(MovieGenre.id == movieGenre.id).delete()

    firstGenre = Genre.query.filter(Genre.name == new_firstGenre).all()
    if(firstGenre is not None and firstGenre != "" and len(firstGenre) > 0):
        firstMovieGenre = MovieGenre(movieId=movie.id,genreId=firstGenre[0].id)
        db.session.add(firstMovieGenre)

    secondGenre = Genre.query.filter(Genre.name == new_secondGenre).all()
    if(secondGenre is not None and secondGenre != "" and len(secondGenre)> 0):
        secondMovieGenre = MovieGenre(movieId=movie.id,genreId=secondGenre[0].id)
        db.session.add(secondMovieGenre)

    db.session.commit()

def update_list(list_id, new_title, notes):
    list = List.query.filter(List.id == list_id).all()[0]

    list.name = new_title
    list.notes = notes

    db.session.commit()

def removeMovieFromList(listId, movieId):
    ListMovie.query.filter(and_(ListMovie.listId == listId, ListMovie.movieId == movieId)).delete()

    db.session.commit()

def startedSession():
    openSession = isOpenSession()
    if openSession:
        lastSession = getLatestSession()
        lastSession.endDate = date.today()
        db.session.commit()
        return False
    else:
        session = Session(startDate=date.today())
        db.session.add(session)
        db.session.commit()
        return True
    
def getLatestSession():
    lastSession = Session.query.order_by(desc(id)).all()[0]
    return lastSession

def getMoviesRankedInSession():
    lastestSession = getLatestSession()
    rankings = Ranking.query.filter(Ranking.sessionId == lastestSession.id).all()
    return rankings

def getTopMoviesInRankingSession():
    daterange  = 0
    sql = text('SELECT movie.id, movie.title, \
                (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as Wins, \
                (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as loseses, \
                ( (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') -  (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') ) as difference, \
                (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as totals, \
                (100 * (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE (ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')  / (SELECT COUNT(winnerMovieId) as Total \
                FROM ranking WHERE (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')) as percent \
                FROM movie  \
                ORDER BY ( (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') -  (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') ) desc, percent desc LIMIT 8')
    rankings = db.engine.execute(sql)
    names = []
    winsCount = []
    totalsCount = []
    differenceCount = []
    for row in rankings:
        names.append(row[0]) #ids
        winsCount.append(row[2])  #wins 
        differenceCount.append(row[4])  #difference 
        totalsCount.append(row[5]) # total
    movies = findMoviesByIdList(names)
    counter = 0
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
        x.winsGained = differenceCount[counter]
        x.cinematicScore = totalsCount[counter]
        x.rankingWinCount = winsCount[counter]
        counter = counter + 1
    return movies


def isOpenSession():
    lastSession = Session.query.order_by(desc(id)).all()
    if len(lastSession) > 0:
        lastSession = lastSession[0]
        if lastSession.endDate is not None:
            if len(str(lastSession)) > 0:
                return False

    return True



def log_movie(movie_id, notes, stars, recommend, faveQuote, newLocation, newPeople, newNotes, newDate):
    movie = Movie.query.filter(Movie.id == movie_id).all()[0]
    movie.notes = notes
    movie.stars = stars
    movie.recommend = recommend
    movie.faveQuote = faveQuote
    db.session.commit()

    if len(newLocation) < 2 and len(newNotes) < 2 and len(newPeople) < 2 and (newDate is None or newDate == '' or newDate == ""):
        return
    
    movie.unwatched = 0
    movie.rewatch = 0
    movie.currentlyWatching = 0
    db.session.commit()

    if newDate is not None and newDate != '' and newDate != "":
        NewnewDate = datetime.strptime(newDate, '%Y-%m-%d')
    else:
        NewnewDate = None

    isFirstWatch = True
    
    watchesFromMovie = MovieWatch.query.filter(MovieWatch.movieId == movie_id).all()
    if len(watchesFromMovie) > 0:
        firstWatcheds = MovieWatch.query.filter(and_(MovieWatch.movieId == movie_id, MovieWatch.firstWatch == 1)).all()
        if len(firstWatcheds) > 0:
            firstWatched = firstWatcheds[0]
            if firstWatched.watchDate is not None and NewnewDate is not None:
                if datetime.strptime(str(firstWatched.watchDate), '%Y-%m-%d') <= NewnewDate:
                    isFirstWatch = False
                else:
                    firstWatched.firstWatch = False
        else:
            firstWatcheds = MovieWatch.query.filter(MovieWatch.movieId == movie_id).order_by(asc(MovieWatch.watchDate)).all()
            if len(firstWatcheds) > 0:
                firstWatched = firstWatcheds[0]
                if firstWatched.watchDate is not None and NewnewDate is not None:
                    if datetime.strptime(str(firstWatched.watchDate), '%Y-%m-%d') <= NewnewDate:
                        isFirstWatch = False
                    else:
                        firstWatched.firstWatch = False
    
    confirmStars = isFirstWatch
    if not confirmStars:
        movies = Movie.query.filter(text("id = " + str(movie_id) + " AND (stars = 'None' OR LENGTH(stars) < 1)")).all()
        if len(movies) > 0:
            #the movie does not have stars 
            confirmStars = True

    movieWatch = MovieWatch(movieId=movie_id, location=newLocation, people=newPeople, notes=newNotes, watchDate=NewnewDate, firstWatch=isFirstWatch, confirmedStars=confirmStars)
    db.session.add(movieWatch)

    if NewnewDate is not None and isFirstWatch:
        if NewnewDate.year == datetime.now().year:
            addMovieToList(28, movie_id)
            addMovieToList(32, movie_id)

    if "Isabella" in newPeople:
        addMovieToList(20, movie_id)
    if "Mom" in newPeople:
        addMovieToList(21, movie_id)
    if "Sebby" in newPeople:
        addMovieToList(22, movie_id)
    if "Lils" in newPeople:
        addMovieToList(23, movie_id)
    if "Dad" in newPeople:
        addMovieToList(24, movie_id)
    if "Charles" in newPeople:
        addMovieToList(25, movie_id)
    
    db.session.commit()


def getMovieGenres(movieId):
    movieGenres = MovieGenre.query.filter(MovieGenre.movieId == movieId).all()
    result = []


    if(len(movieGenres) == 0 or movieGenres is None):
        firstGenre = ""
        secondGenre = ""
        result.append(firstGenre)
        result.append(secondGenre)
        return result

    if(len(movieGenres)) == 1:
        if(movieGenres[0] is not None):
            firstGenre = Genre.query.filter(Genre.id == movieGenres[0].genreId).all()            
        else:
            firstGenre = ""
        
        result.append(firstGenre[0])
        result.append("")
        return result

    if(movieGenres[0] is not None):
        firstGenre = Genre.query.filter(Genre.id == movieGenres[0].genreId).all()            
    else:
        firstGenre = ""
    if(movieGenres[1] is not None):
        secondGenre = Genre.query.filter(Genre.id == movieGenres[1].genreId).all()
    else:
        secondGenre = ""
    if len(firstGenre) > 0:
        firstGenre = firstGenre[0]
    else:
        firstGenre = ""
    if len(secondGenre) > 0:
        secondGenre = secondGenre[0]
    else:
        secondGenre = ""
    result.append(firstGenre)
    result.append(secondGenre)
    return result

def getMovieGenreNames(movieId):
    movieGenres = MovieGenre.query.filter(MovieGenre.movieId == movieId).all()
    result = ""
    if(len(movieGenres) == 0 or movieGenres is None):
        return result
    else: 
        firstGenre = Genre.query.filter(Genre.id == movieGenres[0].genreId).all()
        if len(firstGenre) > 0:
            result = firstGenre[0].name
        else:
            result = ""
        if len(movieGenres) > 1:
            secondGenre = Genre.query.filter(Genre.id == movieGenres[1].genreId).all()
            if len(secondGenre) > 0:
                result = result + " , " + secondGenre[0].name        
    return result

def getUniqueMovies():
    movies = []
    while True:  
        firstMovie = getRandomMovie()
        secondMovie = getRandomMovie()
        if firstMovie.rewatch == 1 or secondMovie.rewatch == 1:
            continue
        if firstMovie.id != secondMovie.id:
                ranking = Ranking.query.filter(or_(and_(Ranking.loserMovieId == firstMovie.id, Ranking.winnerMovieId == secondMovie.id), and_(Ranking.loserMovieId == secondMovie.id, Ranking.winnerMovieId == firstMovie.id))).all()
                if len(ranking) < 1:
                    break
    movies.append(firstMovie)
    movies.append(secondMovie)
    return movies

def getUniqueMoviesReank(movieId):
    firstMovie = Movie.query.filter(Movie.id == movieId).all()[0]
    movies = []
    while True:  
        secondMovie = getRandomRankdeMovie(movieId)
        if firstMovie.id != secondMovie.id: 
            break
    movies.append(firstMovie)
    movies.append(secondMovie)
    return movies

def getUniqueMoviesFromList(listId):
   #print("query")
    # SQL to find pairs of movies from the same list without a ranking relation
    # and considering only rankings where Ranking.overwriteRankingId is NULL
    sql = text("""
SELECT DISTINCT m1.id AS movie1_id, m2.id AS movie2_id
FROM movie m1
JOIN list_movie lm1 ON m1.id = lm1.movieId AND lm1.listId = :listId
JOIN movie m2 ON m1.id < m2.id
JOIN list_movie lm2 ON m2.id = lm2.movieId AND lm2.listId = :listId
WHERE m1.unwatched <> 1 AND m2.unwatched <> 1
AND NOT EXISTS (
    SELECT 1 FROM ranking r
    WHERE ((r.winnerMovieId = m1.id AND r.loserMovieId = m2.id) OR (r.winnerMovieId = m2.id AND r.loserMovieId = m1.id))
    AND r.overwriteRankingId IS NULL
)
LIMIT 1;
""")


   #print("query created")
    
    # Execute the SQL query
    result = db.engine.execute(sql, listId=listId).fetchone()

   #print("query ran")
    
    # If a result is found, retrieve the movie details
    if result:
        ##print("finding movies")
        movies = findMoviesByIdList([result['movie1_id'], result['movie2_id']])
        ##print("movies found")
        return movies
    else:
        # No valid pairs found
        return []


def getUniqueRankingForMovie(movieId):
    movies = []
    sql =  text("SELECT * FROM movie m1 \
                WHERE  \
                m1.unwatched <> 1  \
                and m1.id not in (SELECT loserMovieId FROM ranking r1 where winnerMovieId = " + str(movieId) + ") \
                and m1.id not in (SELECT winnerMovieId FROM ranking r1 where loserMovieId = " + str(movieId) + ") \
                and m1.id <> " + str(movieId) + "")
    rankings = db.engine.execute(sql)
    names = []
    for row in rankings:
        names.append(row[0]) #ids
    movies = findMoviesByIdList(names)
    if(len(movies)) < 1:
        return []
    secondMovie = random.choice(movies)
    return secondMovie

def getUniqueRankingStarForMovie(movieId):
    movies = []
    sql =  text("SELECT * FROM movie m1 \
                WHERE  \
                m1.unwatched <> 1  \
                and m1.stars <> 'None' and m1.stars is not NULL and m1.stars <> '' \
                and m1.id <> " + str(movieId) + "")
    rankings = db.engine.execute(sql)
    names = []
    for row in rankings:
        names.append(row[0]) #ids
    movies = findMoviesByIdList(names)
    if(len(movies)) < 1:
        return []
    secondMovie = random.choice(movies)
    return secondMovie

def getUniqueRankingStarForStarSpecificMovie(movieId, stars):
    movies = []
    sql =  text("SELECT * FROM movie m1 \
                WHERE  \
                m1.unwatched <> 1  \
                and m1.stars = " + str(stars) + " \
                and m1.id <> " + str(movieId) + "")
    rankings = db.engine.execute(sql)
    names = []
    for row in rankings:
        names.append(row[0]) #ids
    movies = findMoviesByIdList(names)
    if(len(movies)) < 1:
        return []
    secondMovie = random.choice(movies)
    return secondMovie

def getUniqueRankingStarForStarRangeSpecificMovie(movieId, stars):
    movies = []
    stars = float(stars)
    sql =  text("SELECT * FROM movie m1 \
                WHERE  \
                m1.unwatched <> 1  \
                and  (m1.stars = " + str(stars) +  " or m1.stars = " + str(stars - 0.5) + " or m1.stars = " + str(stars + 0.5) + ") \
                and m1.id <> " + str(movieId) + "")
    rankings = db.engine.execute(sql)
    names = []
    for row in rankings:
        names.append(row[0]) #ids
    movies = findMoviesByIdList(names)
    if(len(movies)) < 1:
        return []

    while len(movies) > 2:
        second = random.choice(movies)

        existing_ranking = Ranking.query.filter(
                (Ranking.winnerMovieId == movieId) & (Ranking.loserMovieId == second.id)|
                (Ranking.winnerMovieId == second.id) & (Ranking.loserMovieId == movieId)
            ).first()
        
        if not existing_ranking:
            return second
        else:
            movies.remove(second)
    return []

def getUniquieProximity(movieId):
    movie = Movie.query.filter(Movie.id == movieId).all()[0]

    

    movies = Movie.query.filter(and_(or_(text("stars is not NULL and stars <> 'None' and stars <> '' "), Movie.id == movieId), Movie.unwatched != 1)).all()
    index = movies.index(movie)
    size = len(movies)
    if index == size-2:
        return movies[index+1]
    while True:
        #randomly choose the distance from the first movie
        difference = random.randint(1, 20)
        #choose the direction
        up = random.choice([True, False])
        #find movie
        if (difference + index) < (size - 1):
            if up:
                return movies[index+difference]
            else:
                return movies[index-difference]

def getMovieGenreNamesWithCheck(movieId, genres):
    movieIdString = "("
    for x in genres:
        movieIdString = movieIdString + str(x.id) + ","
    movieIdString = movieIdString + "0)"
    textStr1 = 'genreId IN ' + movieIdString

    movieGenres = MovieGenre.query.filter(and_(MovieGenre.movieId == movieId, text(textStr1))).all()
    result = ""
    if(len(movieGenres) == 0 or movieGenres is None):
        return result
    
    else: 
        movieGenres = MovieGenre.query.filter(MovieGenre.movieId == movieId).all()
        firstGenre = Genre.query.filter(Genre.id == movieGenres[0].genreId).all()
        if len(firstGenre) > 0:
            result = firstGenre[0].name
        else:
            result = ""
        if len(movieGenres) > 1:
            secondGenre = Genre.query.filter(Genre.id == movieGenres[1].genreId).all()
            if len(secondGenre) > 0:
                result = result + " , " + secondGenre[0].name        
    return result

def deleteMovie(movieId):
    Movie.query.filter(Movie.id == movieId).delete()
    movieGenres = MovieGenre.query.filter(MovieGenre.movieId == movieId).all()
    for movieGenre in movieGenres:
        MovieGenre.query.filter(MovieGenre.id == movieGenre.id).delete()
    movieLogs = MovieWatch.query.filter(MovieWatch.movieId == movieId).all()
    for movieLog in movieLogs:
        MovieWatch.query.filter(MovieWatch.id == movieLog.id).delete() 
    movieLists = ListMovie.query.filter(ListMovie.movieId == movieId).all()
    for movieList in movieLists:
        ListMovie.query.filter(ListMovie.id == movieList.id).delete() 
    movieRankings = Ranking.query.filter(or_(Ranking.winnerMovieId == movieId, Ranking.loserMovieId == movieId)).all()
    for movieRanking in movieRankings:
        Ranking.query.filter(Ranking.id == movieRanking.id).delete()
    db.session.commit()

def deleteList(listId):
    ListMovie.query.filter(ListMovie.listId == listId).delete()
    List.query.filter(List.id == listId).delete()
    db.session.commit()

def findNumOfRanking(daterange):
    if daterange == 0:
        rankings = Ranking.query.filter(text('ranking.overwriteRankingId IS NULL')).count()
        return rankings
    
    if daterange == 1:
        rankings = Ranking.query.filter(and_(Ranking.modifiedDate >= date.today(), text('ranking.overwriteRankingId IS NULL'))).count()
        return rankings


    rankings = Ranking.query.filter(and_(Ranking.modifiedDate >= date.today() - timedelta(days=daterange), text('ranking.overwriteRankingId IS NULL'))).count()
    return rankings
    

def findNumOfMovies(daterange):
    logs = MovieWatch.query.filter(MovieWatch.watchDate >= date.today() - timedelta(days=daterange)).all()
    return len(logs)

def findNumOfMoviesWeek(daterange):
    logs = MovieWatch.query.filter(MovieWatch.watchDate > date.today() - timedelta(days=daterange)).all()
    return len(logs)

def findNumOfFirstWatchedMovies(daterange):
    logs = MovieWatch.query.filter(and_(MovieWatch.watchDate >= date.today() - timedelta(days=daterange), 
                                        MovieWatch.firstWatch == 1 
                                        )).all()
    return len(logs)

def findNumOfMoviesInWeek():
    today = date.today()
    subtraction = today.weekday() + ((7 if today.weekday() == 0 else 0))
    return findNumOfMovies(subtraction)

def findNumOfMoviesInMonth():
    today = date.today()

    # Calculate the first day of the current month
    first_day_of_month = date(today.year, today.month, 1)

    # Query to find movies watched from the first day of the month to today
    logs = MovieWatch.query.filter(MovieWatch.watchDate >= first_day_of_month).all()
    return len(logs)

def find_recently_watched_days(days):
    logs = MovieWatch.query.filter(MovieWatch.watchDate >= date.today() - timedelta(days=days)).order_by(desc(MovieWatch.watchDate)).all()
    movies = []
    for x in logs:
        movie = Movie.query.filter(Movie.id == x.movieId).all()
        movie[0].lastWatchedDate = x.watchDate
        movies.append(movie[0])
    return movies


def findNumOfWatchedMovies():
    rankings = Movie.query.filter(Movie.unwatched != 1).all()
    return len(rankings)

def findNumOfRewatchedMovies():
    rankings = Movie.query.filter(and_(Movie.rewatch == 1, Movie.unwatched != 1)).all()
    return len(rankings)

def findNumOfCurrentWatch():
    rankings = Movie.query.filter(Movie.currentlyWatching == 1).all()
    return len(rankings)

def findNumOfUnwatchedMovies():
    rankings = Movie.query.filter(Movie.unwatched == 1).all()
    return len(rankings)

def findNumOfMoviesToRecommend():
    sqlText = text("SELECT m1.* \
FROM movie m1 \
JOIN movie_watch mw ON m1.id = mw.movieId \
WHERE  \
    ( \
        (m1.recommend = 'None' OR LENGTH(m1.recommend) < 1) \
        OR \
        (m1.stars = 'None' OR LENGTH(m1.stars) < 1) \
                    OR (m1.liked <> 1 AND m1.liked <> 2 and m1.liked <> 3)      \
    ) and m1.rewatch <> 1 and m1.unwatched <> 1 \
ORDER BY mw.watchDate DESC \
")
    movies = db.engine.execute(sqlText)
    names = []
    for row in movies:
        names.append(row[0])

    return len(names)

def findNumOfMoviesToConfriM():
    logs = MovieWatch.query.filter(
                                        MovieWatch.confirmedStars != 1
                                        ).order_by(text("watchDate desc, id desc")).all()
    
    return len(logs)


def findmoviesToRecommend():
    sqlText = text("SELECT m1.* \
FROM movie m1 \
JOIN movie_watch mw ON m1.id = mw.movieId \
WHERE  \
    ( \
        (m1.recommend = 'None' OR LENGTH(m1.recommend) < 1) \
        OR \
        (m1.stars = 'None' OR LENGTH(m1.stars) < 1) \
              OR (m1.liked <> 1 AND m1.liked <> 2 and m1.liked <> 3)      \
    ) AND m1.rewatch <> 1 and m1.unwatched <> 1 \
ORDER BY mw.watchDate DESC \
")
    movies = db.engine.execute(sqlText)
    names = []
    for row in movies:
        names.append(row[0])

    result = findMoviesByIdList(names)

    return result 



def findUniqueMovieRankings():
    rankings = Ranking.query.filter(text('ranking.overwriteRankingId IS NULL')).all()
    return len(rankings)


def findMoviesWithHighestWins(daterange):
    sql = text('SELECT movie.id, movie.title, \
                (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as Wins, \
                (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as loseses, \
                ( (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') -  (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') ) as difference, \
                (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as totals, \
                (100 * (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE (ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')  / (SELECT COUNT(winnerMovieId) as Total \
                FROM ranking WHERE (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')) as percent \
                FROM movie  \
                ORDER BY ( (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') -  (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') ) desc, percent desc LIMIT 8')
    rankings = db.engine.execute(sql)
    names = []
    winsCount = []
    totalsCount = []
    differenceCount = []
    for row in rankings:
        names.append(row[0]) #ids
        winsCount.append(row[2])  #wins 
        differenceCount.append(row[4])  #difference 
        totalsCount.append(row[5]) # total
    movies = findMoviesByIdList(names)
    counter = 0
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
        x.winsGained = differenceCount[counter]
        x.cinematicScore = totalsCount[counter]
        x.rankingWinCount = winsCount[counter]
        counter = counter + 1
    return movies


def findMoviesWithMostPointsGained(daterange):
    sql = text(' SELECT \
	movie.id, \
	movie.title, \
	(SELECT SUM(ranking.winnerPointsGained) as PointsGained FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as PointsGained, \
	(SELECT SUM(ranking.loserPointsLossed) as PointsLossed FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as PointsLossed, \
    ((SELECT SUM(ranking.winnerPointsGained) as PointsGained FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') - (SELECT SUM(ranking.loserPointsLossed) as PointsLossed FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + '))  as PointsDifference \
	 FROM movie \
     WHERE ((SELECT SUM(ranking.winnerPointsGained) as PointsGained FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') - (SELECT SUM(ranking.loserPointsLossed) as PointsLossed FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')) > 0 \
	 ORDER BY ((SELECT SUM(ranking.winnerPointsGained) as PointsGained FROM ranking WHERE ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') - (SELECT SUM(ranking.loserPointsLossed) as PointsLossed FROM ranking WHERE ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')) desc \
	 LIMIT 8')
    rankings = db.engine.execute(sql)
    names = []
    winsCount = []
    for row in rankings:
        names.append(row[0])
        winsCount.append(row[2])
    movies = findMoviesByIdList(names)
    counter = 0
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
        x.pointsGained = int(winsCount[counter])
        counter = counter + 1
    return movies

# def findMoviesWithLargestUpset():
#     rankings = Ranking.query.filter()

def findMoviesWithHighestWinPercentage(daterange, minimumRankings):
    # sql = text('SELECT movie.id,\
    #             (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.overwriteRankingId IS NULL and  ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as Wins, \
    #             (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as totals, \
    #             (100 * (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')  / (SELECT COUNT(winnerMovieId) as Total \
    #             FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')) as percent \
    #             FROM movie  \
    #             WHERE unwatched <> 1 and  (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') > ' + str(3) + '  \
    #             ORDER BY percent desc, Wins desc  LIMIT 20')
    sql = text('SELECT movie.id,\
                (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.overwriteRankingId IS NULL and  ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as Wins, \
                (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as totals, \
                (100 * (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')  / (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')) as percent \
                FROM movie  \
                WHERE unwatched <> 1 and totals >= ' + str(minimumRankings) + '  \
                ORDER BY percent desc, Wins desc  LIMIT 30')
    rankings = db.engine.execute(sql)
    movies = []
    for row in rankings:
        movie = Movie.query.filter(Movie.id == row[0]).all()[0]
        movie.winsGained = row[3]
        movie.cinematicScore = row[2]
        movie.rankingWinCount = row[1]
        movies.append(movie)
    return movies

def getListsForMovie(movieId):
    listIds = ListMovie.query.filter(ListMovie.movieId == movieId).all()
    lists = []
    for listId in listIds:
        list = List.query.filter(List.id == listId.listId).all()
        if len(list) > 0:
            lists.append(list[0])
    return lists

def getRankingStartDate():
    ranking = Ranking.query.filter().order_by(Ranking.modifiedDate).first()
    return ranking


def findMoviesForMonth(daterange):
    #get the average times each movie has been ranked in some date range
    sql1 = text('SELECT movie.id, movie.title, \
                (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as totals \
                FROM movie \
                WHERE (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') > 0  \
                ORDER BY totals desc')
    rankings1 = db.engine.execute(sql1)
    countOfTotals = []
    for row in rankings1:
        countOfTotals.append(row[2])  #times it has been ranked
    # have the minumum amount of rank be the mean (want to remove the bottom 60%)


    mean = math.ceil(statistics.mean(countOfTotals)) + 1

    result = math.ceil(mean)

    sql = text('SELECT movie.id, movie.title, \
                (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.overwriteRankingId IS NULL and   ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as Wins, \
                (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.overwriteRankingId IS NULL and ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as loseses, \
                ( (SELECT COUNT(winnerMovieId) as Wins FROM ranking WHERE ranking.overwriteRankingId IS NULL and ranking.winnerMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') -  (SELECT COUNT(loserMovieId) as Losess FROM ranking WHERE ranking.overwriteRankingId IS NULL and ranking.loserMovieId = movie.id and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') ) as difference, \
                (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') as totals, \
                (100 * (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')  / (SELECT COUNT(winnerMovieId) as Total \
                FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ')) as percent \
                FROM movie  \
                WHERE (SELECT COUNT(winnerMovieId) as Total FROM ranking WHERE ranking.overwriteRankingId IS NULL and (ranking.loserMovieId = movie.id or ranking.winnerMovieId = movie.id) and julianday(\'now\') - julianday(ranking.modifiedDate) < ' + str(daterange) + ') > ' + str(result) + '  \
                ORDER BY percent desc, Wins desc  LIMIT 20')
    rankings = db.engine.execute(sql)
    names = []
    winsCount = []
    totalsCount = []
    differenceCount = []
    for row in rankings:
        names.append(row[0]) #ids
        winsCount.append(row[2])  #wins 
        differenceCount.append(row[6])  #difference 
        totalsCount.append(row[5]) # total
    movies = findMoviesByIdList(names)
    counter = 0
    for x in movies:
        x.genres = getMovieGenreNames(x.id)
        x.rank = differenceCount[counter]
        x.cinematicCount = totalsCount[counter]
        x.rankingPercentage = winsCount[counter]
        counter = counter + 1
    return movies


def findMoviesByIdList(ids):
    rankings = []
    for x in ids:
        movie = Movie.query.filter(Movie.id == x).all()
        rankings.append(movie[0])
    return rankings

def getProximityMovie():
    movies = find_movies_all()
    result = []
    
    size = len(movies)
    index = random.randint(0, size-2)
    #get first movie
    result.append(movies[index])
    if index == size-2:
        result.append(movies[index+1])
        return result
    while True:
        #randomly choose the distance from the first movie
        difference = random.randint(1, 10)
        #choose the direction
        up = random.choice([True, False])
        #find movie
        if (difference + index) < (size - 1):
            if up:
                result.append(movies[index+difference])
            else:
                result.append(movies[index-difference])
            break
    return result

def getLikedMovies():
    movies = Movie.query.filter(and_(Movie.unwatched != 1, Movie.rewatch != 1, Movie.liked == 1)).all()
    result = []
    if len(movies) < 2:
        return []
    
    while True:
        first = random.choice(movies)
        second = random.choice(movies)

        existing_ranking = Ranking.query.filter(
                (Ranking.winnerMovieId == first.id) & (Ranking.loserMovieId == second.id)|
                (Ranking.winnerMovieId == second.id) & (Ranking.loserMovieId == first.id)
            ).first()
        
        if not existing_ranking:
            result.append(random.choice(movies))
            result.append(random.choice(movies))
            break
    return result

def getunlikedMovies():
    movies = Movie.query.filter(and_(Movie.unwatched != 1, Movie.liked == 3)).all()
    result = []

    result.append(random.choice(movies))
    result.append(random.choice(movies))

    return result

def getmidMovies():
    movies = Movie.query.filter(and_(Movie.unwatched != 1, Movie.liked == 2)).all()
    result = []

    result.append(random.choice(movies))
    result.append(random.choice(movies))

    return result


def getLastRanking():
    # rankings = Ranking.query.order_by(desc(Ranking.modifiedDate)).all()

    # lastRanked = rankings[0]
    lastRanked = Ranking.query.order_by(desc(Ranking.modifiedDate)).first()

    winner = Movie.query.filter(Movie.id == lastRanked.winnerMovieId).all()[0]
    loser = Movie.query.filter(Movie.id == lastRanked.loserMovieId).all()[0]

    checked = lastRanked.flagged

    result = []
    result.append(winner)
    result.append(loser)
    result.append(checked)

    return result

def reverseLastRank():
    lastRanked = Ranking.query.order_by(desc(Ranking.modifiedDate)).first()

    lastRanked.overwriteRankingId = lastRanked.id + 1
    lastRanked.reversed = True

    newLoser = Movie.query.filter(Movie.id == lastRanked.winnerMovieId).all()[0]
    newWinner = Movie.query.filter(Movie.id == lastRanked.loserMovieId).all()[0]

    Pb =  Probability(lastRanked.loserStartingPoints, lastRanked.winnerStartingPoints)
    Pa =  Probability(lastRanked.winnerStartingPoints, lastRanked.loserStartingPoints)
    Ra = int(lastRanked.loserStartingPoints + 50 * (1 - Pa))
    Rb = int(lastRanked.winnerStartingPoints + 50 * (0 - Pb))

    ranking = Ranking(winnerMovieId=newWinner.id, loserMovieId=newLoser.id, modifiedDate=func.now(), winnerStartingPoints=lastRanked.loserStartingPoints, loserStartingPoints=lastRanked.winnerStartingPoints, 
                      winnerPointsGained=50 * (1 - Pa), loserPointsLossed=50 * (0 - Pb), winnerEndingPoints=Ra, losserEndingPoints=Rb, winnerCount=newWinner.rewatchCount, loserCount=newLoser.rewatchCount)
    
    newWinner.rewatchScore = Ra
    if newWinner.rankingWinCount is None:
        newWinner.rankingWinCount = 0
    newWinner.rankingWinCount = newWinner.rankingWinCount + 1
    newWinner.rankingPercentage = round(newWinner.rankingWinCount / newWinner.rewatchCount * 100)

    newLoser.rewatchScore = Rb
    newLoser.rankingWinCount = newLoser.rankingWinCount - 1
    newLoser.rankingPercentage = round(newLoser.rankingWinCount / newLoser.rewatchCount * 100)

    ranking = checkFlag(newWinner, newLoser, ranking)

    db.session.add(ranking)
    db.session.commit()

def findNumOfFlaggedRankings():
    flaggedRankings = Ranking.query.filter(and_(Ranking.flagged == 1, text('overwriteRankingId IS NULL'))).order_by(desc(Ranking.modifiedDate)).all()

    return len(flaggedRankings)

def findNumOfupset():
    flaggedRankings = Ranking.query.filter(and_(Ranking.likeUpset == 1, text('overwriteRankingId IS NULL'))).order_by(desc(Ranking.modifiedDate)).all()

    return len(flaggedRankings)

def findNumOfSkippedRankings():
    flaggedRankings = SharedRanking.query.filter().all()

    return len(flaggedRankings)

def reverseFlaggedRanking(rankingId):
    lastRanked = Ranking.query.order_by(desc(Ranking.modifiedDate)).first()

    lastRanked.overwriteRankingId = lastRanked.id + 1
    lastRanked.reversed = True

    newLoser = Movie.query.filter(Movie.id == lastRanked.winnerMovieId).all()[0]
    newWinner = Movie.query.filter(Movie.id == lastRanked.loserMovieId).all()[0]

    Pb =  Probability(lastRanked.loserStartingPoints, lastRanked.winnerStartingPoints)
    Pa =  Probability(lastRanked.winnerStartingPoints, lastRanked.loserStartingPoints)
    Ra = int(lastRanked.loserStartingPoints + 50 * (1 - Pa))
    Rb = int(lastRanked.winnerStartingPoints + 50 * (0 - Pb))

    ranking = Ranking(winnerMovieId=newWinner.id, loserMovieId=newLoser.id, modifiedDate=func.now(), winnerStartingPoints=lastRanked.loserStartingPoints, loserStartingPoints=lastRanked.winnerStartingPoints, 
                      winnerPointsGained=50 * (1 - Pa), loserPointsLossed=50 * (0 - Pb), winnerEndingPoints=Ra, losserEndingPoints=Rb, winnerCount=newWinner.rewatchCount, loserCount=newLoser.rewatchCount)
    
    newWinner.rewatchScore = Ra
    if newWinner.rankingWinCount is None:
        newWinner.rankingWinCount = 0
    newWinner.rankingWinCount = newWinner.rankingWinCount + 1
    newWinner.rankingPercentage = round(newWinner.rankingWinCount / newWinner.rewatchCount * 100)

    newLoser.rewatchScore = Rb
    newLoser.rankingWinCount = newLoser.rankingWinCount - 1
    newLoser.rankingPercentage = round(newLoser.rankingWinCount / newLoser.rewatchCount * 100)

    ranking = checkFlag(newWinner, newLoser, ranking)

    db.session.add(ranking)
    db.session.commit()

