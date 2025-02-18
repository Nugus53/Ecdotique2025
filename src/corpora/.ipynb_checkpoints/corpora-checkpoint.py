from pickle import EMPTY_LIST
import ipywidgets as widgets
from IPython.display import display, clear_output
from IPython.display import HTML,SVG
from io import StringIO
import json
import time
import pandas as pd
from collatex import Collation, collate
import pprint

class Projet:
    def __init__(self, name: str, option: dict={}):
        self.name = name
        self.witnesses = []
        self.defaultOption=option
        devOut=self.defaultOption["output"] if "output" in self.defaultOption.keys() else 'table'
        self.containers = {
            "option":widgets.Output(),
            "action":{"container":widgets.Output(),
                      "bouton":{
                          "add_witness":widgets.Button(description="Add Witness"),
                          "load_from_JSON":widgets.Button(description="Load JSON"),
                          "collate_text":widgets.Button(description="Collate Texts"),
                          "output_format":widgets.Dropdown(options=['table','csv','tsv','html','html2','svg_simple','svg','xml','tei','json','pandas-html','pandas-latex','pandas-xlsx'],value=devOut)
                      }
            },
            "output":widgets.Output(),
            "witnesses":widgets.Output()}



        self.option = {}
        self.defaultOption=option
        self.containers["action"]["bouton"]["add_witness"].on_click(self.add_witness)
        self.containers["action"]["bouton"]["load_from_JSON"].on_click(self.show_file_picker)
        self.containers["action"]["bouton"]["collate_text"].on_click(self.collate_witnesses)



        style=widgets.Layout(border='3px solid black')
        self.result_container=widgets.Box([widgets.Output()], layout=style)
        self.gui_option({'new':devOut})

        if "path" in self.defaultOption.keys():
            print(self.defaultOption["path"])
            with open(self.defaultOption["path"], "r", encoding="utf-8") as file:
                data = json.load(file)
            self.load_data(data)
            self.collate_witnesses()



    def get_list_witnesses_label(self):
        return [witness.label for witness in self.witnesses]

    def get_witness_by_label(self, label: str):
        return next((w for w in self.witnesses if w.label == label), None)

    def delete_witness_by_label(self, label: str):
        self.witnesses = [w for w in self.witnesses if w.label != label]
        self.create_widgets()

    def collate_witnesses(self,_=None):
      if len(self.witnesses) >0 :
        collation = Collation()
        for witness in self.witnesses:
          collation.add_plain_witness(witness.label, witness.text)
        format_out=self.containers["action"]["bouton"]["output_format"].value
        with self.containers["output"]:
            clear_output()
            match format_out:
              case "csv":
                alignment_table = collate(collation, output="csv", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout=self.option["layout"].value)
              case "tsv":
                alignment_table = collate(collation, output="tsv", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout=self.option["layout"].value)
              case "table" :
                alignment_table = collate(collation, output="table", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout=self.option["layout"].value)
                alignment_table=str(alignment_table)
              case "html2" :
                alignment_table = collate(collation, output="html2", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value)
              case "html" :
                alignment_table = collate(collation, output="html", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout=self.option["layout"].value)
              case "pandas-html":
                alignment_table = collate(collation, output="tsv", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout='horizontal')
                if self.option["layout"].value=='horizontal':
                  alignment_table = HTML(pd.read_csv(StringIO(alignment_table),sep='\t', header=None,index_col=0).fillna('-').to_html(index=True, header=False))
                else :
                  alignment_table = HTML(pd.read_csv(StringIO(alignment_table),sep='\t', header=None,index_col=0).fillna('-').transpose().to_html(index=False, header=True))
              case "pandas-latex":
                alignment_table = collate(collation, output="tsv", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout='horizontal')
                if self.option["layout"].value=='horizontal':
                  alignment_table = pd.read_csv(StringIO(alignment_table),sep='\t', header=None,index_col=0).fillna('-').to_latex(index=True, header=False)
                else :
                  alignment_table = pd.read_csv(StringIO(alignment_table),sep='\t', header=None,index_col=0).fillna('-').transpose().to_latex(index=False, header=True)
              case "pandas-xlsx":
                alignment_table = collate(collation, output="tsv", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout='horizontal')
                if self.option["layout"].value=='horizontal':
                  alignment_table = pd.read_csv(StringIO(alignment_table),sep='\t', header=None,index_col=0).fillna('-').to_excel('/out/output.xlsx',index=True, header=False,encoding='utf-8')
                  alignment_table = "/out/output.xlsx"
                else :
                  alignment_table = pd.read_csv(StringIO(alignment_table),sep='\t', header=None,index_col=0).fillna('-').transpose().to_excel('/out/output.xlsx',index=False, header=True,encoding='utf-8')
                  alignment_table = "/out/output.xlsx"
                    
              case "svg_simple" :
                alignment_table = collate(collation, output="svg_simple", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value)
              case "svg" :
                alignment_table = collate(collation, output="svg", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value)
              case "xml" :
                alignment_table = collate(collation, output="xml", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value)
              case "tei" :
                alignment_table = collate(collation, output="tei", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout=self.option["layout"].value,indent=self.option["indent"].value)
              case "json" :
                alignment_table = collate(collation, output="json", segmentation=self.option["segmentation"].value, near_match=self.option["near_match"].value,layout=self.option["layout"])
    
            #add panda.clipboard
          
            if format_out=="json":
               pprint.pprint(alignment_table)
            elif isinstance(alignment_table, SVG):
                alignment_table.display()
            elif isinstance(alignment_table, HTML):
                display(alignment_table)
            elif isinstance(alignment_table, str):
                print(alignment_table)
            else:
                 display(alignment_table)



        self.create_widgets()

    def gui_option(self,value):


      self.collate_option(value["new"])
      self.create_widgets()

    def collate_option(self,format):
      self.option["segmentation"] = widgets.ToggleButton(
              value= self.defaultOption["segmentation"] if "segmentation" in self.defaultOption.keys() else False,
              description="Segmentation",
              button_style="primary",
              tooltip="Click to toggle",
              icon="check"
              )
      self.option["near_match"]=widgets.ToggleButton(
              value=self.defaultOption["near_match"] if "near_match" in self.defaultOption.keys() else False,
              description="Near_match",
              button_style="primary",
              tooltip="Click to toggle",
              icon="check"
              )
      self.option["indent"]=widgets.ToggleButton(
              value=self.defaultOption["indent"] if "indent" in self.defaultOption.keys() else False,
              description="Indent",
              button_style="primary",
              tooltip="Click to toggle",
              icon="check"
              )
      self.option["layout"]=widgets.Dropdown(
                options=['horizontal', 'vertical',],
                value=self.defaultOption["layout"] if "layout" in self.defaultOption.keys() else 'vertical',
                description='Layout',
                disabled=False,
            )
      match format:
        case "table" :
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        case "csv" :
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        case "tsv" :
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        case "html" :
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        case "html2" :
          items = [self.option["segmentation"],self.option["near_match"]]
        case "svg_simple":
          items = [self.option["segmentation"],self.option["near_match"]]
        case "svg":
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        case "xml":
          items = [self.option["segmentation"],self.option["near_match"]]
        case "tei":
          items = [self.option["segmentation"],self.option["near_match"],self.option["indent"]]
        case "json":
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        
        case "pandas-html" :
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        case "pandas-latex" :
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
        case "pandas-xlsx" :
          items = [self.option["segmentation"],self.option["near_match"],self.option["layout"]]
              
      with self.containers["option"]:
        clear_output()
        display(widgets.Box(items,layout=widgets.Layout(border='3px solid black')))
        self.create_widgets()
    def add_witness(self, _):
        witness = Witness(f"Witness {len(self.witnesses) + 1}", "",self)
        self.witnesses.append(witness)
        self.create_widgets()

    def create_widgets(self):
        with self.containers["action"]["container"]:
            clear_output()
            for key,value in self.containers["action"]["bouton"].items():
                display(value)

        with self.containers["witnesses"]:
            clear_output()
            for witness in self.witnesses:
                display(witness.container)  # Affichage des témoins
            self.containers["action"]["bouton"]["output_format"].observe(self.gui_option, names='value')
    
    
    def show_file_picker(self, _):
        """Affiche un sélecteur de fichier et le remplace après le chargement"""

        file_picker = widgets.FileUpload(accept=".json", multiple=False)
      
        def process_file(change):
            if isinstance(file_picker.value, dict):
                uploaded_file = next(iter(file_picker.value.values()))
                content = uploaded_file['content'].decode("utf-8")  # If it's a dictionary
            elif isinstance(file_picker.value, tuple):
                uploaded_file = file_picker.value[0]
                content = bytes(uploaded_file['content']).decode("utf-8")  # If it's a tuple, take first item
            else:
                raise TypeError("Unexpected file_picker.value type: " + str(type(file_picker.value)))

          
              
            data = json.loads(content)
            self.load_data(data)

            file_picker.close()  # Supprime le sélecteur après le chargement

         
        
        file_picker.observe(process_file, names='value')
        with self.containers["output"]:
          display(file_picker)


    #def load_exemple(self,name)



    def load_data(self,data):
      for label, text in data.items():
        if label not in self.get_list_witnesses_label():
            self.witnesses.append(Witness(label, text, self))
            time.sleep(0.5)  # Pause pour simuler le chargement@
            self.create_widgets()  # Rafraîchit l'interface
        else:
          print(f"Witness '{label}' already exists!")
class Witness:
    def __init__(self, label: str, text: str, parent: Projet):
        self.label = label
        self.text = text
        self.parent = parent
        self.container = widgets.Output()
        self.create_widgets()

    def create_widgets(self):
        self.label_input = widgets.Text(value=self.label, description="Label:", layout=widgets.Layout(width="50%"))
        self.label_input.observe(self.update_label, names="value")

        self.text_input = widgets.Textarea(value=self.text, placeholder=f"Enter text for {self.label}", description="Text:", layout=widgets.Layout(width="100%"))
        self.text_input.observe(self.update_text, names="value")

        self.delete_button = widgets.Button(description="Delete", button_style="danger")
        self.delete_button.on_click(self.delete_witness)

        with self.container:
            clear_output()
            display(self.label_input, self.text_input, self.delete_button)

    def update_label(self, change):
        self.label = change["new"]

    def update_text(self, change):
        self.text = change["new"]

    def delete_witness(self, _):
        self.parent.delete_witness_by_label(self.label)
        with self.container:
            clear_output()

# Création et affichage d'une instance Projet
def corporaMenu(name, option: dict = {}, tab_index: int = 0):
    projet = Projet(name, option=option)
    tab = widgets.Tab()
    tab.children = [projet.containers['witnesses'], projet.containers['output']]
    tab.titles = ["Temoins", "sortie"]
    
    if tab_index:
        tab.selected_index = tab_index 
    display(widgets.VBox([projet.containers['action']['container'], projet.containers['option'],tab]))