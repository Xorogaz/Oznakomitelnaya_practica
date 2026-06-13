import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = np.random.randint(-10000, 10001, 1000)
series = pd.Series(dataset)

print("Статистические данные полученного Датасета:")
print(f"Минимальное значение: {series.min()}")
print(f"Максимальное значение: {series.max()}")
print(f"Количество повторяющихся значений: {series.duplicated().sum()}")
print(f"Сумма чисел: {series.sum()}")
print(f"Среднеквадратическое отклонение: {series.std()}")
print()

plt.figure(figsize=(16, 9), num="Линейный график series")
plt.plot(series, label="Значения series")
plt.title("Линейный график series")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(16, 9), num="Гистограмма значений по сотням")
series_rounded = series.apply(lambda x: round(x / 100) * 100)
plt.hist(series_rounded, bins=200, edgecolor="black")
plt.title("Гистограмма значений по сотням")
plt.xlabel("Значения")
plt.ylabel("Кол-во в series")
plt.grid(False)
plt.show()

df = pd.DataFrame({
    "Без сортировки": series,
    "По возрастанию": series.sort_values().values,
    "По убыванию": series.sort_values(ascending=False).values
})

print("Первые строки DataFrame")
print(df.head())

plt.figure(figsize=(16, 9), num="Отсортированные данные series")
plt.plot(df["По возрастанию"], label="По возрастанию")
plt.plot(df["По убыванию"], label="По убыванию")
plt.title("Отсортированные данные series")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.grid(True)
plt.legend()
plt.show()
