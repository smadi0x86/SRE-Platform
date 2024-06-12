# Run Platform via Docker

We have prepared a Docker image with all necessary dependencies and utilities. You can use it to run exams or labs by following the instructions below or follow the [video guide](https://youtu.be/Xh6sWzafBmw).

# Run the Docker Container

```bash
sudo docker run -it viktoruj/runner
```

# Clone the Git Repository

```
git clone https://github.com/smadi0x86/SRE-Platform
cd SRE-Platform
```

# Update S3 Bucket

By now, you should have created an S3 bucket for the Terraform backend. If you haven't, please refer to the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) to create one.

> [!Warning]
> Make sure to enable bucket versioning when creating the S3 bucket.

## Edit the terragrunt.hcl file to update your S3 bucket name

```bash
vim terraform/environments/terragrunt.hcl
```

```hcl
locals {
region = "eu-north-1"
backend_region = "eu-north-1"
backend_bucket = "sre-learning-platform-state-backet" # update to your own bucket name
backend_dynamodb_table = "${local.backend_bucket}-lock"
}
```

# Set the AWS Key

```bash
export AWS_ACCESS_KEY_ID=Your_Access_Key
export AWS_SECRET_ACCESS_KEY=Your_Secred_Access_Key
```

# Run Your Scenario

## For single environment

Move to the root directory of the project and run the following command:

```bash
TASK=01 make run_cks_mock
```

## For multiple users or multiple environments

Move to the root directory of the project and run the following command:

```bash
USER_ID='user1' ENV_ID='01' TASK=01 make run_cks_mock
```

# Delete Your Scenario

## For single environment

Move to the root directory of the project and run the following command:

```bash
TASK=01 make delete_cks_mock
```

## For multiple users or multiple environments

Move to the root directory of the project and run the following command:

```bash
USER_ID='user1' ENV_ID='01' TASK=01 make delete_cks_mock
```
