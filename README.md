# NUS SDS Datathon - Team DataDestroyers

Our team had the opportunity to participate in the Datathon event organized by NUS ICS. This process was a huge learning experience for us not just in data science theory and applications, but also in soft skills like time management, team coordination, and perseverance. We were given a dataset on approximately 30,000 companies with an outlet in Singapore. This repository contains all the code we used for the analytics and the insights we have derived.

## Problem statement

The challenge presented is to develop a robust predictive model capable of forecasting future sales figures for these companies. The objective is to mine the dataset to identify trends, patterns, and potential causative factors that significantly impact sales outcomes. By integrating historical sales data with predictive analytics, the goal is to achieve accurate sales forecasts that companies can utilize to make informed strategic decisions, optimize inventory management, and allocate resources effectively.

## Methodology

1.  Data Processing:

- Preparing and understanding data
- Data Cleaning: Handling NaN values and redundant columns

2.  Exploratory Data Analysis:

- Examining correlation between numerical variables
- Initial feature selection by running a CatBoost to select important features and reduce noise by evaluating feature importance and Shapley values.
- Coming up with hypotheses based on domain knowledge and using them to develop new feature columns for our final model based on the statistical significance of the hypotheses tests. Making data visualizations to better interpret relationships.
- Additional feature engineering through in sentence embedding NLP model to numerically encode company description

3.  Modeling and Evaluation:

- Used a CatBoost Regressor for our final predictions given the predominance of highly cardinal categorical features in the dataset, the sparsity of data, and the general robustness of gradient boosting models.

- Evaluating the model using K-Fold cross evaluation.

## Hypotheses and Rationale

Brainstorming and research supported by domain knowledge, we arrived at the following hypotheses:

1.  GDP per Capita: GDP per capita raises the spending power of consumers. Companies with offices in more affluent countries are likely to have higher dollar sales than those based in less affluent areas. We webscraped the data and engineered a column ‘GDP per Capita’ (for simplicity, of global ultimate company) to inculcate this idea in our model.
2.  Business Life Cycle: Companies can be in different stages of the business cycle, implying different growth rates and potential outcomes. As per marketing knowledge, these stages refer to Introduction phase, Growth Phase, Maturity Phase, and Decline Phase. As a small example, companies in the introduction phase have the most volatile sales due to intense competition and the need to first penetrate the market successfully.
3.  Associated Companies: Companies in a larger global ultimate chain have an advantage over companies with a smaller chain in terms of efficiency. Companies in a global ultimate chain (which, for simplicity, we define as the list of companies which report the same global ultimate) have the possibility of sharing resources, information and knowledge. Moreover, these companies may complement each other’s operations.
4.  Number of Nouns in Description: An innovative idea, we explored the possibility that having more nouns in the company description may imply more products and services to sell, and thus having more sales.

## Conclusions and Insights

1.  Our hypotheses 1, 2 and 3 above proved to be statistically significant, to our expectation. These two were backed by strong domain knowledge, which holds for this dataset.
2.  Hypothesis 4, while innovative, does not hold. Even though this hypothesis is rejected, we acknowledge the importance of coming up with innovative and unique possible relationships in order to make more comprehensive and more accurate models.
3.  This project helped us understand and practice the methodology while working on a data science project. We would like to mention here the importance of Exploratory Data Analysis, which is in essence, coming up with hypotheses and testing over and over again to gain insightful knowledge.
4.  Selecting important features using Tree Based Feature Selection and feature engineering using domain knowledge and hypothesis tests helped us significantly improve the fit of our model.

#### Packages Used:

- Numpy, Pandas, Matplotlib, Seaborn, Scipy, Sklearn, Tensorflow, Tensorflow_hub, Catboost, Requests, BeautifulSoup, Geopy, Folium, Catboost

#### Contributors

1.  Akshat Ajmera (NUS - Business and Statistics)
2.  Jung Woo Lee (NUS - Quantitative Finance and Statistics)
3.  Pranav Gupta (NUS - Mathematics and Economics)
4.  Priyansh Bimbisariye (NUS - Computer Science with Minors in Entrepreneurship)
5.  Yuv Bindal (NUS - Electrical Engineering and Mathematics)
