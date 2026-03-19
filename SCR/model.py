from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from SCR.data_preprocessing import load_data, clean_data
from SCR.consumption_eda import add_time_features

# Load + prepare
df_raw = load_data()
df = clean_data(df_raw)
df = add_time_features(df)

# Features
X = df[["hour", "month", "weekday", "is_weekend", "is_winter"]]
y = df["consumption"]

# Time-series cross-validation
tscv = TimeSeriesSplit(n_splits=5)
mae_scores = []

for fold, (train_idx, test_idx) in enumerate(tscv.split(X), start=1):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores.append(mae)

    print(f"Fold {fold} MAE: {mae:.2f}")

print(f"\nAverage MAE across folds: {sum(mae_scores) / len(mae_scores):.2f}")