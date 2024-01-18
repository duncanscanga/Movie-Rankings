from flask import render_template, redirect, request, session, url_for
import os
from app.models import addMoviesToListRandom, autoRank, autoRankCertain, autoRankList, checkNotLastRanked, createListWithRandomMovies, currentWatchStreak, currentlyWatching, deleteList, duplicateList, find_all_movies_to_watch, find_all_unwatched_filtered_movies, find_all_unwatched_movies, find_all_watched_filtered_movies, find_all_watched_movies, find_best_movies_by_win_percentage, find_current_watch_movies, find_filtered_currently_movies, find_filtered_movies_by_win_percentage, find_filtered_movies_first_logged, find_filtered_movies_forRanking, find_movies_by_genre_filter, find_recently_watched_days, findHourCountAll, findHourCountThisYear, findMoviesForMonth, findMoviesWithHighestWinPercentage, findNumOfCurrentWatch, findNumOfFirstWatchedMovies, findNumOfFlaggedRankings, findNumOfMoviesInMonth, findNumOfMoviesInWeek, findNumOfMoviesToRecommend, findNumOfMoviesWeek, findNumOfReversedMovies, findNumOfSkippedRankings, findNumOfupset, findUniqueMovieRankings, findmoviesToRecommend, getBestOfEachYear, getBiggestUpsets, getClosestRankings, getFlaggedRankings, getLatestSession, getLikedMovies, getListOfYears, getListsForMovie, getListsOfPeople, getMoviesRankedInSession, getRankOfRecentMovies, getRankingStartDate, getRankingsInList, getRecentRankings, getRecommendedMovies, getSharedRankings, getTimesRankedString, getTimesWatched, getTopMoviesInRankingSession, getUniqueMovies, getUniqueMoviesFromList, getUniqueMoviesReank, getUniqueRankingForMovie, getUniquieProximity, getUnwatchedMoviesFromList, getUpsets, getUpsetsRankings, getmidMovies, getunlikedMovies, isOpenSession, longestWatchStreak, misLikedUosetLoserss, misLikedUosets, predictStars, removeCurrentWatch, removeFlagFromRanking, removeSharedMovie, reverseFlaggedRanking, saveForLater, saveRanking, removeSavedRanking,  add_list, addMovieToList, find_all_filtered_movies_without, find_all_movies_without, find_filtered_movies_logged, find_list_by_id, getAllLists, getListDetails, getListDetailsFromNAme, getListPeople, getMovieLog, getMovieWatches, getMoviesFromList, getPerson, getRandomMovieByList, log_movie, findNumOfRewatchedMovies, removeMovieFromList, reverseLastRank, getLastRanking,  getRankings, getPlusMinusMovies,  getMovieDetails, findMoviesWithMostPointsGained, findMoviesWithHighestWins, findNumOfWatchedMovies, findNumOfUnwatchedMovies, findNumOfMovies, findNumOfRanking, find_filtered_rewatched_movies, find_filtered_unwatched_movies, find_all_movies,  find_filtered_movies_by_stars, find_filtered_movies, filterRecentWatched, getRandomUnrankedMovie, getRandomRecentMovie, find_best_movies,  find_recently_watched, getMovieGenres, find_top_movies, getProximityMovie, deleteMovie, startedSession, top_directors, top_movie_from_year, top_movie_from_year_ordered, unloggedMovies, update_list, update_log, update_movie, find_unwatched_movies, unRewatchMovie, rewatchMovie, getRandomMovie, updateLiked, updateRankings, getMovieById, find_rewatch_movies, find_genres, find_movies_by_genre, updateMovie, find_genres_by_id, getRandomMovieByGenre, add_movie
from babel.dates import format_date, format_datetime, format_time
from app import app
import random
from datetime import date, datetime, timedelta
from flask import jsonify

@app.route('/trending')
def trending():
    minMovies = 3
    hottestMovies = findMoviesWithHighestWinPercentage(1, minMovies)
    biggestUpsets = getBiggestUpsets()
    closestRankings = getClosestRankings()
    return render_template('index-trending.html', closestRankings=closestRankings, hottestMovies=hottestMovies, biggestUpsets=biggestUpsets, minMovies=minMovies)

@app.route('/wins')
def ranking_by_win_percentage():
    movies = find_best_movies_by_win_percentage()
    for x in movies:
        if x.lastWatchedDate is not None:
            x.lastWatchedDate = format_date(x.lastWatchedDate, locale='en')
    return render_template('ranking-by-wins.html', genres="", stars=0, movies = movies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/wins', methods=['POST'])
def ranking_by_win_percentage_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    stars = request.form.get('stars')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_filtered_movies_by_win_percentage(title, director, year, min, max, recommendation, genres, stars)
    return render_template('ranking-by-wins.html', stars=stars, genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)





@app.route('/trending' , methods=['POST'])
def trending_tranding():
    minMovies = request.form.get('minMovies')
    if minMovies == None or  len(minMovies) < 1:
        minMovies = 3
    else:
        minMovies = int(minMovies)
    closestRankings = getClosestRankings()
    biggestUpsets = getBiggestUpsets()
    hottestMovies = findMoviesWithHighestWinPercentage(1, minMovies)

    return render_template('index-trending.html', closestRankings=closestRankings, hottestMovies=hottestMovies, biggestUpsets=biggestUpsets, minMovies=minMovies)

@app.route('/flagged')
def flaggedMovies():
    rankings = getFlaggedRankings()

    return render_template('flagged.html', flagged=rankings)

@app.route('/upsets')
def likeUpset():
    result = misLikedUosets()
    return render_template('upsets.html', movies=result)

@app.route('/upsets-losers')
def likeloserUpset():
    result = misLikedUosetLoserss()
    return render_template('upsets-losers.html', movies=result)

@app.route('/skipped')
def sharedMovies():
    rankings = getSharedRankings()

    return render_template('shared.html', flagged=rankings)

@app.route('/best-of-year')
def bestOfYear():
    result = top_movie_from_year()
    combined = zip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11])  # Combine names and points into tuples
    return render_template('best-of-year.html', combined_list=list(combined))

@app.route('/best-of-year-ordered')
def bestOfYearOrdered():
    result = top_movie_from_year_ordered()
    combined = zip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11])  # Combine names and points into tuples
    return render_template('best-of-year-ordered.html', combined_list=list(combined))

@app.route('/best-directors')
def bestDirector():
    result = top_directors()
    combined = zip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11])  # Combine names and points into tuples
    return render_template('best-directors.html', combined_list=list(combined))


@app.route('/recent-movie-ranks')
def recentMovieRanks():
    logs = getRankOfRecentMovies(3)
    movies = []
    for log in logs:
        movie = getMovieById(log.movieId)
        movie.location = format_date(log.watchDate, locale='en')
        movies.append(movie)

    first = getPlusMinusMovies(movies[0].id)
    second = getPlusMinusMovies(movies[1].id)
    third = getPlusMinusMovies(movies[2].id)

    result = []

    result.append(first)
    result.append(second)
    result.append(third)


    return render_template('recent-watch-ranks.html', movies=movies, result=result)


@app.route('/view-rankings')
def recentViewRankingNoTpOst():
    rankings = getRecentRankings()

    return render_template('recent-rankings.html', flagged=rankings)

@app.route('/removeFlag/<int:ranking_id>')
def removeFlag(ranking_id):
    removeFlagFromRanking(ranking_id)

    return redirect(request.referrer or '/')

@app.route('/removeFlagUpset/<int:ranking_id>')
def removeFlagUpset(ranking_id):
    removeFlagFromRanking(ranking_id)

    return redirect('/upsets')


@app.route('/removeShared/<int:ranking_id>/<int:winner_id>')
def removeShared(ranking_id, winner_id):
    removeSharedMovie(ranking_id, winner_id)
    return redirect('/skipped')

@app.route('/confirm/<int:ranking_id>')
def confirmFLag(ranking_id):
    removeFlagFromRanking(ranking_id)

    return redirect('/view-rankings')

@app.route('/share/<int:first_id>/<int:second_id>')
def sharedRanking(first_id, second_id):
    saveForLater(first_id, second_id)

    return redirect(request.referrer or '/')
    #return ('',204)

@app.route('/reverseFlaggedRanking/<int:ranking_id>')
def reverseeFlag(ranking_id):
    reverseFlaggedRanking(ranking_id)

    return redirect(request.referrer or '/')


@app.route('/reverseTrendingRanking/<int:ranking_id>')
def reverseTrendingRanking(ranking_id):
    reverseFlaggedRanking(ranking_id)

    return redirect('/trending')

@app.route('/reverseViewRanking/<int:ranking_id>')
def reverseeFlagNiot(ranking_id):
    reverseFlaggedRanking(ranking_id)

    return redirect('/view-rankings')

@app.route('/')
def home():
    movies = []
    rankingCountMonth = findNumOfRanking(30)
    rankingCountTotal = findNumOfRanking(0)
    rankingCountToday = findNumOfRanking(1)
    # movies watched this week
    weeklySubtraction = date.today().weekday()
    moviesWatchedInWeek = findNumOfMovies(weeklySubtraction)
    # movies watched this month
    monthlySubtraction = date.today().day - 1
    moviesWatchedInMonth = findNumOfMovies(monthlySubtraction)
    # movies watched this year
    yearlySubtraction = date.today().timetuple().tm_yday - 1
    moviesWatchedInYear = findNumOfMovies(yearlySubtraction)
    # first watches this year
    firstmoviesWatchedInYear = findNumOfFirstWatchedMovies(yearlySubtraction)
    moviesWatched = findNumOfWatchedMovies()
    rewatched = findNumOfRewatchedMovies()
    unwatched = findNumOfUnwatchedMovies()
    unrated = findNumOfMoviesToRecommend()
    currentWatch = findNumOfCurrentWatch()
    flaggedRankings = findNumOfFlaggedRankings()
    skippedRankings =  findNumOfSkippedRankings()
    longestWatchStreakResult = longestWatchStreak()
    currentWatchStreakResult = currentWatchStreak()
    #totalMinutes = findHourCountAll()
    totalMinutes = findHourCountThisYear(yearlySubtraction)
    #months = int(totalMinutes / 43200)
    if totalMinutes is None:
        totalMinutes = 0
    days = int(totalMinutes / 1440)
    hours = int(totalMinutes % 1440 / 60)
    minutes = int(totalMinutes % 1440 % 60)
    hourCount1 =  '{:02d} days, {:02d} hours and {:02d} minutes'.format(days, hours, minutes)
    creationDate = format_date(datetime(2022, 8, 9), locale='en')
    uniqueCount = rankingCountTotal
    averageCount = int (uniqueCount/moviesWatched)
    moviesToRank = int((moviesWatched-1)*moviesWatched)
    percentDone = int( uniqueCount / moviesToRank * 100 ) 
    rankingStartDate = getRankingStartDate()
    daysRanked = (datetime.today() - rankingStartDate.modifiedDate).days
    averageRankingPerDay = int(uniqueCount/daysRanked)
    daysUntilEquilibirum = int((moviesToRank- uniqueCount)/averageRankingPerDay)
    end_date = format_date(datetime.today() + timedelta(days=daysUntilEquilibirum), locale='en')
    if yearlySubtraction == 0:
        howOftenIWatch = 0
    else:
        howOftenIWatch = int(moviesWatchedInYear / (yearlySubtraction / 7))
    reversedRankings = findNumOfReversedMovies()

    return render_template('index.html',currentWatchStreak=currentWatchStreakResult[0], currentWatchStreakResultEnd=currentWatchStreakResult[1], currentWatchStreakResultDays=currentWatchStreakResult[2], longestWatchStreak=longestWatchStreakResult[0], longestWatchStreakEnd=longestWatchStreakResult[1],longestWatchStreakDays=longestWatchStreakResult[2] , unrated=unrated, firstmoviesWatchedInYear=firstmoviesWatchedInYear, monthlySubtraction=monthlySubtraction, yearlySubtraction=yearlySubtraction, weeklySubtraction=weeklySubtraction, skippedRankings=skippedRankings, reversedRankings=f'{reversedRankings:,}', daysRanked=daysRanked, flaggedRankings=flaggedRankings, howOftenIWatch=howOftenIWatch, end_date=end_date, percentDone=percentDone, averageRankingPerDay=averageRankingPerDay, averageCount=averageCount, hourCount1=hourCount1, uniqueCount=uniqueCount, creationDate=creationDate, rankingCountToday=f'{rankingCountToday:,}', currentWatch=currentWatch, movies = movies, rewatched= rewatched, rankingCountTotal = f'{rankingCountTotal:,}', rankingCountMonth = f'{rankingCountMonth:,}', moviesWatchedInWeek = moviesWatchedInWeek, moviesWatchedInMonth = moviesWatchedInMonth, moviesWatchedInYear = moviesWatchedInYear, moviesWatched = moviesWatched, unwatched = unwatched )



@app.route('/rank-all', methods=['GET'])
def rank_all():
    while True:
        firstMovie = getRandomMovie()
        secondMovie = getRandomMovie()
        if firstMovie.title != secondMovie.title:
            break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-all.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

@app.route('/update-rankings/<int:winner_id>/<int:loser_id>/<int:movie_id>', methods=['GET'])
def rank_by_movie_post(winner_id, loser_id, movie_id):
    updateRankings(winner_id, loser_id, False)
    # while True:
    #     firstMovie = getMovieById(movie_id)   
    #     secondMovie = getRandomMovie()
    #     if firstMovie.title != secondMovie.title:
    #         break
    # start = "/static/images/movieposters/"
    # first = start + firstMovie.poster
    # second = start + secondMovie.poster
    # return render_template('rank-by-movie.html', firstMovie = firstMovie, 
    #                        secondMovie = secondMovie, first=first, second = second)
    urlBuild = '/rank-by-movie/' + str(movie_id)
    return redirect(urlBuild)

@app.route('/update-rankings-unique/<int:winner_id>/<int:loser_id>/<int:movie_id>', methods=['GET'])
def rank_by_movie_post_unqiue(winner_id, loser_id, movie_id):
    updateRankings(winner_id, loser_id, False)
    urlBuild = '/rank-by-movie-unique/' + str(movie_id)
    return redirect(urlBuild)


@app.route('/update-rankings-close/<int:winner_id>/<int:loser_id>/<int:movie_id>', methods=['GET'])
def rank_by_movie_post_close(winner_id, loser_id, movie_id):
    updateRankings(winner_id, loser_id, False)
    urlBuild = '/rank-by-close/' + str(movie_id)
    return redirect(urlBuild)


@app.route('/update-rankings/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_all_post(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    # while True:
    #     firstMovie = getRandomMovie()
    #     secondMovie = getRandomMovie()
    #     if firstMovie.title != secondMovie.title:
    #         break
    # start = "/static/images/movieposters/"
    # first = start + firstMovie.poster
    # second = start + secondMovie.poster
    # return render_template('rank-all.html', firstMovie = firstMovie, 
    #                        secondMovie = secondMovie, first=first, second = second)
    return redirect('/rank-all')


@app.route('/rank-by-movie/<string:movie_id>', methods=['GET'])
def rank_by_movie(movie_id):
    while True:
        firstMovie = getMovieById(movie_id)   
        secondMovie = getRandomMovie()
        if firstMovie.title != secondMovie.title:
            if checkNotLastRanked(firstMovie.id, secondMovie.id):
                break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-movie.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

@app.route('/rank-by-movie-unique/<string:movie_id>', methods=['GET'])
def rank_by_movie_unique(movie_id):
    while True:
        firstMovie = getMovieById(movie_id)   
        if firstMovie.rewatchCount >=  (findNumOfWatchedMovies() - 1):
            return ('',204)
        secondMovie = getUniqueRankingForMovie(movie_id)
        if secondMovie == []:
            return ('',204)
        if firstMovie.title != secondMovie.title:
            break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-movie-unique.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


@app.route('/rank-by-close/<string:movie_id>', methods=['GET'])
def rank_by_mclose_unique(movie_id):
    while True:
        firstMovie = getMovieById(movie_id)   
        if firstMovie.rewatchCount >=  (findNumOfWatchedMovies() - 1):
            return ('',204)
        secondMovie = getUniquieProximity(movie_id)
        if secondMovie == []:
            return ('',204)
        if firstMovie.title != secondMovie.title:
            if checkNotLastRanked(firstMovie.id, secondMovie.id):
                    break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-close.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)



@app.route('/all-movies-without-posters')
def all_movies():
    movies = find_all_watched_movies()
    unwatchedMovies = find_all_unwatched_movies()
    return render_template('all-movies.html', movies = movies, unwatchedMovies=unwatchedMovies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/all-movies/<string:director>', methods=['GET'])
def all_movies_director(director):
    movies = find_all_watched_filtered_movies("", director, "", 0, 0, "", "")
    unwatchedMovies = find_all_unwatched_filtered_movies("", director, "", 0, 0, "", "")
    return render_template('all-movies-with-posters.html', unwatchedMovies=unwatchedMovies, genres="", movies = movies, originalTitle="", originalDirector=director, originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/all-movies/<string:director>', methods=['POST'])
def all_movies_director_post(director):
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_all_watched_filtered_movies(title, director, year, min, max, recommendation, genres)
    unwatchedMovies = find_all_unwatched_filtered_movies(title, director, year, min, max, recommendation, genres)
    return render_template('all-movies-with-posters.html', unwatchedMovies=unwatchedMovies, genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)
 
@app.route('/all-movies-year/<string:year>', methods=['GET'])
def all_movies_year(year):
    movies = find_all_watched_filtered_movies("", "", year, 0, 0, "", "")
    unwatchedMovies = find_all_unwatched_filtered_movies("", "", year, 0, 0, "", "")
    return render_template('all-movies-with-posters.html',unwatchedMovies=unwatchedMovies, genres="", movies = movies, originalTitle="", originalDirector="", originalYear=year, originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/all-movies-year/<string:year>', methods=['POST'])
def all_movies_year_post(year):
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_all_watched_filtered_movies(title, director, year, min, max, recommendation, genres)
    unwatchedMovies = find_all_unwatched_filtered_movies(title, director, year, min, max, recommendation, genres)
    return render_template('all-movies-with-posters.html', genres=genres, unwatchedMovies=unwatchedMovies, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)



@app.route('/all-movies-without-posters', methods=['POST'])
def all_movies_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_all_watched_filtered_movies(title, director, year, min, max, recommendation, genres)
    unwatchedMovies = find_all_unwatched_filtered_movies(title, director, year, min, max, recommendation, genres)
    return render_template('all-movies.html', unwatchedMovies=unwatchedMovies, genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)

@app.route('/all-movies', methods=['POST'])
def all_movies_with_posters_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_all_watched_filtered_movies(title, director, year, min, max, recommendation, genres)
    unwatchedMovies = find_all_unwatched_filtered_movies(title, director, year, min, max, recommendation, genres)
    return render_template('all-movies-with-posters.html', unwatchedMovies=unwatchedMovies, genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)


@app.route('/all-movies')
def all_movies_with_posters():
    #movies = find_all_movies()
    return render_template('all-movies-with-posters.html', movies = [], originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/movie-finder', methods=['POST'])
def finder_movies_with_posters_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    watchedBefore = request.form.get('watchedBefore')
    if watchedBefore == None:
        watchedBefore = 0
    else:
        watchedBefore = 1
    listView = request.form.get('listView')
    if listView == None:
            listView = 0
    else:
        listView = 1

    movies = find_all_movies_to_watch(title, director, year, min, max, recommendation, watchedBefore, genres, listView)

    if listView:
        return render_template('movie-finder.html', genres=genres, listView=listView, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation, watchedBefore=watchedBefore)

    if movies is None or len(movies) < 1:
         return render_template('movie-finder.html', genres=genres, listView=listView, movies = [], originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation, watchedBefore=watchedBefore)
    
    unwatched = "No"
    if movies[0].unwatched == 1:
        unwatched = "Yes"

    rewatch = "No"
    if movies[0].rewatch == 1:
        rewatch = "Yes"

    
    movies[0].timesWatched = getTimesWatched(movies[0].id)
    return render_template('movie-generator.html', rewatch=rewatch, unwatched=unwatched, genres=genres, listView=listView, movie = movies[0], originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation, watchedBefore=watchedBefore)



@app.route('/movie-finder')
def finder_movies_with_posters():
    #movies = find_all_movies()
    return render_template('movie-finder.html', movies = [], genres="", originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")




@app.route('/unwatched-without-posters')
def unwatched():
    movies = find_unwatched_movies()
    return render_template('unwatched.html', movies = movies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")


@app.route('/unwatched-without-posters', methods=['POST'])
def unwatched_movies_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    # recommendation = request.form.get('recommendation').strip()
    movies = find_filtered_unwatched_movies(title, director, year, min, max, "", "")
    return render_template('unwatched.html', movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation="")

@app.route('/unwatched', methods=['POST'])
def unwatched_poster_movies_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    # recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_filtered_unwatched_movies(title, director, year, min, max, "", genres)
    return render_template('unwatched-with-poster.html', genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation="")

@app.route('/rewatch-without-posters')
def rewatch():
    movies = find_rewatch_movies()
    return render_template('rewatch.html', movies = movies , originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/rewatch')
def rewatch_with_posters():
    movies = find_rewatch_movies()
    return render_template('rewatch-with-posters.html', genres="", movies = movies , originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/currently-watching')
def currently_watching_with_posters():
    movies = find_current_watch_movies()
    return render_template('currently-watching.html', genres="", movies = movies , originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/currently-watching', methods=['POST'])
def currently_watching_with_posters_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    genres = request.form.get('genres').strip()
    movies = find_filtered_currently_movies(title, director, year, min, max, "", genres)
    return render_template('currently-watching.html', genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation="")



@app.route('/rewatch', methods=['POST'])
def rewatched_poster_movies_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_filtered_rewatched_movies(title, director, year, min, max, recommendation, genres)
    return render_template('rewatch-with-posters.html', genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)


@app.route('/rewatch-without-posters', methods=['POST'])
def rewatched_movies_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    movies = find_filtered_rewatched_movies(title, director, year, min, max, recommendation, genres)
    return render_template('rewatch.html', movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)





@app.route('/unwatched')
def unwatched_with_poster():
    movies = find_unwatched_movies()
    return render_template('unwatched-with-poster.html', genres="", movies = movies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")



@app.route('/rankings-without-posters')
def movies():
    movies = find_top_movies(0)
    return render_template('rankings.html', movies = movies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/rankings-without-posters', methods=['POST'])
def movies_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    movies = find_filtered_movies(title, director, year, min, max, recommendation, "")
    return render_template('rankings.html', movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)

@app.route('/first-logs', methods=['POST'])
def logforsts_post():
    title = request.form.get('title').strip()
    location = request.form.get('location').strip()
    people = request.form.get('people').strip()
    notes = request.form.get('notes').strip()
    start = request.form.get('start')
    end = request.form.get('end')
    # movies = request.form.get('movies').strip()
    # directors = request.form.get('directors').strip()
    # start = request.form.get('start')
    # end = request.form.get('end')
    # movies = find_filtered_movies_logged(location, people, notes, directors, start, end, movies)
    movies = find_filtered_movies_first_logged(location, people, notes, start,end, title)
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')

    return render_template('logs-first-watch.html', movies = movies, location=location, people=people, notes=notes, originalStart=start, originalEnd=end, title=title)


@app.route('/first-logs/<int:days>', methods=['POST'])
def logs_firstpost_days(days):
    title = request.form.get('title').strip()
    location = request.form.get('location').strip()
    people = request.form.get('people').strip()
    notes = request.form.get('notes').strip()
    start = request.form.get('start')
    end = request.form.get('end')
    movies = find_filtered_movies_first_logged(location, people, notes, start,end, title)
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')

    return render_template('logs-first-watch.html', movies = movies, location=location, people=people, notes=notes, originalStart=start, originalEnd=end, title=title)


@app.route('/first-logs')
def logsfriststart():
    movies = find_filtered_movies_first_logged("", "", "", None, None, "")
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')
    return render_template('logs-first-watch.html', movies = movies, location="", people="", notes="", originalStart=None, originalEnd=None, title="")

@app.route('/first-logs/<int:days>')
def logs_stfirstart_days(days):
    movies = find_filtered_movies_first_logged("", "", "", date.today() - timedelta(days=days), date.today(), "")
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')
    return render_template('logs-first-watch.html', movies = movies, location="", people="", notes="", originalStart=date.today() - timedelta(days=days), originalEnd=date.today(), title="")



@app.route('/rankings', methods=['POST'])
def movies_with_posters_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_filtered_movies_forRanking(title, director, year, min, max, recommendation, genres)
    return render_template('rankings-with-posters.html',genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)

@app.route('/logs', methods=['POST'])
def logs_post():
    title = request.form.get('title').strip()
    location = request.form.get('location').strip()
    people = request.form.get('people').strip()
    notes = request.form.get('notes').strip()
    start = request.form.get('start')
    end = request.form.get('end')
    # movies = request.form.get('movies').strip()
    # directors = request.form.get('directors').strip()
    # start = request.form.get('start')
    # end = request.form.get('end')
    # movies = find_filtered_movies_logged(location, people, notes, directors, start, end, movies)
    movies = find_filtered_movies_logged(location, people, notes, start,end, title)
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')

    return render_template('logs.html', movies = movies, location=location, people=people, notes=notes, originalStart=start, originalEnd=end, title=title)


@app.route('/logs/<int:days>', methods=['POST'])
def logs_post_days(days):
    title = request.form.get('title').strip()
    location = request.form.get('location').strip()
    people = request.form.get('people').strip()
    notes = request.form.get('notes').strip()
    start = request.form.get('start')
    end = request.form.get('end')
    movies = find_filtered_movies_logged(location, people, notes, start,end, title)
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')

    return render_template('logs.html', movies = movies, location=location, people=people, notes=notes, originalStart=start, originalEnd=end, title=title)

@app.route('/logs/<int:days>/<int:endDays>', methods=['POST'])
def logs_end_post_days(days, end):
    title = request.form.get('title').strip()
    location = request.form.get('location').strip()
    people = request.form.get('people').strip()
    notes = request.form.get('notes').strip()
    start = request.form.get('start')
    end = request.form.get('end')
    movies = find_filtered_movies_logged(location, people, notes, start,end, title)
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')

    return render_template('logs.html', movies = movies, location=location, people=people, notes=notes, originalStart=start, originalEnd=end, title=title)




@app.route('/logs')
def logs_start():
    movies = find_filtered_movies_logged("", "", "", None, None, "")
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')
    return render_template('logs.html', movies = movies, location="", people="", notes="", originalStart=None, originalEnd=None, title="")

@app.route('/logs/<int:days>')
def logs_start_days(days):
    movies = find_filtered_movies_logged("", "", "", date.today() - timedelta(days=days), date.today(), "")
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')
    return render_template('logs.html', movies = movies, location="", people="", notes="", originalStart=date.today() - timedelta(days=days), originalEnd=date.today(), title="")

@app.route('/logs/<int:days>/<int:end>')
def logs_end_start_days(days, end):
    movies = find_filtered_movies_logged("", "", "", date.today() - timedelta(days=days), date.today() - timedelta(days=end), "")
    for x in movies:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')
    return render_template('logs.html', movies = movies, location="", people="", notes="", originalStart=date.today() - timedelta(days=days), originalEnd=date.today() - timedelta(days=end), title="")


# @app.route('/rankings')
# def movies_with_posters():
#     movies = find_filtered_movies_forRanking("", "", "", 0, 0, "", "")
#     return render_template('rankings-with-posters.html', movies = movies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/rankings')
@app.route('/rankings/<int:scroll_to_id>')
def movies_with_posters(scroll_to_id=None):
    movies = find_filtered_movies_forRanking("", "", "", 0, 0, "", "")
    return render_template('rankings-with-posters.html', movies=movies, scroll_to_id=scroll_to_id, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")



@app.route('/recently-watched-without-posters')
def recently_watched_movies():
    movies = find_recently_watched()
    for x in movies:
        if x.lastWatchedDate is not None:
            x.lastWatchedDate = format_date(x.lastWatchedDate, locale='en')
    return render_template('recentlywatched.html', movies = movies, originalStart=None, originalEnd=None, originalRecommendation="", originalLocation="")

@app.route('/recently-watched')
def recently_watched_movies_with_posters():
    movies = find_recently_watched()
    for x in movies:
        if x.lastWatchedDate is not None:
            x.notes = format_date(x.lastWatchedDate, locale='en')
    return render_template('recentlywatched-with-posters.html', movies = movies, originalStart=None, originalEnd=None, originalRecommendation="", originalLocation="")


@app.route('/recently-watched-without-posters', methods=['POST'])
def recently_watched_movies_post():
    start = request.form.get('start')
    end = request.form.get('end')
    movies = filterRecentWatched(start, end)
    # for x in range(0, len(movies)):
    #     if movies[x].lastWatchedDate is not None:
    #         movies[x].lastWatchedDate = format_date(movies[x].lastWatchedDate, locale='en')
    return render_template('recentlywatched.html', movies = movies, originalStart=start, originalEnd=end)


@app.route('/recently-watched/<int:days>')
def recently_watched_movies_with_posters_range(days):
    movies = find_recently_watched_days(days)
    for x in movies:
        if x.lastWatchedDate is not None:
            x.notes = format_date(x.lastWatchedDate, locale='en')
    return render_template('recentlywatched-with-posters.html', movies = movies, originalStart=date.today() - timedelta(days=days), originalEnd=date.today(), originalRecommendation="", originalLocation="")

@app.route('/recently-watched/<int:days>', methods=['POST'])
def recently_watched_movies_with_posters_post_days(days):
    start = request.form.get('start')
    end = request.form.get('end')
    movies = filterRecentWatched(start, end)
    for x in movies:
        if x.lastWatchedDate is not None:
            x.notes = format_date(x.lastWatchedDate, locale='en')
    return render_template('recentlywatched-with-posters.html', movies = movies, originalStart=start, originalEnd=end)



@app.route('/recently-watched', methods=['POST'])
def recently_watched_movies_with_posters_post():
    start = request.form.get('start')
    end = request.form.get('end')
    movies = filterRecentWatched(start, end)
    for x in movies:
        if x.lastWatchedDate is not None:
            x.notes = format_date(x.lastWatchedDate, locale='en')
    return render_template('recentlywatched-with-posters.html', movies = movies, originalStart=start, originalEnd=end)




@app.route('/rankings-by-stars-without-posters')
def ranking_by_star_movies():
    movies = find_best_movies()
    for x in movies:
        if x.lastWatchedDate is not None:
            x.lastWatchedDate = format_date(x.lastWatchedDate, locale='en')
    return render_template('ranking-by-stars.html', movies = movies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")


@app.route('/rankings-by-stars-without-posters', methods=['POST'])
def ranking_by_star_movies_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    movies = find_filtered_movies_by_stars(title, director, year, min, max, recommendation)
    return render_template('ranking-by-stars.html', movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)

@app.route('/stars', methods=['POST'])
def ranking_by_star_movies_with_poster_post():
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    stars = request.form.get('stars')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    movies = find_filtered_movies_by_stars(title, director, year, min, max, recommendation, genres, stars)
    return render_template('ranking-by-stars-with-posters.html', stars=stars, genres=genres, movies = movies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)


@app.route('/stars')
def ranking_by_star_movies_with_posters():
    movies = find_best_movies()
    for x in movies:
        if x.lastWatchedDate is not None:
            x.lastWatchedDate = format_date(x.lastWatchedDate, locale='en')
    return render_template('ranking-by-stars-with-posters.html', genres="", stars=0, movies = movies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/unrated')
def unlogged_ranking_by_star_movies_with_posters():
    # movies = unloggedMovies()
    movies = findmoviesToRecommend()
    return render_template('unlogged.html', movies=movies)


@app.route('/lists')
def lists():
    lists = getAllLists()
    listOfPeople = getListsOfPeople()
    listOfYears = getListOfYears()
    return render_template('lists-page.html', lists=lists, listOfPeople=listOfPeople, listOfYears=listOfYears)


@app.route('/rankings-page')
def rankings_page():
    return render_template('rankings-page.html')

@app.route('/rankings-types')
def rankings_types():
    return render_template('rankings-types.html')

@app.route('/rank-by-specific/<int:first_movie_id>/<int:second_movie_id>', methods=['GET'])
def rank_by_specific(first_movie_id,  second_movie_id):
    firstMovie = getMovieById(first_movie_id)
    secondMovie = getMovieById(second_movie_id)

    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-specific.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)



@app.route('/update-specific-rankings/<int:winner_id>/<int:loser_id>/<int:movie_id>', methods=['GET'])
def rank_by_specific_movie_post(winner_id, loser_id, movie_id):
    updateRankings(winner_id, loser_id, False)
    while True:
        firstMovie = getMovieById(movie_id)   
        secondMovie = getRandomMovie()
        if firstMovie.title != secondMovie.title:
            break
    urlString = '/ranking-details/' + str(movie_id)
    return redirect(urlString)


@app.route('/rank-by-winner/<int:movie_id>', methods=['GET'])
def rank_by_winner(movie_id):
    if movie_id == 0:
        while True:
            firstMovie = getRandomMovie()
            secondMovie = getRandomMovie()
            if firstMovie.title != secondMovie.title:
                break
    else:
        while True:
            firstMovie = getMovieById(movie_id)   
            secondMovie = getRandomMovie()
            if firstMovie.title != secondMovie.title:
                if checkNotLastRanked(firstMovie.id, secondMovie.id):
                    break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster

    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-winner.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

@app.route('/update-winner-rankings/<int:winner_id>/<int:loser_id>/<int:movie_id>', methods=['GET'])
def rank_by_winner_movie_post(winner_id, loser_id, movie_id):
    updateRankings(winner_id, loser_id, False)
    while True:
        firstMovie = getMovieById(movie_id)   
        secondMovie = getRandomMovie()
        if firstMovie.title != secondMovie.title:
            break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    urlBuild = '/rank-by-winner/' + str(movie_id)
    return redirect(urlBuild)
    # return render_template('rank-by-winner.html', firstMovie = firstMovie, 
    #                        secondMovie = secondMovie, first=first, second=second)

@app.route('/rank-by-loser/<int:movie_id>', methods=['GET'])
def rank_by_loser(movie_id):
    if movie_id == 0:
        while True:
            firstMovie = getRandomMovie()
            secondMovie = getRandomMovie()
            if firstMovie.title != secondMovie.title:
                break
    else:
        while True:
            firstMovie = getMovieById(movie_id)   
            secondMovie = getRandomMovie()
            if firstMovie.title != secondMovie.title:
                if checkNotLastRanked(firstMovie.id, secondMovie.id):
                    break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-loser.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

@app.route('/update-loser-rankings/<int:winner_id>/<int:loser_id>/<int:movie_id>', methods=['GET'])
def rank_by_loser_movie_post(winner_id, loser_id, movie_id):
    updateRankings(winner_id, loser_id, False)
    # while True:
    #     firstMovie = getMovieById(movie_id)   
    #     secondMovie = getRandomMovie()
    #     if firstMovie.title != secondMovie.title:
    #         break
    # start = "/static/images/movieposters/"
    # first = start + firstMovie.poster
    # second = start + secondMovie.poster
    urlBuild = '/rank-by-loser/' + str(movie_id)
    return redirect(urlBuild)
    # return render_template('rank-by-loser.html', firstMovie = firstMovie, 
    #                        secondMovie = secondMovie, first=first, second=second)

@app.route('/genre-rankings')
def genres():
    genres = find_genres()
    return render_template('genre-rankings.html', genres = genres)

@app.route('/genre-movie-rankings/<int:genre_id>', methods=['GET'])
def genre_list(genre_id):
    genre = find_genres_by_id(genre_id)
    movies = find_movies_by_genre(genre_id)
    return render_template('genre-movie-rankings.html', movies = movies, genre = genre, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")

@app.route('/genre-movie-rankings/<int:genre_id>', methods=['POST'])
def genre_list_post(genre_id):
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genre = find_genres_by_id(genre_id)
    movies = find_movies_by_genre_filter(genre_id, title, director, year, min, max, recommendation)
    return render_template('genre-movie-rankings.html', movies = movies, genre = genre, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)


@app.route('/rank-by-rerank/<int:movieId>')
def rank_by_urerank(movieId):
    movies = getUniqueMoviesReank(movieId)
    if len(movies) < 1:
        return redirect ('/')
    firstMovie = movies[0]
    secondMovie = movies[1]
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-rerank.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


@app.route('/rank-by-unique')
def rank_by_unique():
    movies = getUniqueMovies()
    if len(movies) < 1:
        return redirect ('/')
    firstMovie = movies[0]
    secondMovie = movies[1]
    if firstMovie.liked == 1 and secondMovie.liked == 3:
        updateRankings(firstMovie.id, secondMovie.id, True)
        return redirect('/rank-by-unique')
    elif firstMovie.liked == 3 and secondMovie.liked == 1:
        updateRankings(secondMovie.id, firstMovie.id, True)
        return redirect('/rank-by-unique')
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster

    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-unique.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

@app.route('/update-unique-rankings/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_by_unranked_post_unoique(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    return redirect('/rank-by-unique')
    # return render_template('rank-by-unranked-movies.html', firstMovie = firstMovie, 
    #                        secondMovie = secondMovie, first=first, second=second)


@app.route('/update-rerank-rankings/<int:winner_id>/<int:loser_id>/<int:movie_id>', methods=['GET'])
def rank_by_unranked_postrerank(winner_id, loser_id, movie_id):
    updateRankings(winner_id, loser_id, False)
    urlBuild = '/rank-by-rerank/' + str(movie_id)
    return redirect(urlBuild)



@app.route('/rank-by-unranked')
def rank_by_unranked():
    while True:
        firstMovie = getRandomUnrankedMovie()
        secondMovie = getRandomMovie()
        if firstMovie == [] or secondMovie == []:
            return redirect ('/')
        if firstMovie.title != secondMovie.title:
            if checkNotLastRanked(firstMovie.id, secondMovie.id):
                break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster

    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-unranked-movies.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

                           

@app.route('/update-rank-by-unranked/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_by_unranked_post(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    return redirect('/rank-by-unranked')
    # return render_template('rank-by-unranked-movies.html', firstMovie = firstMovie, 
    #                        secondMovie = secondMovie, first=first, second=second)


@app.route('/rank-by-recent')
def rank_by_recent():
    while True:
        firstMovie = getRandomRecentMovie()
        secondMovie = getRandomMovie()
        if firstMovie == [] or secondMovie == []:
            return redirect ('/')
        if firstMovie.title != secondMovie.title:
            if checkNotLastRanked(firstMovie.id, secondMovie.id):
                break
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-recent-watch.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

                           

@app.route('/update-rank-by-recent/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_by_recent_post(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    return redirect('/rank-by-recent')




@app.route('/rank-by-genre/<int:genre_id>')
def rank_by_genre_list(genre_id):
    genre = find_genres_by_id(genre_id)
    if(genre.count < 2):
        return redirect('/')
    counter = 0
    while True:
        firstMovie = getRandomMovieByGenre(genre_id)
        secondMovie = getRandomMovieByGenre(genre_id)
        if firstMovie == [] or secondMovie == []:
            return redirect ('/')
        if firstMovie.title != secondMovie.title:
            if checkNotLastRanked(firstMovie.id, secondMovie.id):
                break
            counter = counter + 1
    if counter > 11:
        return redirect('/')
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-genre.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, genre = genre, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


@app.route('/rank-by-list/<int:list_id>')
def rank_by_list(list_id):
    list = find_list_by_id(list_id)
    if(list.count < 2):
        return redirect('/')
    counter = 0
    while True:
        firstMovie = getRandomMovieByList(list_id)
        secondMovie = getRandomMovieByList(list_id)
        if firstMovie == [] or secondMovie == []:
            return redirect ('/')
        if firstMovie.title != secondMovie.title:
            # if checkNotLastRanked(firstMovie.id, secondMovie.id):
            #     break
            break
        counter = counter +1
        if counter > 11:
            urlBuild = '/list/' + str(list_id)
            return redirect(urlBuild)
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-list.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, list = list, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


@app.route('/rank-by-list-unique/<int:list_id>')
def rank_by_unique_list(list_id):
    list = find_list_by_id(list_id)
    if(list.count < 2):
        str_reditct = '/list/' + str(list_id)
        return redirect (str_reditct)
    movies = getUniqueMoviesFromList(list_id)
    if len(movies) < 1:
        str_reditct = '/list/' + str(list_id)
        return redirect (str_reditct)
    firstMovie = movies[0]
    secondMovie = movies[1]
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-list-unique.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, list = list, first=first, second=second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)



@app.route('/rank-by-movie-in-list/<string:movie_id>/<int:list_id>', methods=['GET'])
def rank_by_movie_in_list(movie_id, list_id):
    list = find_list_by_id(list_id)
    if(list.count < 2):
        str_reditct = '/list/' + str(list_id)
        return redirect (str_reditct)
    counter = 0
    while True:
        firstMovie = getMovieById(movie_id)   
        secondMovie = getRandomMovieByList(list_id)
        if firstMovie.title != secondMovie.title:
            if checkNotLastRanked(firstMovie.id, secondMovie.id):
                break
            counter = counter + 1
    if counter > 11:
        str_reditct = '/list/' + str(list_id)
        return redirect (str_reditct)
    start = "/static/images/movieposters/"
    first = start + firstMovie.poster
    second = start + secondMovie.poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-movie-in-list.html', firstMovie = firstMovie, 
                           secondMovie = secondMovie, list = list, first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)

                           

@app.route('/update-rankings-by-genre/<int:winner_id>/<int:loser_id>/<int:genre_id>', methods=['GET'])
def rank_by_list_post(winner_id, loser_id, genre_id):
    updateRankings(winner_id, loser_id, False)
    urlBuild = '/rank-by-genre/' + str(genre_id)
    return redirect(urlBuild)

@app.route('/update-rankings-by-list/<int:winner_id>/<int:loser_id>/<int:list_id>', methods=['GET'])
def rank_by_genre_post(winner_id, loser_id, list_id):
    updateRankings(winner_id, loser_id, False)
    urlBuild = '/rank-by-list/' + str(list_id)
    return redirect(urlBuild)

@app.route('/update-rankings-by-list-unique/<int:winner_id>/<int:loser_id>/<int:list_id>', methods=['GET'])
def rank_by_list_unique_upadte(winner_id, loser_id, list_id):
    updateRankings(winner_id, loser_id, False)
    urlBuild = '/rank-by-list-unique/' + str(list_id)
    return redirect(urlBuild)

@app.route('/update-rankings-for-movie-by-list/<int:winner_id>/<int:loser_id>/<int:movie_id>/<int:list_id>', methods=['GET'])
def rank_by_movie_inlife(winner_id, loser_id, movie_id, list_id):
    updateRankings(winner_id, loser_id, False)
    urlBuild = '/rank-by-movie-in-list/' + str(movie_id)  + '/' + str(list_id)
    return redirect(urlBuild)


@app.route('/add-list', methods=['GET'])
def add_list_get():
    #movies = find_all_movies()
    return render_template('add-list.html', movies = [])

@app.route('/add-list', methods=['POST'])
def add_list_post():
    new_name = request.form.get('title')
    notes = request.form.get('notes')
    success = add_list(new_name, notes)
    if success > 0:
        return redirect('/list/' + str(success))
    return render_template('add-list.html')


@app.route('/add-movie', methods=['GET'])
def add_movie_get():
    genres = find_genres()
    allGenres = ""
    for genre in genres:
        allGenres += genre.name + " , "
    allGenres = allGenres[:-2]
    return render_template('add-movie.html', allGenres = allGenres)

@app.route('/add-movie', methods=['POST'])
def add_movie_post():
    new_title = request.form.get('title').strip()
    new_year = request.form.get('year')
    new_poster = request.form.get('poster')
    newFirstGenre = request.form.get('firstGenre')
    newSecondGenre = request.form.get('secondGenre')
    new_director = request.form.get('director')
    new_runtime = request.form.get('runtime')
    rewatched = request.form.get('rewatched')
    faveQuote = request.form.get('faveQuote')
    notes = request.form.get('notes')
    stars = request.form.get('stars')
    recommend = request.form.get('recommend')
    date = request.form.get('date')
    location = request.form.get('locationOfWatch')
    people = request.form.get('people')
    watchNotes = request.form.get('watchNotes')
    if rewatched == None:
        rewatched = 0
    else:
        rewatched = 1
    if new_poster is not None and len(new_poster) > 0:
        if not new_poster.endswith('.jpg'):
            new_poster = new_poster + '.jpg'
    success = add_movie(new_title, new_year, people, new_director, new_runtime, rewatched, new_poster, newFirstGenre, newSecondGenre, notes, stars, recommend, date, location, faveQuote, watchNotes)
    if success > 0:
        return redirect('/details/' + str(success))
    return render_template('add-movie.html')


@app.route('/watched/<int:movie_id>', methods=['GET'])
def watched(movie_id):
    updateMovie(movie_id)
    return redirect('/')

@app.route('/rewatch/<int:movie_id>', methods=['GET'])
def rewatch_add(movie_id):
    rewatchMovie(movie_id)
    return ('',204)

@app.route('/save-ranking/<int:first_movie_id>/<int:second_movie_id>', methods=['GET'])
def saveRankung(first_movie_id, second_movie_id):
    saveRanking(first_movie_id, second_movie_id)
    return ('',204)

@app.route('/saved-rankings', methods=['GET'])
def savedMovies():
    #rankings = getSavedMovies()
    return render_template('saved-rankings.html')

@app.route('/unrewatch/<int:movie_id>', methods=['GET'])
def unRewatch_add(movie_id):
    unRewatchMovie(movie_id)
    return ('',204)

@app.route('/uncurrent/<int:movie_id>', methods=['GET'])
def unCurrent_add(movie_id):
    removeCurrentWatch(movie_id)
    return ('',204)

@app.route('/current/<int:movie_id>', methods=['GET'])
def current_add(movie_id):
    currentlyWatching(movie_id)
    return ('',204)


@app.route('/add-to-list/<int:list_id>/<int:movie_id>',methods=['GET'])
def add_to_list(list_id, movie_id):
    addMovieToList(list_id, movie_id)
    return ('',204)

@app.route('/remove-to-list/<int:list_id>/<int:movie_id>',methods=['GET'])
def remove_to_list(list_id, movie_id):
    removeMovieFromList(list_id, movie_id)
    return "<script>window.location.href = document.referrer;</script>"

@app.route('/session',methods=['GET'])
def session():
    started = startedSession()
    if not started:
        return redirect('/session-details')
    return ('',204)

@app.route('/session-details',methods=['GET'])
def session_details():
    session = getLatestSession()
    rankings = getMoviesRankedInSession()
    numOfMoviesRanked = len(rankings)
    topMovies = getTopMoviesInRankingSession()

    return render_template('session-details.html', session = session, numOfMoviesRanked=numOfMoviesRanked, )

@app.route('/reverse-last-rank', methods=['GET'])
def reverse_last_rank():
    reverseLastRank()
    return ('',204)



@app.route('/update-movie/<int:movie_id>', methods=['GET'])
def updateMovieGet(movie_id):
    movie = getMovieById(movie_id)
    genres = find_genres()
    allGenres = ""
    for genre in genres:
        allGenres += genre.name + " , "
    allGenres = allGenres[:-2]
    firstGenre = ""
    secondGenre = ""
    movieGenres = getMovieGenres(movie_id)

    if movieGenres[0] is not None and movieGenres[0] != "":
        firstGenre = movieGenres[0].name
    if movieGenres[1] is not None and movieGenres[1] != "":
        secondGenre = movieGenres[1].name

    return render_template('update-movie.html', movie = movie, allGenres = allGenres, firstGenre = firstGenre, secondGenre = secondGenre)


@app.route('/update-list/<int:list_id>', methods=['GET'])
def updateListGet(list_id):
    list = getListDetails(list_id)
    return render_template('update-list.html', list = list)


@app.route('/update-log/<int:movie_id>', methods=['GET'])
def updateMovieLogGet(movie_id):
    movie = getMovieLog(movie_id)
    return render_template('update-log.html', movie = movie)



@app.route('/random-list')
def finder_movies_with_posters_withList():
    id = createListWithRandomMovies(12)
    reditecString = "/list/" + str(id)
    return redirect(reditecString)


@app.route('/duplicate-list/<int:list_id>')
def dinde_duplicate_list(list_id):
    id = duplicateList(list_id)
    reditecString = "/list/" + str(id)
    return redirect(reditecString)




@app.route('/people', methods=['GET'])
def peopleGet():
    #people = getListPeople()

    return render_template('person-details.html', people=[], originalName="", title="")

@app.route('/people', methods=['POST'])
def listGetPeople_post():
    name = request.form.get('name').strip()
    title = request.form.get('title').strip()

    if len(name) > 1:
        watches = getListDetailsFromNAme(name, title) 
        for x in watches:
            if x.watchDate is not None and len(str(x.watchDate)) != 14:
                x.watchDate = format_date(x.watchDate, locale='en')
        count = len(watches)
        # movies = getPerson(name)
        movies = []

    else:
        name = ""
        movies = []
        count = 0
        title=""
        watches=[]
    
    return render_template('person-details.html', movies=movies, originalName=name, count=count, watches=watches, title=title)

@app.route('/list/<int:list_id>', methods=['GET'])
def listGet(list_id):
    list = getListDetails(list_id)
    movies = getMoviesFromList(list_id)

    unwatched = getUnwatchedMoviesFromList(list_id)

    allMovies = []

    countOfMovies = len(movies) + len(unwatched)

    timesRankedString = ""
    timesRanked= getTimesRankedString(list_id)

    totalRanked = int(len(movies) * (len(movies) -1) / 2)

    timesRankedString = "Rank Unique " + str(timesRanked) + "/" + str(totalRanked)
    if timesRanked == totalRanked:
        timesRankedString = "Fully Ranked"
    
    listOfPeople = getListsOfPeople()
    listOfYears = getListOfYears()

    if list in listOfPeople or list in listOfYears:
        return render_template('list-details-no-add.html', timesRankedString=timesRankedString, genres="", list=list, movies=movies, unwatched=unwatched, countOfMovies=countOfMovies, allMovies=allMovies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")


    return render_template('list-details.html', timesRankedString=timesRankedString, genres="", list=list, movies=movies, unwatched=unwatched, countOfMovies=countOfMovies, allMovies=allMovies, originalTitle="", originalDirector="", originalYear="", originalMinimum=0, originalMaximum=0, originalRecommendation="")



@app.route('/list/<int:list_id>', methods=['POST'])
def listGet_post(list_id):
    title = request.form.get('title').strip()
    director = request.form.get('director').strip()
    year = request.form.get('year').strip()
    min = request.form.get('start')
    max = request.form.get('end')
    recommendation = request.form.get('recommendation').strip()
    genres = request.form.get('genres').strip()
    
    list = getListDetails(list_id)
    movies = getMoviesFromList(list_id)

    allMovies = find_all_filtered_movies_without(title, director, year, min, max, recommendation, movies, genres)
    
    

    unwatched = getUnwatchedMoviesFromList(list_id)


    countOfMovies = len(movies) + len(unwatched)

    timesRankedString = ""
    timesRanked= getTimesRankedString(list_id)

    totalRanked = int(len(movies) * (len(movies) -1) / 2)

    timesRankedString = "Rank Unique " + str(timesRanked) + "/" + str(totalRanked)
    if timesRanked == totalRanked:
        timesRankedString = "Fully Ranked"
    

    return render_template('list-details.html', timesRankedString=timesRankedString,genres=genres, unwatched=unwatched, countOfMovies=countOfMovies, list=list, movies=movies, allMovies=allMovies, originalTitle=title, originalDirector=director, originalYear=year, originalMinimum=min, originalMaximum=max, originalRecommendation=recommendation)


@app.route('/similar/<int:movie_id>', methods=['GET'])
def detailsSimilarGet(movie_id):
    movie = getMovieDetails(movie_id)

    similar = getPlusMinusMovies(movie_id)

    # get similar movies based on director, runtime, year and then genre
    recommendedMovies = getRecommendedMovies(movie_id)

    lists = getListsForMovie(movie_id)

    start = "/static/images/movieposters/"
    poster = start + movie.poster
    similar1 = similar[0]
    actualMovie = similar[1]
    similar2 = similar[2]
    
    return render_template('details-with-similar.html', lists=lists, recommendedMovies=recommendedMovies[0], unwatchedRecommended=recommendedMovies[1], similarDirector=recommendedMovies[2], similarRanking=recommendedMovies[3], relatedMovies=recommendedMovies[4], movie = movie, poster=poster, similar1=similar1, similar2=similar2, actualMovie=actualMovie)



@app.route('/details/<int:movie_id>', methods=['GET'])
def detailsGet(movie_id):
    movie = getMovieDetails(movie_id)

    lists = getListsForMovie(movie_id)

    start = "/static/images/movieposters/"
    poster = start + movie.poster

    if movie.unwatched == 1:
        recommendedMovies = getRecommendedMovies(movie_id)
        return render_template('details-unwatched.html', lists=lists,  movie = movie, poster=poster, similarDirector=recommendedMovies[2], relatedMovies=recommendedMovies[4])
    
    similar = getPlusMinusMovies(movie_id)

    similar1 = similar[0]
    actualMovie = similar[1]
    similar2 = similar[2]
    

    rewatch = "No"
    if movie.rewatch:
        rewatch = "Yes"

    currently = "No"
    if movie.currentlyWatching:
        currently = "Yes"

    timesRankedString = ""
    timesRanked = movie.rewatchCount
    moviesWatched = findNumOfWatchedMovies()

    timesRankedString = "Rank Unique " + str(timesRanked) + "/" + str(moviesWatched - 1)
    if timesRanked == moviesWatched - 1:
        timesRankedString = "Fully Ranked"


    return render_template('details.html', timesRankedString=timesRankedString, lists=lists, currently=currently, movie = movie, poster=poster, similar1=similar1, similar2=similar2, actualMovie=actualMovie,  rewatched=rewatch)


@app.route('/update-movie-liked/<int:movie_id>/<int:liked>', methods=['GET'])
def update_movie_liked(movie_id, liked):
    try:
        updateLiked(movie_id, liked)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))
    

@app.route('/log-movie/<int:movie_id>', methods=['GET'])
def LogGet(movie_id):
    movie = getMovieDetails(movie_id)

    watches = getMovieWatches(movie_id)

    start = "/static/images/movieposters/"
    poster = start + movie.poster

    for x in watches:
        if x.watchDate is not None:
            x.watchDate = format_date(x.watchDate, locale='en')


    return render_template('log-movie.html', movie = movie, poster=poster, watches=watches)




@app.route('/ranking-details/<int:movie_id>', methods=['GET'])
def rankingDetailsGet(movie_id):

    movie = getMovieDetails(movie_id)

    rankings = getRankings(movie_id)
    

    start = "/static/images/movieposters/"
    poster = start + movie.poster


    return render_template('ranking-details.html', movie = movie, poster=poster, winners=rankings[0],  losers=rankings[1])

@app.route('/ranking-upsets/<int:movie_id>', methods=['GET'])
def rankingDeIpsersteGet(movie_id):

    movie = getMovieDetails(movie_id)

    rankings = getUpsets(movie_id)
    

    start = "/static/images/movieposters/"
    poster = start + movie.poster


    return render_template('ranking-upsets.html', movie = movie, poster=poster, winners=rankings[0],  losers=rankings[1])


@app.route('/ranking-details-for-list/<int:list_id>/<int:movie_id>', methods=['GET'])
def rankingDetailsGetList(list_id, movie_id):

    movie = getMovieDetails(movie_id)

    rankings = getRankingsInList(list_id, movie_id)
    

    start = "/static/images/movieposters/"
    poster = start + movie.poster


    return render_template('ranking-details-from-list.html', movie = movie, poster=poster, winners=rankings[0],  losers=rankings[1])

@app.route('/update-movie/<int:movie_id>', methods=['POST'])
def updateMoviePost(movie_id):
    new_title = request.form.get('title')
    new_year = request.form.get('year')
    new_secondGenre = request.form.get('secondGenre')
    new_poster = request.form.get('poster')
    new_firstGenre = request.form.get('firstGenre')
    new_director = request.form.get('director')
    new_runtime = request.form.get('runtime')
    unwatched = request.form.get('unwatched')
    rewatched = request.form.get('rewatched')
    notes = request.form.get('notes')
    stars = request.form.get('stars')
    recommend = request.form.get('recommend')
    date = request.form.get('date')
    faveQuote = request.form.get('faveQuote')
    location = request.form.get('locationOfWatch')
    liked = request.form.get('liked')
    if unwatched == None:
        unwatched = 0
    else:
        unwatched = 1
    if rewatched == None:
        rewatched = 0
    else:
        rewatched = 1
    update_movie(movie_id, new_title, new_year, unwatched, rewatched, new_poster, new_firstGenre, new_secondGenre, new_director, new_runtime, notes, stars, recommend, date, location, faveQuote, liked)
    urlBuild = '/details/' + str(movie_id)
    return redirect(urlBuild)


@app.route('/update-list/<int:list_id>', methods=['POST'])
def updateListPost(list_id):
    new_title = request.form.get('title')
    notes = request.form.get('notes')
    update_list(list_id, new_title, notes)
    urlBuild = '/list/' + str(list_id)
    return redirect(urlBuild)



@app.route('/update-log/<int:movie_id>', methods=['POST'])
def updateLogPost(movie_id):
    notes = request.form.get('notes')
    stars = request.form.get('stars')
    recommend = request.form.get('recommend')
    faveQuote = request.form.get('faveQuote')
    location = request.form.get('newLocation')
    newPeople = request.form.get('newPeople')
    newNotes = request.form.get('newNotes')
    newDate = request.form.get('newDate')
    id = update_log(movie_id, location, newPeople, newNotes, newDate, faveQuote, recommend, stars, notes)
    urlBuild = '/log-movie/' + str(id)
    return redirect(urlBuild)

@app.route('/log-movie/<int:movie_id>', methods=['POST'])
def logMoviePost(movie_id):
    notes = request.form.get('notes')
    stars = request.form.get('stars')
    recommend = request.form.get('recommend')
    faveQuote = request.form.get('faveQuote')

    newLocation = request.form.get('newLocation')
    newPeople = request.form.get('newPeople')
    newNotes = request.form.get('newNotes')
    newDate = request.form.get('newDate')
    log_movie(movie_id, notes, stars, recommend, faveQuote, newLocation, newPeople, newNotes, newDate)
    urlBuild = '/details/' + str(movie_id)
    return redirect(urlBuild)

@app.route('/delete-movie/<int:movie_id>')
def deleteMovieGet(movie_id):
    deleteMovie(movie_id)
    return redirect('/')


@app.route('/delete-list/<int:list_id>')
def deleteListGet(list_id):
    deleteList(list_id)
    return redirect('/lists')

@app.route('/random-movie/<int:list_id>')
def randomgMovieGete(list_id):
    addMoviesToListRandom(list_id)
    resditedSteing = "/list/" + str(list_id)
    return redirect(resditedSteing)


@app.route('/update-proximity-rankings/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_by_proximity_post(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    return redirect('/rank-by-proximity')


@app.route('/update-liked-rankings/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_by_liked_post(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    return redirect('/rank-by-liked')

@app.route('/update-unliked-rankings/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_by_unliked_post(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    return redirect('/rank-by-unliked')

@app.route('/update-mid-rankings/<int:winner_id>/<int:loser_id>', methods=['GET'])
def rank_by_mid_post(winner_id, loser_id):
    updateRankings(winner_id, loser_id, False)
    return redirect('/rank-by-mid')

@app.route('/auto-rank/<int:winner_id>', methods=['GET'])
def auto_rank(winner_id):
    autoRank(winner_id)
    return redirect(request.referrer or '/')

@app.route('/auto-rank-certain/<int:winner_id>', methods=['GET'])
def auto_rank_certain(winner_id):
    autoRankCertain(winner_id)
    return redirect(request.referrer or '/')

@app.route('/auto-rank-list/<int:winner_id>', methods=['GET'])
def auto_rank_list(winner_id):
    autoRankList(winner_id)
    return redirect(request.referrer or '/')
    

@app.route('/rank-by-proximity')
def rank_by_proximity():
    while True:
        movies = getProximityMovie()
        if movies[0].title != movies[1].title:
            if checkNotLastRanked(movies[0].id, movies[1].id):
                break
    start = "/static/images/movieposters/"
    first = start + movies[0].poster
    second = start + movies[1].poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-proximity.html', firstMovie = movies[0], 
                           secondMovie = movies[1], first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


@app.route('/rank-by-liked')
def rank_by_liked():
    while True:
        movies = getLikedMovies()
        if movies[0].title != movies[1].title:
            break
    start = "/static/images/movieposters/"
    first = start + movies[0].poster
    second = start + movies[1].poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-liked.html', firstMovie = movies[0], 
                           secondMovie = movies[1], first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


@app.route('/rank-by-unliked')
def rank_by_unliked():
    while True:
        movies = getunlikedMovies()
        if movies[0].title != movies[1].title:
            if checkNotLastRanked(movies[0].id, movies[1].id):
                break
    start = "/static/images/movieposters/"
    first = start + movies[0].poster
    second = start + movies[1].poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-unliked.html', firstMovie = movies[0], 
                           secondMovie = movies[1], first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


@app.route('/rank-by-mid')
def rank_by_mid():
    while True:
        movies = getmidMovies()
        if movies[0].title != movies[1].title:
            if checkNotLastRanked(movies[0].id, movies[1].id):
                break
    start = "/static/images/movieposters/"
    first = start + movies[0].poster
    second = start + movies[1].poster
    lastRanked = getLastRanking()
    flagged = ""
    if lastRanked[2] == 1:
        flagged = "Flagged"
    return render_template('rank-by-mid.html', firstMovie = movies[0], 
                           secondMovie = movies[1], first=first, second = second, winner=lastRanked[0], loser=lastRanked[1],flagged=flagged)


#Query to update the list of movies a certain person has seen with me
# INSERT INTO list_movie(movieid, listId)
# SELECT movieId, 8 FROM movie_watch
# WHERE people like '%Isabella%'


