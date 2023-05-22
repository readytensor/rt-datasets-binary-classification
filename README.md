# Datasets for Binary Classification Base category on Ready Tensor

This repo contains all files related to the datasets used in algorithm evaluation for the Binary Classification - Base category.

The `datasets` folder contains the main data files and the schema files for all the benchmark datasets under Binary Classification - Base category.

- The `raw` folder contains the original data files from the source (see attributions below). The Jupyter notebook file within each dataset folder is used to convert the raw data file for each dataset into the full processed dataset in `raw` folder into the processed form in `processed` folder.
- `processed` folder contains the processed files. These files are used in algorithm evaluations.

  - The CSV file with suffix "\_train.csv" is used for training
  - "\_test.csv" is used for testing (without the targets)
  - "\_test_key.csv" contains the ids and targets for the test data. This test key file is used to generate scores by comparing with predictions.
  - The JSON file with suffix "\_schema.json" is the schema file for the corresponding dataset.
  - The json file with the suffix "\_inference_requeest_sample.json" contains a sample JSON object with the data to make an inference request to the /infer endpoint.
  - The CSV file with the dataset name, and no other suffix, is the full data (made of both train and test sets).

- The folder `config` contains two csv files - one called `binary_classification_datasets_metadata.csv` which contains the dataset level attribute information. The second csv called `binary_classification_datasets_fields.csv` contains information regarding all the fields in each of the datasets.
- `generate_schemas.py`: contains the code to generate the schema files for each dataset.
- `create_train_test_key_files.py`: contains the code to generate the train, test, and test-key files for each dataset.
- `generate_inference_data.py`: contains the code to generate the inference request sample data for each dataset.
- `run_all.py`: This is used to run the above three scripts in sequence.

---

The following is the list of datasets along with a brief description for each and its attribution:

---

## Breast Cancer - Wisconsin

#### Alias (in scorecards): cancer

#### Domain / Industry: Biosciences

#### Description

Dataset for breast tumor diagnosis. Predict diagnosis: B = benign, M = malignant. Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

#### Dataset characteristics

- Number of samples = 569
- Number of input features = 32
- Has categorical features = No
- Has missing values = No

#### Attribution

Creators: <br/>
Dr. William H. Wolberg, General
W. Nick Street, Computer Sciences
Olvi L. Mangasarian, Computer
Donor: Nick Street

Dataset can be found here:<br/>
https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## In-vehicle coupon recommendation

#### Alias (in scorecards): coupon_recommendations

#### Domain / Industry: E-commerce

#### Description

This data studies whether a person will accept the coupon recommended to them in different driving scenarios.

#### Dataset characteristics

- Number of samples = 12,684
- Number of input features = 25
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Source: <br/>
Wang, Tong, Cynthia Rudin, Finale Doshi-Velez, Yimin Liu, Erica Klampfl, and Perry MacNeille. 'A bayesian framework for learning rule sets for interpretable classification.' The Journal of Machine Learning Research 18, no. 1 (2017): 2357-2393.

Dataset can be found here: <br/>
https://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation

UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Credit Card

#### Alias (in scorecards): credit_card

#### Domain / Industry: Financial services

#### Description

This dataset classifies people described by a set of attributes as good or bad credit risks.
The original dataset comes with a cost matrix. However, it is ignored in this evaluation since the Binary-Classification-Base category does not incorporate cost matrix.
In the original dataset, the target classes were marked as “+” and “-”. These have been replaced by “positive” and “negative”.

#### Dataset characteristics

- Number of samples = 690
- Number of input features = 16
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Source: <br/>
Professor Dr. Hans Hofmann
Institut f"ur Statistik und "Okonometrie
Universit"at Hamburg
FB Wirtschaftswissenschaften
Von-Melle-Park 5
2000 Hamburg 13

Dataset can be found here: <br/>
https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Electrical Grid

#### Alias (in scorecards): electrical_grid

#### Domain / Industry: Energy

#### Description

This dataset stems from the local stability analysis of the 4-node star system (electricity producer is in the center) implementing Decentral Smart Grid Control concept.
The analysis is performed for different sets of input values using the methodology similar to that described in:
SchÃ¤fer, Benjamin, et al. 'Taming instabilities in power grid networks by decentralized control.' The European Physical Journal Special Topics 225.3 (2016): 569-582.].

#### Dataset characteristics

- Number of samples = 10,000
- Number of input features = 13
- Has categorical features = No
- Has missing values = No

#### Attribution

Creator and donor: Vadim Arzamasov (vadim.arzamasov '@' kit.edu ), <br/>
Department of computer science, <br/>
Karlsruhe Institute of Technology; <br/>
Karlsruhe, 76131; Germany

Dataset can be found here: <br/>
https://archive.ics.uci.edu/ml/datasets/Electrical+Grid+Stability+Simulated+Data+
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Employee Attrition

#### Alias (in scorecards): employee_attrition

#### Domain / Industry: Unknown

#### Description

This dataset is available through PyCaret. The task is to predict whether an employee underwent attrition using predictor features such as satisfaction_level, salary category, department, average monthly hours, promotion in last 5 years, etc.
Original source and detailed dataset description are unknown.

#### Dataset characteristics

- Number of samples = 14,999
- Numberof input features = 9
- Has categorical features = Yes
- Has missing values = No

#### Attribution

Original source of data is unknown. <br/>
Dataset can be loaded through PyCaret as follows:

```
from pycaret.datasets import get_data
employee_data = get_data(“employee”)
```

---

## Image Segmentation

#### Alias (in scorecards): image_segmentation

#### Domain / Industry: Unknown

#### Description

Image data described by high-level numeric-valued attributes. The task is to predict the class of the image. Binarized version of the original data set. Original dataset contained 7 classes. The multi-class target feature is converted to a two-class nominal target feature by re-labeling the majority class as positive ('P') and all others as negative ('N'). Originally converted by Quan Sun.

#### Dataset characteristics

- Number of samples = 2,210
- Number of input features = 19
- Has categorical features = No
- Has missing values = No

#### Attribution

Original source: Unknown <br/>
Dataset can be found here: <br/>
https://www.openml.org/d/958

---

## Mushroom

#### Alias (in scorecards): mushroom

#### Domain / Industry: Biosciences

#### Description

Mushrooms described in terms of physical characteristics; classification task: poisonous or edible.

#### Dataset characteristics

- Number of samples = 8,124
- Number of input features = 22
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Source: <br/>
Mushroom records drawn from The Audubon Society Field Guide to North American Mushrooms (1981). G. H. Lincoff (Pres.), New York: Alfred A. Knopf <br/>
Donor: Jeff Schlimmer (Jeffrey.Schlimmer '@' a.gp.cs.cmu.edu)

Dataset can be found here: <br/>
UCI Machine Learning Repository: Mushroom Data Set - https://archive.ics.uci.edu/ml/datasets/mushroom <br/>
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## NBA

#### Alias (in scorecards): nba

#### Domain / Industry: Sports

#### Description

Dataset description unavailable.

#### Dataset characteristics

- Number of samples = 1,340
- Number of input features = 21
- Has categorical features = No
- Has missing values = No

#### Attribution

Original source of data is unknown. <br/>
Dataset can be loaded through PyCaret as follows:

```
from pycaret.datasets import get_data
nba_data = get_data(“nba”)
```

---

## Online Shoppers Purchasing Intention

#### Alias (in scorecards): online_shopping

#### Domain / Industry: E-commerce

#### Description

Dataset for real-time prediction of online shoppers purchasing intention

#### Dataset characteristics

- Number of samples = 12,330
- Number of input features = 17
- Has categorical features = yes
- Has missing values = No

#### Attribution

Source: <br/>

1. C. Okan Sakar <br/>
   Department of Computer Engineering <br/>
   Faculty of Engineering and Natural Sciences, Bahcesehir University, <br/>
   34349 Besiktas, Istanbul, Turkey

2. Yomi Kastro <br/>
   Inveon Information Technologies Consultancy and Trade <br/>
   34335 Istanbul, Turkey

Data used in this paper: <br/>
Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Real-time prediction of online shoppers’ purchasing intention using multilayer perceptron and LSTM recurrent neural networks. Neural Comput & Applic 31, 6893–6908 (2019). https://doi.org/10.1007/s00521-018-3523-0

Dataset can be found here: <br/>
https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset#

---

## Spambase

#### Alias (in scorecards): spambase

#### Domain / Industry: Technology / Internet Services

#### Description

This dataset contains collection of spam and non-spam emails converted to numerical features. Spam e-mails came from postmaster and individuals who had filed spam.Non-spam e-mails came from filed work and personal e-mails, and hence the word 'george' and the area code '650' are indicators of non-spam. These are useful when constructing a personalized spam filter. One would either have to blind such non-spam indicators or get a very wide collection of non-spam to generate a general purpose spam filter.

#### Dataset characteristics

- Number of samples = 4,601
- Number of input features = 57
- Has categorical features = No
- Has missing values = No

#### Attribution

Creators: <br/>
Mark Hopkins, Erik Reeber, George Forman, Jaap Suermondt v
Hewlett-Packard Labs, 1501 Page Mill Rd., Palo Alto, CA 94304

Dataset can be found here: <br/>
UCI Machine Learning Repository: <br/>
https://archive.ics.uci.edu/ml/datasets/spambase <br/>
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Telco Churn

#### Alias (in scorecards): telco_churn

#### Domain / Industry: Telecom

#### Description

Dataset regarding customer churn in telecom industry. <br/>
Context "Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]

#### Dataset characteristics

- Number of samples = 7,043
- Numberof input features = 19
- Has categorical features = No
- Has missing values = Yes

#### Attribution

Original source: <br/>
https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113

Sourced from Kaggle: <br/>
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## Titanic

#### Alias (in scorecards): titanic

#### Domain / Industry: Travel / Miscellaneous

#### Description

Dataset regarding attributes of passengers on the Titanic. Data can be used to build a predictive model that answers the question: “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender, socio-economic class, etc).

#### Dataset characteristics

- Number of samples = 891
- Numberof input features = 7
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Sourced from: <br/>
https://www.kaggle.com/competitions/titanic/data

---
