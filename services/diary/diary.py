from data.models import diary as diary_model
from datetime import datetime

def _diary_exists(name):
    diaries = diary_model.obtain_diaries_by_name(name)
    return not len(diaries) == 0


def _create_session(diary_id):
    current_time = datetime.now()
    #dd/mm/YY H:M:S
    dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
    return diary_model.create_session(diary_id, dt_string)


def obtain_diaries():
    return diary_model.obtain_diaries()


def obtain_diary(diary_id):
    user = user_model.obtain_diary(diary_id)
    if len(diaries) == 0:
        raise Exception("Diary with that name doesn't exist")
    return diaries[0]


def create_diary(name):
    if not _diary_exists(name):
        diary_model.create_diary(name)
    else:
        raise Exception("Diary with that name already exists")


def modify_diary(diary_id, diary_data):
    diary_model.modify_diary(diary_id, diary_data)

def delete_diary(diary_id):
    diary_model.delete_diary(diary_id)


def validate_session(session_id):
    sessions = diary_model.obtain_session(session_id)
    if len(sessions) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sessions[0]['date_time'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Session expired
        return False
    else:
        return True