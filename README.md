# CampusParty-DatabaseProject

CampusParty Application by Kimberly Ekstrand and Aubrie Galinis

-------------------------------------------------------------------------------------------------------------------------------------------------

Thank you for downloading CampusParty!

About our application: CampusParty is an application designed for college campuses to easily track and manage events and student organizations
		       on their campus.

What our application does: Our application is able to:
			   - Insert information into the provided database
			   - Update information in the database
			   - Delete information from the database
			   - Search the database
			   - Create a transcript using information from the database

How to we compiled our code: We created the application using Python v 3.9 in WING IDE.
                             We created the database using DB Browser v 3.12.
			     
			   
			  
To Use this application your database should contain the following 5 Tables and Attributes provided with the SQL commands to create them: 

CREATE TABLE "Club" ( "org_num" TEXT NOT NULL UNIQUE, "org_name" TEXT, "SGA_recognition" TEXT NOT NULL, "budget" INTEGER, "exec_positions" TEXT DEFAULT 'President, Vice President, Secretary, Treasurer'' ', PRIMARY KEY("org_num") )

CREATE TABLE "ClubLeadership" ( "wID" INTEGER NOT NULL UNIQUE, "org_num" INTEGER NOT NULL, "leadership_title" TEXT NOT NULL, "year_enter" INTEGER, "year_exit" INTEGER, FOREIGN KEY("wID") REFERENCES "User"("wID"), FOREIGN KEY("org_num") REFERENCES "Club"("org_num"), PRIMARY KEY("wID","org_num") )

CREATE TABLE "ClubMembership" ( "wID" INTEGER NOT NULL UNIQUE, "member_name" TEXT, "member_email" TEXT, "org_num" INTEGER NOT NULL, "join_date" INTEGER, PRIMARY KEY("wID"), FOREIGN KEY("wID") REFERENCES "User"("wID") )

CREATE TABLE "Event" ( "event_ID" INTEGER NOT NULL UNIQUE, "description" TEXT NOT NULL DEFAULT 'No Description Provided.', "Name" TEXT NOT NULL, "hosting_org" INTEGER NOT NULL COLLATE BINARY, "RSVP" INTEGER NOT NULL DEFAULT 0, "location" TEXT NOT NULL, "date" TEXT NOT NULL, "time" TEXT NOT NULL, "category" TEXT NOT NULL DEFAULT 'Social', FOREIGN KEY("hosting_org") REFERENCES "Club"("org_num"), PRIMARY KEY("event_ID") )

CREATE TABLE "User" ( "wID" INTEGER NOT NULL UNIQUE, "user_name" TEXT NOT NULL, "user_email" TEXT NOT NULL, "user_role" TEXT NOT NULL DEFAULT 'Student', PRIMARY KEY("wID") )
