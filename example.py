from rdkit import Chem # com essa biblioteca poderemos visualizar o composto, a partir de um png
from rdkit.Chem import Draw
import base64
from io import BytesIO


formula = "OC[C@@H](O1)[C@@H](O)[C@H](O)[C@@H](O)[C@H](O)1"
mol = Chem.MolFromSmiles(formula)

image_data = BytesIO()
Draw.MolToImage(mol).save(image_data, format="PNG")
base64_image = base64.b64encode(image_data.getvalue()).decode("utf-8")
Draw.MolToFile(mol, "mol.png")
