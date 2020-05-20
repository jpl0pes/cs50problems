SELECT avg(ratings.rating) as "Average Rating"
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE year = 2012