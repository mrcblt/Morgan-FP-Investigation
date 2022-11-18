import pandas as pd
import numpy as np
from collections import defaultdict
from rdkit.Chem import AllChem as Chem

class Bits_Displayer:
    """
    Displays the bits of compounds.
    """
    def __init__(self, n_bits = 2048):
        """
        Parameters:
         1. n_bits: int, number of bits to be used. Default is 2048.
        """
        self.n_bits = n_bits

    def _feature_name_generator(self):
        """
        Generates default feature names.

        Parameters:
         1. n_bits: Number of bits in the fingerprint.
        
        Returns:
         1. feature_names: List of feature names.
        """
        feature_names = [f"Feature {i}" for i in range(0, self.n_bits)]

        return feature_names

    def create_shap_df(self, shap_values, feature_names = None):
        """
        Creates a dataframe where each row represents a compound and each column represents a bit. 

        Parameters:
            1. shap_values: SHAP values of the compounds.
            2. feature_names: List of feature names. Default is None and in that case, generic feature names are generated.
            3. n_bits: Number of bits in the fingerprint.
        """

        if feature_names is None:
            feature_names = self._feature_name_generator(self.n_bits)

        self.shap_df = pd.DataFrame(shap_values, columns= feature_names)

        self.shap_importance_df = pd.DataFrame(list(np.abs(self.shap_df.values).mean(0)), columns = ["Importance"])
        self.shap_importance_df.index.rename('Bits', inplace=True)
        self.shap_importance_df.sort_values(by= "Importance", ascending= False, inplace= True)

        return self.shap_df, self.shap_importance_df

    def on_bit_calculator(self, df, bit_info_mols):
        df_mol = df.copy()
        self.subs_per_on_bit = defaultdict(list)
        for i, (_, row) in enumerate(df_mol.iterrows()):
            mol = Chem.MolFromSmiles(row["Smiles"])
            bit_info_mol = bit_info_mols[i]
            for bit in bit_info_mol:
                for atom_index, r in bit[bit_info_mol]:
                    self.subs_per_on_bit[bit].append((mol, atom_index, r))
        
        return self.subs_per_on_bit




