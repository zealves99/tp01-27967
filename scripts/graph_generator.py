import json
import os
import matplotlib.pyplot as plt

# --- Base directory of this script ---
base_dir = os.path.dirname(os.path.abspath(__file__))

# --- Paths for input JSON and output folder ---
input_file = os.path.join(base_dir, '..', 'data', 'output', 'layer-graph-data.json')
print(f"Reading data from: {input_file}")
output_dir = os.path.join(base_dir, '..', 'data','output', 'graphs')
os.makedirs(output_dir, exist_ok=True)

# --- Load JSON data ---
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# --- Loop through each entry in JSON (usually only one) ---
for entry in data:
    labels = entry.get('labels', [])
    values = entry.get('data', [[]])[0]

    # --- Bar Chart ---
    plt.figure(figsize=(12,6))
    plt.bar(labels, values, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('PowerUsed (W)')
    plt.title("Power Used by Layer (Bar Chart)")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'layer_bar_graph.png'))
    plt.close()

    # --- Pie Chart with small slices grouped as 'Other' ---
    threshold_percent = 2  # slices below this % will be grouped
    total = sum(values)
    new_labels, new_values = [], []
    other_value = 0

    for label, value in zip(labels, values):
        perc = 100 * value / total
        if perc < threshold_percent:
            other_value += value
        else:
            new_labels.append(label)
            new_values.append(value)

    if other_value > 0:
        new_labels.append('Other')
        new_values.append(other_value)

    plt.figure(figsize=(8,8))
    plt.pie(new_values, labels=new_labels, autopct='%1.1f%%', startangle=140)
    plt.title("Power Used by Layer (Pie Chart)")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'layer_pie_graph.png'))
    plt.close()

print(f"Graphs generated in: {output_dir}")
