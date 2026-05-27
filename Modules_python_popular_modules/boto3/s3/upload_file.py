import boto3

s3 = boto3.client('s3')

s3.upload_file(
    'report.csv',
    'my-bucket',
    'reports/report.csv'
)

print("Uploaded")
