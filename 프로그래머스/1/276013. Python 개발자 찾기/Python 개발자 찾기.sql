-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS 
WHERE 'Python' IN (SKILL_3, SKILL_2, SKILL_1)
ORDER BY ID ASC
;