"""
recommendation.py
---------------------------------------
Recommendation Base Sistem Pakar Skincare
"""

RECOMMENDATIONS = {

    "P01": {
        "condition": "Kulit Berminyak",

        "ingredients": [
            "Niacinamide",
            "Salicylic Acid",
            "Sunscreen"
        ],

        "avoid": [
            "Produk dengan kandungan minyak berlebih (Heavy Oils)"
        ],

        "tips": [
            "Gunakan facial wash khusus kulit berminyak.",
            "Gunakan pelembap berbahan dasar gel.",
            "Gunakan sunscreen minimal SPF 30 setiap pagi."
        ]
    },

    "P02": {
        "condition": "Kulit Kering",

        "ingredients": [
            "Ceramide",
            "Hyaluronic Acid",
            "Glycerin",
            "Sunscreen"
        ],

        "avoid": [
            "Sabun dengan kandungan alkohol tinggi",
            "Eksfoliasi terlalu sering"
        ],

        "tips": [
            "Gunakan pelembap secara rutin.",
            "Hindari mencuci wajah dengan air yang terlalu panas.",
            "Gunakan sunscreen setiap pagi."
        ]
    },

    "P03": {
        "condition": "Kulit Sensitif",

        "ingredients": [
            "Panthenol",
            "Niacinamide",
            "Azelaic Acid",
            "Sunscreen"
        ],

        "avoid": [
            "Salicylic Acid konsentrasi tinggi",
            "Benzoyl Peroxide tanpa konsultasi",
            "Produk yang mengandung alkohol tinggi"
        ],

        "tips": [
            "Gunakan skincare yang bersifat gentle.",
            "Lakukan patch test sebelum mencoba produk baru.",
            "Gunakan sunscreen setiap pagi."
        ]
    },

    "P04": {
        "condition": "Kulit Kombinasi",

        "ingredients": [
            "Niacinamide",
            "Ceramide",
            "Sunscreen"
        ],

        "avoid": [
            "Produk yang terlalu mengeringkan seluruh wajah"
        ],

        "tips": [
            "Gunakan skincare sesuai area wajah.",
            "Gunakan pelembap ringan.",
            "Gunakan sunscreen setiap pagi."
        ]
    },

    "P05": {
        "condition": "Kulit Rentan Berjerawat",

        "ingredients": [
            "Salicylic Acid",
            "Azelaic Acid",
            "Niacinamide",
            "Sunscreen"
        ],

        "avoid": [
            "Produk komedogenik",
            "Memencet jerawat"
        ],

        "tips": [
            "Cuci wajah dua kali sehari.",
            "Jangan menyentuh wajah dengan tangan kotor.",
            "Gunakan sunscreen non-comedogenic."
        ]
    }

}