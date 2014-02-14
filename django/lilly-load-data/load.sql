DELETE FROM AKA;
DELETE FROM Actor;
DELETE FROM Director;
DELETE FROM Genre;
DELETE FROM TVSeason;
DELETE FROM LoanInfo;
DELETE FROM Media;
DELETE FROM Item;
DELETE FROM Summary;
DELETE FROM Production;
DELETE FROM Language;
DELETE FROM Poster;
\COPY Media(mediaID, primary_title, release_year, country, format, film_or_tv, title_sort, rating, tmdb_id, tagline, flag) FROM 'data/Media.dat' WITH DELIMITER '|' NULL '' CSV
\COPY LoanInfo(loanid, loan_type, loan_time, location) FROM 'data/LoanInfo.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Item(itemID, mediaID, call_number, loanid, availability, current) FROM 'data/Item.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Summary(mediaID, summary) FROM 'data/Summary.dat' WITH DELIMITER '|' NULL '' CSV
\COPY AKA(mediaID, secondary_title) FROM 'data/AKA.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Actor(mediaID, performer) FROM 'data/Actor.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Director(mediaID, director) FROM 'data/Director.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Production(mediaID, company, match) FROM 'data/Production.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Genre(mediaID, genre) FROM 'data/Genre.dat' WITH DELIMITER '|' NULL '' CSV
\COPY TVSeason(mediaID, season) FROM 'data/TVSeason.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Language(mediaID, language) FROM 'data/Language.dat' WITH DELIMITER '|' NULL '' CSV
\COPY Poster(mediaID, poster) FROM 'data/Poster.dat' WITH DELIMITER '|' NULL '' CSV
