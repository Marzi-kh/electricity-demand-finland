import pandas as pd
from SCR.data_preprocessing import load_data, clean_data


def basic_overview(df: pd.DataFrame) -> None:

    print("\n" + "=" * 60)
    print("BASIC OVERVIEW")
    print("=" * 60)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nLast 5 rows:")
    print(df.tail())

    print("\nInfo:")
    df.info()

    print("\nMissing values per column:")
    print(df.isna().sum())

    print("\nDuplicate rows:", int(df.duplicated().sum()))

    print("\nNumeric columns:")
    print(list(df.select_dtypes(include=["number"]).columns))

    print("\nNon-numeric columns:")
    print(list(df.select_dtypes(exclude=["number"]).columns))


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("DataFrame index must be a DatetimeIndex (e.g., startTime).")

    df["hour"] = df.index.hour
    df["weekday"] = df.index.dayofweek
    df["month"] = df.index.month
    df["is_weekend"] = (df["weekday"] >= 5).astype(int)

    df["season"] = "other"
    df.loc[df["month"].isin([12, 1, 2]), "season"] = "winter"
    df.loc[df["month"].isin([3, 4, 5]), "season"] = "spring"
    df.loc[df["month"].isin([6, 7, 8]), "season"] = "summer"
    df.loc[df["month"].isin([9, 10, 11]), "season"] = "autumn"

    df["is_winter"] = (df["season"] == "winter").astype(int)

    return df


def consumption_summaries(df: pd.DataFrame, value_col: str = "consumption") -> None:
    if value_col not in df.columns:
        raise ValueError(f"Column '{value_col}' not found. Available: {df.columns.tolist()}")

    print("\n" + "=" * 60)
    print("GROUPED SUMMARIES")
    print("=" * 60)

    print("\n--- Consumption summary (overall) ---")
    print(df[value_col].describe().round(2))

    print("\n--- Variability and peak indicators ---")
    print("Std consumption:", round(df[value_col].std(), 2))
    print("90th percentile:", round(df[value_col].quantile(0.90), 2))
    print("95th percentile:", round(df[value_col].quantile(0.95), 2))
    print("Peak / average ratio:", round(df[value_col].max() / df[value_col].mean(), 2))

    print("\n--- Average consumption by hour ---")
    print(df.groupby("hour")[value_col].mean().round(2))

    print("\n--- Average consumption by weekday (Mon=0) ---")
    print(df.groupby("weekday")[value_col].mean().round(2))

    print("\n--- Average consumption by month ---")
    print(df.groupby("month")[value_col].mean().round(2))

    print("\n--- Average consumption by season ---")
    print(df.groupby("season")[value_col].mean().round(2))

    print("\n--- Duplicates ---")
    print("Duplicate full rows:", df.duplicated().sum())
    print("Duplicate timestamps:", df.index.duplicated().sum())

    s = df[value_col].dropna()
    peak = s.idxmax()
    trough = s.idxmin()
    print("\nPeak consumption timestamp:", peak, "value:", float(df.loc[peak, value_col]))
    print("Lowest consumption timestamp:", trough, "value:", float(df.loc[trough, value_col]))


def main():
    df_raw = load_data()
    df = clean_data(df_raw)

    basic_overview(df)

    df_feat = add_time_features(df)
    consumption_summaries(df_feat, value_col="consumption")


if __name__ == "__main__":
    main()