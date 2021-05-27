-- Find the average salesperson's sales (year to date) per territory name. 
-- Also provide the count of salespeople per territory.
/*
Join on TerritoryID, group by territory name
average the salesYTD
count salespeople
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
-- load in territories.csv
territories = LOAD 'PigExercise/csvs/territories.csv' USING PigStorage(',')
            AS (
                TerritoryID: int,
                Name: chararray,
                CountryRegionCode: chararray,
                Group: chararray,
                SalesYTD: float,
                SalesLastYear: float,
                CostYTD: int,
                CostLastYear: int,
                rowguid: chararray,
                ModifiedDate: chararray
            );
-- filter columns
sales = FOREACH salespeople 
        GENERATE  
            TerritoryID, 
            SalesYTD;
territory = FOREACH territories 
            GENERATE 
                TerritoryID, 
                Name;
-- join tables
joint_results = JOIN sales BY TerritoryID, 
                territory BY TerritoryID;
-- group and aggregate
grouped_results = GROUP joint_results BY territory::Name;
aggregate_results = FOREACH grouped_results 
                    GENERATE 
                        group,
                        AVG(joint_results.sales::SalesYTD) AS average_salesYTD,
                        COUNT(joint_results.sales::SalesYTD) AS count_salesYTD;
STORE aggregate_results INTO 'Exercise2';