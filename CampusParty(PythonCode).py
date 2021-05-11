
import sqlite3
import os
connection = sqlite3.connect("DatabaseProject-1.db")
cursor = connection.cursor()



# MENU FUNCTION: 

def menu():

	choice = -1  # bogus setting to get us started
	Go_Back = 'Go_Back'
	while (choice != Go_Back):
		print ("----------------------------------------------")
		print ("  1  -  Insert Information")
		print ("  2  -  Update Information")
		print ("  3  -  Delete Information")
		print ("  4  -  Search & View Database")
		print ("  5  -  View Transcript")
		print ("  6  -  Go Back")
		print ("---------------------------")
		user_choice = int(input("Select the option you would like to complete: "))
		if (user_choice < 1 or user_choice > 6) :
			choice = ERROR;
		
		else :
			choice = user_choice;
		
		if ( choice ==1):
			print ("\n\n----------------------------------------------")
			print ("  1  -  Insert User")
			print ("  2  -  Insert Club")
			print ("  3  -  Insert Event")
			print ("  4  -  Insert Club Leadership Position")
			print ("  5  -  Insert Club Membership Position")
			print ("  6  -  Go Back")
			print ("---------------------------")
			user_choice_2 = int(input("Select the option you would like to complete: "))
			if (user_choice_2 < 1 or user_choice_2 > 6) :
				choice2 = ERROR;
			
			else :
				choice2 = user_choice_2;

			if ( choice2 == 1):
				insert_user()
			elif ( choice2 == 2):
				insert_club()
			elif ( choice2 == 3):
				insert_event()
			elif ( choice2 == 4):
				insert_leadership()
			elif ( choice2 ==5):
				insert_membership()
			elif (choice2 == 6):
				choice = Go_Back
				print("Going back...")
				menu()
			else:  
				print ("ERROR: ", choice, "is an invalid input. Try again.")	
			

		elif ( choice == 2):
			print ("\n\n----------------------------------------------")
			print ("  1  -  Update User")
			print ("  2  -  Update Club")
			print ("  3  -  Update Event")
			print ("  4  -  Update Leadership Position")
			print ("  5  -  Update Club Membership")
			print ("  6  -  Go Back")
			print ("---------------------------")
			user_choice_3 = int(input("Select the option you would like to complete: "))
			if (user_choice_3 < 1 or user_choice_3 > 6) :
				choice3 = ERROR;
			
			else :
				choice3 = user_choice_3;
				
			if ( choice3 == 1):
				print ("\n\n----------------------------------------------")
				print ("  1  -  Update User Name")
				print ("  2  -  Update User Email")
				print ("  3  -  Update User Role")
				print ("  4  -  Go Back")
				print ("---------------------------")
				user_choice_4 = int(input("Select the option you would like to complete: "))
				if (user_choice_4 < 1 or user_choice_4 > 4) :
					choice4 = ERROR;
				
				else :
					choice4 = user_choice_4;
				
				if ( choice4 == 1):
					update_user_name()
				elif ( choice4 == 2):
					update_user_email()
				elif ( choice4 == 3):
					update_user_role()
				elif (choice4 == 4):
					choice = Go_Back
					print("Going back...")
					menu()
				else:  
					print ("ERROR: ", choice, "is an invalid input. Try again.")	
		

			elif ( choice3 == 2):
				print ("\n\n----------------------------------------------")
				print ("  1  -  Update Club Name")
				print ("  2  -  Update SGA Recognition")
				print ("  3  -  Update Club Budget")
				print ("  4  -  Update Club Executive Board Positions")
				print ("  5  -  Go Back")
				print ("---------------------------")
				user_choice_5 = int(input("Select the option you would like to complete: "))
				if (user_choice_5 < 1 or user_choice_5 > 5) :
					choice5 = ERROR;
				
				else :
					choice5 = user_choice_5;
				if ( choice5 == 1):
					update_club_name()
				elif ( choice5 == 2):
					update_club_sga()
				elif ( choice5 == 3):
					update_club_budget()
				elif ( choice5 == 4):
					update_club_exec_positions()
				elif (choice5 == 5):
					choice = Go_Back
					print("Going back...")
					menu()
				else:  
					print ("ERROR: ", choice, "is an invalid input. Try again.")	
			
			elif ( choice3 == 3):
				print ("\n\n----------------------------------------------")
				print ("  1  -  Update Event Name")
				print ("  2  -  Update Event Description")
				print ("  3  -  Update Event Hosting Organization")
				print ("  4  -  Update Event RSVP count")
				print ("  5  -  Update Event Location")
				print ("  6  -  Update Event Date")
				print ("  7  -  Update Event Time")
				print ("  8  -  Update Event Category")
				print ("  9  -  Go Back")
				print ("---------------------------")
				user_choice_6 = int(input("Select the option you would like to complete: ")) 
				if (user_choice_6 < 1 or user_choice_6 > 9) :
					choice6 = ERROR;
				
				else :
					choice6 = user_choice_6;
				if ( choice6 == 1):
					update_event_name()
				elif ( choice6 == 2):
					update_event_description()
				elif ( choice6 == 3):
					update_event_host_org()
				elif ( choice6 == 4):
					update_event_rsvp()
				elif ( choice6 == 5):
					update_event_location()
				elif ( choice6 == 6):
					update_event_date()
				elif ( choice6 == 7):
					update_event_time()
				elif ( choice6 == 8):
					update_event_category()
				elif (choice6 == 9):
					choice = Go_Back
					print("Going back...")
					menu()
				else:  
					print ("ERROR: ", choice, "is an invalid input. Try again.")	
				

			elif ( choice3 == 4):
				print ("\n\n----------------------------------------------")
				print ("  1  -  Update Leadership Leadership Title")
				print ("  2  -  Update Leadership Year Entered")
				print ("  3  -  Update Leadership Year Exited")
				print ("  4  -  Go Back")
				print ("---------------------------")
				user_choice_7 = int(input("Select the option you would like to complete: "))
				if (user_choice_7 < 1 or user_choice_7 > 4) :
					choice7 = ERROR;
				
				else :
					choice7 = user_choice_7;
				if ( choice7 == 1):
					update_leadership_title()
				elif ( choice7 == 2):
					update_leadership_year_entered()
				elif ( choice7 == 3):
					update_leadership_year_exited()
				elif (choice7 == 4):
					choice = Go_Back
					print("Going back...")
					menu()
				else:  
					print ("ERROR: ", choice, "is an invalid input. Try again.")	
				

			elif ( choice3 == 5):
				print ("\n\n----------------------------------------------")
				print ("  1  -  Update Club Membership Name")
				print ("  2  -  Update Club Membership Email")
				print ("  3  -  Update Club Membership Join Date")
				print ("  4  -  Go Back")
				print ("---------------------------")
				user_choice_8 = int(input("Select the option you would like to complete: "))
				if (user_choice_8 < 1 or user_choice_8 > 4) :
					choice7 = ERROR;
				
				else :
					choice8 = user_choice_8;
				if ( choice7 == 1):
					update_club_member_name()
				elif ( choice7 == 2):
					update_club_member_email()
				elif ( choice7 == 3):
					update_club_member_join_date()
				elif (choice7 == 4):
					choice = Go_Back
					print("Going back...")
					menu()
				else:  
					print ("ERROR: ", choice, "is an invalid input. Try again.")	
				

			elif ( choice3 == 6):
				choice = Go_Back
				print("Going back...")
				menu()


		elif ( choice == 3):
			print ("\n\n----------------------------------------------")
			print ("  1  -  Delete User")
			print ("  2  -  Delete Event by Event ID")
			print ("  3  -  Delete Event by Event Name")
			print ("  4  -  Go Back")
			print ("---------------------------")
			user_choice_8 = int(input("Select the option you would like to complete: "))
			if (user_choice_8 < 1 or user_choice_8 > 4) :
				choice8 = ERROR;
			
			else :
				choice8 = user_choice_8;
			if ( choice8 == 1):
				delete_user()
			elif ( choice8 == 2):
				delete_eventID()
			elif ( choice8 == 3):
				delete_event_name()				
			elif (choice8 == 4):
				choice = Go_Back
				print("Going back...")
				menu()
			else:  
				print ("ERROR: ", choice, "is an invalid input. Try again.")	
				

		elif ( choice == 4):
			print ("\n\n----------------------------------------------")
			print ("  1  - View Club Exec Board")
			print ("  2  -  View Club Member Roster")
			print ("  3  -  View Events within a Category")
			print ("  4  -  View Events hosted by an Organization")
			print ("  5  -  View Events on a Specific Day")
			print ("  6  -  Go Back")
			print ("---------------------------")
			user_choice_9 = int(input("Select the option you would like to complete: "))
			if (user_choice_9 < 1 or user_choice_9 > 6) :
				choice9 = ERROR;
			
			else :
				choice9 = user_choice_9;
			if ( choice9 == 1):
				view_exec()
			elif ( choice9 == 2):
				view_member()
			elif ( choice9 == 3):
				view_event_category()
			elif ( choice9 == 4):
				view_event_org()
			elif ( choice9 == 5):
				view_event_day()
			elif (choice9 == 6):
				choice = Go_Back
				print("Going back...")
				menu()
			else:  
				print ("ERROR: ", choice, "is an invalid input. Try again.")	
 
		elif ( choice == 5):
			view_transcript()
			
		elif (choice == 6):
			choice = Go_Back
			print("Going back...")
			menu()
		else:  
			print ("ERROR: ", choice, "is an invalid input. Try again.")	
		

# FORMAT OUTPUT FUNCTION: 
		
def format_output(results):	# results will be the result of cursor.fetchall()
	
	for row in results:
		for item in row:
			if item != None:
				print("{: <50}".format(item), end="")
			else:
				print("{: <50}".format("None"), end="")
		print()
	print()


# INSERT USER FUNCTION: 

def insert_user():

	global connection
	global cursor
	userwID_input = int(input("Please enter a wID: "))
	username = input("Please enter a name: ") 
	useremail = input("Please enter an email: ") 
	userrole = input("Please enter a role: ") 
	print("You are about to insert the following information") 
	print("User ID: ", userwID_input)
	print("User Name: ", username)
	print("User email: ", useremail)
	print("User Role: ", userrole)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':
	

		insert_user_query = "INSERT INTO User (wid, user_name, user_email, user_role) VALUES (?, ?, ?, ?)" 

		try:
			cursor.execute(insert_user_query, (userwID_input, username, useremail, userrole))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)
			
	else: 
		print("Please re-enter the information for inserting a user: ")
		insert_user()


# INSERT CLUB FUNCTION 

def insert_club():
	
	orgnum = int(input("Please enter a number: "))
	orgname = input("Please enter a name: ") 
	SGArec = input("Is this club SGA recognized? ") 
	budget = int(input("Please enter a budget: "))
	execroles = input("Please enter exec positions: ") 
	
	print("You are about to insert the following information") 
	print("Organization Number: ", orgnum)
	print("Organization Name: ", orgname)
	print("SGA Recognition: ", SGArec)
	print("Budget: ", budget)
	print("Exec Board Roles: ", execroles)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':	
	
		insert_club_query = "INSERT INTO Club (org_num, org_name, SGA_recognition, budget,exec_positions)VALUES (?, \
		?, ?, ?, ?)"
		try:
			cursor.execute(insert_club_query, (orgnum, orgname, SGArec, budget, execroles))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)		
		
	else: 
		print("Please re-enter the information for inserting a club ")
		insert_club()


# INSERT EVENT FUNCTION 

def insert_event():

	global connection
	global cursor
	event_ID = int(input("Please enter an event ID: "))
	description = input("Please enter an event description: ")
	name = input("Please enter an event name: ")
	hosting_org = int(input("Please enter the hosting organization ID: "))
	RSVP = int(input("Please enter the number of RSVP guests: "))
	location = input("Please enter a location: ")
	date = input("Please enter a date: ")
	time = input("Please enter a time: ")
	category = input("Please enter a category: ")
	

	print("You are about to insert the following information") 
	print("Event ID: ", event_ID)
	print("Event Description: ", descfription)
	print("Event Name: ", name)
	print("Hosting Organization: ", hosting_org)
	print("RSVP: ", RSVP)
	print("Location: ", location)
	print("Date: ", date)
	print("Time: ", time)
	print("Category: ", category)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':		
	
		insert_event_query = "INSERT INTO Event (event_ID, description, name, hosting_org, RSVP, location, date, time, category)\
				      VALUES (?,?,?,?,?,?,?,?,?)"
		
		try: 
			cursor.execute(insert_event_query, (event_ID, description, name, hosting_org, RSVP, location, date, time, category))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)
	
	
	else: 
		print("Please re-enter the information for inserting an event: ")
		insert_event()



# INSERT LEADERSHIP FUNCTION 

def insert_leadership():
	wID = int(input("Please enter a wID: "))
	org_num = int(input("Please enter an organization number: "))
	leadership_title = input("Please enter a leaadership role title: ")
	year_entered = int(input("Please enter the year entered into the position: "))
	year_exited = int(input("Please enter the year exiting the position: "))
	
	
	print("You are about to insert the following information") 
	print("wID: ", wID)
	print("Organization Number: ", org_num)
	print("Leadership Title: ", leadership_title)
	print("Year Entered: ", year_entered)
	print("Year Exited: ", year_exited)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':			
		
		insert_leadership_query = "INSERT INTO ClubLeadership (wID, org_num, leadership_title, year_enter, year_exit) VALUES (?, ?, \
		?, ?, ?)"
		
		try: 
			cursor.execute(insert_leadership_query, (wID, org_num, leadership_title, year_entered, year_exited))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)	
			
	else: 
		print("Please re-enter the information for inserting a club leadership position: ")
		insert_leadership()
		
# INSERT MEMBER FUNCTION 

def insert_membership():
	wID = int(input("Please enter a wID: "))
	member_name = input("Please enter the member's name: ") 
	member_email = input("Please enter the member's email: ") 
	org_num = int(input("Please enter an organization number: "))
	join_date = input("Please enter the date the member joined: ") 
	
	print("You are about to insert the following information") 
	print("wID: ",wID)
	print("Member Name: ", member_name)
	print("Member Email: ", member_email)
	print("Organization Number: ", org_num)
	print("Date Joined: ", join_date)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':				
	
		insert_membership_query = "INSERT INTO ClubMembership (wID, member_name, member_email, org_num, join_date) \
		VALUES(?, ?, ?, ?, ?)"
		
		try: 
			cursor.execute(insert_membership_query, (wID, member_name, member_email, org_num, join_date))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)	
		
	else: 
		print("Please re-enter the information for inserting a club member: ") 
		insert_membership()
		
		
# DELETE USER FUNCTION 

def delete_user():
	global connection
	global cursor 
	
	wID = input("Please enter the wID of the user you would like to delete: ")
	
	sql = "DELETE FROM User\
	       WHERE wID = ?"
	
	print("You are about to delete the user with the wID ", wID, " from the database.")
	confirmation = input("Are you sure you want to permanently delete this user? Y or N: ")
	
	while (confirmation != 0):
		if confirmation == "Y":
			try:
				cursor.execute(sql, wID)
				connection.commit()				
			except sqlite3.OperationalError as e:
				print(e)		
		elif confirmation == "N":
			wID = input("Please enter the wID of the user you would like to delete: ")
		else:
			confirmation = input("Bad input. Please enter Y or N")
	

# DELETE EVENT BY ID FUNCTION 
def delete_eventID():
	global connection
	global cursor 
	
	event_ID = input("Please enter the ID of the event you would like to delete: ")
	
	sql = "DELETE FROM Event\
	       WHERE Event_ID = ?"
	
	print("You are about to delete the event with the eventID ", event_ID, " from the database.")
	confirmation = input("Are you sure you want to permanently delete this event? Y or N: ")
	
	while (confirmation != ""):
		if confirmation == "Y":
			try:
				cursor.execute(sql, (event_ID,))
				connection.commit()
			except sqlite3.OperationalError as e:
				print(e)
			break
		elif confirmation == "N":
			break
		else:
			confirmation = input("Bad input. Please enter Y or N")	



#DELETE EVENT BY NAME FUNCTION 
def delete_event_name():
	global connection
	global cursor 
	
	event_name = input("Please enter the name of the event you would like to delete: ")
	
	sql = "DELETE FROM Event\
	       WHERE Name = ?"
	
	print("You are about to delete the event with the name ", event_name, " from the database.")
	confirmation = input("Are you sure you want to permanently delete this event? Y or N: ")
	
	if confirmation == "Y":
		try:
			cursor.execute(sql, (event_name,))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)		
	elif confirmation == "N":
		wID = input("Please enter the wID of the user you would like to delete: ")
	else:
		confirmation = input("Bad input. Please enter Y or N")		
		
		
		
# VIEW EXEC FUNCTION 

def view_exec():
	
	global connection
	global cursor
	
	org_num = int(input("Please enter the club you want to view the executive board for: "))
	
	view_exec_query = "CREATE TEMP VIEW exec_board AS\
	                   SELECT ClubLeadership.wID, User.user_name, ClubLeadership.org_num, ClubLeadership.leadership_title\
	                   FROM ClubLeadership\
			   INNER JOIN User\
			   ON ClubLeadership.wID = User.wID\
			   WHERE ClubLeadership.org_num = 69976"
	
	
	try:
		cursor.execute(view_exec_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
	
	get_table_query = "SELECT user_name, leadership_title\
	                   FROM exec_board"
	
	try:
		cursor.execute(get_table_query)
		print("Name                               Position Title")  
		format_output(cursor.fetchall())
	except sqlite3.OperationalError as e:
		print(e)
	
	drop_table_query = "DROP VIEW exec_board"
	
	try:
		cursor.execute(drop_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
		
		
		
# VIEW MEMBER FUNCTION :

def view_member():
	
	global connection
	global cursor
	
	org_num = int(input("Please enter the club you want to view the members for: "))
	
	view_member_query = "CREATE TEMP VIEW roster AS\
	                     SELECT ClubMembership.wID, User.user_name, ClubMembership.org_num\
			     FROM ClubMembership\
			     INNER JOIN User\
			     ON ClubMembership.wID = User.wID\
			     WHERE ClubMembership.org_num = 179898"
	
	
	try:
		cursor.execute(view_member_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)	
	
	get_table_query = "SELECT user_name\
			   FROM roster"
	
	try:
		cursor.execute(get_table_query)
		print("-"*40)
		print("Member Names for organiation number:" ,org_num)
		format_output(cursor.fetchall())
	except sqlite3.OperationalError as e:
		print(e)
	
	drop_table_query = "DROP VIEW roster"
	
	try:
		cursor.execute(drop_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)	
		
		

# SEARCH & VIEW EVENT BY CATEGORY FUNCTION 
2
def view_event_category():

	global connection
	global cursor 
	
	event_category = input("Please enter the category you want to view events in: ")
	
	view_event_category = "CREATE TEMP VIEW Event_category AS\
	                       SELECT Event.event_ID, Event.Name, Event.hosting_org, Event.date, Event.time, Event.category\
	                       FROM Event\
	                       WHERE Event.category = 'Arts'"
	try:
		cursor.execute(view_event_category)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
	
	get_table_query = "SELECT *\
                           FROM Event_category"
	
	try:
		cursor.execute(get_table_query)
		print("-"*40)
		print("Event ID                           Event Title                        Hosting Org Number\
		 Event Date                         Event Time                         Event Category")
		format_output(cursor.fetchall())
	except sqlite3.OperationalError as e:
		print(e)
	
	drop_table_query = "DROP VIEW Event_category"
	
	try:
		cursor.execute(drop_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
		
		
		

# SEARCH & VIEW EVENG BY ORG NUMBER FUNCTION :

def view_event_org():

	global connection
	global cursor 
	
	event_org = int(input("Please enter the host organization you want to view events for: "))
	
	view_event_org = "CREATE TEMP VIEW Event_Org AS\
	                       SELECT Event.event_ID, Event.Name, Event.hosting_org, Event.date, Event.time, Event.category\
	                       FROM Event\
	                       WHERE Event.hosting_org = 179898"
	try:
		cursor.execute(view_event_org)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
	
	get_table_query = "SELECT *\
                           FROM Event_Org"
	
	try:
		cursor.execute(get_table_query)
		print("-"*40)
		print("Events by Org number:", event_org)
		print("Event ID                           Event Title                        Hosting Org Number\
		 Event Date                         Event Time                         Event Category")		
		format_output(cursor.fetchall())
	except sqlite3.OperationalError as e:
		print(e)
	
	drop_table_query = "DROP VIEW Event_Org"
	
	try:
		cursor.execute(drop_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
		
		

# SEARCH & VIEW EVENT BY DAY FUNCTION :

def view_event_day():

	global connection
	global cursor 
	
	event_day = input("Please enter the day you want to see events on: ")
	
	view_event_day = "CREATE TEMP VIEW Event_Day AS\
	                       SELECT Event.event_ID, Event.Name, Event.hosting_org, Event.date, Event.time, Event.category\
	                       FROM Event\
	                       WHERE Event.date = '9/30/2020'"
	try:
		cursor.execute(view_event_day)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
	
	get_table_query = "SELECT *\
                           FROM Event_Day"
	
	try:
		cursor.execute(get_table_query)
		print("-"*40)
		print("Events on Date:",event_day)
		print("Event ID                           Event Title                        Hosting Org Number\
		 Event Date                         Event Time                         Event Category")		
		
		format_output(cursor.fetchall())
	except sqlite3.OperationalError as e:
		print(e)
	
	drop_table_query = "DROP VIEW Event_Day"
	
	try:
		cursor.execute(drop_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)


# VIEW TRANSCRIPT FUNCTION 

def view_transcript():
	global connection
	global cursor 
	
	user_ID = int(input("Please enter the user ID you would like the transcript for: "))
	
	create_temp_table_query = "CREATE TABLE TempTableTranscript (wID int, name text, leadership_position text, leader_org_num int)" 
	try:
		cursor.execute(create_temp_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
		
	
	insert_temp_table = "INSERT INTO TempTableTranscript SELECT User.wID, User.user_name, ClubLeadership.leadership_title, \
	ClubLeadership.org_num FROM User, ClubLeadership WHERE User.wID = ? \
	AND (ClubLeadership.leadership_title, ClubLeadership.org_num) IN (SELECT ClubLeadership.leadership_title, \
	ClubLeadership.org_num FROM ClubLeadership WHERE ClubLeadership.wID = ?)  "
	
	try:
		cursor.execute(insert_temp_table, (user_ID, user_ID))
		connection.commit()
		print("done")
	except sqlite3.OperationalError as e:
		print(e)
		
	view_temp_table_query = "CREATE VIEW transcript AS\
	                         SELECT wID, name, leadership_position, leader_org_num\
	                         FROM TempTableTranscript\
	                         WHERE wID = 64"
	try:
		cursor.execute(view_temp_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)	
	
	
	get_table_query = "SELECT *\
			   FROM transcript"
	
	try:
		cursor.execute(get_table_query)
		print("-"*40)
		print("Transcript for user:", user_ID)
		print("\nwID                                User Name                          Position Title\
		         Org number")		
		format_output(cursor.fetchall())
	except sqlite3.OperationalError as e:
		print(e)
	
	drop_view_query = "DROP VIEW transcript"
	
	try:
		cursor.execute(drop_view_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
		
	drop_table_query = "DROP TABLE TempTableTranscript"
	
	try:
		cursor.execute(drop_table_query)
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)

# UPDATE USER NAME FUNCTION: 

def update_user_name():
	global connection
	global cursor 
	
	wID = int(input("Please enter a user wID number: "))
	user_name = input("Please enter an updated name for this user: ")
	
	
	print("You are about to change the name for user number ? to ?", wID, user_name)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':
		
		update_user_name_query = "UPDATE User SET user_name = ? WHERE wID = ?"
		try:
			cursor.execute(update_user_name_query, (user_name, wID))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)	
			
	else: 
		print("Please re-enter the information to update a user name: ")
		update_user_name()
		
		
# UPDATE USER EMAIL FUNCTION 

def update_user_email():
	
	global connection
	global cursor
	
	wID = int(input("Please enter a user wID number: "))
	user_email = input("Please enter the updated user email: ")
	
	print("You are about to change the email for user number ? to ?", wID, user_email)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':
		
		update_user_email_query = "UPDATE User SET user_email = ? WHERE wID = ?" 
		
		try:
			cursor.execute(update_user_email_query, (user_email, wID))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)		
			
	else:
		print("Please re-enter the information to update a user email: ")
		update_user_email()
		
		
# UPDATE USER ROLE FUNCTION : 

def update_user_role(): 
	
	global connection
	global cursor
	
	wID = int(input("Please enter a user wID number: "))
	user_role = input("Please enter the updated role for this user: ")
	
	print("You are about to change the role for user number ? to ?", wID, user_role)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':
		
		
		update_user_role_query = "UPDATE User SET user_role = ? WHERE wID = ?" 
		
		try:
			cursor.execute(update_user_role_query, (user_role, wID))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)	
		
	
	else: 
		print("Please re-enter the information to update a user role: ")
		update_user_role()		
		
		
# UPDATE CLUB NAME FUNCTION 

def update_club_name():
	
	global connection
	global cursor	
	org_num = int(input("Please enter the ID for the Organization you want to change: "))
	org_name = input("Please enter the New name for the organization: ") 
	
	print("You are about to change the name for club number ? to ?", org_num, org_name)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':
	
		
		update_club_name_query = "UPDATE Club SET org_name = ? WHERE org_num = ?"
		
		try:
			cursor.execute(update_club_name_query, (org_name, org_num))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)		
	
	else:
		print("Please re-enter the information to update a club name: ")
		upadte_club_name()

# UPDATE CLUB SGA FUNCTION

def update_club_sga():
	
	global connection
	global cursor	
	org_num = int(input("Which organization number are you updating the SGA recognition status for? "))
	SGA_recognition = input("Is this club an SGA recognized club? ") 
		
		
	print("You are about to change the SGA recognition status for club number ? to ?", org_num, SGA_recognition)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':
	
			
		update_club_sga_query = "UPDATE Club SET SGA_recognition = ? WHERE org_num = ?"
		
		try:
			cursor.execute(update_club_sga_query, (SGA_recognition, org_num))
			connection.commit()
		except sqlite3.OperationalError as e:
			print(e)	
	else:
		print("Please re-enter the information to update a club's SGA recognition status: ")
		upadte_club_sga()				
		

# UPDATE CLUB BUDGET FUNCTION

def update_club_budget():

	global connection
	global cursor
	
	org_num = int(input("Please enter the organization number that you want to update: "))
	budget_amount = int(input("Please enter the new budget for this organization. "))
	
	print("You are about to change the budget for club number ? to ?", org_num, budget_amount)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':	
		
		update_club_budget_query = "UPDATE Club SET budget = ? WHERE org_num = ?"
		
	
		try:
			cursor.execute(update_club_budget_query, (budget_amount, org_num))
			connection.commit()
			#print(update_club_budget_query)
	
		except sqlite3.OperationalError as e:
			print(e)
			
	else:
		print("Please re-enter the information to update a club's budget: ")
		upadte_club_budget()			

# UPDATE CLUB EXEC POSITIONS FUNCTION

def update_club_exec_positions(): 
	
	global connection
	global cursor
	
	org_num = int(input("Please enter the organization number that you want to update: "))
	exec_positions = input("Please enter the updated list of exec board positions: ")
	
	print("You are about to change the exec board positions for club number ? to ?", org_num, exec_positions)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':	
			
		update_club_exec_positions_query = "UPDATE Club SET exec_positions = ? WHERE org_num = ?"
		
		try:
			cursor.execute(update_club_exec_positions_query, (exec_positions, org_num))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	
	
	else:
		print("Please re-enter the information to update a club's exec board positions: ")
		upadte_club_exec_positions()		

# UPDATE EVENT NAME FUNCTION 

def update_event_name(): 
	
	global connection
	global cursor	
	
	event_ID =  input("Please enter the event id: ")
	event_name = input("Please enter the updated name for the event: ") 
	
	print("You are about to change the name for event ID number ? to ?", event_ID, event_name)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':	
		
		update_event_name_query = "UPDATE Event SET Name = ? WHERE event_ID = ?"
		
		try:
			cursor.execute(update_event_name_query, (event_name, event_ID))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)		
	
	else:
		print("Please re-enter the information to update an events name: ")
		upadte_event_name()	

# UPDATE EVENT DESCRIPTON FUNCTION 

def update_event_description():
	global connection
	global cursor 
	
	updated_description = input("Please enter new description for the event: ")
	event_id = int(input("Please enter the event id: "))
	
	sql = "UPDATE Event\
	       SET Description = ?\
	       WHERE Event_ID = ?"
	print("You are about to update the event with the ID ", event_id, "from the database.")
	confirmation = input("Are you sure you want to permanently update this event? Y or N: ")
	
	while (confirmation != 0):
		if confirmation == "Y":
			try:
				cursor.execute(sql, (updated_description, event_id))
				connection.commit()
			except sqlite3.OperationalError as e:
				print(e)
			break
		elif confirmation == "N":
			break
		else:
			confirmation = input("Bad input. Please enter Y or N")	


#UPDATE EVENT HOST ORG FUCNTION 

def update_event_host_org():
	global connection
	global cursor 
	
	updated_host_org = input("Please enter new hosting organization for the event: ")
	event_id = int(input("Please enter the event id: "))
	
	sql = "UPDATE Event\
	       SET Hosting_org = ?\
	       WHERE Event_ID = ?"
	
	print("You are about to update the event with the ID ", event_id, "from the database.")
	confirmation = input("Are you sure you want to permanently update this event? Y or N: ")	

	while (confirmation != 0):
		if confirmation == "Y":
			try:
				cursor.execute(sql, (updated_host_org, event_id))
				connection.commit()	
			except sqlite3.OperationalError as e:
				print(e)				
			break
		elif confirmation == "N":
			break
		else:
			confirmation = input("Bad input. Please enter Y or N")	
			

#UPDATE EVENT LOCATION FUNCTION 

def update_event_location():
	global connection
	global cursor 
	
	updated_location = input("Please enter new location for the event: ")
	event_id = int(input("Please enter the event id: "))
	
	sql = "UPDATE Event\
	       SET Location = ?\
	       WHERE Event_ID = ?"
	
	print("You are about to update the event with the ID ", event_id, "from the database.")
	confirmation = input("Are you sure you want to permanently update this event? Y or N: ")
	
	while (confirmation != ""):
		if confirmation == "Y":
			try:
				cursor.execute(sql, (updated_location, event_id))
				connection.commit()	
			except sqlite3.OperationalError as e:
				print(e)						
			break
		elif confirmation == "N":
			break
		else:
			confirmation = input("Bad input. Please enter Y or N")	
			


#UPDATE EVENT DATE FUNCTION 

def update_event_date():
	global connection
	global cursor 
	
	updated_date = input("Please enter new date for the event: ")
	event_id = int(input("Please enter the event id: "))
	
	sql = "UPDATE Event\
	       SET Date = ?\
	       WHERE Event_ID = ?"
	
	print("You are about to update the event with the ID ", event_id, "from the database.")
	confirmation = input("Are you sure you want to permanently update this event? Y or N: ")
	
	while (confirmation != ""):
		if confirmation == "Y":
			try:
				cursor.execute(sql, (updated_date, event_id))
				connection.commit()	
			except sqlite3.OperationalError as e:
				print(e)							
			break
		elif confirmation == "N":
			break
		else:
			confirmation = input("Bad input. Please enter Y or N")	
			
			

#UPDATE EVENT TIME FUNCTION 

def update_event_time():
	global connection
	global cursor 
	
	updated_time = input("Please enter new time for the event: ")
	event_id = int(input("Please enter the event id: "))
	
	sql = "UPDATE Event\
	       SET Time = ?\
	       WHERE Event_ID = ?"
	
	print("You are about to update the event with the ID ", event_id, "from the database.")
	confirmation = input("Are you sure you want to permanently update this event? Y or N: ")
	
	while (confirmation != ""):
		if confirmation == "Y":
			try:
				cursor.execute(sql, (updated_time, event_id))
				connection.commit()	
			except sqlite3.OperationalError as e:
				print(e)							
			break
		elif confirmation == "N":
			break
		else:
			confirmation = input("Bad input. Please enter Y or N")	


#UPDATE EVENT RSVP FUNCTION 

def update_event_rsvp():
	global connection
	global cursor 
	
	updated_rsvp = input("Please enter new Rsvp number for the event: ")
	event_id = int(input("Please enter the event id: "))
	
	sql = "UPDATE Event\
	       SET RSVP = ?\
	       WHERE Event_ID = ?"
	
	print("You are about to update the event with the ID ", event_id, "from the database.")
	confirmation = input("Are you sure you want to permanently update this event? Y or N: ")
	
	while (confirmation != ""):
		if confirmation == "Y":
			try:
				cursor.execute(sql, (updated_rsvp, event_id))
				connection.commit()	
			except sqlite3.OperationalError as e:
				print(e)							
			break
		elif confirmation == "N":
			break
		else:
			confirmation = input("Bad input. Please enter Y or N")	

	try:
		cursor.execute(sql, (updated_rsvp, event_id))
		connection.commit()
	except sqlite3.OperationalError as e:
		print(e)
		
		
# UPDATE EVENT CATEGORY FUNCTION 		

def update_event_category():
	global connection
	global cursor	
	
	event_ID =  input("Please enter the event id: ")
	event_category = input("Please enter the updated category for the event: ") 
	
	print("You are about to change the name for event ID number ? to ?", event_ID, event_name)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':	
			
		update_event_name_query = "UPDATE Event SET category = ? WHERE event_ID = ?"
		
		try:
			cursor.execute(update_event_category_query, (event_category, event_ID))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	
			
	else:
		print("Please re-enter the information to update an events category: ")
		upadte_event_category()		
		
		
# UPDATE LEADERSHIP TITLE FUNCTION 

def update_leadership_title():
	
	global connection
	global cursor	
	
	wID =  int(input("Please enter a wID: "))
	org_num = int(input("Please enter an organization number: ") )
	leadership_title = input("Please enter the new leadership title: ")
	
	print("You are about to change the leadership title for user number ? in organization number ? to ?", wID, org_num, leadership_title)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':		
	
		update_leadership_title_query = "UPDATE ClubLeadership SET leadership_title = ? \
		WHERE wID = ? AND org_num = ?"
		
		try:
			cursor.execute(update_leadership_title_query, (leadership_title, wID, org_num))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	
			
	else:
		print("Please re-enter the information to update a leadership position title: ")
		upadte_leadership_title()	


# UPDATE LEADERSHIP YEAR ENTERED FUNCTION 

def update_leadership_year_entered():
	
	global connection
	global cursor	
	
	wID =  int(input("Please enter a wID: "))
	org_num = int(input("Please enter an organization number: ") )
	year_entered = input("Please enter the updated year entered: ")
	
	print("You are about to change the leadership year entered for user number ? in organization number ? to ?", wID, org_num, year_entered)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':		
		
		update_leadership_year_entered_query = "UPDATE ClubLeadership SET year_enter = ? \
		WHERE wID = ? AND org_num = ?"
		
		try:
			cursor.execute(update_leadership_year_entered_query, (year_entered, wID, org_num))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	
			
	else:
		print("Please re-enter the information to update a leadership position year entered: ")
		upadte_leadership_year_entered()		


#UPDATE LEADERSHIP YEAR EXITED FUNCTION 

def update_leadership_year_exited():
	
	global connection
	global cursor	
	
	wID =  int(input("Please enter a wID: "))
	org_num = int(input("Please enter an organization number: ") )
	year_exited = input("Please enter the updated year exited: ")
	
	print("You are about to change the leadership year exited for user number ? in organization number ? to ?", wID, org_num, year_exited)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':		
	
		update_leadership_year_exited_query = "UPDATE ClubLeadership SET year_exit = ? \
		WHERE wID = ? AND org_num = ?"
		
		try:
			cursor.execute(update_leadership_year_exited_query, (year_exited, wID, org_num))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	

	else:
		print("Please re-enter the information to update a leadership position year exited: ")
		upadte_leadership_year_exited()		


# UPDATE CLUB MEMBER NAME

def update_club_member_name():
	
	global connection
	global cursor	
	
	wID =  int(input("Please enter a wID: "))
	org_num = int(input("Please enter an organization number: ") )
	member_name = input("Please enter the updated club member name: ")
	
	print("You are about to change the member name for user number ? in organization number ? to ?", wID, org_num, member_name)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':		
	
		update_membership_name_query = "UPDATE ClubMembership SET member_name = ? \
		WHERE wID = ? AND org_num = ?"
		
		try:
			cursor.execute(update_membership_name_query, (member_name, wID, org_num))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	
		
	else:
		print("Please re-enter the information to update a member's name: ")
		upadte_club_member_name()		
	

# UPDATE CLUB MEMBER EMAIL 

def update_club_member_email():
	
	global connection
	global cursor	
	
	wID =  int(input("Please enter a wID: "))
	org_num = int(input("Please enter an organization number: ") )
	member_email = input("Please enter the updated club member email: ")
	
	print("You are about to change the member email for user number ? in organization number ? to ?", wID, org_num, member_email)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':		
	
		update_membership_name_query = "UPDATE ClubMembership SET member_email = ? \
		WHERE wID = ? AND org_num = ?"
		
		try:
			cursor.execute(update_membership_email_query, (member_email, wID, org_num))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	
			
	else:
		print("Please re-enter the information to update a member's email: ")
		upadte_club_member_email()				
		

#UPDATE CLUB MEMBER JOIN DATE 

def update_club_member_join_date():
	
	global connection
	global cursor	
	
	wID =  int(input("Please enter a wID: "))
	org_num = int(input("Please enter an organization number: ") )
	join_date = input("Please enter the updated member join date: ")
	
	print("You are about to change the member join date for user number ? in organization number ? to ?", wID, org_num, join_date)
	user_confirmation = input("Would you like to continue? Y or N: ")
	if user_confirmation == 'Y':		
	
		update_membership_join_date_query = "UPDATE ClubMembership SET join_date = ? \
		WHERE wID = ? AND org_num = ?"
		
		try:
			cursor.execute(update_membership_join_date_query, (join_date, wID, org_num))
			connection.commit()
	
		except sqlite3.OperationalError as e:
			print(e)	
			
	else:
		print("Please re-enter the information to update a member's join date: ")
		upadte_club_member_join_date()		
		
		

# COUNT LEADERSHIP TOTAL YEARS
def leadership_total_years():
	global connection
	global cursor 
	
	sql = "SELECT User_ID, wID, Org_name, Leadership_title, DATEDIFF(year, ?, GETDATE()) AS num_years_exec\
	       FROM Memberships, User, Club, ClubLeadership\
	       WHERE User_ID = ?"
	try:
		cursor.execute(sql)
	except sqlite3.OperationalError as e:
		print(e)
		
	

#COUNT MEMBERSHIP TOTAL YEARS 

def yrs_in_club():
	global connection
	global cursor 
	
	sql = "SELECT User_ID, wID, DATEDIFF(year, (start date), GETDATE()) AS num_years_club\
	        FROM Memberships, User\
		WHERE User_ID = wID"
	try:
		cursor.execute(sql)
	except sqlite3.OperationalError as e:
		print(e)
		
		

# COUNT MEMBERS FUNCTION 

def num_member():
	global connection
	global cursor 
	
	sql = "SELECT COUNT(*) FROM ClubMembership\
               WHERE org_num = ?"
	
	try:		
		cursor.execute(sql)
	except sqlite3.OperationalError as e:
		print(e)


# COUNT RSVP FUNCTION 

def num_rsvp_total():
	global connection
	global cursor 
	
	sql = "SELECT SUM(RSVP)\
	       AS total_rsvps\
	       FROM Event"
	
	try:		
		cursor.execute(sql)
	except sqlite3.OperationalError as e:
		print(e)	

		

# MAIN FUNCTION: 

def main():
	
	print('-'*40)	
	print("Welcome to CampusParty!")
	print("What would you like to do today?")
	
	menu()
	
	print('-'*40)
	print("Thank you for using CampusParty!")	
	
main()
