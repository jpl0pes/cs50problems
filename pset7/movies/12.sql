SELECT title
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE id IN
    (
    SELECT movie_id
    FROM stars
    WHERE movie_id IN
        (
        SELECT stars1.movie_id
        FROM stars as "stars1"
	    INNER JOIN
		    (
		    SELECT movie_id
		    FROM stars
		    WHERE
			person_id =
			    (
			    SELECT id
			    FROM people
			    WHERE name = "Johnny Depp"
			    )
		)
		as stars2 ON stars1.movie_id = stars2.movie_id
        WHERE
        stars1.person_id =
            (
            SELECT id
            FROM people
            WHERE name = "Helena Bonham Carter"
            )
        )
    )
ORDER BY rating DESC





