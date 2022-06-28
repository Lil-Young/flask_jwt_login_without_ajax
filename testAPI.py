from flask import Flask
from flask_validation_extended import Validator
from flask_validation_extended.params import Route, Json, Query
from flask_validation_extended.types import List
from flask_validation_extended.rules import MinLen, Min, Max, IsoDatetime

app = Flask(__name__)

"""
id: URI 파라미터에 수집하며, int여야 한다.
username: Body-Json에서 수집하며, str이여야 하고, 최소 길이가 5보다 커야 한다.
age: Body-Json에서 수집하며, int여야 하고, 16 ~ 98 사이여야 한다
nicknames: Body-Json에서 수집하며, str으로 구성된 list여야 한다.
birthday: Body-Json에서 수집하며, str이여야 하고, ISO Datetime format이여야 한다.
expire: Body-Json에서 수집하며, int여야 하지만, 반드시 입력받지 않아도 된다.(Optional)
is_admin: Query에서 수집하며, bool이여야 하며, 입력되지 않을 경우, false로 취급한다.
"""
@app.route("/update/<int:id>", methods=["POST"])
@Validator()
def hello(
        id=Route(int),
        username=Json(str, rules=MinLen(5)),
        age=Json(int, rules=[Min(18), Max(99)]),
        nicknames=Json(List(str)),
        birthday=Json(str, rules=IsoDatetime()),
        expire=Json(int, optional=True),
        is_admin=Query(bool, default=False)
     ):
    return "Update Complete! %s" % locals()


if __name__ == "__main__":
    app.run(debug=True)