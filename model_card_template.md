# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model used for this project is a Random Forest Classifier from scikit-learn version 1.5.1, utilizing default parameters.

## Intended Use

The model is designed to classify individuals into income brackets based on census data:

- <=50K: Individuals earning less than or equal to $50K/year

- >50K: Individuals earning more than $50K/year

## Training Data

The model was trained on the Census Income Dataset from 1994, obtained from the UC Irvine Machine Learning Repository ([link](https://archive.ics.uci.edu/dataset/20/census+income)). The original dataset contains 32561 rows and 14 different features, including demographic and employment details.

The data was split into training and testing subsets with an 80/20 ratio and underwent basic preprocessing like One-Hot Encoding.

## Evaluation Data

The test data comprises 20% of the original dataset which was reserved for evaluation.

## Metrics
The metrics observed are precision, recall, and the F1 score.

The overall results for the data were as follows:
Precision: 0.7389
Recall: 0.6340
F1: 0.6824

## Ethical Considerations

Census data may have inherent flaws due to collection methods and potential political influences. Certain demographics can be underrepresented, which should be taken into account when interpreting the results of this or any analysis.

## Caveats and Recommendations

Given that the data used is from 1994, it's worth exploring how more recent data might impact the results. The age of this data also means it should not be the sole basis for any important recommendations and should be considered alongside other indicators.