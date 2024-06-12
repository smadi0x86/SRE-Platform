# Common Issues

Please refer to the following troubleshooting steps if you encounter any issues while using the platform.

If you encounter an issue that is not listed here, please open an issue in the [original repository](https://github.com/ViktorUJ/cks).

## Issue 1

Getting an error message when running the `TASK=01 make run_cks_mock` command:

```bash
Error: S3 policy error (AccessDenied): Access Denied
Error: S3 policy action (s3:GetBucketPolicy) is not allowed
```

### Solution

- Go to the [AWS Management Console](https://console.aws.amazon.com/).
- Navigate to the [S3 service](https://s3.console.aws.amazon.com/s3/).
- Select the bucket that you created for the backend.
- Click on the **Permissions** tab.
- Uncheck the **Block all public access** option (This is not the best solution, it has security risks so proceed carefully!).
- Click on the **Bucket Policy** button.
- Add the following policy to the bucket policy editor:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetBucketPolicy",
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME"
    }
  ]
}
```

- Replace `YOUR_BUCKET_NAME` with the name of your bucket.
- Click on the **Save** button.
