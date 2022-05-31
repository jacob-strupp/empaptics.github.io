# Empaptics 

Empaptics is a portmanteau of "empathic" and "haptics". The empaptics system is a real time emotional classification and forecasting
pipeline that I built out for a client who saw applications for cross cultural business exchanges, and emotional monitoring 
in children with developmental disorders. The classifier and data set included here laid the foundation for the final product 
that was shipped.

The EEG_IADS data set consists of 3 channel EEG (collected from a proprietary BCI that the client developed) of 120 individuals
being exposed to emotional triggers from the International Affective Digitized Sounds (IADS) database. For each observation in 
the data set, the fractal dimension of the EEG epoch was calculated (this was done for each channel). Each observation contains
the label of the emotional trigger (Saddness:0, Anger:1, Happiness:2, Fear:3).
