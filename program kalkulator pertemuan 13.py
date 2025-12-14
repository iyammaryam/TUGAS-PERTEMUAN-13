try:
    # Input angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Input operator
    operator = input("Masukkan operator (+, -, *, /): ")

    # Proses perhitungan
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 == 0:
            raise ZeroDivisionError
        hasil = angka1 / angka2
    else:
        raise Exception("Operator tidak valid! Gunakan +, -, *, atau /")

    print("Hasil:", hasil)

except ValueError:
    print("Error: Input harus berupa angka!")
except ZeroDivisionError:
    print("Error: Tidak boleh membagi dengan nol!")
except Exception as e:
    print("Error:", e)