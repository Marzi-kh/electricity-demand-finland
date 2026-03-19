from pathlib import Path
import pandas as pd

def load_data() -> pd.DataFrame:
    base_dir = Path(__file__).resolve().parents[1]
    file_path = base_dir / "Data" / "data.csv"
    print("looking here:", file_path)
    df = pd.read_csv(file_path, sep=";", engine="python")
    df.columns = df.columns.astype(str).str.replace('"', '').str.strip()
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["startTime"] = pd.to_datetime(df["startTime"], errors="coerce", utc=True)
    df["endTime"] = pd.to_datetime(df["endTime"], errors="coerce", utc=True)
    df = df.rename(columns={"Electricity consumption in Finland": "consumption"})

    df["consumption"] = pd.to_numeric(df["consumption"], errors="coerce")

    df = df.dropna(subset=["startTime", "consumption"])

    df = df.set_index("startTime").sort_index()
    df = df[~df.index.duplicated(keep="first")]

    df = df.drop(columns=["endTime"], errors="ignore")

    return df[["consumption"]]

if __name__ == "__main__":
    df_raw = load_data()
    df = clean_data(df_raw)

    print(df.head())
    print(df.shape)
    print(df.index.min(), "→", df.index.max())


