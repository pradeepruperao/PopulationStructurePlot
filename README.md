# PopulationStructurePlot
Generate the population (admixture) structure plot
# Usage
python3 structure_plot.py
Note: Need to add minor inputs in script like file name.

# Input
The input should be the output of the admixture analysis with sample names in the first column as below

A78 0.999980 0.000010 0.000010
B06 0.999980 0.000010 0.000010
F55 0.999980 0.000010 0.000010
I53 0.999980 0.000010 0.000010
K86 0.999980 0.000010 0.000010
B43 0.999973 0.000017 0.000010

# Output
The output is of mainly of three types based on the sample number.
Input file with sample number less than 50 will generate below image
![structure_plotLt50](https://github.com/user-attachments/assets/ad77875e-d757-41bc-be61-3a70281271dd)

Input file with sample number between 50 to 100 will generate below image
![structure_plotGt50](https://github.com/user-attachments/assets/608bbb8a-198c-4554-b62a-1ef82819ca25)

Input file with sample number more than 100 will generate below image
![structure_plotGt100](https://github.com/user-attachments/assets/3798cbcf-b024-4a18-85ff-d457134f5fc1)
