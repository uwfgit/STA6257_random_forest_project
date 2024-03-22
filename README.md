# STA6257 Random Forest Project
Authors: Kristen Monaco, Praya Cheekapara, Raymond Fleming, Teng Ma

## Instructions

In the wake of escalating biodiversity loss and species extinction, predictive modeling has emerged as a crucial tool for conservation strategies. This project harnesses the power of machine learning to dissect patterns within the South African National Red List, aiming to forecast the extinction risk of plant species. Utilizing a dataset comprising 946 taxa, we embark on a multifaceted approach to determine the predictors most instrumental in classifying species as extinct, threatened, or not-threatened. The dataset is rich, featuring attributes like unique identifiers, group classification (Extinct, Threatened, Not-Threatened), life form, growth form, taxonomic family, habitat range, and a spectrum of threats assessed during the Red List evaluation.

Our methodology unfolds in several rigorous steps. Initially, we preprocess the data, ensuring categorical variables are encoded meaningfully and continuous variables are treated for missing values, with special attention to maintaining the integrity and interpretability of the data. We then split the dataset into training and testing sets, adhering to a 70:30 ratio, to balance exploration with validation. The training set undergoes class imbalance treatment using the ROSE library, aiming for a balanced representation across classes, crucial for avoiding biased predictions.

To tackle the wide numerical range across features, we apply five normalization techniques, each offering a different perspective on scaling and distribution alignment, thus preparing our data for the nuanced demands of machine learning algorithms. These techniques include Min-Max normalization, Z-Score standardization, Maximum absolute scaling, and L1 and L2 norm normalizations, each transforming the feature space to enhance algorithm performance.

In the heart of our analysis lies the Random Forest model, celebrated for its robustness and ability to handle complex, high-dimensional data. By leveraging techniques like Bootstrap sampling and random feature selection, it constructs a "forest" of decision trees, each contributing to the ensemble's predictive might. This approach not only enhances accuracy but also provides insight into feature importance, guiding conservation efforts effectively.

Moreover, we evaluate our models using a comprehensive set of metrics—accuracy, recall, precision, and F1 score—to ensure a holistic assessment of performance. Beyond individual models, we explore model fusion through voting, integrating predictions across five models to harness collective intelligence for superior accuracy.

By marrying advanced machine learning techniques with critical conservation data, this project aims to offer a novel lens through which to view species extinction risk. Our findings not only illuminate the factors driving species towards extinction but also pave the way for targeted conservation strategies, ultimately contributing to the preservation of biodiversity in South Africa and beyond.

## GitHub Repo:
[STA6257_random_forest_project](https://uwfgit.github.io/STA6257_random_forest_project/)

![](rf.png)

## Tools
- vscode
- rstudio
- quarto
- R

More information:
[STA6257_random_forest_project](https://uwfgit.github.io/STA6257_random