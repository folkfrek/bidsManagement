SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT=0;

DROP TABLE IF EXISTS Members;
CREATE TABLE Members (
    memberID int NOT NULL AUTO_INCREMENT,
    cycleID int DEFAULT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (memberID),
    FOREIGN KEY (cycleID) REFERENCES Cycles (cycleID)
);

INSERT INTO Members VALUES (1, 2, "Ophelia.Murillo@us.af.mil"), (2, 6, "Beau.Davie@us.af.mil"), (3, 1, "Natasha.Fernandez@us.af.mil"), (4, 5, "Ammar.Clegg@us.af.mil"), (5, 2, "Usamah.Franco@us.af.mil"), (6, 8, "Macaulay.Larsen@us.af.mil"), (7, 5, "Isabelle.Nolan@us.af.mil"), (8, 1, "Krystal.Medina@us.af.mil"), (9, 3, "Angharad.Potter@us.af.mil"), (10, 3, "Byron.Spooner@us.af.mil"), (11, 1, "Shereen.Nichols@us.af.mil"), (12, 1, "Ruby.Duarte@us.af.mil"), (13, 8, "Kelise.Sosa@us.af.mil"), (14, 5, "Tayler.Raymond@us.af.mil"), (15, 3, "Rhodri.Richmond@us.af.mil"), (16, 8, "Amman.Massey@us.af.mil"), (17, 1, "Rohan.Barry@us.af.mil"), (18, 4, "Harry.Barclay@us.af.mil"), (19, 4, "Gillian.Britt@us.af.mil"), (20, 1, "Katlyn.Hibbert@us.af.mil"), (21, 5, "Adam.Johnson@us.af.mil"), (22, 5, "Brittney.McKenzie@us.af.mil"), (23, 8, "Robert.Williamson@us.af.mil"), (24, 1, "Izaac.Mccullough@us.af.mil"), (25, 4, "Emily.Marks@us.af.mil");

DROP TABLE IF EXISTS Assignments;
CREATE TABLE Assignments (
    assignmentID int NOT NULL AUTO_INCREMENT,
    commanderID int DEFAULT NULL,
    cycleID int DEFAULT NULL,
    location varchar(255),
    PRIMARY KEY (assignmentID),
    FOREIGN KEY (commanderID) REFERENCES Commanders (commanderID),
    FOREIGN KEY (cycleID) REFERENCES Cycles (cycleID)
);

INSERT INTO Assignments VALUES (1, 1, 4, "Ft Meade"), (2, 2, 2, "Beale"), (3, 3, 4, "Travis"), (4, 4, 7, "Eglin"), (5, 5, 5, "Wright-Patterson"), (6, 6, 1, "Moody"), (7, 7, 1, "Shaw"), (8, 8, 1, "Ft Bragg"), (9, 9, 9, "Buckley"), (10, 10, 9, "NORAD"), (11, 11, 3, "Ft Hood"), (12, 12, 4, "JB Langley"), (13, 13, 1, "JBER"), (14, 14, 5, "Peterson"), (15, 15, 1, "JB Andrews"), (16, 1, 1, "Ft Meade"), (17, 7, 7, "Shaw"), (18, 16, 2, "Wright-Patterson"), (19, 16, 2, "Wright-Patterson"), (20, 17, 9, "Eglin"), (21, 12, 9, "JB Langley"), (22, 4, 1, "Eglin"), (23, 10, 2, "NORAD"), (24, 18, 7, "Ft Bragg"), (25, 8, 4, "Ft Bragg");

DROP TABLE IF EXISTS Cycles;
CREATE TABLE Cycles (
    cycleID int NOT NULL AUTO_INCREMENT,
    season varchar(255) NOT NULL,
    year int NOT NULL,
    PRIMARY KEY (cycleID)
);

INSERT INTO Cycles VALUES (1, "Summer", 2022), (2, "Winter", 2023), (3, "Summer", 2023), (4, "Winter", 2024), (5, "Summer", 2024), (6, "Winter", 2025), (7, "Summer", 2025), (8, "Winter", 2026), (9, "Summer", 2026), (10, "Winter", 2027), (11, "Summer", 2027), (12, "Winter", 2028), (13, "Summer", 2028), (14, "Winter", 2029), (15, "Summer", 2029), (16, "Winter", 2030), (17, "Summer", 2030);


DROP TABLE IF EXISTS Commanders;
CREATE TABLE Commanders (
    commanderID int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    PRIMARY KEY (commanderID)
);

INSERT INTO Commanders Values (1, "Emily.Mackay@us.af.mil"), (2, "Anastasia.Clarkson@us.af.mil"), (3, "Inigo.Montoya@us.af.mil"), (4, "Paddy.Rangel@us.af.mil"), (5, "Finnian.Morgan@us.af.mil"), (6, "Leoni.Bernal@us.af.mil"), (7, "Isra.Roach@us.af.mil"), (8, "Brody.Nieves@us.af.mil"), (9, "Leilani.Maddox@us.af.mil"), (10, "Rania.Bond@us.af.mil"), (11, "Maria.Wilkins@us.af.mil"), (12, "Stacy.Schneider@us.af.mil"), (13, "Korban.Barlow@us.af.mil"), (14, "Mackenzie.Fowler@us.af.mil"), (15, "Caelan.Corrigan@us.af.mil"), (16, "Anaya.Boyle@us.af.mil"), (17, "Angel.Tillman@us.af.mil"), (18, "Juan.Mendez@us.af.mil");

DROP TABLE IF EXISTS Bids;
CREATE TABLE Bids (
    bidID int NOT NULL AUTO_INCREMENT,
    assignmentID int DEFAULT NULL,
    memberID int DEFAULT NULL,
    bidByMember boolean DEFAULT 0,
    bidByCommander boolean DEFAULT 0,
    PRIMARY KEY (bidID),
    FOREIGN KEY (assignmentID) REFERENCES Assignments (assignmentID) ON DELETE CASCADE,
    FOREIGN KEY (memberID) REFERENCES Members (memberID) ON DELETE CASCADE
);

INSERT INTO Bids VALUES (1, 6, 3, 1, 0), (2, 7, 8, 1, 0), (3, 8, 11, 1, 1), (4, 13, 12, 0, 1), (5, 15, 17, 1, 0), (6, 16, 20, 1, 1), (7, 22, 24, 1, 0), (8, 22, 8, 1, 1), (9, 13, 3, 0, 1), (10, 15, 11, 1, 1), (11, 8, 17, 0, 1), (12, 16, 3, 0, 1);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;