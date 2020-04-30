# Käyttötapaukset

Käyttäjä haluaa luoda käyttäjätilin
```
INSERT INTO account(date_çreated, datem_modified, name, username, password, email, address)
VALUES (current_timestamp, current_timestamp, ?, ?, ?, ?, ?)
```

Käyttäjä haluaa nähdä kaikki kaikki luodut matkat
```
SELECT * FROM trip
```
Käyttäjä haluaa hakea matkoja joiden maksimihinta = x

```
SELECT * FROM trip
WHERE trip.price <= x
SORT BY trip.start_date
```

Käyttäjä haluaa hakea matkoja, joiden lähtöpäivä on päivämäärän x jälkeen
```
SELECT * FROM trip
WHERE trip.start_date > x
SORT BY trip.start_date
```

Käyttäjä haluaa hakea matkoja, joilla voi harrastaa ainakin lajeja sports = {x, y, z}
```
SELECT * FROM trip
LEFT JOIN trip_sport ON trip_sport.trip_id = trip.id
WHERE trip_sport IN (x, y, z)
GROUP BY trip.id
HAVING COUNT(DISTINCT trip_sport.sport_id) = 3
```

Käyttäjä haluaa luoda uuden matkan
```
INSERT INTO trip(date_created, date_modified, name, destination, start_date, end_date, price, description, registration_dl, max_participants, account_id)
VALUES (current_timestamp, current_timestamp, ?, ?, ?, ?, ?, ?, ?, ?, ?)

INSERT INTO trip_sport(date_created, date_modified, trip_id, sport_id)
VALUES (current_timestamp, current_timestamp, ?, ?)

INSERT INTO trip_level(date_created, date_modified, trip_id, level_id)
VALUES (current_timestamp, current_timestamp, ?, ?)

INSERT INTO trip_user(date_created, date_modified, trip_id, level_id)
VALUES (current_timestamp, current_timestamp, ?, ?)'''
```
Käyttäjä haluaa muokata matkaa
```
UPDATE trip
SET date_modified = current_timestamp, name = ?, price = ?
WHERE trip.id = ?

INSERT INTO trip_sport(date_created, date_modified, trip_id, sport_id)
VALUES (current_timestamp, current_timestamp, ?, ?)

DELETE FROM trip_sport
WHERE trip_sport.trip.id = ? AND trip_sport.sport_id = ?

DELETE FROM trip_level
WHERE trip_level.trip.id = ? AND trip_level.level_id = ?
```

Käyttäjä haluaa poistaa luomansa matkan

```
DELETE FROM trip_sport
WHERE trip_sport.trip_id = ? AND trip_sport.sport_id = ?

DELETE FROM trip_level
WHERE trip_level.trip_id = ? AMD trip_level.level_id = ?

DELETE FROM trip_user
WHERE trip_user.trip_id = ? AND trip_user.account_id = ?
```

Käyttäjä haluaa nähdä, mille matkoille hän on ilmoittautunut
```
SELECT Trip.id, Trip.name, Trip.destination, Trip.start_date, Trip.end_date FROM Trip
LEFT JOIN Trip_User ON Trip_User.trip_id = Trip.id
LEFT JOIN Account ON Account.id = Trip_User.account_id
WHERE Account.id = ?
ORDER BY Trip.registration_dl
```
Käyttäjä haluaa ilmoittautua matkalle

```
INSERT INTO trip_user(date_created, date_modified, trip_id, account_id)
VALUES (current_timestamp, current_timestamp, ?, ?)

```

Käyttäjä haluaa perua ilmoittautumisensa
```
DELETE FROM trip_user
WHERE trip_user.trip_id = ? AND trip_user.account_id = ?
```

Käyttäjä haluaa nähdä matkat, joille hän on ilmoittautunut

```
SELECT Trip.id, Trip.name, Trip.destination, Trip.start_date, Trip.end_date FROM Trip
LEFT JOIN Account ON Account.id = Trip.account_id
WHERE Account.id = ?
ORDER BY Trip.registration_dl
```

Käyttäjä haluaa nähdä matkalle ilmoittautuneiden määrän

```
SELECT COUNT(*) FROM Account
LEFT JOIN Trip_User ON Trip_User.account_id = Account.id
LEFT JOIN Trip ON Trip.id = Trip_User.trip_id
WHERE Trip.id = ?
```
