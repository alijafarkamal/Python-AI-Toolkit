# import matplotlib.pyplot as plt

# # Convert the 'Date' column to datetime
# data['Date'] = pd.to_datetime(data['Date'])

# # Plot the closing prices
# plt.figure(figsize=(10, 6))
# plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
# plt.title('XRP Closing Prices Over Time')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend()
# plt.grid()
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
# # Load your CSV file
# file_path = "XRP.csv"  # Replace with your actual CSV file path
# data = pd.read_csv(file_path)
# # Convert the 'Date' column to datetime
# data['Date'] = pd.to_datetime(data['Date'])
# # Plot the closing prices
# plt.figure(figsize=(10, 6))
# plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
# plt.title('XRP Closing Prices Over Time')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend()
# plt.grid()
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your CSV file
# file_path = "XRP1.csv"  # Replace with the actual path to your CSV file
# data = pd.read_csv(file_path)

# # Convert 'date' column to datetime format
# data['date'] = pd.to_datetime(data['date'])

# # Plot the closing prices
# plt.figure(figsize=(10, 6))
# plt.plot(data['date'], data['close'], label='Close Price', color='blue')
# plt.title('XRP Closing Prices in 2024')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend()
# plt.grid()
# plt.show()

# # Plot High-Low prices as a bar chart
# plt.figure(figsize=(10, 6))
# plt.bar(data['date'], data['high'], color='green', alpha=0.6, label='High')
# plt.bar(data['date'], data['low'], color='red', alpha=0.6, label='Low')
# plt.title('XRP High and Low Prices in 2024')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend()
# plt.xticks(rotation=45)
# plt.show()

# # Save the processed DataFrame as a CSV if needed
# data.to_csv("processed_xrp_data.csv", index=False)

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load your CSV file
# file_path = "XRP1.csv"  # Replace with the actual path to your CSV file
# data = pd.read_csv(file_path)

# # Convert 'date' column to datetime format
# data['date'] = pd.to_datetime(data['date'])

# # Set Seaborn style for better aesthetics
# sns.set_theme(style="whitegrid")

# # Plot the closing prices (Line Plot with Seaborn)
# plt.figure(figsize=(12, 6))
# sns.lineplot(x='date', y='close', data=data, color='blue', label='Close Price', linewidth=2)
# plt.title('XRP Closing Prices in 2024', fontsize=16)
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Price (USD)', fontsize=12)
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Plot High-Low Prices (Improved Bar Chart with Matplotlib)
# plt.figure(figsize=(12, 6))
# plt.bar(data['date'], data['high'], color='green', alpha=0.6, label='High')
# plt.bar(data['date'], data['low'], color='red', alpha=0.6, label='Low')
# plt.title('XRP High and Low Prices in 2024', fontsize=16)
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Price (USD)', fontsize=12)
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Pairplot for Relationships Between Features
# sns.pairplot(data[['open', 'high', 'low', 'close']], diag_kind="kde", corner=True)
# plt.suptitle("Relationships Between Open, High, Low, Close", y=1.02, fontsize=16)
# plt.show()

# # Monthly Averages for Close Prices (Line Plot)
# data['month'] = data['date'].dt.month
# monthly_avg = data.groupby('month')['close'].mean().reset_index()

# plt.figure(figsize=(10, 5))
# sns.lineplot(x='month', y='close', data=monthly_avg, marker='o', color='purple', label='Avg Close Price')
# plt.title('Average Monthly Closing Prices (2024)', fontsize=16)
# plt.xlabel('Month', fontsize=12)
# plt.ylabel('Price (USD)', fontsize=12)
# plt.legend()
# plt.xticks(range(1, 13))
# plt.grid()
# plt.tight_layout()
# plt.show()

# # Distribution Plot for Closing Prices
# plt.figure(figsize=(10, 5))
# sns.histplot(data['close'], bins=20, kde=True, color='blue')
# plt.title('Distribution of XRP Closing Prices in 2024', fontsize=16)
# plt.xlabel('Closing Price (USD)', fontsize=12)
# plt.ylabel('Frequency', fontsize=12)
# plt.tight_layout()
# plt.show()

# # Box Plot for High and Low Prices
# plt.figure(figsize=(10, 5))
# sns.boxplot(data=data[['high', 'low']])
# plt.title('High vs Low Price Distribution', fontsize=16)
# plt.xlabel('Price Type', fontsize=12)
# plt.ylabel('Price (USD)', fontsize=12)
# plt.tight_layout()
# plt.show()
# import pandas as pd
# import plotly.express as px

# # Load your CSV file
# file_path = "XRP1.csv"  # Replace with the actual path to your CSV file
# data = pd.read_csv(file_path)

# # Convert 'date' column to datetime format
# data['date'] = pd.to_datetime(data['date'])

# # Create an interactive line plot
# fig = px.line(
#     data,
#     x='date',
#     y='close',
#     title='XRP Closing Prices in 2024',
#     labels={'date': 'Date', 'close': 'Closing Price (USD)'},
#     hover_data={'date': True, 'close': ':.2f'}  # Show date and close price on hover
# )

# # Customize layout
# fig.update_layout(
#     xaxis_title='Date',
#     yaxis_title='Price (USD)',
#     hovermode='x unified',  # Shows one hover tooltip across x-axis
#     template='plotly_white'
# )

# # Show plot
# fig.show()



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors

# Load your CSV file
file_path = "XRP1.csv"  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Convert 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# 1. Line Plot for Closing Prices
plt.figure(figsize=(12, 6))
plt.plot(data['date'], data['close'], label='Close Price', color='blue', linewidth=2)
plt.title('XRP Closing Prices in 2024', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend()
plt.grid()
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"Date: {data['date'][sel.index].strftime('%Y-%m-%d')}\nClose: {data['close'][sel.index]:.2f}"
))
plt.tight_layout()
plt.show()

# 2. High-Low Prices Bar Plot
plt.figure(figsize=(12, 6))
plt.bar(data['date'], data['high'], color='green', alpha=0.6, label='High')
plt.bar(data['date'], data['low'], color='red', alpha=0.6, label='Low')
plt.title('XRP High and Low Prices in 2024', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"Date: {data['date'][sel.index].strftime('%Y-%m-%d')}\nHigh: {data['high'][sel.index]:.2f}\nLow: {data['low'][sel.index]:.2f}"
))
plt.tight_layout()
plt.show()

# 3. Distribution of Closing Prices
plt.figure(figsize=(10, 5))
sns.histplot(data['close'], bins=20, kde=True, color='blue')
plt.title('Distribution of XRP Closing Prices in 2024', fontsize=16)
plt.xlabel('Closing Price (USD)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.show()

# 4. Box Plot for High and Low Prices
plt.figure(figsize=(10, 5))
sns.boxplot(data=data[['high', 'low']])
plt.title('High vs Low Price Distribution', fontsize=16)
plt.xlabel('Price Type', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.tight_layout()
plt.show()




# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Load your CSV file
# file_path = "XRP1.csv"  # Replace with the actual path to your CSV file
# data = pd.read_csv(file_path)

# # Convert 'date' column to datetime format
# data['date'] = pd.to_datetime(data['date'])

# # 1. Line Plot for Closing Prices
# fig1 = px.line(
#     data,
#     x='date',
#     y='close',
#     title='XRP Closing Prices in 2024',
#     labels={'date': 'Date', 'close': 'Closing Price (USD)'},
#     hover_data={'date': True, 'close': ':.2f'}
# )

# # 2. High-Low Bar Plot
# fig2 = go.Figure()
# fig2.add_trace(go.Bar(x=data['date'], y=data['high'], name='High Prices', marker=dict(color='green', opacity=0.6)))
# fig2.add_trace(go.Bar(x=data['date'], y=data['low'], name='Low Prices', marker=dict(color='red', opacity=0.6)))
# fig2.update_layout(
#     title='XRP High and Low Prices in 2024',
#     xaxis_title='Date',
#     yaxis_title='Price (USD)',
#     barmode='group',
#     template='plotly_white'
# )

# # 3. Distribution of Closing Prices
# fig3 = px.histogram(
#     data,
#     x='close',
#     nbins=20,
#     title='Distribution of XRP Closing Prices in 2024',
#     labels={'close': 'Closing Price (USD)'},
#     color_discrete_sequence=['blue']
# )

# # 4. Box Plot for High and Low Prices
# fig4 = px.box(
#     data,
#     y=['high', 'low'],
#     title='High vs Low Price Distribution',
#     labels={'value': 'Price (USD)', 'variable': 'Price Type'}
# )

# # Show all figures one after another
# fig1.show()
# fig2.show()
# fig3.show()
# fig4.show()

