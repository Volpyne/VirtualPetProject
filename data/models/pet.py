from data.database import Database

def obtain_pet(pet_id):
    obtain_pets_sql = f"""
        SELECT id, name, role 
        FROM PET 
        WHERE ID = {pet_id}
    """
    bd = Database()
    return [{"id": register[0],
             "name": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_pets_sql)]

def obtain_pets(pet_id):
    obtain_pets_sql = f"""
        SELECT id, name, role 
        FROM PET 
    """
    bd = Database()
    return [{"id": register[0],
             "name": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_pets_sql)]

def create_pet(name, appearance):
    create_pet_sql = f"""
        INSERT INTO PET(NAME, APPEARANCE)
        VALUES ('{name}',)
    """
    bd = Database()
    bd.execute_sql(create_pet_sql)


def modify_pet(pet_id, pet_data):
    modify_pet_sql = f"""
        UPDATE PET
        SET NAME='{pet_data["name"]}'
        WHERE ID='{pet_id}'
    """
    bd = Database()
    bd.execute_sql(modify_pet_sql)


def obtain_pet_by_name(name):
    obtain_pet_sql = f"""
            SELECT id, name, role 
            FROM PET u
            WHERE RNAME='{name}'
        """
    bd = Database()
    return [{"id": register[0],
             "name": register[1],
             "role": register[2]
             } for register in bd.execute_sql(obtain_pet_sql)]


def delete_pet(pet_id):
    obtain_pets_sql = f"""
        DELETE
        FROM PET 
        WHERE ID = {pet_id}
    """
    bd = Database()
    bd.execute_sql(obtain_pets_sql)


def create_session(pet_id, dt_string):
    create_session_sql = f"""
               INSERT INTO SESSIONS(PET_ID, DATE_TIME)
               VALUES ('{pet_id}', '{dt_string}')
           """
    bd = Database()
    return bd.execute_sql(create_session_sql, True)


def obtain_session(session_id):
    obtain_session_sql = f"""
        SELECT ID, PET_ID, DATE_TIME FROM SESSIONS WHERE ID = {session_id}
    """
    bd = Database()
    return [{"id": register[0],
             "pet_id": register[1],
             "date_time": register[2]}
            for register in bd.execute_sql(obtain_session_sql)]
