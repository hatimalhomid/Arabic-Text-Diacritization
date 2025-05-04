# Arabic-Text-Diacritization


## Overview
This project addresses the restoration of Arabic diacritics (حركات) to undiacritized text — a critical task for improving pronunciation, clarity, and text-to-speech systems. It models diacritization as a character-level sequence prediction problem, using deep learning approaches.

# Project Structure
- Arabic_Text_Diacritization_Challenge_final.ipynb: Main Jupyter notebook containing the implementation
- clean_notebook_forgithub.py: Utility script for cleaning notebook metadata
- requirements.txt: List of Python dependencies


## Models Used
BiLSTM – Performs well even with limited data. (30% of training data only)

Custom Transformer – Best performance with 97.33% validation accuracy.

Fine-Tuned AraBERT – Reliable, but benefits from more fine-tuning time.

## Dataset
Size: 4.27M parallel samples of diacritized and undiacritized Arabic.

Split: 80% train, 10% val, 10% test.

Tokenization: Character-level.

Vocabulary: 73 characters, 199 diacritic tokens.

Key Preprocessing Steps
Normalization of Arabic characters.

Removal of non-Arabic content and malformed entries.

Alignment and tokenization by characters.

## Evaluation
Model	Validation Accuracy
BiLSTM	97.24%
Transformer	97.33%
AraBERT	94.26%

 ***Inference tests (random not hardest) show accurate predictions across all models except fine-tuned Arabert made one mistake.***

## Try It Out
Best Model Available (Custom Transformer):

🔗 https://huggingface.co/hatimalhomid/arabic-diacritization-transformer/blob/main/README.md

## Tools & Environment
- Google Colab (A100 GPU)

- PyTorch

- Hugging Face Transformers

##  Recommendations
- Train LSTM on the Full Dataset: Utilize the entire dataset when training the LSTM model to maximize its generalization capability and performance.

- Incorporate Beam Search Decoding: Replace or augment greedy decoding with beam search to explore multiple candidate sequences and enhance prediction quality.

- Introduce Morphological Constraints: Integrate morphological rules and constraints into the decoding process to ensure syntactic and grammatical correctness in the output.

- Extend Training Duration: Allocate longer training time, particularly for models like AraBERT and Transformer, to allow for better convergence and improved accuracy.

- Fine-Tune Large Pre-Trained Models: Consider fine-tuning models such as mBERT, XLM-R, and ALLaM-7B, which have been pre-trained on extensive Arabic corpora including Harakat (diacritics). Their linguistic coverage can significantly boost diacritization accuracy

