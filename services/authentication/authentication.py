from data.models import user as user_model
from datetime import datetime

def _user_exists(username, password):
    users = user_model.obtain_users_by_username_password(username, password)
    return not len(users) == 0


def _create_session(user_id):
    current_time = datetime.now()
    #dd/mm/YY H:M:S
    dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
    return user_model.create_session(user_id, dt_string)


def obtain_users():
    return user_model.obtain_users()


def obtain_user(user_id):
    user = user_model.obtain_user(user_id)
    if len(users) == 0:
        raise Exception("Username doesn't exist")
    return users[0]


def create_user(username, password, mail):
    if not _user_exists(username, password):
        user_model.create_user(username, password, mail)
    else:
        raise Exception("Username or mail already exists")


def modify_user(user_id, user_data):
    user_model.modify_user(user_id, user_data)

def delete_user(user_id):
    user_model.delete_user(user_id)


def login(username, password):
    if _diary_exists(username, password):
        user = user_model.obtain_user_by_username_password(username, password)[0]
        return _create_session(user['id'])
    else:
        raise Exception("Username or password is incorrect")


def validate_session(session_id):
    sessions = user_model.obtain_session(session_id)
    if len(sessions) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sessions[0]['date_time'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Session expired
        return False
    else:
        return True
