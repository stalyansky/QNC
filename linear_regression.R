#Written by Seth Talyansky on September 29, 2025
library(ggplot2)

data <- data.frame(age = c(3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17), wing_length = c(1.4, 1.5, 2.2, 2.4, 3.1, 3.2, 3.2, 3.9, 4.1, 4.7, 4.5, 5.2, 5.0))

#Exercise 1
ggplot(data, aes(x=age, y=wing_length)) + geom_point()

#Exercise 2
model <- lm(wing_length ~ age, data=data)
slope <- coef(summary(model))[2]
intercept <- coef(summary(model))[1]
se <- coef(summary(model))[2, 2]
ggplot(data, aes(x=age, y=wing_length)) + geom_point() + geom_abline(slope=slope, intercept=intercept, linetype='dashed')

#Exercise 3
summary(model)
print('The null hypothesis can be rejected at the 0.05 significance level because the P-value associated with the F-statistic is 3.01e-09')

#Exercise 4
ggplot(data, aes(x=age, y=wing_length)) + geom_point() + geom_abline(slope=slope, intercept=intercept, linetype='dashed') + geom_abline(slope=slope-se, intercept=intercept, linetype='dashed', alpha=0.5) + geom_abline(slope=slope+se, intercept=intercept, linetype='dashed', alpha=0.5)

#Exercise 5
print('R^2 is 0.9634')

#Exercise 6
r <- round(0.9635^0.5, 2)
print(paste('Pearson\'s r is', r))

#Exercise 7
data$wing_length <- data$wing_length + rnorm(nrow(data))
model <- lm(wing_length ~ age, data=data)
slope <- coef(summary(model))[2]
intercept <- coef(summary(model))[1]
se <- coef(summary(model))[2, 2]
print(summary(model))
ggplot(data, aes(x=age, y=wing_length)) + geom_point() + geom_abline(slope=slope, intercept=intercept, linetype='dashed') + geom_abline(slope=slope-se, intercept=intercept, linetype='dashed', alpha=0.5) + geom_abline(slope=slope+se, intercept=intercept, linetype='dashed', alpha=0.5)
print('The fit is worse after adding the noise (now R^2 is only 0.36)')