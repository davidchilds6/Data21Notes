import io

import boto3
from pprint import pprint
import json
import csv
import pandas as pd

# Boto 3 scans .aws in ~ for credentials to gain access to the aws

s3_client = boto3.client("s3")  # client object https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session
bucket_list = s3_client.list_buckets()
# pprint(bucket_list, sort_dicts=False)

# for bucket in bucket_list["Buckets"]:
#     print(bucket["Name"])

# for index, bucket in enumerate(bucket_list["Buckets"], start = 1):
#     print(f"{index}: {bucket['Name']}")


bucket_name = "data-eng-resources"
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="big-data/pig-demo")
# pprint(bucket_contents)

# for name in bucket_contents["Contents"]:
#     pprint(name["Key"])


s3_resource = boto3.resource("s3")  # resource object
# bucket = s3_resource.Bucket(bucket_name)
# contents = bucket.objects.all()
# for item in contents:
#     print(item.key)

# How to actually access stuff in a bucket in s3 as opposed to just printing.
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key="python/chatbot-intent.json"
)

# pprint(s3_object)

contents = s3_object["Body"].read()
contents_dict = json.loads(contents)
# pprint(contents_dict)


s3_object2 = s3_client.get_object(
    Bucket=bucket_name,
    Key="python/fish-market.csv"
)

contents2 = s3_object2["Body"].read()
#contents2_df = pd.read_csv(s3_object2["Body"])

pprint(contents2)



# see if we can find a sol similar for txt files.


# Writing to s3 first example if file already exists.
# create and save json file with your name in using python
my_dict = {
    "name": "Dave C",
    "age": 24
}
#
# with open("davec.json", "w") as jsonfile:
#     json.dump(my_dict, jsonfile)


# s3_client.upload_file(
#     Filename="davec.json",
#     Bucket="data-eng-resources",
#     Key="Data21/davec.json"
# )

# s3_client.put_object(
#     Body=json.dumps(my_dict),
#     Bucket="data-eng-resources",
#     Key="Data21/Put/davec2.json"
# )

# df = pd.DataFrame([[1.1, 2.2, 3.3, 4.4, 5.5], [10, 20, 30, 40, 50]])
#
# str_buffer = io.StringIO()
# df.to_csv(str_buffer)

# s3_client.put_object(
#     Body=str_buffer.getvalue(),
#     Bucket="data-eng-resources",
#     Key="Data21/CSV/dchilds.csv"
# )
#
# s3_resource.Object("data-eng-resources", "Data21/CSV/dchilds2.csv").put(Body=str_buffer.getvalue())


