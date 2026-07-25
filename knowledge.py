"""
knowledge.py
---------------------------------------
Knowledge Base Sistem Pakar Skincare
Metode: Certainty Factor (CF)

Berisi:
1. Data gejala
2. Data kondisi kulit
3. Nilai CF Pakar
4. Nilai CF User
"""

# ==========================================
# DATA GEJALA
# ==========================================

SYMPTOMS = {
    "G01": {
        "name": "Kulit terasa berminyak di seluruh wajah",
        "cf_expert": 0.9
    },
    "G02": {
        "name": "Pori-pori tampak besar",
        "cf_expert": 0.8
    },
    "G03": {
        "name": "Kulit terasa tertarik setelah mencuci muka",
        "cf_expert": 0.9
    },
    "G04": {
        "name": "Kulit mengelupas atau bersisik",
        "cf_expert": 0.8
    },
    "G05": {
        "name": "Kulit mudah kemerahan",
        "cf_expert": 0.9
    },
    "G06": {
        "name": "Perih atau panas setelah memakai skincare",
        "cf_expert": 0.9
    },
    "G07": {
        "name": "Jerawat aktif meradang",
        "cf_expert": 0.9
    },
    "G08": {
        "name": "Banyak komedo",
        "cf_expert": 0.8
    },
    "G09": {
        "name": "Minyak cepat muncul kembali setelah cuci muka",
        "cf_expert": 0.7
    },
    "G10": {
        "name": "Berminyak hanya di area T-Zone",
        "cf_expert": 0.9
    },
    "G11": {
        "name": "Pipi terasa kering",
        "cf_expert": 0.8
    },
    "G12": {
        "name": "Kulit sensitif terhadap perubahan suhu",
        "cf_expert": 0.7
    },
    "G13": {
        "name": "Jerawat besar di bawah kulit",
        "cf_expert": 0.7
    }
}

# ==========================================
# DATA KONDISI KULIT
# ==========================================

CONDITIONS = {
    "P01": "Kulit Berminyak",
    "P02": "Kulit Kering",
    "P03": "Kulit Sensitif",
    "P04": "Kulit Kombinasi",
    "P05": "Kulit Rentan Berjerawat"
}

# ==========================================
# NILAI CERTAINTY FACTOR USER
# ==========================================

USER_CF = {
    1: {
        "label": "Tidak",
        "value": 0.0
    },
    2: {
        "label": "Kurang Yakin",
        "value": 0.2
    },
    3: {
        "label": "Sedikit Yakin",
        "value": 0.4
    },
    4: {
        "label": "Cukup Yakin",
        "value": 0.6
    },
    5: {
        "label": "Yakin",
        "value": 0.8
    },
    6: {
        "label": "Sangat Yakin",
        "value": 1.0
    }
}