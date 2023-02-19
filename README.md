# APR-Survey
A Survey on Automated Program Repair Techniques










# Dataset Overlap
The dataset overlap problem refers to the training data and test benchmark overlap. The problem may cause the model to learn the correct fix for the test sample during the training phase, which may lead to the illusion of getting good repair results.


Here we give a simple example to illustrate the dataset overlap problem. Figure 1 shows an overlapping part in the train dataset and the test benchmark (Defects4J). Therefore, the overlapping projects need to be removed from the training set during the model training process.
![图片1](https://user-images.githubusercontent.com/102460432/219946126-547f36fc-76bb-4228-a395-bb1d312368d0.jpg)
Figure 1. A example of dataset overlap.
