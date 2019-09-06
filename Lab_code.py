# Laurence SanBoeuf
# Week 2, Lab 3
# Time: 1 hr
# Description: Calculates runoff in gallons with pre-set values. Plot length, plot width, and rainfall in inches. These values can be changed in the code.


plot_length = 50  #Length of plot area in ft
plot_width = 20  #Width of plot area in ft
area = plot_length*plot_width  #Area in ft
areain = (plot_length*12)* (plot_width*12)  #Area in inches
rainfall=1  #Amount of recorded rainfall in inches
rainfall_inches = areain*rainfall  #Volume of rainfall in certain area (inches cubed)
runoff_gallons = rainfall_inches*0.004329 #Volume of rainfall in area (gallons)

print "Plot_length is:", (plot_length), "ft"
print "Plot_width is:", (plot_width), "ft"
print "Rainfall_inches is:",(rainfall_inches), "in^2"
print "Runoff_gallons is:", (runoff_gallons), "gal"
