"""
Project: Matrix Computation & Data Visualization
------------------------------------------------
Performs matrix operations using NumPy and simple data visualization using pandas & matplotlib.

Time Complexity:
  - Matrix addition/multiplication: O(n^3) for multiplication, O(n^2) for addition
  - Data visualization: O(n)
Space Complexity: O(n^2)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def matrix_operations():
    """Perform basic matrix operations using NumPy."""
    # Define two 2x2 matrices
    A = np.array([[2, 4], [6, 8]])
    B = np.array([[1, 3], [5, 7]])

    print("Matrix A:\n", A)
    print("\nMatrix B:\n", B)

    # Matrix addition
    addition = A + B
    print("\nAddition:\n", addition)

    # Matrix multiplication (dot product)
    multiplication = np.dot(A, B)
    print("\nMultiplication:\n", multiplication)

    return addition, multiplication


def dataset_visualization():
    """Visualize dataset trends using pandas and matplotlib."""
    # Create a small dataset
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [250, 300, 280, 400, 500],
        "Profit": [40, 60, 55, 80, 100]
    }

    df = pd.DataFrame(data)
    print("\nData Summary:\n", df.describe())

    # Create a figure before plotting
    plt.figure(figsize=(8, 5))

    # Plot Sales and Profit trends
    plt.plot(df["Month"], df["Sales"], label="Sales", marker='o')
    plt.plot(df["Month"], df["Profit"], label="Profit", marker='s')

    # Add titles and labels
    plt.title("Monthly Sales & Profit Trend")
    plt.xlabel("Month")
    plt.ylabel("Value (in ₹)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()  # Avoid layout overlap

    # Display the plot
    plt.show()


# Run both functions only when file is executed directly
if __name__ == "__main__":
    print("=== Matrix Operations ===")
    matrix_operations()

    print("\n=== Data Visualization ===")
    dataset_visualization()
