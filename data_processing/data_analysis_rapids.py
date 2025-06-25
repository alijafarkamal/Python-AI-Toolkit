import cudf

data = cudf.read_csv("dataset.csv")

summary = data.describe()
filtered_data = data[data["sales"] > 1000]

print("Data Summary:")
print(summary)

print("Filtered Data:")
print(filtered_data)
