CREATE DATABASE IF NOT EXISTS bandnamesdb;
USE bandnamesdb;

CREATE TABLE IF NOT EXISTS adjectives (
  id INT AUTO_INCREMENT PRIMARY KEY,
  adjective VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS nouns (
  id INT AUTO_INCREMENT PRIMARY KEY,
  noun VARCHAR(100) NOT NULL
);

TRUNCATE TABLE adjectives;
TRUNCATE TABLE nouns;

INSERT INTO adjectives (adjective) VALUES
('Midnight'), ('Last'), ('Blue'), ('Silent'), ('Broken'),
('Electric'), ('Golden'), ('Lonely'), ('Crystal'), ('Wild');

INSERT INTO nouns (noun) VALUES
('Llamas'), ('Biscuits'), ('Echoes'), ('Dragons'), ('Sailors'),
('Rockets'), ('Rivers'), ('Shadows'), ('Knights'), ('Nomads');
