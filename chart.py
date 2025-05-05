import pandas as pd
import matplotlib.pyplot as plt

# 1. Load your data
df = pd.read_csv("uk_logistics_companies.csv")

# 2. Prepare a simple breakdown: “With Website” vs “No Website”
df["has_website"] = df["website"].apply(lambda u: "With Website" if u else "No Website")
counts = df["has_website"].value_counts()

# 3. Plot a pie chart
fig, ax = plt.subplots()
ax.pie(
    counts.values,
    labels=counts.index,
    autopct="%1.1f%%",
    startangle=90
)
ax.set_title("Website Availability among UK Logistics Companies")

# 4. Save to file instead of showing
plt.savefig("website_availability_pie.png", dpi=150, bbox_inches="tight")
print("✅ Chart saved to website_availability_pie.png")
