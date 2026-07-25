"""
certainty_factor.py
---------------------------------------
Inference Engine
Metode Certainty Factor
"""
from back.knowledge import SYMPTOMS
from back.rules import RULES

def calculate_cf(user_cf, expert_cf):
    """
    Menghitung nilai Certainty Factor
    Rumus:
    CF(H,E) = CF User × CF Pakar
    """

    return user_cf * expert_cf


def combine_cf(cf1, cf2):

    """
    Menggabungkan dua nilai Certainty Factor

    Rumus:
    CFcombine = CF1 + CF2 × (1 − CF1)
    """

    return cf1 + (cf2 * (1 - cf1))
def diagnose(user_answers):
    """
    Menghitung nilai Certainty Factor untuk setiap rule.
    Parameter:
        user_answers -> dictionary
        contoh:
        {
            "G01": 1.0,
            "G02": 0.8,
            "G09": 0.6
        }

    Return:
        dictionary hasil diagnosis
    """

    results = {}

    for rule in RULES:

        cf_values = []

        for symptom_code in rule["symptoms"]:

            # jika user tidak menjawab gejala
            if symptom_code not in user_answers:
                continue

            user_cf = user_answers[symptom_code]

            expert_cf = SYMPTOMS[symptom_code]["cf_expert"]

            cf = calculate_cf(user_cf, expert_cf)

            cf_values.append(cf)

        # jika tidak ada gejala yang cocok
        if not cf_values:
            results[rule["condition"]] = 0
            continue

        # gabungkan semua CF
        final_cf = cf_values[0]

        for cf in cf_values[1:]:
            final_cf = combine_cf(final_cf, cf)

        results[rule["condition"]] = round(final_cf, 4)

    return results

if __name__ == "__main__":

    user_answers = {
        "G01": 1.0,
        "G02": 0.8,
        "G09": 0.6
    }

    result = diagnose(user_answers)

    print(result)