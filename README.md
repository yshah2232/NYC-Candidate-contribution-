# NYC-Fundraising Data

## Data Set - NYC.csv

### Intro to Data set

- Column names                 Data type
- cmte_id                      object
- cand_id                      object
- cand_nm                      object
- contbr_nm                    object
- contbr_city                  object
- contbr_st                    object
- contbr_zip                   object
- contbr_employer              object
- contbr_occupation            object
- contb_receipt_amt           float64
- contb_receipt_dt             object
- receipt_desc                 object
- memo_cd                      object
- memo_text                    object
- form_tp                      object
- file_num                      int64
- tran_id                      object
- election_tp                  object
- Party                        object
- Date                 datetime64[ns]


### Questions Answered 
#### Basic Data analysis and wrangling 

1. Whether its possible to identify the ’Party’ for each candidate ? **(data wrangling)**

2. Convert the contb receipt dt column into an actual date object ?**(data wrangling)**

3. Using group by, show the number (count) of donations given to each party ?

4. Using group by, show the number of donations given to each party,over time ?

5. Using group by, show the total dollar amount of donations given to each party ?

6. Using group by, show the total dollar amount of donations given to each party, over time ?

7. Which occupations donated the top 5 most money?

8. Which occupations donated the least 5 amount of money?

9. Which employer’s employees gave the most money, give the top 5 ?

10. For each candidate, what were the top 5 occupations that donated to their election ?

11. For the 5 candidates that raised the most money, graph their donations by time, in a line graph ?
