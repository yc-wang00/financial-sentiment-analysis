
<h3 align="center">Financial News Sentiment Analysis</h3>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/status-active-success.svg)]() -->
<!-- [![Platform](https://img.shields.io/badge/platform-reddit-orange.svg)](https://www.reddit.com/user/Wordbook_Bot) -->
<!-- [![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues) -->
<!-- [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE) -->

</div>

---

<p align="center"> A financial news sentiment analysis demo powered by TitanML and Streamlit, using data source from EOD
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 How it works ](#-how-it-works-)
    - [Installation](#installation)
    - [Build dataset.](#build-dataset)
    - [Finetuning](#finetuning)
    - [Deployment](#deployment)
    - [Run APP](#run-app)
- [⛏️ Built Using ](#️-built-using-)

## 🧐 About <a name = "about"></a>

This project builds a Streamlit application designed to facilitate the process of inferencing in a sentiment analysis project, which is deployed using TitanML.


## 🏁 How it works <a name = "working"></a>

#### Installation

1. install requirements package 
```
pip install -r requirements.txt
```
2. login to TitanML platform:
```
iris login
```
now you can start viewing metrics in Titan Dashboard [app.titanml.co]

#### Build dataset. 
1. For this demo, I am using a combination of `financial_phrasebank` and `FiQA`. [https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis]

2. Data Preprocessing: divided the dataset into `train.csv` and `validation.csv` (it has to be the exact name)
3. Upload dataset to TitanHub
```
iris upload <dataset>
```

#### Finetuning
In titanML platform, you can build the task by command generator, and finetune model by:
```
iris finetune <--->
```

#### Deployment

1. once the model finishes finetuning in titanML, you can pull the ready-to-go docker image by: 
```
iris pull <--->
```
2. Deploy: You can test the local deployment by running:

```
docker run -it --rm --gpus all -p8000:8000 --shm-size 256m <--->
```

This will start a script doing everything you need to deploy the model in `localhost:8000`

#### Run APP

Once you have the model deployed in the local machine, you can test your app by running streamlit application:
```
streamlit run src/main.py 
```

🎉 Now you can start playing around it! 



## ⛏️ Built Using <a name = "built_using"></a>

- [TitanML](https://app.titanml.co/) - NLP Optimization Platform
- [Streamlit](https://streamlit.io/) - Python app framework
