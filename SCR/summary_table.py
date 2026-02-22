import pandas as pd
from SCR import data_preprocessing
from SCR import consumption_eda


def create_summary_table(df, mae=None):
    summary = {
        "Metric": [
            "Peak consumption",
            "Lowest consumption",
            "Winter avg",
            "Summer avg",
            "Peak hour",
            "Model error (MAE)"
        ],
        "Value": [
            round(df["consumption"].max(), 2),
            round(df["consumption"].min(), 2),
            round(df[df["season"] == "winter"]["consumption"].mean(), 2),
            round(df[df["season"] == "summer"]["consumption"].mean(), 2),
            df.groupby(df.index.hour)["consumption"].mean().idxmax(),
            round(mae, 2) if mae is not None else "N/A"
        ]
    }

    return pd.DataFrame(summary)


def main():
    df_raw = data_preprocessing.load_data()
    df = data_preprocessing.clean_data(df_raw)
    df = consumption_eda.add_time_features(df)

    table = create_summary_table(df)
    print("\nSUMMARY TABLE")
    print(table)


if __name__ == "__main__":
    main()