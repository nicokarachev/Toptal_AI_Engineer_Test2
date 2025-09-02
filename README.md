Task Description

Implement the functionality below.

REQUIREMENTS

1) Load the dataset:


It contains a list of paragraphs in English and French, each marked with the correct language.

2) Split the dataset into train (80 percent) and test (20 percent)

3) Create an ML model that given a piece of text detects the language. The model must be generic and work if extra languages are added to the dataset. Using language detection libraries is not allowed.

4) Calculate the accuracy of the prediction on the test set. You should obtain a 99 percent accuracy or more.

5) Implement a simple tokenizer function that given a string will return an array of tokens.

6) Punctuation marks such as "!", "?", ",", ".", "...", ";", and ":" should be replaced by EXCLAMATION, COMMA, etc.

7) Complex punctuation marks like "?!" or "!!!" should be their own tokens, i.e. EXCLAM_QUESTION, STRONG_EXCLAM.

8) E-mail addresses should be replaced with E_MAIL, Twitter handles (@<word>) should be replaced with TWITTER.

9) "Data is love, data is life!" -> [ 'Data', 'is', 'love', 'COMMA', 'data', 'is', 'life', 'EXCLAMATION']

10) Here is a strange example... Right?!' -> ['Here', 'is', 'a', 'strange',

' example', 'ELLIPSIS', 'Right', 'EXCLAM_QUESTION']

11) This is weird! Too weird!!! >

['This', 'is', 'weird', 'EXCLAMATION', 'Too', 'weird', 'STRONG_EXCLAM']