## 2022 - Fall_projects 
### FINANCIAL MODELING OF AUTO INSURANCE USING MONTE CARLO SIMULATION

Factors to consider - 
1. Age (18-24: 1.5, 25-45: 1, 45-60: 1.3, 60+: 1.6)
2. Driving History (DUI: 1.2 if yes, Reckless Driving: 1.1 if yes, Speeding ticket: 1.05 if yes in past one year : Yes/No) 
3. Credit Score (300-579: 1.2, 580-669: 1.1, 670-739: 1, 740-799: 0.95, 800-850: 0.88)
4. Years of driving (less than 1: 1.1 , 1-5: 1.05, 6-15: 1, 15+: 0.97) 
5. Location (Urban: 1.05, Rural: 0.97, Suburban: 1)
6. Insurance History (Continuous coverage over past 6 months: 1.05,Continuous coverage over past 1 year: 1, Continuous coverage over past 3+ years: 0.95, No previous coverage: 1.2)
7. Annual Mileage (0-7500: 1, 7500-10000: 1.1, 10000-15000: 1.15, 15000+: 1.2)(The amount that you drive)
8. Marital Status (Married: 0.95, Single/Divorced/Widowed: 1)
9. Claims History (Filed within last one year: 1.3, 1-3 years: 1.2, No claims filed: 1)
10. Coverage level (10k-20k: , .......30k-40k: 1, ....., 140k-150k, 150k+)
11. Deductible (No deductible: 1.2, 250$:1, 500$: 0.9, 1000$: 0.8)
12. Vehicle (NCAP rating- 0: 1.15, 1: 1.1, 2: 1.05, 3: 1, 4: 0.95, 5: 0.9)
 

Scenario and Purpose:

The purpose of this project is to determine the insurance premium rate of a renter's insurance based on the factors


1. Decide which variables to generate using pseudo random generator: claims amount, claims probability