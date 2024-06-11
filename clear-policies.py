import boto3

# Create a client for IAM
iam_client = boto3.client("iam")

# Account ID
account_id = "735341528488"

# List of policies to delete
policy_names = [
    "defaultUser_defaultId_cluster1-k8s",
    "defaultUser_defaultId_cluster2-k8s",
    "defaultUser_defaultId_cluster3-k8s",
    "defaultUser_defaultId_cluster4-k8s",
    "defaultUser_defaultId_cluster5-k8s",
    "defaultUser_defaultId_cluster6-k8s",
    "defaultUser_defaultId_cluster7-k8s",
    "defaultUser_defaultId_cluster8-k8s",
    "defaultUser_defaultId_cluster9-k8s",
    "defaultUser_defaultId_cluster10-k8s",
]

# Iterate over the list of policy names and delete each one
for policy_name in policy_names:
    try:
        # Get the policy ARN
        policy_arn = f"arn:aws:iam::{account_id}:policy/{policy_name}"

        # Delete the policy
        iam_client.delete_policy(PolicyArn=policy_arn)
        print(f"Successfully deleted policy: {policy_name}")
    except Exception as e:
        print(f"Error deleting policy {policy_name}: {e}")
