
-- 1. Most Common Day of the Week for Incidents
SELECT dayname("Published Date") AS day_of_week, COUNT(*) AS incident_count
FROM austin_traffic_incidents
GROUP BY day_of_week
ORDER BY incident_count DESC;

-- 2. Peak Incident Hour
SELECT EXTRACT(HOUR FROM "Published Date") AS hour, COUNT(*) AS incident_count
FROM austin_traffic_incidents
GROUP BY hour
ORDER BY incident_count DESC
LIMIT 1;

-- 3. Top Locations (most incident-prone coordinates)
SELECT location, COUNT(*) AS incident_count
FROM austin_traffic_incidents
GROUP BY location
ORDER BY incident_count DESC
LIMIT 5;

-- 4. Most Common Incident Descriptions
SELECT "Issue Reported", COUNT(*) AS count
FROM austin_traffic_incidents
GROUP BY "Issue Reported"
ORDER BY count DESC
LIMIT 5;

-- 5. Monthly Incident Trend
SELECT TO_CHAR("Published Date", 'Month') AS month, COUNT(*) AS incident_count
FROM austin_traffic_incidents
GROUP BY month
ORDER BY incident_count DESC
LIMIT 3;
