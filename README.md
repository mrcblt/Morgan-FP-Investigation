# Interpreting Morgan Fingerprint Bits Over a Complete Dataset

It is already very easy to display the encoded substructures of a Morgan Fingeprint bit for a specific molecule. However, if you train a machine learning model, for example a random forest, using Morgan fingerprints and look at the most important bits (feature importance), it is not sufficient to look at the substructure of this bit for a specific molecule. Due to collisions during fingerprint folding, it can happen that several substructures are encoded in one Morgan bit. For this, the analysis needs to be extended to all molecules.

This notebook attempts to illustrate this scenario and give an overview of the most important substructures of any bit for an example random forest model.
