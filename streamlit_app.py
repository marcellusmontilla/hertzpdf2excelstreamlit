import streamlit as st

def calculate_projection(initial_balance, monthly_income, monthly_expenses, projection_months):
    balance = initial_balance
    projection_data = []

    for month in range(projection_months):
        balance += monthly_income - monthly_expenses
        projection_data.append(balance)

    return projection_data

def main():
    st.title("Financial Projection App")

    st.sidebar.header("Input Parameters")
    initial_balance = st.sidebar.number_input("Initial Balance", value=10000)
    monthly_income = st.sidebar.number_input("Monthly Income", value=5000)
    monthly_expenses = st.sidebar.number_input("Monthly Expenses", value=3000)
    projection_months = st.sidebar.number_input("Projection Months", value=12)

    projection_data = calculate_projection(initial_balance, monthly_income, monthly_expenses, projection_months)

    st.subheader("Financial Projection Chart")
    st.line_chart(projection_data)

if __name__ == "__main__":
    main()
