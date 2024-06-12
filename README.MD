# SRE Learning Platform

The **SRE Learning Platform** is an open-source project designed to help IT engineers prepare for the **CKA (Certified Kubernetes Administrator)**, **CKS (Certified Kubernetes Security Specialist)**, **CKAD (Certified Kubernetes Application Developer)**, and **LFCS (Linux Foundation Certified System Administrator)** exams.

This platform provides hands-on labs, practice tests, and expert guidance to ensure certification success.

Also, the platform can be used for educational purposes, workshops, and training sessions. It is a great tool for learning EKS and prepare for HR interviews.

> [!Important]
> This repository is a fork of [ViktorUJ/cks](https://github.com/ViktorUJ/cks) and has been adjusted based on specific needs. For all details, refer to the original repository.

## Quick Start

To quickly get started with the SRE Learning Platform, follow these steps:

1. [Run the Platform via Docker](docs/run_from_docker.md)
2. [Set Up Multiple Users or Environments](docs/multiple_users_envs.md)
3. [Explore Labs](docs/labs.md)
4. [View Helpful Links](docs/links.md)
5. [Check Tips and Tricks](docs/tips_and_tricks.md)

For a visual guide, watch the [video instructions](https://youtu.be/Xh6sWzafBmw).

## Requirements

Before you begin, ensure you have the following installed:

- [GNU Make](https://www.gnu.org/software/make/) >= 4.2.1
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) >= v1.6.6
- [Terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/install/) >= v0.54.8
- [jq](https://jqlang.github.io/jq/download/) >= 1.6
- [AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) + [Access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) with [Admin privilege for VPC, EC2, IAM, EKS](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html) > 2.2.30
- [AWS profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## Configuration

To configure the platform, modify the **backend_bucket** (and optionally **region** and **backend_region**) in [terraform/environments/terragrunt.hcl](terraform/environments/terragrunt.hcl#L4).

## Common Issues

If you encounter any issues while using the platform, refer to the [Common Issues](docs/common_issues.md) document for troubleshooting steps.

## Commands

Run all commands from the project's root directory. For detailed command instructions and usage scenarios, refer to the original repository's [README](https://github.com/ViktorUJ/cks).

## Documentation

For more detailed information on using the platform, refer to the following documents:

- [Labs](docs/labs.md)
- [Links](docs/links.md)
- [Multiple Users Environments](docs/multiple_users_envs.md)
- [Run from Docker](docs/run_from_docker.md)
- [Tips and Tricks](docs/tips_and_tricks.md)

## License and Usage Agreement

- [Apache License 2.0](LICENSE)

## Contribution

If you want to contribute, please refer to the [original repository](https://github.com/ViktorUJ/cks).

## Contacts

If you encounter any issues or have questions about the project, you can reach out via email: [viktoruj@gmail.com](mailto:viktoruj@gmail.com).
