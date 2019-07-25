import json
import random
from flask import jsonify, Response
from flask_restful import Resource

class RandomEmailGenerator:
    _secure_random = random.SystemRandom()

    def __init__(self):
        with open("./plugins/randomemail/names.json", 'r', encoding="utf-8") as namesfile:
            self._namesdict = json.loads(namesfile.read())
            namesfile.close()

        with open("./plugins/randomemail/emaildomains.json", 'r', encoding="utf-8") as emailfile:
            self._emaillist = json.loads(emailfile.read())["emails"]
            emailfile.close()

    def getRandomName(self):
        regiondict = self._secure_random.choice(self._namesdict)
        gender = self._secure_random.randint(0, 1)
        if gender is 0:
            forename = self._secure_random.choice(regiondict["male"])
            gender = "male"
        else:
            forename = self._secure_random.choice(regiondict["female"])
            gender = "female"

        surname = self._secure_random.choice(regiondict["surnames"])
        emaildomain = self._secure_random.choice(self._emaillist)

        return {"forename": forename, "surname": surname, "gender": gender, "region": regiondict["region"], "email": forename.lower() + "." + surname.lower() + "@" + emaildomain}


class RandomEmail(Resource):
    def get(self):
        generator = RandomEmailGenerator()
        lol = generator.getRandomName()
        print(lol)
        return Response(json.dumps(lol), status=200, content_type="application/json; charset=utf-8")