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

    plt.figure(figsize=(11, 5))
    plt.plot(df.index, df["consumption"], linewidth=1)

    plt.title("Electricity Consumption Over Time")
    plt.xlabel("Time")
    plt.ylabel("Consumption (MWh)")
    plt.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/time_series.png", dpi=300)
    plt.close()


def plot_hourly_pattern(df):
    _ensure_outdir()

    hourly = df.groupby(df.index.hour)["consumption"].mean()

    plt.figure(figsize=(8, 4))
    plt.plot(hourly.index, hourly.values, marker="o", linewidth=2)

    plt.title("Average Consumption by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Consumption (MWh)")
    plt.xticks(range(0, 24, 2))
    plt.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/hourly.png", dpi=300)
    plt.close()

def plot_monthly_pattern(df):
    _ensure_outdir()

    monthly = df.groupby(df.index.month)["consumption"].mean()
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.figure(figsize=(8, 4))
    bars = plt.bar(monthly.index, monthly.values)

    plt.title("Average Consumption by Month")
    plt.xlabel("Month")
    plt.ylabel("Consumption (MWh)")
    plt.xticks(range(1, 13), month_labels)
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    # value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/monthly.png", dpi=300)
    plt.close()

def plot_weekday_pattern(df):
    _ensure_outdir()

    weekday = df.groupby(df.index.weekday)["consumption"].mean()
    labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    plt.figure(figsize=(8, 4))
    bars = plt.bar(weekday.index, weekday.values)

    plt.title("Average Consumption by Weekday")
    plt.xlabel("Day of Week")
    plt.ylabel("Consumption (MWh)")
    plt.xticks(range(7), labels)
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    # value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:,.0f}",
            ha="center",
            va="bottom",
            fontsize=8
        )

    plt.tight_layout()
    plt.savefig(f"{OUTDIR}/weekday.png", dpi=300)
    plt.close()


def main():
    df_raw = load_data()
    df = clean_data(df_raw)
    df = add_time_features(df)

    plot_time_series(df)
    plot_hourly_pattern(df)
    plot_monthly_pattern(df)
    plot_weekday_pattern(df)


if __name__ == "__main__":
    main()