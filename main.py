import CentralMeasurement as mo
import File as file
import Graphic as g

df = file.FileReading()

file_name = "Sonuc.csv"

print("\nVERİ SETİ\n")
print(df)


df_table1 = g.CreateChart(df, "Column1", 1)
df_table2 = g.CreateChart(df, "Column2", 2)
df_table3 = g.CreateChart(df, "Column3", 3)

print("\nAYKIRI DEĞER HESAPLAMA - COLUMN-1\n")
table1 = mo.Sort(df_table1.copy())
outliers1 = mo.OutlierCalculation(table1)
print("Aykırı değerler --> ", end=' ')
print(outliers1)

table1 = [value for value in table1 if value not in outliers1]
file.CentralTrendencyDistributionInformation(table1, file_name)

print("\nAYKIRI DEĞER HESAPLAMA - COLUMN-2\n")
table2 = mo.Sort(df_table2.copy())
outliers2 = mo.OutlierCalculation(table2)
print("Aykırı değerler --> ", end=' ')
print(outliers2)

table2 = [value for value in table2 if value not in outliers2]
file.CentralTrendencyDistributionInformation(table2, file_name)

print("\nAYKIRI DEĞER HESAPLAMA - COLUMN-3\n")
table3 = mo.Sort(df_table3.copy())
outliers3 = mo.OutlierCalculation(table3)
print("Aykırı değerler --> ", end=' ')
print(outliers3)

table3 = [value for value in table3 if value not in outliers3]
file.CentralTrendencyDistributionInformation(table3, file_name)