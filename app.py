from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

import func

app = Flask(__name__)
api = Api(app)


class GetNum(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("data", type=list, location='json')
        parser.add_argument("rule", type=list, location='json')
        params = parser.parse_args()
        numbers = params["data"]
        rule = params["rule"]
        result = []
        for number in numbers:
            for i in rule:
                switch = {
                    "a": func.fun_a(number),
                    "b": func.fun_b(number),
                    "c": func.fun_c(number),
                    "d": func.fun_d(number),
                    "e": func.fun_e(number),
                    "f": func.fun_f(number),
                }
                try:
                    number = switch[i]
                except KeyError:
                    abort(404, message=f"Function '{i}' does not exist")

            result.append(number)

        return result


api.add_resource(GetNum, "/start")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
