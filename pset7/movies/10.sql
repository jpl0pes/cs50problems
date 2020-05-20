SELECT DISTINCT(people.name)
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
JOIN directors ON movies.id = directors.movie_id
JOIN people on directors.person_id = people.id
WHERE ratings.rating >= 9.0
ORDER BY ratings.rating DESC, movies.title DESC