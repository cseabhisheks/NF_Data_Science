# A company tracked its monthly sales performance during the year 2025.

# The data is given below:

# info = {
#     "Months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

#     "Units_Sold": [10, 15, 20, 18, 25, 30,
#                    35, 32, 28, 40, 45, 50],

#     "Revenue": [100, 150, 200, 180, 250, 300,
#                 350, 320, 280, 400, 450, 500]
# }
# Tasks
# 1. Line Plot

# Create a line graph showing the monthly revenue trend throughout the year.

# 2. Bar Chart

# Create a bar chart displaying units sold each month.

# 3. Pie Chart

# Show the percentage contribution of revenue for the first six months (Jan–Jun).

# 4. Histogram

# Create a histogram of monthly revenues to analyze the distribution of revenue values.

# 5. Scatter Plot

# Plot Units Sold vs Revenue and examine whether there is a relationship between them.

info = {
    "Months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

    "Units_Sold": [10, 15, 20, 18, 25, 30,
                   35, 32, 28, 40, 45, 50],

    "Revenue": [100, 150, 200, 180, 250, 300,
                350, 320, 280, 400, 450, 500]
}

#line plot
import matplotlib.pyplot as plt

plt.plot(info["Months"], info["Revenue"], marker="o", color="blue")

plt.title("Monthly Revenue Trend (2025)")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()
# bar chart
plt.bar(info["Months"], info["Units_Sold"], color="green")

plt.title("Units Sold per Month (2025)")
plt.xlabel("Months")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)# rotate the x axis label

plt.show()
# pie chart
first_half_months = info["Months"][:6]
first_half_revenue = info["Revenue"][:6]

plt.pie(
    first_half_revenue,
    labels=first_half_months,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue Contribution (Jan–Jun)")
plt.show()
#histogram
plt.hist(info["Revenue"], bins=5, color="purple", edgecolor="black")

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")

plt.show()
#scatter plot
plt.scatter(
    info["Units_Sold"],
    info["Revenue"],
    color="red",
    s=100,
    alpha=0.7
)

plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue")

plt.show()