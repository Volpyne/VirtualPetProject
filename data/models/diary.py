from data.database import Database

def obtain_diary(diary_id):
    obtain_diaries_sql = f"""
        SELECT id, name, role
        FROM DIARY 
        WHERE ID = {diary_id}
    """
    bd = Database()
    return [{"id": register[0],
             "name": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_diaries_sql)]

def obtain_diaries():
    obtain_diaries_sql = f"""
        SELECT id, name, role
        FROM DIARY 
    """
    bd = Database()
    return [{"id": register[0],
             "name": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_diaries_sql)]

def create_diary(name):
    create_diary_sql = f"""
        INSERT INTO DIARY(NAME)
        VALUES ('{name}')
    """
    bd = Database()
    bd.execute_sql(create_diary_sql)


def modify_diary(diary_id, diary_data):
    modify_user_sql = f"""
        UPDATE DIARY
        SET NAME='{diary_data["name"]}'
        WHERE ID='{diary_id}'
    """
    bd = Database()
    bd.execute_sql(modify_diary_sql)


def obtain_diary_by_name(name):
    obtain_diary_sql = f"""
            SELECT id, name 
            FROM DIARY u
            WHERE NAME='{name}'
        """
    bd = Database()
    return [{"id": register[0],
             "name": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_diary_sql)]


def delete_diary(diary_id):
    obtain_diaries_sql = f"""
        DELETE
        FROM DIARY 
        WHERE ID = {diary_id}
    """
    bd = Database()
    bd.execute_sql(obtain_diaries_sql)


def create_session(diary_id, dt_string):
    create_session_sql = f"""
               INSERT INTO SESSIONS(DIARY_ID, DATE_TIME)
               VALUES ('{diary_id}', '{dt_string}')
           """
    bd = Database()
    return bd.execute_sql(create_session_sql, True)


def obtain_session(session_id):
    obtain_session_sql = f"""
        SELECT ID, DIARY_ID, DATE_TIME FROM SESSIONS WHERE ID = {session_id}
    """
    bd = Database()
    return [{"id": register[0],
             "diary_id": register[1],
             "date_time": register[2]}
            for register in bd.execute_sql(obtain_session_sql)]