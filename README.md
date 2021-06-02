# twitter_analysis

use [twint](https://github.com/twintproject/twint) to scrape data

## CLI command

- `twint -u username` - Scrape all the Tweets of a user (doesn't include retweets but includes replies).
- `twint -u username -s pineapple` - Scrape all Tweets from the user's timeline containing pineapple.
- `twint -s pineapple` - Collect every Tweet containing pineapple from everyone's Tweets.
- `twint -u username --year 2014` - Collect Tweets that were tweeted before 2014.
- `twint -u username --since "2015-12-20 20:30:15"` - Collect Tweets that were tweeted since 2015-12-20 20:30:15.
- `twint -u username --since 2015-12-20` - Collect Tweets that were tweeted since 2015-12-20 00:00:00.
- `twint -u username -o file.txt` - Scrape Tweets and save to file.txt.
- `twint -u username -o file.csv --csv` - Scrape Tweets and save as a csv file.
- `twint -u username -o file.json --json` - Scrape Tweets and save as a json file.

## data to collect

1. #ธรรมศาสตร์และการชุมนุม #เกียมอุดมไม่ก้มหัวให้เผด็จการ
2. #saveวันเฉลิม
3. #16ตุลาไปแยกปทุมวัน
4. #กูสั่งให้มึงอยู่ใต้รัฐธรรมนูญ
5. #25พฤศจิกาไปSCB #ม็อบ25พฤศจิกาทวงคืนสมบัติชาติ
6. #ม็อบ2ธันวา

## Exploratory data analysis
