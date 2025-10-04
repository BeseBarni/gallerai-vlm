import jupytext
import nbformat
import glob

SCRIPT_FILES = sorted(glob.glob('src/*.py'))
OUTPUT_NOTEBOOK = 'gai-vlm.ipynb'


if not SCRIPT_FILES:
    raise ValueError("No Python files found in the 'src' directory.")

final_notebook = nbformat.v4.new_notebook()

for file_path in SCRIPT_FILES:
    print(f"Processing: {file_path}")

    notebook_part = jupytext.read(file_path)

    final_notebook.cells.extend(notebook_part.cells)

jupytext.write(final_notebook, OUTPUT_NOTEBOOK)

print(f"\n✅ Notebook successfully generated at: {OUTPUT_NOTEBOOK}")