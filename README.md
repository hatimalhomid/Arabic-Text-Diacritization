# Arabic-Text-Diacritization


## Overview
This project addresses the restoration of Arabic diacritics (حركات) to undiacritized text — a critical task for improving pronunciation, clarity, and text-to-speech systems. It models diacritization as a character-level sequence prediction problem, using deep learning approaches.

# Project Structure
- Arabic_Text_Diacritization_Challenge_final.ipynb: Main Jupyter notebook containing the implementation
- clean_notebook_forgithub.py: Utility script for cleaning notebook metadata
- requirements.txt: List of Python dependencies


## Models Used
BiLSTM – Performs well even with limited data.

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

 ***Inference tests show accurate predictions across all models.***

## Try It Out
Best Model Available (Custom Transformer):

🔗 https://huggingface.co/hatimalhomid/arabic-diacritization-transformer/blob/main/README.md

## Tools & Environment
- Google Colab (A100 GPU)

- PyTorch

- Hugging Face Transformers

## Future Recommendations
Train LSTM on the full dataset

Use beam search for better decoding

Add morphological constraints for correctness

Fine-tune larger models (e.g., XLM-R, ALLaM-7B)
