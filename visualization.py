import matplotlib.pyplot as plt
import seaborn as sns

def plot_category_distribution(df, column):
    plt.figure(figsize=(10,6))
    sns.countplot(x=column, data=df)
    plt.title(f'Distribution of {column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_time_series(df, date_col, value_col):
    df_grouped = df.groupby(date_col)[value_col].sum().reset_index()
    plt.figure(figsize=(12,6))
    sns.lineplot(x=date_col, y=value_col, data=df_grouped)
    plt.title(f'{value_col} Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
