import matplotlib.pyplot as plt
import seaborn as sns

def CreateChart(df, column, index):
    df_table = df[column].copy()
    
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 3, index)
    sns.boxplot(x=df_table)
    plt.title(column + " Aykırı Değerler")
    
    plt.tight_layout()
    plt.show()
    
    return df_table