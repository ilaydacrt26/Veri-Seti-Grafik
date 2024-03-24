import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def Sıralama(table):
    n = len(table)
    for i in range(n):
        for j in range(0, n-i-1):
            if table[j] > table[j+1]:
                temp = table[j]
                table[j] = table[j+1]
                table[j+1] = temp
                
    return table    

def AyrkırıDeğerHesapla(table):    
    ayrık_değerler = []
    
    q1 = table[int(len(table)* 0.25)]
    q3 = table[int(len(table)* 0.75)]

    IQR = q3 - q1 # çeyreklik aralığı
    LAL = q1 - (1.5 * IQR) # alt sınır hesaplama
    UAL = q3 + (1.5 * IQR) # üst sınır hesaplama

    for i in range(len(table)):
        if table[i] < LAL or table[i] > UAL:
            ayrık_değerler.append(table[i])  
            
    return ayrık_değerler

def Ortalama(table):
    toplam = 0
    for i in range(len(table)):
        toplam += table[i]
    return toplam / (len(table))

def ModHesapla(table):
    frekanslar = {}
    for eleman in table:
        if eleman in frekanslar:
            frekanslar[eleman] += 1
        else:
            frekanslar[eleman] = 1
    
    mod_degerler = []
    max_frekan = max(frekanslar.values())
    for eleman, frekan in frekanslar.items():
        if frekan == max_frekan:
            mod_degerler.append(eleman)
            
    return mod_degerler

def MedyanHesapla(table):
    n = len(table)
    sıralı_table = sorted(table)
    if n % 2 == 0:
        medyan = (sıralı_table[n // 2 - 1] + sıralı_table[n // 2]) / 2
    else:
        medyan = sıralı_table[n // 2]
    return medyan

def DeğişimAralığıHesapla(table):
    min_deger = min(table)
    max_deger = max(table)
    degisim_araligi = max_deger - min_deger
    return degisim_araligi

def OrtalamaMutlakSapmaHesapla(table):
    ortalama = sum(table) / len(table)  # Veri setinin ortalaması
    mutlak_sapmalar = [abs(deger - ortalama) for deger in table]  # Her bir değerin ortalama değerden uzaklıkları
    ortalama_mutlak_sapma = sum(mutlak_sapmalar) / len(table)  # Mutlak sapmaların ortalaması
    return ortalama_mutlak_sapma

def VaryansHesapla(table):
    ortalama = Ortalama(table)
    karelerin_toplami = sum((deger - ortalama) ** 2 for deger in table)
    varyans = karelerin_toplami / len(table)
    return varyans

def StandartSapmaHesapla(table):
    ortalama = Ortalama(table)
    karelerin_toplami = sum((deger - ortalama) ** 2 for deger in table)
    varyans = karelerin_toplami / len(table)
    standart_sapma = varyans ** 0.5
    return standart_sapma

def DeğişimKatsayısıHesapla(table):
    standart_sapma = StandartSapmaHesapla(table)
    ortalama = Ortalama(table)
    degisim_katsayisi = (standart_sapma / ortalama) * 100  # Yüzde olarak ifade etmek için
    return degisim_katsayisi

def ÇeyreklerAralığıHesapla(table):
    n = len(table)
    q1_index = int(n * 0.25)  # Q1 için indeks hesapla
    q3_index = int(n * 0.75)  # Q3 için indeks hesapla
    q1 = table[q1_index]  # Q1 değerini bul
    q3 = table[q3_index]  # Q3 değerini bul
    çeyrekler_aralığı = q3 - q1
    return çeyrekler_aralığı

def EğilimDağılımBilgileri(table, dosya_adi):
    
    #dosyaya yazdırma kısmı
    with open(dosya_adi, 'a') as dosya:
        dosya.write("---MERKEZI EGILIM OLCULERI---\n")
        dosya.write("Aritmetik Ortalama : {}\n".format(Ortalama(table)))
        dosya.write("Mod : {}\n".format(ModHesapla(table)))
        dosya.write("Medyan : {}\n".format(MedyanHesapla(table)))

        dosya.write("\n---MERKEZI DAGILIM OLCULERI---\n")
        dosya.write("Degisim Araligi : {}\n".format(DeğişimAralığıHesapla(table)))
        dosya.write("Ortalama Mutlak Sapma : {}\n".format(OrtalamaMutlakSapmaHesapla(table)))
        dosya.write("Varyans : {}\n".format(VaryansHesapla(table)))
        dosya.write("Standart Sapma : {}\n".format(StandartSapmaHesapla(table)))
        dosya.write("Degisim Katsayisi : {}\n".format(DeğişimKatsayısıHesapla(table)))
        dosya.write("Ceyrekler Araligi : {}\n\n\n".format(ÇeyreklerAralığıHesapla(table)))
     
    # consola yazdırma kısmı
    print("\n---MERKEZİ EĞİLİM ÖLÇÜLERİ---")
    print("Aritmetik Ortalama : ", Ortalama(table))
    print("Mod : ", ModHesapla(table))
    print("Medyan : ", MedyanHesapla(table))

    print("\n---MERKEZİ DAĞILIM ÖLÇÜLERİ---")
    print("Değişim Aralığı : ", DeğişimAralığıHesapla(table))
    print("Ortalama Mutlak Sapma : ", OrtalamaMutlakSapmaHesapla(table))
    print("Varyans : ", VaryansHesapla(table))
    print("Standart Sapma : ", StandartSapmaHesapla(table))
    print("Değişim Katsayısı : ", DeğişimKatsayısıHesapla(table))
    print("Çeyrekler Aralığı : ", ÇeyreklerAralığıHesapla(table))
                        
# Veri setini oku
data = pd.read_csv('Veri.txt', delimiter=',', header=None, names=['Column1', 'Column2', 'Column3'])
df = data.copy()
df = df.select_dtypes(include = ['int64', 'float64'])
df.head()

dosya_adı = "Sonuc.txt"

print("\nVERİ SETİ\n")
print(df)

# tek sütun için işlem yapmakta kullanılır
df_table1 = df["Column1"].copy() 
df_table2 = df["Column2"].copy()
df_table3 = df["Column3"].copy()

# Aykırı değerleri göstermek için kutu grafiği kullanma
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
sns.boxplot(x=df_table1)
plt.title("Column1 Aykırı Değerler")

plt.subplot(1, 3, 2)
sns.boxplot(x=df_table2)
plt.title("Column2 Aykırı Değerler")

plt.subplot(1, 3, 3)
sns.boxplot(x=df_table3)
plt.title("Column3 Aykırı Değerler")

plt.tight_layout()
plt.show()

print("\nAYKIRI DEĞER HESAPLAMA - COLUMN-1\n")
table1 = Sıralama(df_table1.copy())
aykırıDeğerler1 = AyrkırıDeğerHesapla(table1)
print("Aykırı değerler --> ", end=' ')
print(aykırıDeğerler1)

table1 = [değer for değer in table1 if değer not in aykırıDeğerler1] # aykırı değerleri ayrıştırma kısmı
EğilimDağılımBilgileri(table1, dosya_adı)

print("\nAYKIRI DEĞER HESAPLAMA - COLUMN-2\n")
table2 = Sıralama(df_table2.copy())
aykırıDeğerler2 = AyrkırıDeğerHesapla(table2)
print("Aykırı değerler --> ", end=' ')
print(aykırıDeğerler2)

table2 = [değer for değer in table2 if değer not in aykırıDeğerler2] # aykırı değerleri ayrıştırma kısmı
EğilimDağılımBilgileri(table2, dosya_adı)

print("\nAYKIRI DEĞER HESAPLAMA - COLUMN-3\n")
table3 = Sıralama(df_table3.copy())
aykırıDeğerler3 = AyrkırıDeğerHesapla(table3)
print("Aykırı değerler --> ", end=' ')
print(aykırıDeğerler3)

table3 = [değer for değer in table3 if değer not in aykırıDeğerler3] # aykırı değerleri ayrıştırma kısmı
EğilimDağılımBilgileri(table3, dosya_adı)