# STA6257 Random Forest Project
Authors: Kristen Monaco, Praya Cheekapara, Raymond Fleming, Teng Ma

## Instructions

The loss of biodiversity and extinction of species are getting worse, so predictive modeling has become a crucial tool for conservation strategies. This project uses machine learning to analyze patterns in the South African National Red List, aiming to predict which plant species are at risk of extinction. With a dataset containing 946 taxa, we take a multifaceted approach to determine the most important factors that classify species as extinct, threatened, or not-threatened. The dataset is comprehensive and includes unique identifiers, group classification (Extinct, Threatened, Not-Threatened), life form, growth form, taxonomic family, habitat range, and various threats assessed during the Red List evaluation.

Our methodology unfolds in several rigorous steps. The first step of our methodology is to preprocess the data. We make sure that categorical variables are encoded in a meaningful way and handle missing values for continuous variables, while still keeping the data's integrity and interpretability intact. After that, we divide the dataset into training and testing sets, following a 70:30 ratio to balance exploration and validation. To avoid biased predictions, we use the ROSE library to address class imbalance in the training set, aiming for a balanced representation across all classes.

To handle the wide range of numbers in our features, we use five different ways to normalize them. Each technique has its own way of scaling and aligning the distribution, so that our data is ready for machine learning algorithms. These techniques include Min-Max normalization, Z-Score standardization, Maximum absolute scaling, and L1 and L2 norm normalizations. They all transform the feature space to improve algorithm performance.

The heart of our analysis is all about the Random Forest model, which is famous for being super strong and able to handle really complex data. It does this by using cool techniques like Bootstrap sampling and randomly picking features, creating a whole "forest" of decision trees that work together to make predictions. This not only makes it more accurate but also helps us figure out which features are most important, so we can focus on conservation efforts in the best way possible.

Additionally, we make sure to use a wide range of metrics like accuracy, recall, precision, and F1 score to get a complete picture of how well our models perform. And not just that, we also combine the predictions from five different models through voting to take advantage of their collective intelligence and achieve even higher accuracy.

The goal of this project is to use advanced machine learning techniques and critical conservation data to give us a new way of understanding why species are at risk of extinction. Our discoveries not only show us what factors are causing species to become extinct, but also help us develop targeted strategies for conservation. Ultimately, this will contribute to protecting biodiversity in South Africa and beyond.

## GitHub Repo:
[STA6257_random_forest_project](https://uwfgit.github.io/STA6257_random_forest_project/)

## Presentation Link:
[Quarto Slides](https://raymondfleming.github.io/RandomForestPresentation/#/title-slide)

![](rf.png)

## Tools
- vscode
- rstudio
- quarto
- R