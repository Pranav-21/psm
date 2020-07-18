#---------------Practical of Multiple Linear Regression-----------------#
#-----------------------------Pranav Mahajan----------------------------#

#-----Data from :- https://www.kaggle.com/sonalisingh1411/startup50-----#
#------------------------------Data Import------------------------------#

data<-read.csv("C:/Users/Moraya/Desktop/50_Startups.csv")
data1 <- data


#-create subset of data to remove categorical data which is imp for mlr-#
input = subset(data, select = -c(4))


#--------display the structure of Data with datatype of variables-------#
str(input)


#-----------------------------column names------------------------------#
names(input)


#----------------------------missing value------------------------------#
sapply(data, function(x) sum(is.na(x)))


#-------------partition of data for testing of prediction---------------#
set.seed(23)
library(caret)
train<-createDataPartition(input$Profit,p=0.7,list=FALSE)
training<-input[train,]
testing<-input[-train,]


#-----------------Numerical method(Correlation matrix)------------------#
cor(training)


#---------------------Model Creation:enter method-----------------------#
model1 <- lm(Profit~., data = training)


#summary() is used to produce summary of the results of model functions-#
summary(model1)


#------to check multicollinearity use Variance Inflation Factor---------#
library(car)
vif(model1)


#--------------------Model Creation:tepwise method----------------------#
model2 <- step(lm(Profit~., data = training),direction = "both")


#summary() is used to produce summary of the results of model functions-#
summary(model2)


#------to check multicollinearity use Variance Inflation Factor---------#
vif(model2)


#-------------------------Assumption of Model---------------------------#
#----------par() is use for multiple graphs in a single plot------------#
#--mfrow= c(nrows, ncols) is to create a matrix of nrows x ncols plots--# 
par(mfrow=c(2,2))
plot(model2)


#-dwtest examines whether the errors are autocorrelated with themselves-#
library(lmtest)
dwtest(model2)


#--ncvTest() provides us with another test of the homoscedasticity(CV)--#
ncvTest(model2)


#--histogram representation of residuals -to ckeck normal distribution--#
hist(model2$residuals)


#-------------Predicton Method on entire testing data set---------------# 
testing$log_Predicted<-predict(model2,testing)


