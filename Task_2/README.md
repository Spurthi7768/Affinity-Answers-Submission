# Task -2
The following questions test your aptitude for interacting with databases. The questions are based off the following public SQL DB: https://docs.rfam.org/en/latest/database.html

## Question
 How many types of tigers can be found in the taxonomy table of the dataset?  
 What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)

## Answer

**Query** : SELECT COUNT(*) AS total_tigers FROM taxonomy WHERE species LIKE '%Panthera tigris%';

**Output** : 

![image](https://github.com/Spurthi7768/Affinity-Answers-Submission/assets/67674744/e101b737-c3a7-44de-b9db-949da48c7ecc)




**Query** : SELECT ncbi_id FROM taxonomy WHERE species LIKE '%Panthera tigris sumatrae%';

**Output** : 


![image](https://github.com/Spurthi7768/Affinity-Answers-Submission/assets/67674744/0c7adbe8-0e94-4491-ad3c-1f2870984932)




## Question
 Find all the columns that can be used to connect the tables in the given database.


## Answer

**Query**: SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'Rfam' AND COLUMN_KEY = 'PRI' ORDER BY table_name;

**Output**: 

![image](https://github.com/Spurthi7768/Affinity-Answers-Submission/assets/67674744/e975e494-9f5d-45b6-9c9c-add00ceab559)



## Question
 Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)


## Answer

**Query** : SELECT MAX(length) AS max_length,taxonomy.ncbi_id,species FROM taxonomy JOIN rfamseq ON taxonomy.ncbi_id=rfamseq.ncbi_id WHERE species LIKE '%Oryza sativa%' GROUP BY taxonomy.ncbi_id ORDER BY max_length DESC LIMIT 1;

**Output**:


![image](https://github.com/Spurthi7768/Affinity-Answers-Submission/assets/67674744/27eacdf2-25d1-44eb-a849-b72a27a5b8f6)



## Question
We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)


## Answer

**Query** : SELECT f.rfam_acc AS family_accession, f.description AS family_name, MAX(r.length) AS max_sequence_length FROM family AS f JOIN full_region AS fr ON f.rfam_acc = fr.rfam_acc JOIN rfamseq AS r ON fr.rfamseq_acc = r.rfamseq_acc GROUP BY f.rfam_acc, f.description HAVING max_sequence_length > 1000000 ORDER BY max_sequence_length DESC LIMIT 120, 15;

**Output** : 


![image](https://github.com/Spurthi7768/Affinity-Answers-Submission/assets/67674744/780c73f1-7ad8-4520-a140-fafed2ea953d)



