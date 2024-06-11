# SRE Learning Platform

The **SRE Learning Platform** is an open-source project designed to help IT engineers prepare for the **CKA (Certified Kubernetes Administrator)**, **CKS (Certified Kubernetes Security Specialist)**, **CKAD (Certified Kubernetes Application Developer)**, and **LFCS (Linux Foundation Certified System Administrator)** exams. This platform provides hands-on labs, practice tests, and expert guidance to ensure certification success.

This repository is a fork of [ViktorUJ/cks](https://github.com/ViktorUJ/cks) and has been adjusted based on specific needs. For all details, refer to the original repository.

## Quick Start

To quickly get started, follow the instructions to run the platform via Docker:

[Run via Docker](docs/run_from_docker.MD)

[![Video Instruction](docs/images/run_via_docker.gif)](https://youtu.be/Xh6sWzafBmw "Run via Docker")

## Requirements

- [GNU Make](https://www.gnu.org/software/make/) >= 4.2.1
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) >= v1.6.6
- [Terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/install/) >= v0.54.8
- [jq](https://jqlang.github.io/jq/download/) >= 1.6
- [AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) + [Access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) with [Admin privilege for VPC, EC2, IAM, EKS](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html) > 2.2.30
- [AWS profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

Or you can [run via Docker](docs/run_from_docker.MD) ([video instruction](https://youtu.be/Xh6sWzafBmw)).

## Configuration

To configure the platform, change **backend_bucket** (and optionally **region** and **backend_region**) in [terraform/environments/terragrunt.hcl](terraform/environments/terragrunt.hcl#L4).

## Commands

Run all commands from the project's root directory. For detailed command instructions and usage scenarios, refer to the original repository's [README](https://github.com/ViktorUJ/cks).

## License and Usage Agreement

- [Apache License 2.0](LICENSE)

## Contribution

If you want to contribute, please refer to the [original repository](https://github.com/ViktorUJ/cks).

## Contacts

If you encounter any issues or have questions about the project, you can reach out via email [viktoruj@gmail.com](mailto:viktoruj@gmail.com).
