from back.knowledge import SYMPTOMS, USER_CF, CONDITIONS
from back.recommendation import RECOMMENDATIONS
from back.certainty_factor import diagnose


def input_user_answers():
    """
    Meminta input tingkat keyakinan user
    """

    answers = {}

    print("=" * 70)
    print(" SISTEM PAKAR REKOMENDASI KANDUNGAN AKTIF SKINCARE ".center(70))
    print("=" * 70)

    print("\nSilakan pilih tingkat keyakinan Anda terhadap setiap gejala.\n")

    for key, value in USER_CF.items():
        print(f"{key}. {value['label']} ({value['value']})")

    print("\n" + "-" * 70)

    for code, symptom in SYMPTOMS.items():

        while True:

            try:
                print(f"\n{code} - {symptom['name']}")
                choice = int(input("Pilih (1-6): "))

                if choice in USER_CF:
                    answers[code] = USER_CF[choice]["value"]
                    break

                print("❌ Pilihan harus antara 1 sampai 6.")

            except ValueError:
                print("❌ Masukkan angka!")

    return answers


def show_result(results):

    # Urutkan hasil berdasarkan CF terbesar
    sorted_results = sorted(
        results.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n")
    print("=" * 70)
    print("HASIL PERHITUNGAN CERTAINTY FACTOR".center(70))
    print("=" * 70)

    print(f"{'Kode':<8}{'Kondisi Kulit':<35}{'Persentase'}")
    print("-" * 70)

    for code, cf in sorted_results:
        print(f"{code:<8}{CONDITIONS[code]:<35}{cf * 100:>8.2f}%")

    # Diagnosis terbaik
    best_condition = sorted_results[0][0]
    best_cf = sorted_results[0][1]

    recommendation = RECOMMENDATIONS[best_condition]

    print("\n" + "=" * 70)
    print("DIAGNOSIS UTAMA".center(70))
    print("=" * 70)

    print(f"Kondisi Kulit : {CONDITIONS[best_condition]}")
    print(f"Nilai CF      : {best_cf:.4f}")
    print(f"Persentase    : {best_cf * 100:.2f}%")

    print("\n" + "=" * 70)
    print("REKOMENDASI KANDUNGAN AKTIF".center(70))
    print("=" * 70)

    for item in recommendation["ingredients"]:
        print(f"✓ {item}")

    print("\n" + "=" * 70)
    print("YANG SEBAIKNYA DIHINDARI".center(70))
    print("=" * 70)

    for item in recommendation["avoid"]:
        print(f"✗ {item}")

    print("\n" + "=" * 70)
    print("TIPS PERAWATAN".center(70))
    print("=" * 70)

    for i, item in enumerate(recommendation["tips"], start=1):
        print(f"{i}. {item}")

    print("\n" + "=" * 70)


def main():

    while True:

        answers = input_user_answers()

        results = diagnose(answers)

        show_result(results)

        while True:
            ulang = input("\nIngin melakukan diagnosis lagi? (y/n): ").lower()

            if ulang in ("y", "n"):
                break

            print("Masukkan hanya y atau n.")

        if ulang == "n":
            print("\nTerima kasih telah menggunakan Sistem Pakar Skincare.")
            break

        print("\n" * 2)


if __name__ == "__main__":
    main()