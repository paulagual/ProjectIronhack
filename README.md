<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100" align="right"/>

<img src="https://cloud.google.com/images/solutions/big-data/big-data_2x.png?hl=es" alt="Google Analytics Project" width="300"/>


#  Final Project Ironhack Data Bootcamp
*Paula Gual*

*Data Part Time Barcelona May 2019*


## Content
- [Project Description](#project)
- [Dataset](#dataset)
- [Workflow](#workflow)
    * [Preprocessing](#preprocessing)
    * [EDA](#eda)
    * [Feature Engineering and Feature Selection](#feature)
    * [Model](#model)
- [Results](#results)
- [Conclusions](#conclusions)

<a name="project"></a>

## Project Description

In this project we will create a Machine Leaning Model to predict if a visit of the Google Merchandising store will buy or not.



<a name="dataset"></a>


## Dataset

The dataset I will be using for the project is basically data from the Google Analytics account of the Google Merchandising store. This dataset is available on Kaggle.

[Google Analytics from Google Merchandising Store]https://www.kaggle.com/colinpearse/ga-analytics-with-json-columns



<a name="workflow"></a>


## Workflow

### Import Data

I've imported all the Dataset in a pandas dataframe, using the chunk method, as the original data csv is huge.
<a name="preprocessing"></a>


### Preprocessing

I've classified all the variables on my dataset:

**CATEGORICAL:**

* channelGrouping: Channel of arrival of the visit
* fullVisitorId: Visitor ID
* sessionId: Session ID (contains Visitor ID)
* socialEngagementType: Type of engagement
* deviceBrowser: Name of the Browser
* deviceCategory: Name of the device category 
* deviceOS: The OS of the device
* geoCity: City of the visit
* geoContinent: Continent of the visit
* geoCountry: Country of the visit
* geoMetro: Metro of the visit
* geoDomain: Domain of the visit
* geoRegion: Region of the visit
* geoSubContinent: Subcontinent of the visit   
* trafficSourceAdContent: Source of the Ads
* adwordsClickAdNetworkType: Ad Source
* adwordsClickGclId: Ad Click ID
* adwordsClickInfo.slot: Place of the ad
* trafficSourceCampaign: Name of the souce campaign
* trafficSourceKeyword: Name of the source Keyword
* trafficSourceMedium: Name of the source Medium
* trafficSourceReferralPath: Referral Path
* trafficSourceSource: Name of the source
    
    
**BOOLEAN:**
* deviceIsMobile: is the device mobile
* totalsBounces: Is bounce 
* totalsNewVisits: Is new visit 
* adwordsClickIsVideoAd: Is from ad video 
* trafficSourceIsTrueDirect: Is it a true direct visit

**ORDINAL:**
* visitId: Visit ID integer (is the date in unix time)   
* visitNumber: The number of visit of one user

**NUMERICAL:**

**INTEGER:**
* totalsHits: number of hits
* totalsPageviews: number of pageviews
* totalsTransactionRevenue: (TARGET) logaritm if the revenue
* totalsVisits: Number of visits
* adwordsClickInfoPage: click from ad in page
   
**DATE:**
* date: Date of the visit
* visitStartTime: unix time of the visit

I've preprocessed and cleaned all the data vars, manly replace the Nans using different strategies, depending on the data. I have also fixed some uncorrect types, of the variables.
<a name="eda"></a>


### EDA

I have divided the EDA in two parts: EDA of the numeric vars and the EDA of the categorical vars.

For the **EDA of the numeric vars**, I have first analysed the Target. Then the other numeric variables, by themselves (distribution) and comparing them to the target. Also I have visualized all the data, manly with scatterplots and boxplots.

I have also checked the correlation, and deleted a variable (hits) that was highly correlated with another (Pageviews).

For the **EDA of the categorical vars** I have studied the different values for each one, and also compared those number of values depending on the target var. Also I have visualized all the data, manly with bar charts.

In some cases, as the variable had many posible outcomes, I have created a new var with only the most repeated values, or the most related values to the target.
<a name="feature"></a>


### Feature Engineering and Feature Selection

I have selected the features that based on the EDA I belive are more related to the target.

The categorical vars I have encoded them, and craeted dummies.

<a name="model"></a>


### Model

In the **model selection** process I will take into account:
1.- It is a binaty classification problem
2.- The data is Sparse
3.- The target is very unbalanced (1,29% vs 98,71)
4.- There is a lot of data 903455 rows and 48 columns

**Model Selection**
1.- I'll use a decision tree
2.- I'll try to balance the classes down sampling the data
3.- I'll use Under ROC Curve (AUROC) as metric

**Algorithm** Ramdom Forest
**Parameters**
{'bootstrap': True,
 'criterion': 'gini',
 'max_depth': 9,
 'max_features': 'auto',
 'n_estimators': 100}

<a name="results"></a>

## Results

The final results of the model are:

F1: 0.96
Confusion Matrix: 
(2144,  159)
(30, 2273)
AUC: 0.96

**Feature Importance**
Importance / Feature
0.5045 / totalsPageviews
0.1228 / totalsBounces
0.0820 / continet_Americas
0.0374 / source_Googleplex
0.0315 / referral_Home

<a name="conclusions"></a>


## Conclusions


The conclusion is that it **is possible to predict the conversion** in an ecommerce, only having the data from the Google Analytics data of the visits.



       
       




