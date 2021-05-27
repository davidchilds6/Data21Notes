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
                        SUBSTRING(FirstName, 0, 1) AS FirstInitial,
                        SUBSTRING(REPLACE(MiddleName, 'NULL', ''), 0, 1) AS MiddleInitial,
                        LastName,
                        REPLACE(Suffix, 'NULL', '') AS Suffix;
employee_ids = FOREACH employees 
                GENERATE BusinessEntityID;
joint_results = JOIN people_filtered BY BusinessEntityID, 
                employee_ids BY BusinessEntityID;
final_results = FOREACH joint_results 
                GENERATE 
                    CONCAT( 
                        people_filtered::FirstInitial,
                        '. ', 
                        people_filtered::MiddleInitial, 
                        '. ',
                        people_filtered::LastName, 
                        ' ',
                        people_filtered::Suffix) AS FullName;
STORE final_results INTO 'Exercise3';