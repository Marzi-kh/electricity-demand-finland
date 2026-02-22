import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from SCR.data_preprocessing import load_data, clean_data
from SCR.consumption_eda import add_time_features


OUTDIR = "outputs/figures"


def _ensure_outdir():
    os.makedirs(OUTDIR, exist_ok=True)


def plot_time_series(df):
    _ensure_outdir()
    plt.figure(figsize=(10, 5))
    df["consumption"].plot()
    plt.title("Electricity Consumption Over Time")
    plt.xlabel("Time")
    plt.ylabel("Consumption (MWh)")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/time_series.png")
    plt.close()


def plot_hourly_pattern(df):
    _ensure_outdir()
    hourly = df.groupby(df.index.hour)["consumption"].mean()
    plt.figure(figsize=(8, 4))
    hourly.plot()
    plt.title("Average Consumption by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Consumption (MWh)")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/hourly.png")
    plt.close()


def plot_monthly_pattern(df):
    _ensure_outdir()
    monthly = df.groupby(df.index.month)["consumption"].mean()
    plt.figure(figsize=(8, 4))
    monthly.plot()
    plt.title("Average Consumption by Month")
    plt.xlabel("Month")
    plt.ylabel("Consumption (MWh)")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/monthly.png")
    plt.close()


def plot_seasonal_pattern(df):
    _ensure_outdir()
    seasonal = df.groupby("season")["consumption"].mean()
    plt.figure(figsize=(6, 4))
    seasonal.plot(kind="bar")
    plt.title("Average Consumption by Season")
    plt.xlabel("Season")
    plt.ylabel("Consumption (MWh)")
    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/seasonal.png")
    plt.close()


def main():
    df_raw = load_data()
    df = clean_data(df_raw)
    df = add_time_features(df)

    plot_time_series(df)
    plot_hourly_pattern(df)
    plot_monthly_pattern(df)
    plot_seasonal_pattern(df)


if __name__ == "__main__":
    main()