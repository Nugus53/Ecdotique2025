import ipywidgets as widgets
from IPython.display import display, Markdown, IFrame, clear_output
import subprocess

class LatexDoc:
    def __init__(self, name):
        self.name = name
        compile_button = widgets.Button(description="Compile with LuaLaTeX")
        compile_button.on_click(self.compile_latex)
        self.containers = {"btn": widgets.Output(), "pdf": widgets.Output(), "latex": widgets.Output()}
        with self.containers["btn"]:
            display(compile_button)
        hbox_layout = widgets.HBox([self.containers['latex'], self.containers['pdf']])
        hbox_layout.children[0].layout.width = '50%'  # Set first widget (latex) to 50% width
        hbox_layout.children[1].layout.width = '50%'  # Set second widget (pdf) to 50% width

        display(widgets.VBox([self.containers['btn'], hbox_layout]))

    def view_latex(self):
        latex_path = f"{self.name}.tex"
        pdf_path = f"{self.name}.pdf"

        pdf_widget = IFrame(pdf_path, width=800, height=600)
        display(pdf_widget)
        with open(latex_path, 'r') as file:
            latex_code = file.read()
        markdown_content = f"```latex\n{latex_code}\n```"
        latex_widget = Markdown(markdown_content)
        
        with self.containers["pdf"]:
            clear_output()
            display(pdf_widget)
        with self.containers["latex"]:
            clear_output()
            display(latex_widget)

    def compile_latex(self, change):
        try:
            subprocess.run(['lualatex', '-interaction=batchmode', f"{self.name}.tex"], check=True)
            self.view_latex()
            print(f"LaTeX compiled successfully! Output saved as {self.name}.pdf")
        except subprocess.CalledProcessError as e:
            self.view_latex()
            print(f"Error during compilation: {e}")
