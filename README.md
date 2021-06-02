# twitter_analysis

[twitter trend data](https://getdaytrends.com/thailand/)

use [twint](https://github.com/twintproject/twint) to scrape data

## CLI commands of `twint`

- `twint -u username` - Scrape all the Tweets of a user (doesn't include retweets but includes replies).
- `twint -u username -s pineapple` - Scrape all Tweets from the user's timeline containing pineapple.
- `twint -s pineapple` - Collect every Tweet containing pineapple from everyone's Tweets.
- `twint -u username --year 2014` - Collect Tweets that were tweeted before 2014.
- `twint -u username --since "2015-12-20 20:30:15"` - Collect Tweets that were tweeted since 2015-12-20 20:30:15.
- `twint -u username --since 2015-12-20` - Collect Tweets that were tweeted since 2015-12-20 00:00:00.
- `twint -u username -o file.txt` - Scrape Tweets and save to file.txt.
- `twint -u username -o file.csv --csv` - Scrape Tweets and save as a csv file.
- `twint -u username -o file.json --json` - Scrape Tweets and save as a json file.

## collected tweets (`.json`)

|hashtag|num of tweets|oldest|latest|size|
|:-:|:-:|:-:|:-:|:-:|
|#ธรรมศาสตร์และการชุมนุม|17,656|2020-02-25 15:22:56|2021-05-22 11:19:13|23.5MB|
|#เกียมอุดมไม่ก้มหัวให้เผด็จการ|4,227|2020-02-25 19:44:42|2021-05-31 14:11:52|5.7MB|
|#saveวันเฉลิม|86,219|2020-06-04 19:29:59|2021-06-02 03:46:23|107MB|
|#16ตุลาไปแยกปทุมวัน|||||
|#กูสั่งให้มึงอยู่ใต้รัฐธรรมนูญ|19,065|2020-11-17 00:01:28|021-05-08 09:45:02|24.5MB|
|#25พฤศจิกาไปSCB|49,050|2020-11-24 22:25:13|2021-04-09 22:21:18|54.5MB|
|#ม็อบ25พฤศจิกาทวงคืนสมบัติชาติ|823|2020-11-20 14:04:15|2020-11-30 23:10:21|1.1MB|
|#ม็อบ2ธันวา|11,178|2020-11-19 20:31:19|2021-02-15 13:58:18|13.1MB|

## Data Dictionary

|column|data type|description|
|:-:|:-:|:-:|
|`id`| int | tweet ID |
|`conversation_id`| int | ? |
|`created_at`| timestamp | date & time |
|`date`| timestamp | only date |
|`time`| timestamp | only time |
|`timezone`| int | +7:00 |
|`user_id`| str | user ID |
|`username`| srt | username |
|`name`| str | display name |
|`place`|  | ? |
|`tweet`| str | tweet content |
|`language`| str |auto-detected, `th` or `en` or `und`|
|`mentions`|  | ? |
|`urls`| list of str | embedded urls |
|`photos`| list of str | embedded photos |
|`replies_count`| int | num of replies |
|`retweets_count`| int | num of retweets |
|`likes_count`| int | num of likes |
|`hashtags`| list of str | hashtags |
|`cashtags`|  | ? |
|`link`| str | permanent link of the tweet |
|`retweet`| bool | whether the tweet is retweet or not |
|`quote_url`|  |  |
|`video`|  |  |
|`thumbnail`|  |  |
|`near`|  |  |
|`geo`|  |  |
|`source`|  |  |
|`user_rt_id`|  |  |
|`user_rt`|  |  |
|`retweet_id`|  |  |
|`reply_to`| list of str |  |
|`retweet_date`|  |  |
|`translate`|  |  |
|`trans_src`|  |  |
|`trans_dest`|  |  |

## Exploratory data analysis
