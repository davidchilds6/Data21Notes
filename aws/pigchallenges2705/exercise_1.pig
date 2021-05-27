-- Output the full names of the Top 5 Salespeople
/*
Join salespeople.csv to employees.csv, on Buisness Entity
Order By Sales YTD descending, Limit 5
*/
-- load in salespeople.csv
salespeople = LOAD 'PigExercise/csvs/salespeople.csv' USING PigStorage(',')
            AS (
                BusinessEntityID: int,
                TerritoryID: int,
                SalesQuota: int,
                Bonus: int,
                CommissionPct: float,
                SalesYTD: float,
                SalesLastYear: float,
                rowguid: chararray,
                ModifiedDate: chararray
            );
-- load in people.csv
people = LOAD 'PigExercise/csvs/people.csv' USING PigStorage(',')
        AS (
            BusinessEntityID: int,
            PersonType: chararray,
            NameStyle: int,
            Title: chararray,
            FirstName: chararray,
            MiddleName: chararray,
            LastName: chararray,
            Suffix: chararray,
            EmailPromotion: int,
            AdditionalContactInfo: chararray,
            Demographics: chararray,
            rowguid: chararray,
            ModifiedDate: chararray
        );
-- remove null characters with empty strings
poeple_filtered = FOREACH people 
                GENERATE
                        BusinessEntityID,
                        REPLACE(Title, 'NULL', '') AS Title,
                        FirstName,
                        REPLACE(MiddleName, 'NULL', '') AS MiddleName,
                        LastName,
                        REPLACE(Suffix, 'NULL', '') AS Suffix;
-- transform data into required fields only
sales = FOREACH salespeople 
        GENERATE 
                BusinessEntityID, 
                SalesYTD;
names = FOREACH poeple_filtered 
        GENERATE 
                BusinessEntityID, 
                CONCAT( 
                    Title,
                    ' ',
                    FirstName,
                    ' ', 
                    MiddleName, 
                    ' ',
                    LastName, 
                    ' ',
                    Suffix) AS FullName;
-- join tables on ID
joint_results = JOIN names BY BusinessEntityID,
                 sales BY BusinessEntityID;
-- order and limit
ordered_results = ORDER joint_results BY sales::SalesYTD DESC;
final_results = LIMIT ordered_results 5;
STORE final_results INTO 'Exercise1';