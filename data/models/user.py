from data.database import Database

def obtain_user(user_id):
    obtain_users_sql = f"""
        SELECT id, username, role 
        FROM USER 
        WHERE ID = {user_id}
    """
    bd = Database()
    return [{"id": register[0],
             "username": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_users_sql)]

def obtain_users():
    obtain_users_sql = f"""
        SELECT id, username, role 
        FROM USER 
    """
    bd = Database()
    return [{"id": register[0],
             "username": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_users_sql)]

def create_user(username, password, mail):
    create_user_sql = f"""
        INSERT INTO USER(USERNAME, PASSWORD, MAIL)
        VALUES ('{username}','{password}','{mail}')
    """
    bd = Database()
    bd.execute_sql(create_user_sql)


def modify_user(user_id, user_data):
    modify_user_sql = f"""
        UPDATE USER
        SET USERNAME='{user_data["username"]}', PASSWORD='{user_data["password"]}'
        WHERE ID='{user_id}'
    """
    bd = Database()
    bd.execute_sql(modify_user_sql)


def obtain_user_by_username_password(username, password):
    obtain_user_sql = f"""
            SELECT id, username, role 
            FROM USER u
            WHERE USERNAME='{username}' and PASSWORD='{password}'
        """
    bd = Database()
    return [{"id": register[0],
             "username": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_user_sql)]


def delete_user(user_id):
    obtain_users_sql = f"""
        DELETE
        FROM USER 
        WHERE ID = {user_id}
    """
    bd = Database()
    bd.execute_sql(obtain_users_sql)


def create_session(user_id, dt_string):
    create_session_sql = f"""
               INSERT INTO SESSIONS(USER_ID, DATE_TIME)
               VALUES ('{user_id}', '{dt_string}')
           """
    bd = Database()
    return bd.execute_sql(create_session_sql, True)


def obtain_session(session_id):
    obtain_session_sql = f"""
        SELECT ID, USER_ID, DATE_TIME FROM SESSIONS WHERE ID = {session_id}
    """
    bd = Database()
    return [{"id": register[0],
             "user_id": register[1],
             "date_time": register[2]}
            for register in bd.execute_sql(obtain_session_sql)]
