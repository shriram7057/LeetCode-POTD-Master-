PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE Person(
  driver_id INT PRIMARY KEY,
  name VARCHAR(50),
  address VARCHAR(100)
);

CREATE TABLE Car(
  license VARCHAR(20) PRIMARY KEY,
  model VARCHAR(20),
  year INT
);

CREATE TABLE Owns(
  driver_id INT,
  license VARCHAR(20),
  FOREIGN KEY(driver_id) REFERENCES Person(driver_id),
  FOREIGN KEY(license) REFERENCES Car(license)
);

-- Insert data
INSERT INTO Person VALUES (1, 'Shree', 'India');
INSERT INTO Person VALUES (2, 'Ravi', 'Delhi');

INSERT INTO Car VALUES ('ABC123', 'Toyota', 2020);
INSERT INTO Car VALUES ('XYZ789', 'Honda', 2022);

INSERT INTO Owns VALUES (1, 'ABC123');
INSERT INTO Owns VALUES (2, 'XYZ789');

-- Show output
SELECT * FROM Person;
SELECT * FROM Car;
SELECT * FROM Owns;

-- Join output (combined view)
SELECT Person.name, Car.model, Car.license
FROM Owns
JOIN Person ON Owns.driver_id = Person.driver_id
JOIN Car ON Owns.license = Car.license;


