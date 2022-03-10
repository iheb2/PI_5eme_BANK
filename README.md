# Online Bank With Frauds detection
![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Spring-Boot-red)
![Frontend](https://img.shields.io/badge/Frontend-Angular/HTML/CSS/JS-green)
![Data-base](https://img.shields.io/badge/MySql-red)
![Flask](https://img.shields.io/badge/Flask/Rest-Api-blueviolet)



![alt text](https://raw.githubusercontent.com/iheb2/Pi_5eme_Bank/master/bn1.png)
![alt text](https://raw.githubusercontent.com/iheb2/Pi_5eme_Bank/master/bn2.png)

  
## 📝 Description
- A 6-month academic group project to develop an online bank that can manage customers, operations, employees and financial products...
After satisfying the functional and non-functional requirements of the specification. I proposed to my supervisors to add 3 fraud detection sections as explained below and done .

## 📝 Architecture overview
- In a web application project, we mainly have two main parts that interact together which are the Web Interface part and the Business part. This project consists in developing a full stack web application with a RESTFUL API using Spring Boot for the Back End and the the Back End and the Angular framework for the Front End.

![alt text](https://raw.githubusercontent.com/iheb2/Pi_5eme_Bank/master/archi1.png)

## 📝 My tasks

1- Elaborating the report .
2- Transaction management :
Enabling customers to do transactions and to track history.
Training a classification model and then devoloping a fraud detection Flask Rest Api and using it in the application : Anti money laundering Detector (Deep learning ). If the flag of fraud is raised the agents can consult the operation to identify whether a fraud or not else the transaction is executed . .
3- Insurance Reclamation management :
Enabling customers reclaim for insurance indemnisation .
Training a classification model and then devoloping a fraud detection Flask Rest Api and using it in the application : Insurance Fraud Detector . If the flag of fraud is raised the agents can consult the operation to identify whether a fraud or not else the amount is fixed and refunded .
4- Credit card management :
Delivering credit cards to allow customers to pay online .
Training a classification model using deeplearning and then devoloping a fraud detection Flask Rest Api and using it in the application : Credit card payment Fraud Detector. If the flag of fraud is raised the agents can consult the operation to identify whether a fraud or not else the amount asked to preleve from the account is authorized.



## ⏳ Dataset
- Download the dataset for custom training and place those two folders  in a folder named **"dataset"**
- https://drive.google.com/drive/folders/1WCxe1EuxLo6qyGVpupcEMTgN83xpgHM_ 

## :desktop_computer:	Installation

### :Requirements
* Python 3.6+
* tensorflow>=1.15.2
* keras==2.3.1
* imutils==0.5.3
* numpy==1.18.2
* opencv-python==4.2.0.*
* matplotlib==3.2.1
* scipy==1.4.1

## : Setup the environment
1. Create a new virtual environment 
2. Activate the new environment
3. Donwlnload the file requirement.txt  
4. Install the requirement 
```bash
$ pip install -r requirements.txt 

```
## 🎯 Inference demo
 Testing in  **Real time ** with the pc camera   :-
```bash
$ python detect_mask_video.py

```

