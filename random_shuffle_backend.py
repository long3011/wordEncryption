from flask import Flask,jsonify
from flask_cors import CORS
import random
import json
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/encrypt/<str>')
def encrypt(str):
    try:
        if os.stat("../shuffling_words/key_value.json").st_size != 0:
            with open('../shuffling_words/key_value.json') as f:
                key_value = json.load(f)
        else:
            key_value = {}
        str_var = " !#$%&()*+,-.0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        var_shuffle=list(str_var)
        random.shuffle(var_shuffle)
        shuffled= ''.join(var_shuffle)  # value
        key_of_shuffle= ''.join(random.choices(var_shuffle, k=3))  # key
        value_list=[str_var,shuffled]
        if key_of_shuffle not in key_value:
            key_value[key_of_shuffle]=value_list
            with open('../shuffling_words/key_value.json', 'w') as f:
                json.dump(key_value, f)
        new_string=key_of_shuffle
        for i in str:
            if i not in value_list[0]:  # if letter not in wordShuffle library then return original character
                new_string += i
            else:
                new_string += value_list[1][
                    value_list[0].index(i)]  # match each character based on their index to their second value
        response = {
            "newString": new_string
        }
        return jsonify(response)
    except FileNotFoundError as e:
        f = open("../shuffling_words/key_value.json", "x")
        return encrypt(str)

@app.route('/decrypt/<str>')
def decrypt(str):
    if len(str)>3:
        try:
            with open('../shuffling_words/key_value.json') as f:
                key_value = json.load(f)
            value_list=key_value[str[0:3]]
            new_string = ""
            for i in str[3:]:
                if i not in value_list[0]:
                    new_string += i
                else:
                    new_string += value_list[0][value_list[1].index(i)]
            response = {
                "newString": new_string
            }
            return jsonify(response)
        except FileNotFoundError as e:
            return e
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)