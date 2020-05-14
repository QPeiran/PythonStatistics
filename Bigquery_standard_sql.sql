##############################################

SELECT TIMESTAMP_TRUNC(timestamp, WEEK) week
  , REGEXP_EXTRACT(details.python, r'^\d*\.\d*') python
  , COUNT(*) downloads
FROM `the-psf.pypi.downloads2017*`
WHERE file.project='pyspark'
GROUP BY week, python
ORDER BY week



##############################################

SELECT TIMESTAMP_TRUNC(timestamp, WEEK) week
  , REGEXP_EXTRACT(details.python, r'^\d*\.\d*') python
  , COUNT(*) downloads
FROM `the-psf.pypi.downloads2017*`
WHERE file.project='pyspark'
GROUP BY week, python
HAVING python != '3.6' AND week<'2017-12-30'
ORDER BY week


#############################################

SELECT TIMESTAMP_TRUNC(timestamp, WEEK) week
  , REGEXP_EXTRACT(details.python, r'^\d*\.\d*') python
  , COUNT(*) downloads
FROM `fh-bigquery.pypi.pypi_2017`
WHERE project='pyspark'
AND timestamp>'2000-01-01' # nag
GROUP BY week, python
HAVING python != '3.6' AND week<'2017-12-30'
ORDER BY week