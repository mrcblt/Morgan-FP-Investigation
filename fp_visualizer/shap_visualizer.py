import pandas as pd
import numpy as np

class Bits_Displayer:
    """
    Displays the bits of compounds.
    """
    def __init__(self):
        pass

    def _feature_name_generator(self, n_bits):
        """
        Generates default feature names.

        Parameters:
         1. n_bits: Number of bits in the fingerprint.
        
        Returns:
         1. feature_names: List of feature names.
        """
        feature_names = [f"Feature {i}" for i in range(0, n_bits)]

        return feature_names

    def create_shap_df(self, shap_values, n_bits, feature_names = None):
        """
        Creates a dataframe where each row represents a compound and each column represents a bit. 

        Parameters:
            1. shap_values: SHAP values of the compounds.
            2. feature_names: List of feature names. Default is None and in that case, generic feature names are generated.
            3. n_bits: Number of bits in the fingerprint.
        """
        self.n_bits = n_bits
        if feature_names is None:
            feature_names = self._feature_name_generator(n_bits)
        self.shap_df = pd.DataFrame(shap_values, columns= feature_names)

        




