def Sort(table):
    n = len(table)
    for i in range(n):
        for j in range(0, n-i-1):
            if table[j] > table[j+1]:
                temp = table[j]
                table[j] = table[j+1]
                table[j+1] = temp
    return table    

def OutlierCalculation(table):
    
    discrete_values = []
    
    q1 = table[int(len(table)* 0.25)]
    q3 = table[int(len(table)* 0.75)]

    IQR = q3 - q1
    LAL = q1 - (1.5 * IQR)
    UAL = q3 + (1.5 * IQR)
        
    for i in range(len(table)):
        if table[i] < LAL or table[i] > UAL:
            discrete_values.append(table[i])
            
    return discrete_values

def Average(table):
    
    total = 0
    
    for i in range(len(table)):
        total += table[i]
    return total / (len(table))

def ModeCalculation(table):
    
    frequencies = {}
    for element in table:
        if element in frequencies:
            frequencies[element] += 1
        else:
            frequencies[element] = 1
    
    mode_values = []
    max_frekan = max(frequencies.values())
    for element, frekan in frequencies.items():
        if frekan == max_frekan:
            mode_values.append(element)
    
    return mode_values

def MedianCalculation(table):
    n = len(table)
    sort_table = sorted(table)
    if n % 2 == 0:
        median = (sort_table[n // 2 - 1] + sort_table[n // 2]) / 2
    else:
        median = sort_table[n // 2]
    return median

def VariationRangeCalculation(table):
    min_value = min(table)
    max_value = max(table)
    change_interval = max_value - min_value
    return change_interval

def MeanAbsoluteDeviationCalculation(table):
    average = sum(table) / len(table)
    absolute_deviations = [abs(value - average) for value in table]
    mean_absolute_deviation = sum(absolute_deviations) / len(table)
    return mean_absolute_deviation

def VarianceCalculation(table):
    average = Average(table)
    sum_of_squares = sum((value - average) ** 2 for value in table)
    variance = sum_of_squares / len(table)
    return variance

def StandartDeviationCalculation(table):
    average = Average(table)
    sum_of_squares = sum((value - average) ** 2 for value in table)
    variance = sum_of_squares / len(table)
    standart_deviation = variance ** 0.5
    return standart_deviation

def CoefficientOfVariationCalculation(table):
    standart_deviation = StandartDeviationCalculation(table)
    average = Average(table)
    coefficient_of_variation = (standart_deviation / average) * 100
    return coefficient_of_variation

def InterquartileRangeCalculation(table):
    n = len(table)
    q1_index = int(n * 0.25)
    q3_index = int(n * 0.75)
    q1 = table[q1_index]
    q3 = table[q3_index]
    interqurtile_range = q3 - q1
    return interqurtile_range