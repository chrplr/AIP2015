To prepare the stimuli (if the bmp do not already exist)

python create_English_French_Basque_cards.py
ls *Basque*.bmp >basque_stims.txt
ls *English*.bmp >english_stims.txt
ls *French*.bmp >french_stims.txt

To run the experiment:

Lire Instructions.txt


python training.py (si première fois)
python stroop.py
