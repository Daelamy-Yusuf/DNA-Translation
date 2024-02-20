# DNA to Amino Acid
## This repository contains a Python script to translate DNA sequences into protein sequences. The translation is performed using the standard genetic code.
Program's operation can be outlined as follows:
1. **Inputting DNA**: Users can input the DNA sequence to be converted. This input can be customized according to the user's needs, allowing input from a file or from the terminal.
2. **Removing lines and spaces**: Create a new variable by removing lines and spaces from the previous variable using the replace() function and print it to the terminal.
3. **Reversing DNA sequence**: Reverse the existing DNA sequence using the [::-1] function and call this function. This function will reverse the order so that the first letter becomes the last.
4. **Translating DNA into RNA**: Create a dictionary with .maketrans() before translating and translate it using .translate(), then print the result to the terminal.
5. **Replacing RNA codons with proteins**: First, create a dictionary to translate RNA into proteins. Then, create a loop using for where every 3 letters of RNA codons will be translated into proteins and print them to the terminal.
6. **Counting the number of each type of amino acid**: Counting is done by creating a list where each type of amino acid starts from 0. Then create a loop using for where every same letter is read, it will increase by 1.
7. **Printing the number of each amino acid**: First, create a list of names and letters of each amino acid and print the number of codons using len(), and create a loop using for which contains if the number of amino acids read is not the same as 0 then the number of amino acids will be printed to the terminal.

**Output**: The translated protein sequences will be displayed in the terminal

**The DNA sequence is:**
>TTATTCTAATAAGTAATAATCAACGTAAAAATTAACAATATTAATAGAAATATAATTGATTATTTTTATTAATATAGTATTGTTAAATTGTATTATAGAACTGTATGATAAAGTTGTCTGCAT

**The RNA sequence is:**
>AUGCAGACAACUUUAUCAUACAGUUCUAUAAUACAAUUUAACAAUACUAUAUUAAUAAAAAUAAUCAAUUAUAUUUCUAUUAAUAUUGUUAAUUUUUACGUUGAUUAUUACUUAUUAGAAUAA

**The protein sequence is:**
>MQTTLSYSSIIQFNNTILIKIINYISINIVNFYVDYYLLE*

**Another information**
>Total codon : 41
Asparagine : 5
Aspartic Acid : 1
Glutamic Acid : 1
Glutamine : 2

**Contributors:**
* Ahmad Daelamy Yusuf
* Fatimah Azzahra
* Virginia Valensiene Elichatiti
* Yasmina Ashfa Zahidah

Feedback and Contributions:
Feedback and contributions are welcome! Feel free to open an issue or submit a pull request.

Disclaimer:
This script assumes that the input DNA sequences are valid and in the correct format. It does not perform any validation checks on the sequences.

License:
This project is licensed under the MIT License - see the LICENSE file for details.
