REM   Script: NoCodeKingsDB
REM   Our Oracle Live SQL database framework

CREATE Table "User" (  
    userID int NOT NULL,  
    firstName varchar(30),  
    lastName varchar(40) NOT NULL,  
    email varchar(40) NOT NULL,  
    phone int,  
    psword varchar(40),  
    subStatus number(1)  
    constraint User_subStatus check (subStatus IN (1,0)),  
    adminID int NOT NULL,  
    PRIMARY KEY (userID)  
);

CREATE Table "User" (  
    userID int NOT NULL,  
    firstName varchar(30),  
    lastName varchar(40) NOT NULL,  
    email varchar(40) NOT NULL,  
    phone int,  
    psword varchar(40),  
    subStatus number(1)  
    constraint User_subStatus check (subStatus IN (1,0)),  
    adminID int NOT NULL,  
    PRIMARY KEY (userID)  
) 
 
CREATE Table "Admin" (  
    adminID int NOT NULL,  
    firstName varchar(30),  
    lastName varchar(40),  
    email varchar(40),  
    phone int,  
    psword varchar(40),  
    subStatus number(1)  
    constraint Admin_subStatus check (subStatus IN (1,0)),  
    paymentID int NOT NULL,  
    PRIMARY KEY (adminID)  
);

CREATE Table "Admin" (  
    adminID int NOT NULL,  
    firstName varchar(30),  
    lastName varchar(40),  
    email varchar(40),  
    phone int,  
    psword varchar(40),  
    subStatus number(1)  
    constraint Admin_subStatus check (subStatus IN (1,0)),  
    paymentID int NOT NULL,  
    PRIMARY KEY (adminID)  
);

CREATE Table Payment ( 
    paymentID int NOT NULL, 
    amount decimal, 
    adminID int, 
    userID int, 
    PRIMARY KEY (paymentID) 
);

