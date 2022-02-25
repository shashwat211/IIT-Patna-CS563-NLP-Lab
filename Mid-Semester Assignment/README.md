# CS563 Natural Language Processing: Mid-Semester Assignment

## Student Details

| Name              | Roll Number |
| ----------------- | ----------- |
| Shashwat Mahajan  | 1801CS46    |

## Setup of environment and running the code
### Creating environment with the required packages
Use the ```requirements.txt``` file to install the required packages. The environment name here is `nlp-midsem`. You may change it if you want. Use `conda-forge` channel if packages aren't found.

```
conda create --name nlp-midsem --file requirements.txt
```  

### Activate the new environment
```
conda activate nlp-midsem
```

### Running the Code
The two files ```Q1.ipynb``` and ```Q2.ipynb``` are both Jupyter Notebooks. Both can be viewed on any editor(eg. VS Code) with the environment (```nlp-midsem```) activated. Alternatively they can also be viewed/run using the following commands:
```
jupyter-notebook Q1.ipynb
```

```
jupyter-notebook Q2a.ipynb
```
  
```
jupyter-notebook Q2b.ipynb
```
  

---
  
## Question 1: Automated Spelling Corrector
  

---
  

### First Order HMM without Contextual Emission
  

---
_Number of train samples_ : 9279
_Number of test samples_ : 1879

**Accuracy of the model: 0.9195359281437125**

> Class-wise accuracies

| Class (Alphabet)   |   Precision |   Recall |       F1 |
|--------------------|-------------|----------|----------|
| a                  |    0.931884 | 0.946981 | 0.939372 |
| b                  |    0.775862 | 0.75     | 0.762712 |
| c                  |    0.943231 | 0.927039 | 0.935065 |
| d                  |    0.92233  | 0.904762 | 0.913462 |
| e                  |    0.922249 | 0.932285 | 0.92724  |
| f                  |    0.836478 | 0.869281 | 0.852564 |
| g                  |    0.921569 | 0.859756 | 0.88959  |
| h                  |    0.923304 | 0.928783 | 0.926036 |
| i                  |    0.918728 | 0.943739 | 0.931065 |
| j                  |    0.888889 | 1        | 0.941176 |
| k                  |    0.893258 | 0.913793 | 0.903409 |
| l                  |    0.912903 | 0.918831 | 0.915858 |
| m                  |    0.931174 | 0.888031 | 0.909091 |
| n                  |    0.908705 | 0.928416 | 0.918455 |
| o                  |    0.954151 | 0.945946 | 0.950031 |
| p                  |    0.871345 | 0.851429 | 0.861272 |
| q                  |    0.666667 | 0.666667 | 0.666667 |
| r                  |    0.927602 | 0.919283 | 0.923423 |
| s                  |    0.915929 | 0.9      | 0.907895 |
| t                  |    0.93588  | 0.937158 | 0.936519 |
| u                  |    0.90429  | 0.916388 | 0.910299 |
| v                  |    0.878788 | 0.892308 | 0.885496 |
| w                  |    0.921875 | 0.859223 | 0.889447 |
| x                  |    0.714286 | 0.625    | 0.666667 |
| y                  |    0.889313 | 0.910156 | 0.899614 |
| z                  |    0.764706 | 0.866667 | 0.8125   |
  
All predictions are output into the ```predictions.txt``` file.  

---

### Working on the given case of spelling errors
The following sentence (P1) was given with the highlighted wrong words. The corrected words are shown in the sentence P2.  
  
_P1:_ star wars is **ploying** at **thi** regal lloyd **center** and imax multnomah st portland **ang** also at **tho** **centupy** eastport plaza **wuuld** any of **thoss** times **wurk** for **yoz**  
  
_P2:_ star wars is **playing** at **the** regal lloyd **centre** and imax multnomah st portland
**and** also at **the** **century** eastport plaza **would** any of **those** times **work** for **you**  
  
We create a string of these wrong words and evaluate these words according to our viterbi algorithm.
---
```
Percentage corrected spellings: 30.0%
```
---

### Ease and difficulty of correction
  

---
It can be observed in the corrected outputs below that the model performs well in case of long words(century, would) and also for very repetitive words (ie, you).
```
Corrected Spelling: century
Corrected Spelling: would
Corrected Spelling: you
```

On the contrary the model is not able to perform very well on words with ambiguous spelling patterns / uncommon occurances like 'centre'. As an example the trail of ```['t', 'r', 'e']``` seen in the word 'centre' is very rarely observed in the train set. Thus the model does not learn to predict such a spelling and performs poorly in these cases.
  
---

## Question 2a: POS Tagger (Modifications and Evaluation)
  

---
_Evaluated 783 sentences._  
_**Time taken**: 19:58 min (1.53s/it)_

**Accuracy of the model: 0.8687766892740517**  

> Class-wise accuracies

| Class (Alphabet)   |   Precision |    Recall |       F1 |
|--------------------|-------------|-----------|----------|
| ''                 |   0         | 0         | 0        |
| -LRB-              |   0         | 0         | 0        |
| -RRB-              |   0.652174  | 0.535714  | 0.588235 |
| :                  |   0.619048  | 0.393939  | 0.481481 |
| CC                 |   0.0357143 | 0.0192308 | 0.025    |
| CD                 |   0.794805  | 0.72      | 0.755556 |
| DT                 |   0.813031  | 0.790634  | 0.801676 |
| EX                 |   0.789119  | 0.881027  | 0.832544 |
| FW                 |   0.909091  | 0.526316  | 0.666667 |
| IN                 |   0         | 0         | 0        |
| JJ                 |   0.774687  | 0.870313  | 0.81972  |
| JJR                |   0.677768  | 0.683303  | 0.680524 |
| JJS                |   0.661538  | 0.544304  | 0.597222 |
| LS                 |   0.814815  | 0.578947  | 0.676923 |
| MD                 |   0         | 0         | 0        |
| NN                 |   0.855615  | 0.91954   | 0.886427 |
| NNP                |   0.759666  | 0.794923  | 0.776895 |
| NNPS               |   0.825058  | 0.814709  | 0.819851 |
| NNS                |   0.666667  | 0.444444  | 0.533333 |
| PDT                |   0.78481   | 0.710311  | 0.745704 |
| PRP                |   0.333333  | 0.4       | 0.363636 |
| PRP$               |   0.765333  | 0.864458  | 0.811881 |
| RB                 |   0.734848  | 0.713235  | 0.723881 |
| RBR                |   0.713974  | 0.626437  | 0.667347 |
| RBS                |   0.425     | 0.62963   | 0.507463 |
| RP                 |   1         | 0.285714  | 0.444444 |
| TO                 |   0.533333  | 0.615385  | 0.571429 |
| UH                 |   0.847458  | 0.797267  | 0.821596 |
| VB                 |   0         | 0         | 0        |
| VBD                |   0.798354  | 0.762279  | 0.779899 |
| VBG                |   0.754685  | 0.738333  | 0.74642  |
| VBN                |   0.666667  | 0.397351  | 0.497925 |
| VBP                |   0.657534  | 0.657534  | 0.657534 |
| VBZ                |   0.701681  | 0.668     | 0.684426 |
| WDT                |   0.858726  | 0.786802  | 0.821192 |
| WP                 |   0.795181  | 0.75      | 0.77193  |
| WP$                |   0.871795  | 0.62963   | 0.731183 |
| WRB                |   1         | 0.25      | 0.4      |

  
### Working on the given case of POS Tagging
We run the viterbi algorithm on the given sentence using the parameters learned through the Hidden Markov Model. 

```
That_/DT former_/JJ Sri_/NN Lanka_/IN skipper_/NNP and_/CC ace_/NNP batsman_/NNP Aravinda_/NNP De_/NNP Silva_/NNP 
is_/VBZ a_/DT man_/NN of_/JJ few_/JJ words_/NN was_/NN very_/RB much_/JJ evident_/NN on_/IN Wednesday_/NNP 
when_/WRB the_/DT legendary_/NNP batsman_/NNP ,_/NNP who_/WP has_/VBZ always_/RB let_/VBN his_/PRP$ bat_/JJ 
talk_/NN ,_/CC struggled_/VBD to_/TO answer_/VB a_/DT barrage_/JJ of_/NN questions_/NNS at_/IN a_/DT 
function_/NN to_F_/TO promote_/VB
```

---

## Question 2b: POS Tagger (Modifications and Evaluation in Viterbi)
  

---

We modify our viterbi algorithm to run it on best 3 cases at each step. As a consequence, at each step we have 3 probabilities to consider for each node. While determining the best 3 possibilities from the previous step, we consider the best probabilities among the 3 possibilities for each of the 3 best nodes. We run the modified viterbi algorithm on our sentence given in the assignment and get the following result as an output in ```taggedresult.txt``` file.

```
That_/DT former_/JJ Sri_/NN Lanka_/IN skipper_/NNP and_/CC ace_/NNP batsman_/NNP Aravinda_/NNP De_/NNP Silva_/NNP 
is_/VBZ a_/DT man_/NN of_/JJ few_/JJ words_/NN was_/NN very_/RB much_/JJ evident_/NN on_/IN Wednesday_/NNP 
when_/WRB the_/DT legendary_/NNP batsman_/NNP ,_/NNP who_/WP has_/VBZ always_/RB let_/VBN his_/PRP$ bat_/JJ 
talk_/NN ,_/CC struggled_/VBD to_/TO answer_/VB a_/DT barrage_/JJ of_/NN questions_/NNS at_/IN a_/DT 
function_/NN to_F_/TO promote_/VB
```
---

## Question 2c: 
  

---
The output is the same in both the cases even though we are taking most probable 3 paths. This is because, actually in Viterbi algorithm all the paths are taken into consideration. This is done through the usage of a dynamic programming approach in the algorithm. All states are stored in multidimensional array (dimension depending on the ngram selected) and maximum probability is taken at each step from all previous possible states using the transition and emission matrices. So even if we take most probable 3 paths it won’t make a difference as the best possible path is already considered in the dynamic programming approach of Viterbi algorithm.
______________________
Thanking You!

Shashwat Mahajan