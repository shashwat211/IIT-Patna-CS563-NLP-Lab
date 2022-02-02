# CS563 Natural Language Processing Lab
## Assignment 1
Parts of Speech Tagging using second order Hidden Markov Model.

## Team Details:

Team Code: `1801cs15_1801cs46`

Team Name: `kacha_badam`

Team Members:

| Name              | Roll Number |
| ----------------- | ----------- |
| Bhumika Shivani   | 1801CS15    |
| Shashwat Mahajan  | 1801CS46    |

## Second Order Hidden Markov Model (HMM)
### Creating environment with the required packages
Use the ```requirements.txt``` file to install the required packages. The environment name here is `nlp-a1`. You may change it if you want.

```conda create --name nlp-a1 --file requirements.txt```  

### Activate the new environment
```conda activate nlp-a1```

### Running the Code
```python3 main.py```

### Error Analysis from Output
---
#### HMM for 36 tags 
---
_Evaluated 783 sentences._  
_**Time taken**: 13:52 min (1.06s/it)_

**HMM Model Accuracy = 0.8588479175827627**

> Class-wise Accuracies 

| Class (Tag)   |   Accuracy |
|---------------|------------|
| #             |   0        |
| ''            |   0        |
| -LRB-         |   0.5625   |
| -RRB-         |   0.75     |
| :             |   0        |
| CC            |   0.877315 |
| CD            |   0.854054 |
| DT            |   0.938688 |
| EX            |   0.695652 |
| FW            |   0        |
| IN            |   0.93628  |
| JJ            |   0.795255 |
| JJR           |   0.649351 |
| JJS           |   0.741935 |
| LS            |   0        |
| MD            |   0.940476 |
| NN            |   0.881295 |
| NNP           |   0.863536 |
| NNPS          |   0.403226 |
| NNS           |   0.837108 |
| PDT           |   0.333333 |
| PRP           |   0.907738 |
| PRP$          |   0.893617 |
| RB            |   0.807128 |
| RBR           |   0.5      |
| RBS           |   0.3      |
| RP            |   0.56     |
| TO            |   0.929412 |
| VB            |   0.862986 |
| VBD           |   0.820919 |
| VBG           |   0.65371  |
| VBN           |   0.735499 |
| VBP           |   0.765873 |
| VBZ           |   0.866667 |
| WDT           |   0.845361 |
| WP            |   0.717391 |
| WP$           |   1        |
| WRB           |   0.611111 |
  
After this number of tags is reduced to 4 as per assignment.  

---

#### HMM for 4 tags
---
_Evaluated 783 sentences._  
_**Time taken**: 00:02 min (317.48it/s)_

**HMM Model Accuracy = 0.8873044789245556**

> Class-wise Accuracies 

| Class (Tag)   |   Accuracy |
|---------------|------------|
| A             |   0.789972 |
| N             |   0.879392 |
| O             |   0.952872 |
| V             |   0.814131 |


______________________
Thanking You!

kacha_badam