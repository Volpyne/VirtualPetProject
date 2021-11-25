from flask import Flask, request, jsonify
from services.authentication import authentication
from services.diary import diary
from services.pet import pet
from flask import render_template

app = Flask(__name__)

@app.route('/')
def get_index():
    title_VP = 'Virtual Pet'
    return render_template('index.html', title = title_VP)

@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    if 'username' not in user_data or user_data['username'] == '':
        return 'Username required', 412
    if 'password' not in user_data:
        return 'Password required', 412
    if 'mail' not in user_data:
        return 'Email required', 412

    return 'OK', 200


@app.route('/user/<user_id>', methods=['PUT'])
def modify_user(user_id):
    user_data = request.get_json()
    if 'username' not in user_data or user_data['username'] == '':
        return 'Username required', 412
    if 'password' not in user_data:
        return 'Password required', 412
    authentication.modify_user(user_id, user_data)
    return 'OK', 200

@app.route('/user', methods=['GET'])
def obtain_users():
    return jsonify(authentication.obtain_users())


@app.route('/user/<user_id>', methods=['GET'])
def obtain_user(user_id):
     try:
         user = authentication.obtain_user(user_id)
         return jsonify(user)
     except Exception:
         return 'User not found', 404


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    authentication.delete_user(user_id)
    return "Deleted", 200


@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    if 'username' not in user_data:
        return 'Username required', 412
    if 'password' not in user_data:
        return 'Password required', 412

    return jsonify({"session_id": 1})
    return 'OK', 200


#DIARY

@app.route('/diary', methods=['POST'])
def create_diary():
    diary_data = request.get_json()
    if 'name' not in diary_data or diary_data['name'] == '':
        return 'Name required', 412

    #diary.create_diary(diary_data['name'])
    return 'OK', 200


@app.route('/diary/<diary_id>', methods=['PUT'])
def modify_diary(diary_id):
    diary_data = request.get_json()
    if 'name' not in diary_data or diary_data['name'] == '':
        return 'Name required', 412
    #diary.modify_diary(diary_id, diary_data)
    return 'OK', 200


@app.route('/diary', methods=['GET'])
def obtain_diaries():
    return jsonify(diary.obtain_diaries())


@app.route('/diary/<diary_id>', methods=['GET'])
def obtain_diary(diary_id):
     try:
         diary = diary.obtain_diary(diary_id)
         return jsonify(diary)
     except Exception:
         return 'Diary not found', 404


@app.route('/diary/<diary_id>', methods=['DELETE'])
def delete_diary(diary_id):
    diary.delete_diary(diary_id)
    return "Deleted", 200


#PET

@app.route('/pet', methods=['POST'])
def create_pet():
    pet_data = request.get_json()
    if 'name' not in pet_data or pet_data['name'] == '':
        return 'Name required', 412

    return 'OK', 200

@app.route('/pet/<pet_id>', methods=['PUT'])
def modify_pet(pet_id):
    pet_data = request.get_json()
    if 'name' not in pet_data or pet_data['name'] == '':
        return 'Name required', 412
    pet.modify_pet(pet_id, pet_data)
    return 'OK', 200

@app.route('/pet', methods=['GET'])
def obtain_pets():
    return jsonify(pet.obtain_pets())

@app.route('/pet/<pet_id>', methods=['GET'])
def obtain_pet(pet_id):
     try:
         pet = pet.obtain_pet(pet_id)
         return jsonify(pet)
     except Exception:
         return 'Pet not found', 404


@app.route('/pet/<pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    pet.delete_pet(pet_id)
    return "Deleted", 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)