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
|#16ตุลาไปแยกปทุมวัน|278,311|2020-10-16 16:10:02|2021-04-16 16:23:46|336MB|
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

### 1. #ธรรมศาสตร์และการชุมนุม

![#ธรรมศาสตร์และการชุมนุม](https://user-images.githubusercontent.com/44984892/120426112-ab858900-c399-11eb-897d-76faf00d2960.png)

- total tweets : 17,656 
- distinct users : 8,087

|num of posts (per person)|num of people|
|:-:|:-:|
|1|5512|
|2|1206|
|3|494|
|4|265|
|5|115|
|6|107|
|7|80|
|8|46|
|9|42|
|10|30|
|...|...|
|74|1|
|86|1|
|87|1|
|175|1|

- most frequently retweeted tweets

|datetime|username|tweet|retweet|url|
|:-:|:-:|:-:|:-:|:-:|
|2020-09-11 16:42:07|malykh_jj|หลายคนก่อนเข้ามาประกวดบอกอยากเป็นกระบอกเสียง อยากใช้ Platformเวทีนางงามในการแก้ปัญหา แต่พอถึงเวลามีปัญหาจริงละเงียบกริบ คือไรคุณพี่ สงสารมารีญามากที่แบกวงการนางงามอยู่ขอบคุณมารีญามากเป็นกระบอกเสียงที่ดีและมีจุดยืน #มารีญา #คัดค้านนําเข้าเศษพลาสติก #ธรรมศาสตร์และการชุมนุม  https://t.co/Eb3FV8TWjT|81673|[link](https://twitter.com/malykh_jj/status/1304354526401495040)|
|2020-02-26 18:12:52|beenobeeta|เมิงงง มธ ประกาศ จะนำ นศ ไปราชดำเนิน  ยังไงดี น้องเค้าเปิดแล้วนะ #ธรรมศาสตร์และการชุมนุม|63250|[link](https://twitter.com/beenobeeta/status/1232624568348495872)|
|2020-02-26 19:03:58|xiaozaoput|"หนังสือก็ต้องอ่าน รัฐบาลก็ต้องด่า" มันส์สุดทีน55555   #ธรรมศาสตร์และการชุมนุม  https://t.co/eZwgrW1Hty|62298|[link](https://twitter.com/Xiaozaoput/status/1232637427203706880)|
|2020-09-19 19:09:30|nnoophilaa|แม่เจ้า หนึ่งทุ่ม คนเต็มท้องสนามหลวงเลย มันแบบ... กุว่ามันจะจบที่รุ่นเราจริงๆแหละทุกคน ความหวังมันมากขึ้นไปเรื่อยๆ 😭🙏🏻 #19กันยาทวงอํานาจคืนราษฏร #ธรรมศาสตร์และการชุมนุม #ม็อบ19กันยา  https://t.co/MEQWh6UBCx|62037|[link](https://twitter.com/nnoophilaa/status/1307290721309741057)|
|2020-02-26 18:03:50|chennietckjd|อย่างชอบ5555555555555  #ธรรมศาสตร์และการชุมนุม  https://t.co/GNLkXK4ipR|50168|[link](https://twitter.com/chennietckjd/status/1232622292984745984)|
|2020-09-11 16:40:11|annabeeannabell|ตอนนี้ตำรวจกำลังซ้อมปาแก๊สน้ำตาที่ชลบุรี เราไม่รู้ว่าจะติดแท๊กไหน #ธรรมศาสตร์และการชุมนุม  https://t.co/yCqGG34blk|50045|[link](https://twitter.com/annabeeannabell/status/1304354041795719169)|
|2020-02-26 21:40:21|pine_js852|น้องคนนี้จังหวะโบ๊บ๊ะมาก ชอบตอนแม่ห้าม  แม่ : แชมป์อย่าไปนะลูก! ช : ได้แม่.. ตอนนี้แม่น้องเค้ารู้ยัง 555555555555 #ธรรมศาสตร์และการชุมนุม  https://t.co/IHcRA3X1Na|46506|[link](https://twitter.com/Pine_js852/status/1232676781519278080)|
|2020-02-26 19:55:02|volleyship|"ตัดมาจากวีดีโอของน้อง  ช่วงท่อนฮุค" น้องๆเฉียบมาก👍🏻 #ไม่ทนไม่ถอยไม่ยอม #ราชมงคลจะไม่ทนอีกต่อไป #ธรรมศาสตร์และการชุมนุม #อภิปรายไม่ใว้วางใจรัฐบาล cr: fb Sumatee Kaongam  https://t.co/b2FG4nGn3H|43683|[link](https://twitter.com/volleyship/status/1232650278941286401)|
|2020-02-26 20:33:17|june16425|ขอพื้นที่ขำก่อนค่ะ555555 #ธรรมศาสตร์และการชุมนุม  https://t.co/bQd1awz6XH|42421|[link](https://twitter.com/june16425/status/1232659904751497216)|
|2020-02-26 21:16:25|realnameismynx|ที่สงสัยคือธรรมศาสตร์เขาทำได้ไงวะ อุดมการณ์ที่แรงชิบหายเพื่อประชาธิปไตย หล่อหลอมนักศึกษาทุกคนเป็นหมื่นๆให้รับใช้ความถูกต้องได้ขนาดนี้อ่ะ 47ปีที่แล้วกับตอนนี้คือไม่เปลี่ยนเลย กูโครตยอมการปลูกฝังจิตสำนึกของสถาบันเขา ยาแรงไม่หยุด #ธรรมศาสตร์และการชุมนุม|40989|[link](https://twitter.com/realnameismynx/status/1232670757899001857)|

### 4. #16ตุลาไปแยกปทุมวัน

![#16ตุลาไปแยกปทุมวัน](https://user-images.githubusercontent.com/44984892/120428932-bee72300-c39e-11eb-84cb-f3efaabd6ca9.png)

- total tweets : 278,311
- distinct users : 104,008

|num of posts (per person)|num of people|
|:-:|:-:|
|1|57887|
|2|18127|
|3|9084|
|4|5227|
|5|3304|
|6|2218|
|7|1663|
|8|1230|
|9|937|
|10|711|
|...|...|
|144|1|
|211|1|
|232|1|

- most frequently retweeted tweets

|datetime|username|tweet|retweet|url|
|:-:|:-:|:-:|:-:|:-:|
|2020-10-16 19:24:30|violettewautier|การชุมนุมต่อสู้เพื่อความยุติธรรม เพื่อประชาธิปไตย โดยไม่ได้ใช้ความรุนแรงของกลุ่มเยาวชน ต้องไม่ถูกปฏิบัติจากคนที่ต้องปกป้องประชาชนแบบนี้ ต้องไม่ใช้ความรุนแรง กลุ่มเยาวชนเค้าตัวเปล่านะคะ ต้องทำขนาดนี้เลยหรอคะ #16ตุลาไปแยกปทุมวัน|151500|[link](https://twitter.com/violettewautier/status/1317078966667128832)|
|2020-10-16 18:59:31|tptourpab|คุณเห็นความแตกต่างของ 2 กลุ่มนี้ไหม คุณเอะใจ มีคำถามอะไรบ้างไหม   #16ตุลาไปแยกปทุมวัน  https://t.co/QSsV7fdKS4|107177|[link](https://twitter.com/tptourpab/status/1317072679023697921)|
|2020-10-16 20:15:42|thebattz|อห โคตรสุดเลยภาพนี้ มือเปล่าๆประจันหน้ากับรถฉีดน้ำอะ 😭😭😭 #16ตุลาไปแยกปทุมวัน  https://t.co/63Pr2GBOn0|94728|[link](https://twitter.com/Thebattz/status/1317091852311408645)|
|2020-10-16 19:18:22|ud_awat|พวกคุณใช้ความรุนแรงแบบนี้กับประชาชนมือเปล่า รับไม่ได้จริงๆ พวกคุณไม่เหลือแม้แต่ความคน ไม่เหลือแล้วจริงๆ. #16ตุลาไปแยกปทุมวัน #หยุดคุกคามประชาชน|91899|[link](https://twitter.com/ud_awat/status/1317077424056590336)|
|2020-10-16 18:58:02|25novemm|เหี้ยมาก น้ำสีฟ้าที่มันฉีดใส่ เป็นเคมีฟิสิกส์ เหมือนตอนอีม็อบฮ่องกง ใช้เป็นหลักฐาน ระบุตัวตนคนในม็อบ สีฟ้า จะติดตัวนานเป็นอาทิตย์ อีเลว อีหน้าสัด #16ตุลาไปแยกปทุมวัน|87483|[link](https://twitter.com/25novemm/status/1317072307269955586)|
|2020-10-16 23:25:11|angangopilan|ล่าสุดหนูพึ่งได้ให้สัมภาษณ์กับสื่อแคนาดา (CBC in Canada, radio: as it Happens)เรื่องที่เกิดขึ้นในวันนี้ เราจะไม่มีวันเงียบ เราจะไม่ยอมให้รัฐปั้นเรื่องในแบบของเขา รุ่นเราคือรุ่นที่หลุดพ้นจากสังคมแห่งการจำยอม dictatorship shall perish, all hail democracy #16ตุลาไปแยกปทุมวัน|86561|[link](https://twitter.com/AngAngOpilan/status/1317139536518946816)|
|2020-10-16 19:10:18|jankzinn|มึงอันนี้เหี้ยมากอะ หลวงพี่เข้าไปไหว้คนขับรถฉีดน้ำอะเห็นแล้วแบบจะร้อง😭 #16ตุลาไปแยกปทุมวัน  https://t.co/rXIsLCEFYG|85091|[link](https://twitter.com/Jankzinn/status/1317075393036259329)|
|2020-10-16 19:21:50|8laryn|เซพพี่คนนี้เค้สด้วยนะคะ เห็นเค้ายืนขวางรถให้มาซักพักแล้ว #16ตุลาไปแยกปทุมวัน  https://t.co/KcmsHEFfbV|84489|[link](https://twitter.com/8laRyn/status/1317078297029734401)|
|2020-10-16 19:25:12|vousjay2|ทุกคนอย่าให้คลิปนี้หายไป ขอร้อง ช่วยรีกันไปเยอะๆๆๆๆๆ ใครเซฟได้เซฟ เผื่อคลิปหายอีกกก #16ตุลาไปแยกปทุมวัน  https://t.co/jnc5NAve2Y|83345|[link](https://twitter.com/vousjay2/status/1317079142521688065)|
|2020-10-16 19:42:08|liszukung|เชี่ยเอ๊ย คุณฐาปนีย์แม่งแนวหน้ามาก มีเสียงแว่วๆพูดอยู่ตลอด "ปิดตา ไม่ต้องห่วงพี่" กุอยากจะรักงานได้สักครึ่งนึงของเขา #16ตุลาไปแยกปทุมวัน  https://t.co/Xh8bzhD6ui|83260|[link](https://twitter.com/liszukung/status/1317083405461409792)|