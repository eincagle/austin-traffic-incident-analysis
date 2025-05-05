# austin-traffic-incident-analysis

## Tableau Dashboard

You can view the interactive [Traffic Incident Analysis Dashboard](https://public.tableau.com/shared/NXQKTMPSM?:display_count=n&:origin=viz_share_link).

![Austin Traffic Incident Heatmap and Analysis](https://github.com/user-attachments/assets/28f4ddbf-c801-47b2-80ef-5a61f360f9ec)

## Traffic Incident Analysis

This project analyzes real-time traffic incidents to visualize key patterns and trends, including geographic hotspots and incident types. 

## Key Insights

**1. Most Common Days for Incidents**  
- Fridays reported the most incidents (**5,694**), followed by Thursdays and Wednesdays.  
- This suggests a weekday rush-hour traffic pattern.

**2. Peak Incident Hour**  
- The highest frequency of incidents occurs at **10 PM (22:00)**.  
- May indicate increased late-night hazards or lower visibility issues.

**3. Top Locations for Incidents**  
- Most incidents occurred near these coordinates:  
  - POINT (-97.611818 30.256997): 49 incidents  
  - POINT (-97.648566 30.386857): 42 incidents  
- Can be mapped to identify and address local traffic hotspots.

**4. Most Reported Issues**  
- Top 3 traffic issues:  
  - Traffic Hazard: 9,798  
  - Crash Urgent: 9,575  
  - Collision: 4,626  
- Shows critical areas for safety and maintenance intervention.

**5. Busiest Months**  
- Peak months for incident reporting:  
  - May (4,761), August (4,468), April (4,409)  
- Suggests seasonal surges, potentially useful for staffing or awareness campaigns.


## Project Components
- **Python Code**: Data cleaning and preprocessing using Python (`pandas`).
- **Cleaned Data**: CSV file containing the cleaned data.
- **Tableau Dashboard**: Interactive visualizations of traffic incidents.

## How to Run the Python Script
1. Clone the repository:
   ```bash
   git clone https://github.com/eincagle/austin-traffic-incident-analysis
   cd austin-traffic-incident-analysis
