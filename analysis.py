import sqlite3
import pandas as pd

DB_PATH = "data/price_history.db"


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_connection():
    return sqlite3.connect(DB_PATH)


# ==========================================
# LOAD ALL PRICE DATA
# ==========================================

def get_price_data():
    conn = get_connection()

    query = """
    SELECT
        name,
        price,
        timestamp
    FROM prices
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# ==========================================
# PRODUCT SUMMARY STATS
# ==========================================

def get_summary_stats():

    df = get_price_data()

    if df.empty:
        return pd.DataFrame()

    summary = (
        df.groupby("name")["price"]
        .agg(
            Current_Price="last",
            Lowest_Price="min",
            Highest_Price="max",
            Average_Price="mean",
            Records="count"
        )
        .reset_index()
    )

    summary["Average_Price"] = summary["Average_Price"].round(0)

    return summary


# ==========================================
# PRODUCT HISTORY
# ==========================================

def get_product_history():

    df = get_price_data()

    if df.empty:
        return pd.DataFrame()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df = df.sort_values("timestamp")

    return df


# ==========================================
# PRODUCT INSIGHTS
# ==========================================

def get_product_insights(product_name):

    history = get_product_history()

    product_df = history[
        history["name"] == product_name
    ]

    if product_df.empty:
        return None

    current_price = product_df["price"].iloc[-1]

    lowest_price = product_df["price"].min()

    highest_price = product_df["price"].max()

    average_price = product_df["price"].mean()

    volatility = product_df["price"].std()

    return {
        "current_price": current_price,
        "lowest_price": lowest_price,
        "highest_price": highest_price,
        "average_price": average_price,
        "volatility": volatility
    }


# ==========================================
# BUY RECOMMENDATION ENGINE
# ==========================================

def get_buy_recommendation(product_name):

    insights = get_product_insights(product_name)

    if insights is None:
        return "No Data"

    current_price = insights["current_price"]

    average_price = insights["average_price"]

    if current_price <= average_price * 0.95:
        return "BUY NOW"

    elif current_price >= average_price * 1.05:
        return "WAIT"

    else:
        return "FAIR PRICE"


# ==========================================
# BEST DEAL PRODUCT
# ==========================================

def get_best_deal():

    summary = get_summary_stats()

    if summary.empty:
        return None

    summary["Deal_Score"] = (
        (summary["Average_Price"] - summary["Current_Price"])
        / summary["Average_Price"]
    ) * 100

    best_deal = summary.sort_values(
        "Deal_Score",
        ascending=False
    ).iloc[0]

    return best_deal


# ==========================================
# MOST VOLATILE PRODUCT
# ==========================================

def get_most_volatile_product():

    history = get_product_history()

    if history.empty:
        return None

    volatility_df = (
        history.groupby("name")["price"]
        .std()
        .reset_index()
    )

    volatility_df.columns = [
        "Product",
        "Volatility"
    ]

    most_volatile = volatility_df.sort_values(
        "Volatility",
        ascending=False
    ).iloc[0]

    return most_volatile


# ==========================================
# OVERALL DASHBOARD METRICS
# ==========================================

def get_dashboard_metrics():

    summary = get_summary_stats()

    if summary.empty:
        return None

    metrics = {
        "total_products": len(summary),
        "average_price": summary["Average_Price"].mean(),
        "lowest_price": summary["Lowest_Price"].min(),
        "highest_price": summary["Highest_Price"].max()
    }

    return metrics