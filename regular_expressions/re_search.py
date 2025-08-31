import re;

string = "The date that I wrote this post is 08-30-2025 @ 5:57pm.";

searchDate = re.search("\d\d-\d\d-\d\d\d\d", string); # 08-30-2025.
groupSearchDate = searchDate.group(0);

searchDate2 = re.search("date.*.wro", string); # date that I wro
groupSearchDate2 = searchDate2.group(0);

print(dict(groupSearchDate=groupSearchDate))
print(dict(groupSearchDate2=groupSearchDate2))