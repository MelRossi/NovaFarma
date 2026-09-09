"""
NovaFarma Category Demand Analytics — Exploratory Data Analysis
Fuente: Pharma Sales Data (Milan Zdravkovic) - https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data
"""

import pandas as pd

CATS = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']


def load_data(path="../data/raw/salesdaily.csv"):
    df = pd.read_csv(path)
    df['datum'] = pd.to_datetime(df['datum'], format='%m/%d/%Y')
    df.rename(columns={'datum': 'Date'}, inplace=True)
    return df


def data_quality_report(df):
    print("Shape:", df.shape)
    print("Nulls per column:\n", df.isnull().sum())
    print("Duplicated dates:", df['Date'].duplicated().sum())
    print("Date range:", df['Date'].min(), "-", df['Date'].max())


def category_contribution(df):
    total = df[CATS].sum().sum()
    return (df[CATS].sum() / total * 100).sort_values(ascending=False).round(2)


def yoy_growth(df):
    df = df.copy()
    df['Year'] = df['Date'].dt.year
    yearly = df[df['Year'].between(2015, 2018)].groupby('Year')[CATS].sum()
    return (yearly.pct_change().dropna() * 100).round(1)


def volatility(df):
    cv = (df[CATS].std() / df[CATS].mean() * 100).sort_values(ascending=False)
    return cv.round(1)


def seasonality(df):
    df = df.copy()
    df['Month'] = df['Date'].dt.month
    return df.groupby('Month')[CATS].sum().sum(axis=1)


def weekday_pattern(df):
    df = df.copy()
    df['Weekday'] = df['Date'].dt.day_name()
    return df.groupby('Weekday')[CATS].sum().sum(axis=1).sort_values(ascending=False)


def build_star_schema(df, out_dir="../data/processed"):
    """Genera FactSales.csv y DimCategory.csv listos para Power BI."""
    fact = df.melt(id_vars=['Date'], value_vars=CATS,
                    var_name='CategoryCode', value_name='UnitsSold')
    fact = fact.sort_values(['Date', 'CategoryCode']).reset_index(drop=True)
    fact['UnitsSold'] = fact['UnitsSold'].round(2)
    fact.to_csv(f"{out_dir}/FactSales.csv", index=False)

    dim_cat = pd.DataFrame({
        'CategoryCode': CATS,
        'TherapeuticGroup': [
            'Anti-inflammatory & antirheumatic (non-steroid) - Acetic acid derivatives',
            'Anti-inflammatory & antirheumatic (non-steroid) - Propionic acid derivatives',
            'Analgesics/antipyretics - Salicylic acid derivatives',
            'Analgesics/antipyretics - Pyrazolones and anilides (e.g. paracetamol)',
            'Psycholeptics - Anxiolytics',
            'Psycholeptics - Hypnotics and sedatives',
            'Drugs for obstructive airway diseases',
            'Antihistamines for systemic use',
        ],
        'CategoryGroup': [
            'Pain & Inflammation', 'Pain & Inflammation', 'Pain & Inflammation', 'Pain & Inflammation',
            'Mental Health', 'Mental Health', 'Respiratory', 'Respiratory',
        ],
    })
    dim_cat.to_csv(f"{out_dir}/DimCategory.csv", index=False)
    return fact, dim_cat


if __name__ == "__main__":
    df = load_data()
    data_quality_report(df)
    print("\nCategory contribution %:\n", category_contribution(df))
    print("\nYoY growth %:\n", yoy_growth(df))
    print("\nVolatility (CV%):\n", volatility(df))
    print("\nSeasonality (avg units by month):\n", seasonality(df))
    print("\nWeekday pattern:\n", weekday_pattern(df))
    build_star_schema(df)
    print("\nStar schema files written to data/processed/")
