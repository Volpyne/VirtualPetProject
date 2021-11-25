from data.models import pet as pet_model

def _pet_exists(name, password):
    pets = pet_model.obtain_pets_by_name(name)
    return not len(pets) == 0


def _create_session(pet_id):
    current_time = datetime.now()
    #dd/mm/YY H:M:S
    dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
    return user_model.create_session(pet_id, dt_string)


def obtain_pets():
    return pets_model.obtain_pets()


def obtain_pet(pet_id):
    pet = pet_model.obtain_pet(pet_id)
    if len(pets) == 0:
        raise Exception("Pet doesn't exist")
    return pets[0]


def create_pet(name):
    if not _pet_exists(name):
        pet_model.create_pet(name)
    else:
        raise Exception("Pet name already exists")


def modify_pet(pet_id, pet_data):
    pet_model.modify_pet(pet_id, pet_data)

def delete_pet(pet_id):
    pet_model.delete_pet(pet_id)