CREATE TABLE Media(mediaID VARCHAR(20) NOT NULL PRIMARY KEY,
		      primary_title VARCHAR(200) NOT NULL, 
		      release_year INTEGER NOT NULL,
                      country VARCHAR(45) NOT NULL, 
		      format VARCHAR(20) NOT NULL,
                      film_or_tv VARCHAR(20) NOT NULL,
                      title_sort VARCHAR(200) NOT NULL,
                      rating VARCHAR(20) NOT NULL,
                      tmdb_id VARCHAR(20) NOT NULL,
                      tagline VARCHAR(400) NOT NULL,
		      flag VARCHAR(20) NOT NULL);

CREATE TABLE LoanInfo(loanid VARCHAR(10) NOT NULL PRIMARY KEY,
                      loan_type VARCHAR(30) NOT NULL,
                      loan_time VARCHAR(10) NOT NULL,
                      location VARCHAR(20) NOT NULL);

CREATE TABLE Item(itemID VARCHAR(20) NOT NULL PRIMARY KEY,
                  mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID),
                  call_number VARCHAR(65) NOT NULL,
		  loanid VARCHAR(10) NOT NULL REFERENCES LoanInfo(loanid),
                  availability VARCHAR(25) NOT NULL,
		  current BOOLEAN NOT NULL);

CREATE TABLE AKA(AKA_id SERIAL PRIMARY KEY,
		 mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID), 
		 secondary_title VARCHAR(250) NOT NULL); 

CREATE TABLE Actor(actor_id SERIAL PRIMARY KEY,
		  mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID), 
		  performer VARCHAR(50) NOT NULL); 

CREATE TABLE Summary(mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID),
                     summary VARCHAR(1600) NOT NULL);

CREATE TABLE Director(director_id SERIAL PRIMARY KEY,
		      mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID),
		      director VARCHAR(40) NOT NULL);

CREATE TABLE Genre(genre_id SERIAL PRIMARY KEY,
	     mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID), 
	     genre VARCHAR(20) NOT NULL);

CREATE TABLE TVSeason(mediaID VARCHAR(20) NOT NULL PRIMARY KEY REFERENCES Media(mediaID), 
		      season INTEGER NOT NULL);

CREATE TABLE Production(production_id SERIAL PRIMARY KEY,
                        mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID),
                        company VARCHAR(100) NOT NULL,
                        match VARCHAR(100) NOT NULL);

CREATE TABLE Language(language_id SERIAL PRIMARY KEY,
                      mediaID VARCHAR(20) NOT NULL REFERENCES Media(mediaID),
                      language VARCHAR(50) NOT NULL);

CREATE TABLE Poster(mediaID VARCHAR(20) NOT NULL PRIMARY KEY REFERENCES Media(mediaID),
                    poster VARCHAR(100) NOT NULL);
