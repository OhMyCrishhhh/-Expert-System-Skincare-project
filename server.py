from flask import Flask, send_from_directory, request, jsonify

from back.certainty_factor import diagnose
from back.knowledge import CONDITIONS
from back.recommendation import RECOMMENDATIONS

app = Flask(
    __name__,
    static_folder="frontv2",
    static_url_path=""
)


# ==========================
# FRONTEND
# ==========================

@app.route("/")
def home():
    return send_from_directory("frontv2", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontv2", path)


# ==========================
# API DIAGNOSIS
# ==========================

@app.route("/diagnose", methods=["POST"])
def diagnose_api():

    user_answers = request.get_json()

    print("=" * 60)
    print("USER ANSWERS")
    print(user_answers)
    print("=" * 60)

    # Hitung CF
    results = diagnose(user_answers)

    print("HASIL CF")
    print(results)

    # Ambil kondisi dengan CF tertinggi
    best_code = max(results, key=results.get)

    best_cf = results[best_code]

    recommendation = RECOMMENDATIONS[best_code]

    response = {

        "condition": CONDITIONS[best_code],

        "cf": round(best_cf * 100),

        "ingredients": recommendation["ingredients"],

        "avoid": recommendation["avoid"],

        "tips": recommendation["tips"]

    }

    print("=" * 60)
    print("FINAL RESULT")
    print(response)
    print("=" * 60)

    return jsonify(response)


# ==========================
# RUN
# ==========================

if __name__ == "__main__":
    app.run(debug=True)