#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "🚀 Starting the workflow..."

# Step 1: Activate virtual environment
echo "▶️ Activating virtual environment..."
source ./venv/bin/activate

# Step 2: Regenerate requirements.txt
echo "▶️ Generating requirements.txt..."
pipreqs ./src --force

# Step 3: Generate the Kaggle notebook from Python scripts
echo "▶️ Generating Kaggle notebook..."
python generate_notebook.py

# Step 4: Push the notebook to Kaggle using the Kaggle API
echo "▶️ Pushing to Kaggle..."
kaggle kernels push -p .

echo "✅ Workflow finished successfully!"