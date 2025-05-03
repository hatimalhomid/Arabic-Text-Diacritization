import nbformat

def clean_widgets_metadata(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    if 'widgets' in nb.metadata:
        if 'state' not in nb.metadata['widgets']:
            print(f"Fixing notebook: {notebook_path}")
            del nb.metadata['widgets']  # Remove incomplete widget metadata

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

clean_widgets_metadata('C:\\Users\\Hatim\\Desktop\\Arabic-Text-Diacritization\\Arabic-Text-Diacritization\\Arabic_Text_Diacritization_Challenge_final.ipynb')
