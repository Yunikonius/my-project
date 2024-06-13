import pandas as pd

# Пример для Series
s = pd.Series([1, 2, 3, 4, 5])
mean_value = s.mean()
print("Среднее значение Series:", mean_value)

# Пример для DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
mean_values_columns = df.mean()
print("\nСредние значения по столбцам:")
print(mean_values_columns)

mean_values_rows = df.mean(axis=1)
print("\nСредние значения по строкам:")
print(mean_values_rows)