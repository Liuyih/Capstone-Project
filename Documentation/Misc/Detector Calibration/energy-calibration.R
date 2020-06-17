data = read.csv("/home/ian/Downloads/energy-calibration.csv")
fit <- lm(data$energykev ~ poly(data$channel, 2, raw=TRUE))
summary(fit)
res = residuals(fit)

plot(
  data$channel,
  data$energykev,
  xlab="Channel #",
  ylab="Energy (KeV)",
  main="Energy Calibration",
)

predicted <- predict(fit)
lines(data$channel,predicted)

# legend("topright", legend=paste("R squared: ", format(summary(fit)$adj.r.squared, digits=4)))
summary(fit)$adj.r.squared