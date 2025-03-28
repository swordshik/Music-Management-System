CREATE DATABASE IF NOT EXISTS MusicLibrary;
USE MusicLibrary;

CREATE TABLE Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL );

CREATE TABLE Album (
    album_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id INT,
    release_year INT,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id) ON DELETE CASCADE );

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL );

CREATE TABLE Song (
    song_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    album_id INT,
    genre_id INT,
    artist_id INT,
    release_year INT,
    FOREIGN KEY (album_id) REFERENCES Album(album_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id) ON DELETE CASCADE,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id) ON DELETE CASCADE );

-- Existing data insertion
INSERT INTO Artist (name) VALUES
('The Beatles'),
('Queen'),
('Arctic Monkeys'),
('Nirvana'),
('Дайте Танк'),
('Imagine Dragons'),
('NF');

INSERT INTO Album (title, artist_id, release_year) 
VALUES 
('Abbey Road', 1, 1969),
('A Night at the Opera', 2, 1975),
('AM', 3, 2013),
('Nevermind', 4, 1991),
('Вечный огонь', 5, 2017),
('Evolve', 6, 2017),
('Perception', 7, 2017);

INSERT INTO Genre (name) VALUES
('Rock'),
('Pop'),
('Alternative Rock'),
('Grunge'),
('Electronic');

INSERT INTO Song (title, album_id, genre_id, artist_id, release_year) 
VALUES 
('Come Together', 1, 1, 1, 1969),
('Bohemian Rhapsody', 2, 1, 2, 1975),
('Do I Wanna Know?', 3, 3, 3, 2013),
('Smells Like Teen Spirit', 4, 4, 4, 1991),
('Сквозь землю', 5, 1, 5, 2017),
('Believer', 6, 5, 6, 2017),
('Let You Down', 7, 5, 7, 2017);

-- New data insertion
INSERT INTO Artist (name) VALUES
('Gorillaz'),
('Caravan Palace'),
('Seatbelts'),
('Radiohead'),
('Howard'),
('Серебряная Свадьба'),
('Car Seat Headrest'),
('Caro Burrows');

INSERT INTO Album (title, artist_id, release_year) 
VALUES 
('Humanz', 8, 2017),
('Robot Face', 9, 2015),
('Cowboy Bebop OST 1', 10, 1998),
('The King of Limbs', 11, 2011),
('Together Alone', 12, 2018),
('Single', 13, 2014),
('Teens of Denial', 14, 2016),
('Burrows', 15, 2017);

INSERT INTO Genre (name) VALUES
('Alternative'),
('Electro-Swing'),
('Jazz'),
('Experimental Rock'),
('Indie-Pop'),
('Indie Rock');

INSERT INTO Song (title, album_id, genre_id, artist_id, release_year) 
VALUES 
('She\'s My Collar', 8, 1, 8, 2017),
('Aftermath', 9, 2, 9, 2015),
('Tank!', 10, 3, 10, 1998),
('Lotus Flower', 11, 4, 11, 2011),
('Your Honor', 12, 5, 12, 2018),
('Ag', 13, 6, 13, 2014),
('Culture', 14, 7, 14, 2016),
('Closet Lunatic', 15, 5, 15, 2017);

-- Select query to view the inserted data
SELECT ar.name AS artist, a.title AS album, s.title AS song_title, g.name AS genre, s.release_year AS year
FROM Song s
JOIN Album a ON s.album_id = a.album_id
JOIN Artist ar ON s.artist_id = ar.artist_id
JOIN Genre g ON s.genre_id = g.genre_id;
