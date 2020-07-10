# Indian-Dance-Form-Classification

 <p align="center">
  <img width="460" height="300" src="https://img.freepik.com/free-vector/character-indian-faceless-women-traditional-dancing-pose_1302-19143.jpg?size=626&ext=jpg">
</p>

## About:
Classical Dance forms are one of the most precious things in India. Different regions have their own dance forms.

This International Dance Day, an event management company organized an evening of Indian classical dance performances to celebrate the rich, eloquent, and elegant art of dance. After the event, the company plans to create a microsite to promote and raise awareness among people about these dance forms. However, identifying them from images is a difficult task.


The eight categories of Indian classical dance are as follows:
- Manipuri
- Bharatanatyam
- Odissi
- Kathakali
- Kathak
- Sattriya
- Kuchipudi
- Mohiniyattam


## Goal:
Through this project we want to detect Indian Classical Dance forms by looking at an image.

## Usage:
clone the repository first.
```console
git clone https://github.com/sahasuman343/Indian-Dance-Form-Classification
```
For a quick look without going deep into the model go to command propmt/Anaconda prompt

```console
cd "folder containing the downloaded files"
```
Download the required repositories
```console
pip install requirements.txt
```
then type:

```console
python app.py
```
then navigate to the localhost with the port number showing in the terminal.

## Contents:
  - Dataset
  - Data Processing
  - Defining and training Model
  - Model Deployment

## Dataset
 Download the dataset manualy from [here](https://www.kaggle.com/souravkgoyal/identify-the-dance-form)
 
 or
 Download Data using your Kaggle Api Key
 ```python
 kaggle datasets download -d souravkgoyal/identify-the-dance-form
 ```
  - ### Dataset Description:
  The data folder consists of two folders and two .csv files. The details are as follows:
- train: Contains 364 images for 8 classes 'Manipuri','Bharatanatyam','Odissi','Kathakali','Kathak','Sattriya','Kuchipudi','Mohiniyattam'
- test: Contains 156 images
- train.csv: 364 x 2
- test.csv: 156 x 1

## Data Processing:
To Build the Model first we need to make the data suitable for traing.

This Data Processing is done in the file image_seperation.py

this file makes  traing and validation data set with 8 different categories for 8 different dance forms.

To run the preprocessing step(Make sure that the image_seperation.py and the train folder downloaded from kaggle are in same directory)
```console
python image_separation.py
```
## Defining and training Model:
Here we are using Transfer learning to create this model. We mainly used VGG16 model with some tuning. The model is prepared in the file model.py.

To train the model 
```console
python model.py
```
make sure you have a good processor or gpu configured, too much waiting is not good for health this days.

after the process beeing finished the model with best validation accuracy has been saved as best_model.h5
 
Congratulations !! you have sucecssfully built the model.

## Model Deployment:
 Now we have our model ready and we are all set to deploy it rather than running it. Here we are using Flask to deploy our model.
 
 app.py contains the flask app
 ```console
python app.py
```
## Enjoy!!
If you like the work, Fork me on github
Thank you, 
Stay Safe, Stay Healthy
 
