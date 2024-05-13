# 1. Plots
Plotting multiple points
```
plot(c(1,4,5), c(4,-1,6))
```
### Parameters
- xlab, ylab
- col # change point color
- cex # change size of the plotting point
- pch # To change point style

# 2. Line Graphs
```
plot(c(1,4,5), c(4,-1,6), type='line')
```
### Parameters
- type='l' for the plot to be with line
- lwd # change line width
- lty # change line style

To display more than one line in a graph, use the plot() function together with the lines()

# 3. Scatterplots
- Use plot() 

To display more than one type of point in a graph, use the plot() function together with the points()

# 4. Pie chart
```
pie(c(1,2,3,4))
```
### Parameters
- init.angle
- label = c('cow', 'goat', 'sheep' ,'horse')
- col

Use legend() to put legend. By default, the plotting of the first pie starts from the x-axis and move counterclockwise.

# 5. Bar Chart
```
barplot(c(1,2,3), names.arg = c('cow', 'goat', 'horse'), col='blue', density = 10, width = c(1,2,3,4),  horiz = TRUE)

```