# -*- coding: utf-8 -*-
"""Student's_Mental_Health (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OLGkhbkUaWqaRf2MGYKkTrCZmsXotIuO

# **Analyzing Students' Mental Health**

Does going to university in a different country affect your mental health? A Japanese international university surveyed its students in 2018 and published a study the following year that was approved by several ethical and regulatory boards.

The study found that international students have a higher risk of mental health difficulties than the general population, and that social connectedness (belonging to a social group) and acculturative stress (stress associated with joining a new culture) are predictive of depression.

For this project, I will explore the \`students\` data using SQL and Python to find out if we can come to a similar conclusion for international students and see if the length of stay is a contributing factor.

# Overview of the dataset
"""

SELECT *
FROM [students].[dbo].[students.csv]

"""# Explore and understand the data

<span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">Count the number of records in the dataset as<i> <b>total_records</b></i>, and see how many records we have for each student type as <b><i>count_inter_dom</i></b>.</span>
"""

SELECT
	COUNT(*) AS total_records
FROM [students].[dbo].[students.csv]

SELECT
	inter_dom AS student_type,
	COUNT(*) AS count_inter_dom
FROM [students].[dbo].[students.csv]
GROUP BY inter_dom;

"""# Filter to understand the data for each student type

<span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">Explore the data for each student type in <b><i>inter_dom</i></b></span> <span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">&nbsp;by doing three queries that filter for the two student types represented in the table, as well as the students with unknown status (</span>`NULL`<span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">).</span>

### _**International student**_
"""

-- Query for students with student type 'inter'
SELECT *
FROM [students].[dbo].[students.csv]
WHERE inter_dom = 'Inter';

"""### **_Domestic student_**"""

-- Query for students with student type 'dom'
SELECT *
FROM [students].[dbo].[students.csv]
WHERE inter_dom = 'Dom';

"""### **_Unknown student_**"""

-- Query for students with unknown student type
SELECT *
FROM [students].[dbo].[students.csv]
WHERE inter_dom IS NULL;

"""# Query the summary statistics of the diagnostics scores for all students

<span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">Find the summary statistics for each diagnostic test using aggregate functions. Round the averages to two decimal places and use aliases <i><b>min_phq</b></i></span><span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">, <i><b>max_phq</b></i>, and <b><i>avg_phq</i></b></span><span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">; repeat this structure for all tests (<i><b>_scs</b></i></span> <span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">&nbsp;and <i><b>_as</b></i></span><span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">).</span>
"""

SELECT
-- Query for calculating scores of Depression of all students
	ROUND(AVG(CAST(todep AS int)),2) AS avg_phq,
    ROUND(MIN(CAST(todep AS int)),2) AS min_phq,
	ROUND(MAX(CAST(todep AS int)),2) AS max_phq,

-- Query for calculating scores of Social Connectedness of all students
    ROUND(AVG(CAST(tosc AS int)),2) AS avg_scs,
	ROUND(MIN(CAST(tosc AS int)),2) AS min_scs,
	ROUND(MAX(CAST(tosc AS int)),2) AS max_scs,

-- Query for calculating score of Acculturative Stress of all students
    ROUND(AVG(CAST(toas AS int)),2) AS avg_as,
	ROUND(MIN(CAST(toas AS int)),2) AS min_as,
	ROUND(MAX(CAST(toas AS int)),2) AS max_as

FROM [students].[dbo].[students.csv];

"""# Summarize the data for international students only

<span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">Narrow down the results down further to see the summary statistics for international students only through filtering and grouping.</span>
"""

SELECT
-- Query for calculating average Depression score of international students
	ROUND(AVG(CAST(todep AS int)),2) AS inter_avg_phq,
	ROUND(MIN(CAST(todep AS int)),2) AS inter_min_phq,
	ROUND(MAX(CAST(todep AS int)),2) AS inter_max_phq,

-- Query for calculating Social Connectedness scores of international students
	ROUND(AVG(CAST(tosc AS int)),2) AS inter_avg_scs,
	ROUND(MIN(CAST(tosc AS int)),2) AS inter_min_scs,
	ROUND(MAX(CAST(tosc AS int)),2) AS inter_max_scs,

-- Query for calculating Acculturative Stress scores of international students
	ROUND(AVG(CAST(toas AS int)),2) AS inter_avg_as,
	ROUND(MIN(CAST(toas AS int)),2) AS inter_min_as,
	ROUND(MAX(CAST(toas AS int)),2) AS inter_max_as
FROM [students].[dbo].[students.csv]
WHERE inter_dom = 'Inter';

"""# See the impact of length of stay

<span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">Let's see how the length of stay of an international student impacts the&nbsp;</span> <span style="box-sizing: inherit; font-weight: 700; color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">average</span> <span style="color: rgb(101, 112, 124); font-family: Studio-Feixen-Sans, Arial, sans-serif; background-color: rgb(255, 255, 255);">&nbsp;diagnostic scores, I order the results by descending order of the length of stay.</span>
"""

-- Find the average scores by length of stay for international students, and view them in descending order
SELECT CAST(stay AS numeric) AS length_of_stay,
       ROUND(AVG(CAST(todep AS int)), 2) AS average_phq,
       ROUND(AVG(CAST(tosc AS int)), 2) AS average_scs,
       ROUND(AVG(CAST(toas AS int)), 2) AS average_as
FROM [students].[dbo].[students.csv]
WHERE inter_dom = 'Inter'
GROUP BY CAST(stay AS numeric)
ORDER BY length_of_stay DESC;

"""# Analyze the correlation between length of stay and diagnostic scores

With the result from section 5, I use Python to calculate the correlation between length of stay and average diagnostic scores for international students.
"""

# Calculating correlation coefficients

import pyodbc
import pandas as pd
data = [
[10,13,32,50],
[8,10,44,65],
[7,4,48,45],
[6,6,38,58],
[5,0,34,91],
[4,8,33,87],
[3,9,37,78],
[2,8,37,77],
[1,7,38,72]
]
stay_depression = pd.DataFrame(data, columns=['length_of_stay', 'average_phq','average_scs','average_as'])
print(stay_depression.corr())

"""# CONCLUSION

In conclusion, even though the study found that social connectedness and acculturative stress are predictive of depression for international students, further exploration into the dataset shows that the length of stay is not quite a contributing factor.

The correlation coefficient between "stay" with "average\_phq" and "average\_scs" is 0.27 and 0.14 respectively. The numbers show weakly correlated relationships between length of stay with depression and social connectedness, which means two things:

- The longer a student stays in a new country doesn't neccessarily lead to the more they feel belonged to the native social group;
- And level of depressionn also doesn't strongly depend on how long they have been living in a new country.

On the other hand, the correlation coefficient between "stay" and "average\_as" is -0.64 indicates a quite strongly negative relationship, which means the longer the stay associated with the less stress associated with joining a new culture as international students will gradually accomodate themselves to the new environment.
"""