from prophet import Prophet
import pandas as pd


def generate_forecast(product_df):

    df = product_df.copy()

    df = df.rename(
        columns={
            "timestamp": "ds",
            "price": "y"
        }
    )

    df["ds"] = pd.to_datetime(df["ds"])

    model = Prophet()

    model.fit(df[["ds", "y"]])

    future = model.make_future_dataframe(
        periods=30
    )

    forecast = model.predict(future)

    return forecast
