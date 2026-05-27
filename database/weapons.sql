CREATE TABLE Weapons (
    name VARCHAR(50),
    data TEXT,
    strategy TEXT,
    advanced_strategy TEXT,
    gun1 VARCHAR(50) DEFAULT 'Unknown',
    gun2 VARCHAR(50) DEFAULT 'Unknown',
    gun3 VARCHAR(50) DEFAULT 'Unknown',
    FOREIGN KEY (gun1) REFERENCES Guns(name),
    FOREIGN KEY (gun2) REFERENCES Guns(name),
    FOREIGN KEY (gun3) REFERENCES Guns(name)
);