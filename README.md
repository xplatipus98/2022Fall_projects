## 2022 - Fall_projects 
### FINANCIAL MODELING OF INSURANCE COMPANY (AUTO INSURANCE) USING MONTE CARLO SIMULATION

Team Members:
Antara chansarkar
Saket Naik
Sparsh Sadafal

In this project, we aim to find out the optimum price of an Auto insurance product using Monte Carlo Simulation. We simulated random insurance customers and demand of elasticity to maintain a balance between premium increase and resulting customer attrition.

Below are the characteristics we considered to determine premium of a customers- 
1. Age
2. Driving History  
3. Credit Score 
4. Years of driving  
5. Location 
6. Insurance History 
7. Annual Mileage 
8. Marital Status 
9. Claims History 
10. Coverage level
11. Deductible 
12. Vehicle 

Methodology:
1. Set relativity values for each of the characteristics mentioned above to find total premium
2. Generate users with ramdom values of the above variables
3. Multiply the relativity values of the users with the base premium to find out individual premium
4. Find out the total claims using claims frequency and severity with gaussian distribution and truncated normal distribution
5. Set a threshold for customer attrition and increase the value of base premium
6. Calculated the customer attrition and profit after increased premium
7. Keep increasing premium until optimum premium with minimum customer attrition is obtained

Instructions:
1. Run the main function
2. Run the viz.ipynb notebook for visualizations and result

