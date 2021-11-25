import sqlite3

sql_user = '''
CREATE TABLE USER(
ID INTEGER PRIMARY KEY, 
USERNAME TEXT, 
PASSWORD TEXT, 
MAIL TEXT, 
ROLE TEXT
)
'''

sql_pet = '''
CREATE TABLE PET(
ID INTEGER PRIMARY KEY, 
NAME TEXT, 
APPEARANCE TEXT
)
'''

sql_diary = '''
CREATE TABLE DIARY(
ID INTEGER PRIMARY KEY,
 NAME TEXT,
 TEXT TEXT,
 DATES DATE, 
 PAGES INTEGER, 
 BOOKMARKS STRING
 )
'''

sql_exercise = '''
CREATE TABLE EXERCISE(
TEXT STRING PRIMARY KEY, 
DURATION FLOAT, 
ANIMATION BOOLEAN
)
'''

sql_user_pet = '''
CREATE TABLE USER_PET(
ID_USER INTEGER, 
ID_PET INTEGER, 
FOREIGN KEY(ID_USER) REFERENCES USER(INTEGER), 
FOREIGN KEY(ID_PET) REFERENCES PET(INTEGER)
)
'''

sql_user_diary = '''
CREATE TABLE USER_DIARY(
ID_USER INTEGER, 
ID_DIARY INTEGER, 
FOREIGN KEY(ID_USER) REFERENCES USER(NUMBER), 
FOREIGN KEY(ID_DIARY) REFERENCES DIARY(NAME)
)
'''

sql_user_exercise = '''
CREATE TABLE USER_EXERCISE(
ID_USER INTEGER, 
TEXT_EXERCISE STRING, 
FOREIGN KEY(ID_USER) REFERENCES USER(NUMBER), 
FOREIGN KEY(TEXT_EXERCISE) REFERENCES EXERCISE(STRING)
)
'''

sql_sessions = '''
CREATE TABLE SESSIONS(
IDSE INTEGER PRIMARY KEY,
ID_USER TEXT,
DATE_TIME TEXT,
FOREIGN KEY(ID_USER) REFERENCES USER(ID_USER)
)
'''

if __name__ == '__main__':
    try:
        print('Creating database..')
        connection = sqlite3.connect('../../VirtualPet.db')

        print('Creating tables..')
        connection.execute(sql_user)
        connection.execute(sql_pet)
        connection.execute(sql_diary)
        connection.execute(sql_exercise)
        connection.execute(sql_user_pet)
        connection.execute(sql_user_diary)
        connection.execute(sql_user_exercise)
        connection.execute(sql_sessions)

        connection.close()
        print('Done')
    except Exception as e:
        print(f'Error creating database: {e}', e)
