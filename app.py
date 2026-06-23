import streamlit as st
from analytics.analysis import (
    get_summary_stats,
    get_product_history,
    get_best_deal,
    get_most_volatile_product
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Hyperlocal Price Intelligence",
    layout="wide"
)

st.title("🛒 Hyperlocal Price Intelligence Dashboard")


page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Insights",
        "Forecast"
    ]
)
# =========================
# SUMMARY SECTION
# =========================

if page == "Dashboard":

    summary = get_summary_stats()

    if summary is None or summary.empty:
        st.warning("No data found in database.")
        st.stop()

    total_products = len(summary)
    avg_price = summary["Average_Price"].mean()
    lowest_price = summary["Lowest_Price"].min()
    highest_price = summary["Highest_Price"].max()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Products Tracked", total_products)
    col2.metric("Average Price", f"₹{avg_price:,.0f}")
    col3.metric("Lowest Price", f"₹{lowest_price:,.0f}")
    col4.metric("Highest Price", f"₹{highest_price:,.0f}")

    st.divider()

    st.subheader("📊 Product Summary")

    st.dataframe(summary, use_container_width=True)

    history = get_product_history()

    st.divider()

    st.subheader("🔍 Product Analysis")

    products = history["name"].unique()

    selected_product = st.selectbox(
        "Select Product",
        products,
        key="dashboard_product"
    )

    product_df = history[
        history["name"] == selected_product
    ]

    current_price = product_df["price"].iloc[-1]
    lowest_product_price = product_df["price"].min()
    highest_product_price = product_df["price"].max()
    avg_product_price = product_df["price"].mean()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Current Price", f"₹{current_price:,.0f}")
    c2.metric("Lowest Price", f"₹{lowest_product_price:,.0f}")
    c3.metric("Highest Price", f"₹{highest_product_price:,.0f}")
    c4.metric("Average Price", f"₹{avg_product_price:,.0f}")

    st.divider()

    st.subheader("📈 Price Trend")

    st.line_chart(
        product_df.set_index("timestamp")["price"]
    )

    st.divider()

    st.subheader("🟢 Buy Recommendation")

    difference = (
        (current_price - avg_product_price)
        / avg_product_price
    ) * 100

    if current_price <= avg_product_price * 0.95:
        st.success(
            f"""
BUY NOW ✅

Current price is {abs(difference):.1f}% below average price.
Price is close to its historical minimum.
"""
        )

    elif current_price >= avg_product_price * 1.05:
        st.error(
            f"""
WAIT ⏳

Current price is {difference:.1f}% above average price.
Better opportunities may come later.
"""
        )

    else:
        st.info(
            """
FAIR PRICE ℹ️

Current price is close to historical average.
Buy if needed, otherwise monitor trends.
"""
        )

    st.divider()

    with st.expander("📋 View Raw Price History"):
        st.dataframe(
            product_df,
            use_container_width=True
        )

if page == "Analytics":

    st.header("📊 Analytics")

    history = get_product_history()

    selected_product_analytics = st.selectbox(
    "Select Product",
    history["name"].unique(),
    key="analytics_product"
)

    product_df = history[
        history["name"] == selected_product_analytics
    ]

    st.subheader("Price Trend")

    st.line_chart(
        product_df.set_index("timestamp")["price"]
    )

    st.subheader("Price History")

    st.dataframe(
        product_df,
        use_container_width=True
    )

if page == "Insights":

    st.header("💡 Market Insights")

    best_deal = get_best_deal()

    volatile = get_most_volatile_product()

    st.success(
        f"""
🔥 Best Deal Available

Product: {best_deal['name']}

Current Price: ₹{best_deal['Current_Price']:,.0f}

Average Price: ₹{best_deal['Average_Price']:,.0f}
"""
    )

    st.warning(
        f"""
⚡ Most Volatile Product

Product: {volatile['Product']}

Volatility: ₹{volatile['Volatility']:,.0f}
"""
    )

    st.divider()

    st.subheader("📊 Complete Product Ranking")

    summary = get_summary_stats()

    summary["Savings %"] = (
        (summary["Average_Price"] - summary["Current_Price"])
        / summary["Average_Price"]
    ) * 100

    summary = summary.sort_values(
        "Savings %",
        ascending=False
    )

    st.dataframe(
        summary,
        use_container_width=True
    )

if page == "Forecast":

    from analytics.forecast import generate_forecast

    st.header("🔮 Price Forecasting")

    history = get_product_history()

    product = st.selectbox(
        "Select Product",
        history["name"].unique(),
        key="forecast_product"
    )

    product_df = history[
        history["name"] == product
    ]

    forecast = generate_forecast(product_df)

    chart_data = forecast[
        ["ds", "yhat"]
    ].set_index("ds")

    st.line_chart(chart_data)

    current_price = product_df["price"].iloc[-1]

    future_price = forecast["yhat"].iloc[-1]

    change_pct = (
        (future_price - current_price)
        / current_price
    ) * 100

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Current Price",
        f"₹{current_price:,.0f}"
    )

    c2.metric(
        "Forecast Price",
        f"₹{future_price:,.0f}"
    )

    c3.metric(
        "Expected Change",
        f"{change_pct:.2f}%"
    )

    if future_price > current_price * 1.03:
        st.success(
            "📈 Prices are expected to rise. Consider buying now."
        )

    elif future_price < current_price * 0.97:
        st.warning(
            "📉 Prices are expected to fall. Waiting may save money."
        )

    else:
        st.info(
            "➖ Prices are expected to remain stable."
        )