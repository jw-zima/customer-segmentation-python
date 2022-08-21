
# customer-segmentation
<p align="left">
    <a alt="EDA">
        <img src="https://img.shields.io/badge/%20-EDA%20-orange" /></a>
    <a alt="Clustering">
        <img src="https://img.shields.io/badge/%20-Clustering%20-orange" /></a>
</p>

## General info

#### Problem Statement

**Customer Personality Analysis** is an analysis of a company’s ideal customers. It helps a business to better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers.

Customer personality analysis helps a business to modify its product based on its target customers from different types of **customer segments**.

Aim of this project is to determine clusters of similar customers based on their purchase behavior.

Dataset comes from the **kaggle** platform. 

## Notes

In order to preview reports in the *reports* folder use *GitHub & BitBucket HTML Preview*, i.e., just prepend this fragment to the URL of any HTML file: **[https://htmlpreview.github.io/?](https://htmlpreview.github.io/?)** e.g.:
* https://htmlpreview.github.io/?https://github.com/jw-zima/customer-segmentation/blob/main/reports/Report%20pandas-profiler%20-%20raw%20data.html (EDA of raw dataset)
* https://htmlpreview.github.io/?https://github.com/jw-zima/customer-segmentation/blob/main/reports/Report%20pandas-profiler%20-%20extended%20data.html (EDA of extended nd cleaned dataset)

## Technologies

<p align="left">
    <a alt="Jupyter Notebook">
        <img src="https://img.shields.io/badge/%20-Jupyter%20Notebook%20-blue" /></a>
    <a alt="python">
        <img src="https://img.shields.io/badge/%20-python%20-blue" /></a>
</p>

Additionally pre-commit add-ins were used:
<p align="left">
    <a alt="flake8">
        <img src="https://img.shields.io/badge/%20-flake8%20-steelblue" /></a>
    <a alt="isort">
        <img src="https://img.shields.io/badge/%20-isort%20-steelblue" /></a>
    <a alt="interrogate">
        <img src="https://img.shields.io/badge/%20-interrogate%20-steelblue" /></a>
</p>

## Usage

This project contains explanatory analysis along with clustering and profiling exercise performed in the [ipython notebooks](https://github.com/jw-zima/customer-segmentation/tree/main/notebooks) </br>
It does not contain a e2e pipeline that allow to load any data and perform clustering.

## Project Organization


    ├── README.md               <- The top-level README for developers using this project.
    │
    ├── data
    │   ├── external            <- Data from third party sources.
    │   ├── interim             <- Intermediate data that has been transformed.
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   └── raw                 <- The original, immutable data dump.
    │
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting
    │
    ├── src                     <- Source code for use in this project.
    │   ├── data                <- Scripts to load or generate data
    │   ├── features            <- Scripts to turn raw data into features for modeling
    │   ├── models              <- Scripts to train models and then use trained models to make predictions
    │   └── visualization       <- Scripts to create exploratory and results oriented visualizations
    │
    ├── .gitignore              <- List of files not sent to the repo
    ├── .pre-commit-config.yaml <- Add-ins executed in pre-commit
    ├── LICENSE                 <- License file
    └── env.yml                 <- File to create environment with list of all necessary packages


## References

Dataset from kaggle - [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
