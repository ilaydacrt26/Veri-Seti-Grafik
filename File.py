import pandas as pd
import CentralMeasurement as mo

def CentralTrendencyDistributionInformation(table, file_name):
    
    with open(file_name, 'a') as dosya:
        dosya.write("---MERKEZI EGILIM OLCULERI---\n")
        dosya.write("Aritmetik Ortalama : {}\n".format(mo.Average(table)))
        dosya.write("Mod : {}\n".format(mo.ModeCalculation(table)))
        dosya.write("Medyan : {}\n".format(mo.MedianCalculation(table)))

        dosya.write("\n---MERKEZI DAGILIM OLCULERI---\n")
        dosya.write("Degisim Araligi : {}\n".format(mo.VariationRangeCalculation(table)))
        dosya.write("Ortalama Mutlak Sapma : {}\n".format(mo.MeanAbsoluteDeviationCalculation(table)))
        dosya.write("Varyans : {}\n".format(mo.VarianceCalculation(table)))
        dosya.write("Standart Sapma : {}\n".format(mo.StandartDeviationCalculation(table)))
        dosya.write("Degisim Katsayisi : {}\n".format(mo.CoefficientOfVariationCalculation(table)))
        dosya.write("Ceyrekler Araligi : {}\n\n\n".format(mo.InterquartileRangeCalculation(table)))
     
    print("\n---MERKEZİ EĞİLİM ÖLÇÜLERİ---")
    print("Aritmetik Ortalama : ", mo.Average(table))
    print("Mod : ", mo.ModeCalculation(table))
    print("Medyan : ", mo.MedianCalculation(table))

    print("\n---MERKEZİ DAĞILIM ÖLÇÜLERİ---")
    print("Değişim Aralığı : ", mo.VariationRangeCalculation(table))
    print("Ortalama Mutlak Sapma : ", mo.MeanAbsoluteDeviationCalculation(table))
    print("Varyans : ", mo.VarianceCalculation(table))
    print("Standart Sapma : ", mo.StandartDeviationCalculation(table))
    print("Değişim Katsayısı : ", mo.CoefficientOfVariationCalculation(table))
    print("Çeyrekler Aralığı : ", mo.InterquartileRangeCalculation(table))
    
def FileReading():
    data = pd.read_csv('Veri.csv', delimiter=',', header=None, names=['Column1', 'Column2', 'Column3'])
    df = data.copy()
    df = df.select_dtypes(include = ['int64', 'float64'])
    df.head()
    return df