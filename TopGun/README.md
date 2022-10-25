#### KSW 2022 Fall Program

# 🍎 Predicting apple sugar sweetness by applying apple images on hybrid machine learning model: Machine Learning and Deep Learning    


## Team TopGun
    
| Name         |Call sign| University               | Major                                   | Email               | Github    |
| :-----------------:| :---------: | :------------------------: | :------------------------------------------: | :-------------------: | :------------------------------: |
| Heejun Park |YODA   | Yeonsei Univ.| Computer & Telecommunications Engineering|parkie0517@gmail.com| https://github.com/parkie0517|
| Hanbi Kim |PHEONIX  | Chungbuk Nat'l Univ.   | Computer Science | hanbikim20@g.cbnu.ac.kr  | https://github.com/hanbikim    |
| Jeongho Ha |JAY | Jeju Nat'l Univ.       | Computer Engineering | hjh4212@naver.com| https://github.com/hjh1248    |
| Seokkhyeon Heo|EASY | Jeju Nat'l Univ.   | Blockchain Security |gj4535@gmail.com| https://github.com/gj1515   |
| Taeyun Kim |KAMTAE  | Jeju Nat'l Univ.  | Tourism Management & Big Data Science |persimm0ncrack@gmail.com| https://github.com/kamtae |
| Jeffrey Tsai| GOKU | Purdue Univ.  | Computer & Information Technology | jeffrey051622@gmail.com |https://github.com/jtsai23|
| Kyungrock Kwon| ROCK | Purdue Univ.  | Systems Analysis & Design |kyungrock99@gmail.com |  |


    

## Research problem statement
Farmers harvest apples without checking the sweetness level. They pick all apples and send them to Agricultural Products Processing Center (APC). Then a machine in APC measures their level. The problem is to harvest apples without knowing the Brix value, i.e., not checking whether it has commercial value. it is challenging for farmers to predict the optimal harvesting time based only on their experience. For consumers, it is difficult to select the best apples in terms of sugar level or sweetness.     

There are two universal ways to measure sugar levels: The destructive sugar levels measurement method (DM) and the Non-destructive sugar levels measurement method (NDM). DM measures sugar levels by testing the juice from cut fruits. It is a more affordable method than NDM. A disadvantage is that cut fruits lose their value to be sold. NDM displays sugar levels by detecting the reflected wavelength from the apples that were irradiated to near-infrared. It measures the sweetness of apples without damaging the fruits and shows the sugar levels immediately. However, the method is expensive, and the accuracy of the outputs is not stable. 

## Overview
<img src="https://user-images.githubusercontent.com/74577775/197632750-8ff7440f-b8e8-4a09-88fa-faad3c52954d.jpeg" width="700" height="500"></img>

## Research novelty

    1. Develop a Hybrid Machine Learning (HML) model that combines ML and DL models.
    2. Predict apple sweetness(Brix level) from apple images taken by a smartphone.

## Environment Setting
### Machine Learning
    - Python 3.8.2
    - scikit-learn
    
### Deep Learning
    - Python 3.7.15 
    - tensorflow 2.9.2
    - keras 2.9.0
    - VGG16
    - EfficientNetB0
