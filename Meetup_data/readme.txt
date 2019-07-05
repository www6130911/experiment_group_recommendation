I. INTRODUCTION:
This is dataset crawled from Meetup.com and used in the experiments of the following paper:
Tuan-Anh Nguyen Pham, Xutao Li, Gao Cong, Zhenjie Zhang: A General Graph-based Model for Recommendation in Event-based Social Networks. ICDE 2015.

Please kindly cite the paper if you choose to use the data.



II. INSTRUCTIONS:
The dataset consists of the data from two regions, New York City (NYC) and state of California (CA), each of which contains two parts: training and test datasets.
Each part has several files as follows:

*events.txt : contains information of venues, groups and time of events.
Format of each line: 
    Event_id Venue_id Time Group_id
where the format of Time is YYYYMMDDhhmmss.


*event_users.txt : contains events' participant lists.
Format of each line: 
    Event_id User_id User_id User_id ...


*user_groups.txt : contains users' group lists.
Format of each line: 
    User_id Group_id Group_id Group_id ...


*group_tags.txt : contains groups' tag lists.
Format of each line: 
    Group_id Tag_id Tag_id Tag_id ...


*user_tags.txt : contains users' tag lists.
Format of each line: 
    User_id Tag_id Tag_id Tag_id ...
