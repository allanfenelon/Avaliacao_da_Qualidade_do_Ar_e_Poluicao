import os
from nbconvert import MarkdownExporter
import nbformat

# Caminho absoluto para o diretório de notebooks
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Diretório raiz do projeto
notebook_filename = os.path.join(project_dir, "notebooks", "2. MODELING.ipynb")  # Caminho absoluto para o notebook
markdown_dir = os.path.join(project_dir, "markdown")  # Diretório onde o arquivo .md será salvo

# Caminho para o arquivo Markdown
markdown_filename = os.path.join(markdown_dir, os.path.basename(notebook_filename).replace(".ipynb", ".md"))


if not os.path.exists(markdown_dir):
    os.makedirs(markdown_dir)


if not os.path.exists(notebook_filename):
    print(f"Erro: O arquivo {notebook_filename} não foi encontrado.")
else:
    if not os.path.exists(markdown_filename):
        with open(notebook_filename, "r", encoding="utf-8") as notebook_file:
            notebook_content = nbformat.read(notebook_file, as_version=4)
        markdown_exporter = MarkdownExporter()
        body, resources = markdown_exporter.from_notebook_node(notebook_content)
        with open(markdown_filename, "w", encoding="utf-8") as markdown_file:
            markdown_file.write(body)
        print(f"Conversão concluída! O arquivo {markdown_filename} foi salvo.")
    else:
        print(f"O arquivo {markdown_filename} já existe no repositório de Markdown.")
