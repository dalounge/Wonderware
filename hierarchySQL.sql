DROP TABLE #RefStorage
DROP TABLE #RefStorage2
DECLARE @ISENTITYNULL INT

DECLARE @FULLALARMCLINTSTRING NVARCHAR(MAX)


DECLARE @ENTITYID NVARCHAR(MAX)
DECLARE @NEXTREFSTRING NVARCHAR(MAX) 
DECLARE @NAME NVARCHAR(MAX)
DECLARE @REFSTRING NVARCHAR(MAX)


CREATE TABLE #RefStorage
(
                FULLALARMCLINTSTRING NVARCHAR(MAX),
    ENTITYID NVARCHAR(MAX),
    NEXTREFSTRING NVARCHAR(MAX),
                NAME NVARCHAR(MAX),
                REFSTRING NVARCHAR(MAX)

)

CREATE TABLE #RefStorage2
(
                FULLALARMCLINTSTRING NVARCHAR(MAX),
    ENTITYID NVARCHAR(MAX),
    NEXTREFSTRING NVARCHAR(MAX),
                NAME NVARCHAR(MAX),
                REFSTRING NVARCHAR(MAX)

)

 INSERT INTO #RefStorage (FULLALARMCLINTSTRING, ENTITYID, NEXTREFSTRING,NAME,REFSTRING)
SELECT reference_string+'.'+ [name],[entity_id],'Symbol:'+[name] ,[name], reference_string FROM [dbo].[internal_get_gtb_visual_element_references_preview_view] where reference_string ='ClientControl:AlarmClient'

WHILE 1=1
BEGIN
                IF (SELECT COUNT(*) FROM #RefStorage WHERE (ENTITYID <> 'NULL') AND (ENTITYID IS NOT NULL) ) <> 0
                                BEGIN
                                DELETE FROM #RefStorage2
                                INSERT INTO  #RefStorage2 (FULLALARMCLINTSTRING, ENTITYID, NEXTREFSTRING,NAME,REFSTRING)
                                SELECT 
                                 CASE WHEN T1.[name] IS NULL THEN FULLALARMCLINTSTRING ELSE  FULLALARMCLINTSTRING+'.'+ T1.[name] END , [entity_id],'Symbol:'+T1.[name] ,T1.[name], reference_string 
                                FROM #RefStorage 
                                LEFT OUTER JOIN [dbo].[internal_get_gtb_visual_element_references_preview_view] T1 
                                ON NEXTREFSTRING = reference_string AND reference_string IS NOT NULL
                                DELETE FROM #RefStorage
                                INSERT INTO  #RefStorage
                                SELECT * FROM #RefStorage2
                                PRINT 'pass' 
                                END
                ELSE
                                BREAK
                

END
--IF (SELECT TOP 1 [entity_id]fROM [dbo].[internal_get_gtb_visual_element_references_preview_view] where reference_string = @NEXTREFSTRING) = 'NULL'
--                                                             BEGIN
--                                                             SET @FULLALARMCLINTSTRING = @FULLALARMCLINTSTRING+'.'+@SUBNAME
--                                                             SET @ISENTITYNULL = 1
--                                                             END
--                                             ELSE
SELECT * FROM #RefStorage2

DROP TABLE #RefStorage
DROP TABLE #RefStorage2
