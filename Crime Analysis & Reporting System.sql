CREATE TABLE Victims (
    VictimID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Address VARCHAR(100),
    PhoneNumber VARCHAR(15)
);

-- Sample values
/*INSERT INTO Victims (VictimID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber) VALUES
(1, 'John', 'Doe', '1990-03-15', 'Male', '123 Main St, City, Country', '+1234567890'),
(2, 'Jane', 'Smith', '1985-07-22', 'Female', '456 Elm St, City, Country', '+1987654321'),
(3, 'Michael', 'Johnson', '1978-11-10', 'Male', '789 Oak St, City, Country', '+1122334455'),
(4, 'Emily', 'Brown', '1995-05-03', 'Female', '321 Pine St, City, Country', '+1554433221'),
(5, 'David', 'Martinez', '1982-09-18', 'Male', '654 Birch St, City, Country', '+1443225566'),
(6, 'Jessica', 'Taylor', '1998-01-20', 'Female', '987 Maple St, City, Country', '+1669988775'),
(7, 'Daniel', 'Wilson', '1973-12-05', 'Male', '234 Cedar St, City, Country', '+1777666555'),
(8, 'Sarah', 'Anderson', '1989-04-30', 'Female', '876 Walnut St, City, Country', '+1888777666'),
(9, 'Christopher', 'Thomas', '1993-08-12', 'Male', '543 Cherry St, City, Country', '+1999888777'),
(10, 'Amanda', 'Garcia', '1980-06-25', 'Female', '135 Fir St, City, Country', '+1666555444');*/

CREATE TABLE Suspects (
    SuspectID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    ContactInformation VARCHAR(100)
);

-- Sample values
/*INSERT INTO Suspects (SuspectID, FirstName, LastName, DateOfBirth, Gender, ContactInformation) VALUES
(1, 'Robert', 'Johnson', '1980-05-20', 'Male', '123 Main St, City, Country, +1234567890'),
(2, 'Emma', 'Wilson', '1992-09-12', 'Female', '456 Elm St, City, Country, +1987654321'),
(3, 'William', 'Brown', '1975-03-05', 'Male', '789 Oak St, City, Country, +1122334455'),
(4, 'Olivia', 'Martinez', '1988-07-30', 'Female', '321 Pine St, City, Country, +1554433221'),
(5, 'James', 'Taylor', '1983-11-18', 'Male', '654 Birch St, City, Country, +1443225566'),
(6, 'Sophia', 'Anderson', '1997-01-25', 'Female', '987 Maple St, City, Country, +1669988775'),
(7, 'Alexander', 'Garcia', '1970-12-15', 'Male', '234 Cedar St, City, Country, +1777666555'),
(8, 'Isabella', 'Thomas', '1985-04-20', 'Female', '876 Walnut St, City, Country, +1888777666'),
(9, 'Liam', 'Wilson', '1990-08-02', 'Male', '543 Cherry St, City, Country, +1999888777'),
(10, 'Ava', 'Johnson', '1987-06-15', 'Female', '135 Fir St, City, Country, +1666555444');*/

CREATE TABLE Incidents (
    IncidentID INT PRIMARY KEY,
    IncidentType VARCHAR(50),
    IncidentDate DATE,
    Latitude DECIMAL(9,6),
    Longitude DECIMAL(9,6),
    Description TEXT,
    Status VARCHAR(20),
    VictimID INT,
    SuspectID INT,
    FOREIGN KEY (VictimID) REFERENCES Victims(VictimID),
    FOREIGN KEY (SuspectID) REFERENCES Suspects(SuspectID)
);

-- Sample values
/*INSERT INTO Incidents (IncidentID, IncidentType, IncidentDate, Latitude, Longitude, Description, Status, VictimID, SuspectID) VALUES
(1, 'Robbery', '2024-04-01', 18.5204, 73.8567, 'A convenience store was robbed.', 'Closed', 1, 1),
(2, 'Homicide', '2024-04-05', 18.5244, 73.7926, 'A murder occurred in the park.', 'Open', 2, NULL),
(3, 'Theft', '2024-04-10', 18.5203, 73.8567, 'A car was stolen from the parking lot.', 'Under Investigation', NULL, 2),
(4, 'Robbery', '2024-04-15', 18.5314, 73.8457, 'A bank was robbed.', 'Open', 3, 3),
(5, 'Homicide', '2024-04-20', 18.5089, 73.8838, 'A body was found in an abandoned building.', 'Closed', 4, NULL),
(6, 'Theft', '2024-04-25', 18.5021, 73.8839, 'Several items were stolen from a residence.', 'Closed', 5, NULL),
(7, 'Robbery', '2024-04-30', 18.5048, 73.8496, 'A jewelry store was robbed.', 'Open', 6, NULL),
(8, 'Homicide', '2024-05-05', 18.4934, 73.8474, 'A body was found in the river.', 'Open', NULL, 5),
(9, 'Theft', '2024-05-10', 18.4915, 73.8697, 'A laptop was stolen from a coffee shop.', 'Closed', 7, NULL),
(10, 'Robbery', '2024-05-15', 18.4963, 73.8565, 'A gas station was robbed.', 'Under Investigation', NULL, NULL);*/

CREATE TABLE LawEnforcementAgencies (
    AgencyID INT PRIMARY KEY,
    AgencyName VARCHAR(100),
    Jurisdiction VARCHAR(100),
    ContactInformation VARCHAR(100)
);

-- Sample values
/*INSERT INTO LawEnforcementAgencies (AgencyID, AgencyName, Jurisdiction, ContactInformation) VALUES
(1, 'City Police Department', 'Citywide', '+1234567890'),
(2, 'County Sheriff Department', 'Countywide', '+1987654321'),
(3, 'State Bureau of Investigation', 'Statewide', '+1122334455'),
(4, 'Federal Bureau of Investigation', 'National', '+1554433221'),
(5, 'Drug Enforcement Administration', 'National', '+1443225566'),
(6, 'Immigration and Customs Enforcement', 'National', '+1669988775'),
(7, 'Transportation Security Administration', 'National', '+1777666555'),
(8, 'Secret Service', 'National', '+1888777666'),
(9, 'Bureau of Alcohol, Tobacco, Firearms and Explosives', 'National', '+1999888777'),
(10, 'U.S. Marshals Service', 'National', '+1666555444');*/

CREATE TABLE Officers (
    OfficerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BadgeNumber VARCHAR(20),
    OfficerRank VARCHAR(50),
    ContactInformation VARCHAR(100),
    AgencyID INT,
    FOREIGN KEY (AgencyID) REFERENCES LawEnforcementAgencies(AgencyID)
);

-- Sample values
/*INSERT INTO Officers (OfficerID, FirstName, LastName, BadgeNumber, OfficerRank, ContactInformation, AgencyID) VALUES
(1, 'Michael', 'Smith', '12345', 'Detective', '+1234567890', 1),
(2, 'Jennifer', 'Johnson', '54321', 'Sergeant', '+1987654321', 2),
(3, 'Christopher', 'Brown', '98765', 'Lieutenant', '+1122334455', 3),
(4, 'Jessica', 'Davis', '67890', 'Agent', '+1554433221', 4),
(5, 'David', 'Wilson', '13579', 'Inspector', '+1443225566', 5),
(6, 'Emily', 'Martinez', '24680', 'Officer', '+1669988775', 6),
(7, 'Daniel', 'Taylor', '97531', 'Special Agent', '+1777666555', 7),
(8, 'Sarah', 'Anderson', '86420', 'Deputy', '+1888777666', 8),
(9, 'Matthew', 'Thomas', '31415', 'Inspector', '+1999888777', 9),
(10, 'Ashley', 'Garcia', '27182', 'Deputy Marshal', '+1666555444', 10);*/

CREATE TABLE Evidence (
    EvidenceID INT PRIMARY KEY,
    Description TEXT,
    LocationFound VARCHAR(100),
    IncidentID INT,
    FOREIGN KEY (IncidentID) REFERENCES Incidents(IncidentID)
);

-- Sample values
/*INSERT INTO Evidence (EvidenceID, Description, LocationFound, IncidentID) VALUES
(1, 'Fingerprint on the window', 'Inside the house', 1),
(2, 'Bloodstains on the floor', 'Crime scene', 2),
(3, 'Weapon found near the victim', 'Park bench', 2),
(4, 'Surveillance footage from the store', 'Security cameras', 3),
(5, 'Footprints near the crime scene', 'Alleyway', 4),
(6, 'DNA sample from the victim', 'Hospital', 5),
(7, 'Stolen items recovered in suspect''s house', 'Suspect''s residence', 6),
(8, 'Drug paraphernalia found in the car', 'Vehicle', 7),
(9, 'CCTV footage of the suspect at the scene', 'Street corner', 8),
(10, 'Eyewitness testimony', 'Courtroom', 9);*/

CREATE TABLE Reports (
    ReportID INT PRIMARY KEY,
    IncidentID INT,
    ReportingOfficerID INT,
    ReportDate DATE,
    ReportDetails TEXT,
    Status VARCHAR(20),
    FOREIGN KEY (IncidentID) REFERENCES Incidents(IncidentID),
    FOREIGN KEY (ReportingOfficerID) REFERENCES Officers(OfficerID)
);

-- Sample values
/*INSERT INTO Reports (ReportID, IncidentID, ReportingOfficerID, ReportDate, ReportDetails, Status) VALUES
(1, 1, 1, '2024-04-02', 'Investigated the robbery incident.', 'Finalized'),
(2, 2, 2, '2024-04-06', 'Conducted initial investigation at the crime scene.', 'Draft'),
(3, 3, 3, '2024-04-11', 'Gathered witness statements and evidence.', 'Finalized'),
(4, 4, 4, '2024-04-16', 'Started investigation into the bank robbery.', 'Draft'),
(5, 5, 5, '2024-04-21', 'Submitted forensic report on the homicide case.', 'Finalized'),
(6, 6, 6, '2024-04-26', 'Compiled evidence against the suspect.', 'Draft'),
(7, 7, 7, '2024-05-01', 'Submitted initial report on the jewelry store robbery.', 'Finalized'),
(8, 8, 8, '2024-05-06', 'Continued investigation into the river body case.', 'Draft'),
(9, 9, 9, '2024-05-11', 'Finalized report on the laptop theft.', 'Finalized'),
(10, 10, 10, '2024-05-16', 'Reviewed evidence and prepared case for investigation.', 'Draft');*/

CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,
    CaseDescription VARCHAR(255) NOT NULL
);

/*INSERT INTO Cases (CaseDescription) VALUES
    ('Robbery at Main Street'),
    ('Assault at City Park'),
    ('Burglary at Elm Street'),
    ('Vandalism at Oak Avenue'),
    ('Kidnapping at Pine Street'),
    ('Homicide at Maple Avenue'),
    ('Fraud at Lakeview Drive'),
    ('Drug Trafficking at Sunset Boulevard'),
    ('Arson at Hillcrest Road'),
    ('Forgery at Riverwalk Lane');*/






