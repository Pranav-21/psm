#-------------------------Pranav Mahajan--------------------------------#

#-------Data from:- https://www.kaggle.com/suncor/social-adv/data-------#
#------------------------------Data Import------------------------------#
input<-read.csv("C:/Users/Moraya/Desktop/Social_Network_Ads.csv")
data<-input


#--------------------Removing irreleavent column------------------------#
data <- data[-1]  #--removes the first variable(Uid) from the data set--#

#-----------------------------column names------------------------------#
names(data)


#----------------------------missing value------------------------------#
sapply(data, function(x) sum(is.na(x)))

######## Missing values with Mean Method ########  
#train$Age[is.na(train$Age)] = mean(train$Age, na.rm = TRUE)
#test$Age[is.na(test$Age)] = mean(test$Age, na.rm = TRUE)
########## Removing that row which has missing vaue ######## 
#test = test[!is.na(test$Fare),]

#---------------Conversion from integer to Categorical------------------# 
data$Purchased = as.factor(data$Purchased)

#--------display the structure of Data with datatype of variables-------#
str(data)

#summary() is used to produce summary of the results of model functions-#
summary(data)


#-------------partition of data for testing of prediction---------------#
set.seed(123)
library(caret)
Train <- createDataPartition(data$Purchased, p=0.7, list=FALSE)
training <- data[ Train, ]
testing <- data[ -Train, ]


#########################################################################
#--------------Practical of Multiple Logistic Regression----------------#
#########################################################################
#-------------------------Assumption of Model---------------------------#
#----------par() is use for multiple graphs in a single plot------------#
#--mfrow= c(nrows, ncols) is to create a matrix of nrows x ncols plots--# 
par(mfrow=c(1,2))
#--------------------------Outliers in Boxplot--------------------------#
boxplot(data$EstimatedSalary)
boxplot(data$Age)

#### Winsorizing technique #####
#summary(data$EstimatedSalary)
#upper<-150000+1.5*IQR(data$EstimatedSalary)
#upper
#data$EstimatedSalary[data$EstimatedSalary > upper]<-upper
#boxplot(data$EstimatedSalary)
#summary(data$EstimatedSalary)

################ For AGE Variable ############

#boxplot(data$Age)
#summary(data$Age)

#### Winsorizing technique #####
#upper<-60+1.5*IQR(data$Age);upper
#train1$Age[data$Age > upper]<-upper

#lower<-10-1.5*IQR(data$Age);lower
#data$Age[data$Age < lower]<-lower
#boxplot(data$Age)
#summary(data$Age)

#--------------------------Model Creation:ente--------------------------# 
model = glm(Purchased ~., family = 'binomial', data = data)


#summary() is used to produce summary of the results of model functions-#
summary(model)


#--anova shows the significanceof each change(using a chi square test)--#
anova(model,test='Chisq')


#---------------------variable signifcance selection--------------------# 
#-----------------------WAY OF GIVING OWN REFERENCE---------------------#
table(training$Gender)

# Model Building 

reg.model1 = step(glm(Purchased~ relevel(Gender ,ref ='Male')
                      +Age+EstimatedSalary, 
                      family = 'binomial', data = training)
                  ,direction = "both")
summary(reg.model1)
anova(reg.model1,test='Chisq')


#---------------------------Accuracy of model---------------------------# 
# concordance and discordance 
Acc=function(model){
  Data = cbind(model$y, model$fitted.values) 
  ones = Data[Data[,1] == 1,]
  zeros = Data[Data[,1] == 0,]
  conc=matrix(0, dim(zeros)[1], dim(ones)[1])
  disc=matrix(0, dim(zeros)[1], dim(ones)[1])
  ties=matrix(0, dim(zeros)[1], dim(ones)[1])
  for (j in 1:dim(zeros)[1])
  {
    for (i in 1:dim(ones)[1])
    {
      if (ones[i,2]>zeros[j,2])
      {conc[j,i]=1}
      else if (ones[i,2]<zeros[j,2])
      {disc[j,i]=1}
      else if (ones[i,2]==zeros[j,2])
      {ties[j,i]=1}
    }
  }
  Pairs=dim(zeros)[1]*dim(ones)[1]
  PercentConcordance=(sum(conc)/Pairs)*100
  PercentDiscordance=(sum(disc)/Pairs)*100
  PercentTied=(sum(ties)/Pairs)*100
  return(list("Percent Concordance"=PercentConcordance,"Percent Discordance"=PercentDiscordance,"Percent Tied"=PercentTied,"Pairs"=Pairs))
}

Acc(model)
Acc(reg.model1)

#------to check multicollinearity use Variance Inflation Factor---------# 
library(car)
vif(model)
vif(reg.model1)

#------------------------------odds Ratio-------------------------------# 
exp(coef(model))
exp(coef(reg.model1))

#-----------------Predicton Method on testing data set------------------# 
testing$log_Predicted<-predict(model,testing) 
testing$log_Predicted1<-predict(reg.model1,testing)

#----------------type='response'-interms of probability-----------------#
testing$probs <-predict(model, testing, type='response')
testing$Predict<-as.factor(ifelse(testing$probs>0.70,1,0))
testing$probs1 <-predict(reg.model1, testing, type='response')
testing$Predict1<-as.factor(ifelse(testing$probs1>0.70,1,0))

#-----------------------Accuracy of testing data------------------------#
table(testing$Purchased, testing$Predict)
table(testing$Purchased, testing$Predict1)

#A confusion matrix describe the performance model on a set of test data#
library(caret)
confusionMatrix(testing$Purchased, testing$Predict, positive = "1")
confusionMatrix(testing$Purchased, testing$Predict1, positive = "1")


#--------ROC Curve can help in deciding the best threshold value--------#
library(ROCR)
library(ggplot2)


#----------------------Make predictions on test set---------------------#
predictTrain = predict(model,testing ,type="response")
predictTrain1 = predict(reg.model1,testing ,type="response")

#-----------------Predicton Method on testing data set------------------#
ROCRpred = prediction(predictTrain, testing$Purchased)
ROCRpred1 = prediction(predictTrain1, testing$Purchased)

#------------------------Performance function---------------------------#
ROCRperf = performance(ROCRpred, "tpr", "fpr")
ROCRperf1 = performance(ROCRpred1, "tpr", "fpr")

#--------------------------ploting Roc Curve----------------------------#
plot(ROCRperf)
plot(ROCRperf1)


#--------------------AUC(Area Under The ROC Curve)----------------------#
pred = prediction(testing$probs, testing$Purchased)
as.numeric(performance(pred, "auc")@y.values)
pred = prediction(testing$probs1, testing$Purchased)
as.numeric(performance(pred, "auc")@y.values)

#########################################################################
#--------------------Practical of Decision tree-------------------------#
#########################################################################
#-----------Taken All integar variable &  convert to numeric------------#
data1 = subset(data, select = -c(1,4))
names(data1)
str(data1)
data1<-data.frame(apply(data1,2, as.numeric))
str(data1)


#-------------------Taken all categorical variable----------------------#
data2 = subset(data, select = c(1,4))
str(data2)


#------------------combine Numeric & categorical Variable---------------# 
data<-data.frame(data2,data1)
str(data)
names(data)

#-----------------------To Verify the Partition-------------------------#
prop.table(table(data$Purchased))
prop.table(table(training$Purchased))
prop.table(table(testing$Purchased))


#----------------------Building Model & Plotting Model------------------#
library(rpart)
Model =rpart(Purchased~.,data=training,method = "class")

#            , parms = list(prior = c(.84,.16), split = "gini"))
library(rpart.plot)
rpart.plot.version1(Model, main = "Model Before Pruning",
                    type = 5, extra = 1,cex = 0.5,tweak =1.5,varlen = 0)
#     ,faclen=0) # to get full name 
#     type is to get variable name in nodes
#     extra is used to get no. of observatioin or 6 to get % 
#     Cex text size of entry plot 
#     tweak to increase the size of nodes label & cut off point 
#     Varlen is used to get full name of variable in nodes  
#     faclen is used to get full name of levels in branches


#----------------------Prediction on Training data----------------------#
training$Predicted=predict (Model,training,type ="class")
#A confusion matrix describe the performance model on a set of test data#
library(caret)
confusionMatrix(training$Predicted,training$Purchased)


#---------------------------Doing Pre-Pruning---------------------------# 
c<-rpart.control(minsplit =10, minbucket = 5, maxdepth = 3)
training$Predicted<-NULL


#-------------------Re-Building Model & Plotting Model------------------#
tune_fit <- rpart(Purchased~.,data=training,method ="class", control =c)
rpart.plot.version1(tune_fit, main = "Model After Pruning",
                    type = 5, extra = 1,cex = 0.5,tweak =2.2,
                    faclen = 0,varlen = 0)


#----------------------Prediction on Training data----------------------# 
training$Predicted=predict (tune_fit,training,type ="class")
library(caret)
confusionMatrix(training$Purchased,training$Predicted)


#-----------------------Prediction on Testing data----------------------# 
testing$Predicted=predict(tune_fit,testing,type ="class")
library(caret)
confusionMatrix(testing$Predicted,testing$Purchased)


#########################################################################
#--------------------Practical of k-NN alorithm-------------------------#
#########################################################################
#------------Data Normalization for get same range of data--------------#
#-------------it bring every call under the range of to 1---------------#
normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x))) }


#---------------------summary before normalization----------------------#
summary(data$EstimatedSalary)


#------------------make new dataframe for normalize data----------------#
data2 <- as.data.frame(lapply(data1, normalize))



#---------------------summary after normalization-----------------------#
summary(data2$Age)
summary(data2$EstimatedSalary)


#---------partition of data for testing of prediction(manually)---------#
data_train <- data2[1:250,]
data_test <- data2[251:400,]
data_train_labels <- data[1:250,2]
data_test_labels <- data[251:400,2]


#---------The kNN algorithm is applied to the training data set---------#
#-k is generally chosen as the squareroot of the number of observations-#
#-------------------Manual method k =40 is knn value--------------------# 
library(class)
#-----------------use the knn() function to test data-------------------#
data_test$data_test_pred <- knn(train = data_train, test = data_test,cl = data_train_labels, k=40)


#-------------------- Model Performance on testing data-----------------#
library(e1071)
library(caret)
confusionMatrix(data_test$data_test_pred,data_test_labels)


#-------method-2 using k fold cross validation for value of k-----------# 
# cv= k fold cross validation and number (k)=40 
# tunelength means different value of k and try 
# if tunelength is 15 then different 15 k values 
#method = "center"(x-mean(x)) 
#method = "scale" (x-mean(x))/standard deviation.
library(e1071)
trctrl <- trainControl(method = "repeatedcv", number = 40, repeats = 3)

knn_fit <- train(Purchased~., data = training, method = "knn",
                 trControl=trctrl,
                 preProcess = c("center", "scale"),
                 tuneLength = 15)


#-----------------------To get the Best Model---------------------------#
knn_fit
plot(knn_fit)


#-------------------Model Prediction testing data ----------------------#
testing$predicted <- predict(knn_fit, newdata = testing)


#------------------Model Performance on testing data--------------------#
#A confusion matrix describe the performance model on a set of test data#
confusionMatrix(testing$predicted, testing$Purchased )




