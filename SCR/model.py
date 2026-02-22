from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from SCR.data_preprocessing import load_data, clean_data
from SCR.consumption_eda import add_time_features

# Load + prepare
df_raw = load_data()
df = clean_data(df_raw)
df = add_time_features(df)

# Features
X = df[["hour", "month", "weekday"]]
y = df["consumption"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Model
model = RandomForestRegressor(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", round(mae, 2))
