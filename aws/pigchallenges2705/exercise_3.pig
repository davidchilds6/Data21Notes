-- Output a file containing a list of all names of employees
-- as initials and surname (e.g. "D. R. Harvey").
/*
Join people and employees on buisnessentityid
substring first and middle names
filter null and concat
*/
-- load in csvs
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
employees = LOAD 'PigExercise/csvs/employees.csv' USING PigStorage(',')
            AS (
                BusinessEntityID: int,
                NationalIDNumber: long, 
                LoginID: chararray,
                OrganizationNode: int,
                OrganizationLevel: int,
                JobTitle: chararray,
                BirthDate: chararray,
                MaritalStatus: chararray,
                Gender: chararray,
                HireDate: chararray,
                SalariedFlag: int,
                VacationHours: int,
                SickLeaveHours: int,
                CurrentFlag: int, 
                rowguid: chararray,
                ModifiedDate:chararray
            );
-- filter columns
people_filtered = FOREACH people 
                GENERATE
                        BusinessEntityID,
                        FirstName,
                        REPLACE(MiddleName, 'NULL', '') AS MiddleName,
                        LastName,
                        REPLACE(Suffix, 'NULL', '') AS Suffix;
people_init = FOREACH people_filtered 
                GENERATE 
                        BusinessEntityID,
                        SUBSTRING(FirstName, 0, 1) AS FirstInitial,
                        SUBSTRING(MiddleName, 0, 1) AS MiddleInitial,
                        LastName,
                        Suffix;
employee_ids = FOREACH employees 
                GENERATE BusinessEntityID;
-- join on BusinessEntityID
joint_results = JOIN people_init BY BusinessEntityID, 
                employee_ids BY BusinessEntityID;
-- return concat names
final_results = FOREACH joint_results 
                GENERATE 
                    CONCAT( 
                        people_init::FirstInitial,
                        '. ', 
                        people_init::MiddleInitial, 
                        '. ',
                        people_init::LastName, 
                        ' ',
                        people_init::Suffix) AS FullName;
STORE final_results INTO 'Exercise3';

-- initial problems solved when separating the replace aggregations and substring aggregations into separate variables.
/* in theory replacing this for above would avoid empty middle names
final_results = FOREACH joint_results
                GENERATE (MiddleInitial=='[A-Z]'?
                    CONCAT(
                        people_init::FirstInitial,
                        '. ',
                        people_init::MiddleInitial,
                        '. ',
                        people_init::LastName,
                        ' ',
                        people_init::Suffix):
                     CONCAT(
                        people_init::FirstInitial,
                        '. ',
                        people_init::LastName,
                        ' ',
                        people_init::Suffix)) AS FullName;
 */