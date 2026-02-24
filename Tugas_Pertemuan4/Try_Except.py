# Studi Kasus: Kalkulator Sederhana dengan Try-Except dan User Input
 
class OperasiTidakValidError(Exception):
    """Custom exception untuk operasi yang tidak valid."""
    pass
 
def kalkulator():
    print("=" * 45)
    print("    KALKULATOR SEDERHANA PYTHON")
    print("=" * 45)
    print("Operasi yang tersedia: +, -, *, /")
    print("Ketik 'keluar' untuk menghentikan program.")
    print("=" * 45)
 
    while True:
        try:
            input1 = input("\nMasukkan angka pertama: ")
            if input1.lower() == "keluar":
                print("Program dihentikan")
                break
            angka1 = float(input1)

            angka2 = float(input("Masukkan angka kedua: "))
 
            operasi = input("Masukkan operasi (+, -, *, /): ")
 
            if operasi not in ["+", "-", "*", "/"]:
                raise OperasiTidakValidError(
                    f"Operasi '{operasi}' tidak dikenali."
                )
 
            if operasi == "+":
                hasil = angka1 + angka2
            elif operasi == "-":
                hasil = angka1 - angka2
            elif operasi == "*":
                hasil = angka1 * angka2
            elif operasi == "/":
                hasil = angka1 / angka2
 
        except ValueError:
            print("[ERROR] Input tidak valid. Masukkan angka yang benar")
 
        except ZeroDivisionError:
            print("[ERROR] Tidak dapat membagi dengan nol")
 
        except OperasiTidakValidError as e:
            print(f"[ERROR] {e} Gunakan salah satu dari: +, -, *, /")
 
        else:
            print(f"\nHasil: {angka1} {operasi} {angka2} = {hasil}")
 
        finally:
            print("------------------------------------")
            print("kalkulasi selesai.")
 
kalkulator()
