-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE

GROUP BY USER_ID, PRODUCT_ID #묶어서
HAVING COUNT(*) > 1 #중복된게 2이상 COUNT
ORDER BY USER_ID ASC, PRODUCT_ID DESC; #오름/내림차순

