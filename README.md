# Global Consumption Trends for Market Expansion Strategy

## Project Overview  
This project analyses global consumption trends using World Bank data to identify high-growth markets and inform data-driven business expansion strategies.  

The analysis simulates a real-world scenario in which an organisation evaluates international markets based on macroeconomic indicators and consumption patterns to support strategic decision-making.

---

## Dashboard  

The dashboard provides a visual analysis of global consumption trends, enabling identification of high-growth markets and regional performance differences.

![Dashboard](dashboard.png)

---

## Business Problem  
Businesses expanding internationally must determine which markets offer the highest growth potential while balancing risk and stability.  

This project demonstrates how consumption data can be used to:
- Identify emerging high-growth markets  
- Benchmark mature economies (e.g. UK) against global trends  
- Support strategic market entry decisions  

---

## Key Metrics  
- Household final consumption expenditure  
- Year-on-year consumption growth rate  
- UK vs global consumption comparison  
- Long-term trend analysis  

---

## Analytical Approach  

- Extracted data from the World Bank API (JSON format)  
- Performed data cleaning and preprocessing (handling missing values and inconsistencies)  
- Transformed time-series data for analysis  
- Calculated growth rates using percentage change  
- Conducted comparative trend analysis (UK vs global)  
- Developed visualisations to support insight generation  

---

## Key Insights  

### Global Growth Outpaces the UK  
Global consumption has increased significantly over time, while UK growth remains relatively stable.  

Business implication: Mature economies demonstrate slower, more stable growth patterns. Expansion into faster-growing markets may yield higher returns.

---

### Emerging Markets Drive Consumption Growth  
Emerging economies exhibit significantly higher consumption growth compared to developed markets.  

Business implication: Growth is concentrated in developing regions, presenting strong opportunities for expansion.

---

### Sustained Long-Term Growth Trend  
Global consumption shows a consistent upward trajectory over time.  

Business implication: Increasing purchasing power globally supports long-term demand and expansion potential.

---

## Recommendations  

- Prioritise entry into high-growth emerging markets  
- Use consumption trends as a key input for market selection  
- Monitor macroeconomic indicators to identify early-stage opportunities  
- Diversify across stable and high-growth markets to balance risk  

---

## Limitations  

- Analysis is based on historical macroeconomic data and may not capture short-term volatility  
- External factors (e.g. political risk, inflation, currency fluctuations) are not included  
- Data availability varies across countries and time periods  

---

## Tools and Technologies  

- Python (pandas, matplotlib)  
- REST API (World Bank Open Data)  
- Data cleaning and transformation  
- Time-series analysis  
- Tableau (dashboard development)  

---

## How to Run  

```bash
python3 analysis.py

