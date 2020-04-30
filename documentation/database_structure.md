#Tietokannan rakenne

##Tietokantakaavio

##Taulujen luonti

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	email VARCHAR(144) NOT NULL, 
	address VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE sport (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE level (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE trip (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(32) NOT NULL, 
	destination VARCHAR(32) NOT NULL, 
	start_date DATETIME, 
	end_date DATETIME, 
	price INTEGER NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	registration_dl DATETIME, 
	max_participants INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE trip_sport (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	trip_id INTEGER NOT NULL, 
	sport_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trip_id) REFERENCES trip (id), 
	FOREIGN KEY(sport_id) REFERENCES sport (id)
);

CREATE TABLE trip_level (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	trip_id INTEGER NOT NULL, 
	level_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trip_id) REFERENCES trip (id), 
	FOREIGN KEY(level_id) REFERENCES level (id)
);

CREATE TABLE trip_user (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	trip_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(trip_id) REFERENCES trip (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
