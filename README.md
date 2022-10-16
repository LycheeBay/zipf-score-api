# zipf-score-api
An API that, given a string of text, can calculate the Zipf commonality score for each of the non-stop-words.

## Packages Used
- SpaCy
- Pandas
- Flask

## How To Call
`[hosting link]/?text=[text you wish to process]`

## What It Returns
`{word 1: Zipf score 1, word 2: Zipf score 2, ...}`
Returned in ascending order in Zipf score.

## Important Notes
1. If a word is not found in the list, it will return with a Zipf value of 0.
2. Stop words and tokens that are not exclusively letters are dumped.
