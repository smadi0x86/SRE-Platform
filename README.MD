# Welcome to the SRE Learning Platform

The **SRE Learning Platform** is an open-source hub designed to help IT engineers effectively prepare for the **CKA (Certified Kubernetes Administrator)**, **CKS (Certified Kubernetes Security Specialist)**, and **CKAD (Certified Kubernetes Application Developer)** exams. This platform also offers invaluable hands-on experience with **AWS EKS (Elastic Kubernetes Service)**, equipping users with practical insights for real-world applications. Whether you're aiming to validate your skills, boost your career prospects in Kubernetes administration, security, application development, or delve into AWS EKS, this platform provides hands-on labs, practice tests, and expert guidance to ensure certification success.

- Prepare for the **CKA**: [Certified Kubernetes Administrator Exam](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- Enhance your skills for the **CKS**: [Certified Kubernetes Security Specialist Exam](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/)
- Excel in the **CKAD**: [Certified Kubernetes Application Developer Exam](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/)

Master Kubernetes concepts, gain practical experience, and excel in the CKA, CKS, and CKAD exams with the **SRE Learning Platform**.

## Quick Start
To quickly get started, follow the instructions to run the platform via Docker:

[Run via Docker](docs/run_from_docker.MD)

[![Video Instruction](docs/images/run_via_docker.gif)](https://youtu.be/Xh6sWzafBmw "Run via Docker")

<details>
  <summary><strong>Requirements</strong></summary>

- [GNU Make](https://www.gnu.org/software/make/) >= 4.2.1
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) >= v1.6.6
- [Terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/install/) >= v0.54.8
- [jq](https://jqlang.github.io/jq/download/) >= 1.6
- [AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) + [Access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) (or [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)) with [Admin privilege for VPC, EC2, IAM, EKS](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html) > 2.2.30
- [AWS profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

Or you can [run via Docker](docs/run_from_docker.MD) ([video instruction](https://youtu.be/Xh6sWzafBmw))

</details>

<details>
  <summary><strong>Repository Structure</strong></summary>

The repository is organized into the following sections:

- **[Makefile](Makefile)** - Contains scenarios for launching hands-on labs and mock exams.
- **[tasks](tasks)** - Contains lab scenarios and mock exam scripts.
  - **[cka](tasks/cka)** - Everything related to CKA.
    - **[labs](tasks/cka/labs)** - Hands-on labs for the CKA exam.
    - **[mock](tasks/cka/mock)** - Mock scripts for the CKA exam.
  - **[cks](tasks/cks)** - Everything related to CKS.
    - **[labs](tasks/cks/labs)** - Hands-on labs for the CKS exam.
    - **[mock](tasks/cks/mock)** - Mock scripts for the CKS exam.
- **[terraform](terraform)** - Contains modules and Terraform environments.
  - **[environments](terraform/environments)** - Terragrunt (Terraform) environments.
  - **[modules](terraform/modules)** - Terraform modules.

</details>

<details>
  <summary><strong>About CKA, CKS, CKAD Scenarios</strong></summary>

- The platform uses **AWS** to create the following resources: **VPC**, **subnets**, **security groups**, **EC2** (spot), **S3**.
- After launching the scenarios, the platform will create all necessary resources and provide access to Kubernetes clusters.
- To create clusters, the platform uses **kubeadm**.
- You can easily add your own scenario using the existing Terraform module [k8s_self_management](terraform/modules/k8s_self_management).
- The [k8s_self_management](terraform/modules/k8s_self_management) module supports versions:
````
k8s version  : [ 1.21 , 1.29 ]   https://kubernetes.io/releases/
Rintime :
    docker                   [1.21 , 1.23]
    cri-o                    [1.21 , 1.29]
    containerd               [1.21 , 1.29]   # cks, cka  default 1.29
    containerd_gvizor        [1.21 , 1.29]
OS for nodes  :
   ubuntu  :  20.04 LTS  ,  22.04 LTS   # cks default  20.04 LTS
CNI :  calico
````

</details>

## Configuration
To configure the platform, change **backend_bucket** (and optionally **region** and **backend_region**) in [terraform/environments/terragrunt.hcl](terraform/environments/terragrunt.hcl#L4).

## Commands
Run all commands from the project's root directory.

<details>
<summary><strong>CMDB</strong></summary>

- `make cmdb_get_env_all` - Get a list of all resources in CMDB.
- `USER_ID='myuser' ENV_ID='01' make cmdb_get_user_env_data` - Show all created resources of user **myuser** in environment **01**.
- `USER_ID='myuser' ENV_ID='01' make cmdb_get_user_env_lock` - Show all lock resources of user **myuser** in environment **01**.
- `USER_ID='myuser' make cmdb_get_user_env_lock` - Show all lock resources of user **myuser** in **all** environments.
- `USER_ID='myuser' make cmdb_get_user_env_data` - Show all data resources of user **myuser** in **all** environments.
- `CMDB_ITEM='CMDB_data_myuser_02_k8s_cluster1' make cmdb_get_item` - Get detailed information about **CMDB_data_myuser_02_k8s_cluster1** resource.

</details>

<details>
<summary><strong>CKA</strong></summary>

### CKA Task
- `TASK=01 make run_cka_task` - Create CKA [hands-on lab](docs/labs.MD#cka-labs) number 01.
- `TASK=01 make delete_cka_task` - Delete CKA hands-on lab.
- `TASK=01 make run_cka_task_clean` - Run CKA task with clean Terragrunt cache.
- `make output_cka_task` - Show **outputs** from **cka_task**.

### CKA Mock
- `TASK=01 make run_cka_mock` - Create mock CKA exam [number 01](tasks/cka/mock/01).
- `make delete_cka_mock` - Delete mock CKA exam.
- `TASK=01 make run_cka_mock_clean` - Create mock CKA exam [number 01](tasks/cka/mock/01) with clean Terragrunt cache.
- `make output_cka_mock` - Show **outputs** from **cka_mock**.

</details>

<details>
<summary><strong>CKAD</strong></summary>

### CKAD Mock
- `TASK=01 make run_ckad_mock` - Create mock CKAD exam [number 01](tasks/ckad/mock/01).
- `make delete_ckad_mock` - Delete mock CKAD exam.
- `TASK=01 make run_ckad_mock_clean` - Create mock CKAD exam [number 01](tasks/ckad/mock/01) with clean Terragrunt cache.
- `make output_ckad_mock` - Show **outputs** from **ckad_mock**.

</details>

<details>
<summary><strong>CKS</strong></summary>

### CKS Task
- `TASK=10 make run_cks_task` - Create CKS [hands-on lab](docs/labs.MD#cks-labs) number 10.
- `TASK=10 make delete_cks_task` - Delete CKS hands-on lab.
- `TASK=10 make run_cks_task_clean` - Run CKS task with clean Terragrunt cache.
- `make output_cks_task` - Show **outputs** from **cks_task**.

### CKS Mock
- `TASK=01 make run_cks_mock` - Create mock CKS exam [number 01](tasks/cks/mock/01).
- `make delete_cks_mock` - Delete mock CKS exam.
- `TASK=01 make run_cks_mock_clean` - Create mock CKS exam [number 01](tasks/cks/mock/01) with clean Terragrunt cache.
- `make output_cks_mock` - Show **outputs** from **cks_mock**.

</details>

<details>
<summary><strong>HR</strong></summary>

### HR Mock
- `TASK=01 make run_hr_mock` - Create mock HR exam [number 01](tasks/hr/mock/01).
- `make delete_hr_mock` - Delete mock HR exam.
- `TASK=01 make run_hr_mock_clean` - Create mock HR exam [number 01](tasks/hr/mock/01) with clean Terragrunt cache.
- `make output_hr_mock` - Show **outputs** from **hr_mock**.

</details>

<details>
<summary><strong>EKS</strong></summary>

### EKS Task
- `TASK={lab_number} make run_eks_task` - Create hands-on lab.
- `make delete_eks_task` - Delete EKS lab cluster.

</details>

<details>
<summary><strong>DEV</strong></summary>

- `make lint` - Run linter on the project.

</details>

## Usage Scenarios

<details>
<summary><strong>CKA Hands-On Lab</strong></summary>

- Choose [a hands-on lab](docs/labs.MD#cka-labs) number.
- Create CKA lab cluster: `TASK={lab_number} make run_cka_task`.
- Find {master_external_ip} in Terraform output.
- Log in to master node via SSH: `ssh ubuntu@{master_external_ip} -i {key}`.
- Check init logs: `tail -f /var/log/cloud-init-output.log`.
- Read lab descriptions in `{lab_number}/README.MD`.
- Check solution in `{lab_number}/SOLUTION.MD`.
- Delete CKA lab cluster: `make delete_cka_task`.
- Clean CKA lab cluster `.terraform` folder: `make clean_cka_task`.

</details>

<details>
<summary><strong>Mock CKA Exam</strong></summary>

[Video instruction for launching **CKA mock exam**](https://www.youtube.com/watch?v=P-YYX4CTWIg)

- Choose [a mock exam](tasks/cka/mock) number.
- Change instance type from `spot` to `ondemand` in `{mock_number}/env.hcl` if needed.
- Create mock CKA exam: `TASK={mock_number} make run_cka_mock`.
- Find `worker_pc_ip` in Terraform output.
- Connect to `worker_pc_ip` with your SSH key and user `ubuntu`.
- Open questions list `{mock_number}/README.MD` and do tasks.
- Use `ssh {kubernetes_nodename}` from work pc to connect to node.
- Run `time_left` on work pc to check time.
- Run `check_result` on work pc to check result.
- Delete mock CKA exam: `make delete_cka_mock`.
- Find exam solutions in `{mock_number}/worker/files/solutions` and [video](https://youtu.be/IZsqAPpbBxM) for [mock 01](tasks/cka/mock/01).
- Find exam tests in `{mock_number}/worker/files/tests.bats`.

</details>

<details>
<summary><strong>CKS Hands-On Lab</strong></summary>

- Choose [CKS lab](docs/labs.MD#cks-labs) number.
- Change **ami_id** in `{lab_number}/scripts/terragrunt.hcl` if you changed **region**.
- Create CKS lab cluster: `TASK={lab_number} make run_cks_task`.
- Find {master_external_ip} in Terraform output.
- Log in to master node via SSH: `ssh ubuntu@{master_external_ip} -i {key}`.
- Check init logs: `tail -f /var/log/cloud-init-output.log`.
- Read lab descriptions in `{lab_number}/README.MD`.
- Check solution in `{lab_number}/SOLUTION.MD`.
- Delete CKS lab cluster: `make delete_cks_task`.
- Clean CKS lab cluster `.terraform` folder: `make clean_cks_task`.

</details>

<details>
<summary><strong>Mock CKS Exam</strong></summary>

[Video instruction for launching **CKS mock exam**](https://youtu.be/_GbsBOMaJ9Q)

- Choose [a mock exam](tasks/cks/mock) number.
- Change **ubuntu_version** in `{mock_number}/env.hcl` if needed.
- Change instance type from `spot` to `ondemand` in `{mock_number}/env.hcl` if needed.
- Create mock CKS exam: `TASK={mock_number} make run_cks_mock` or `TASK={mock_number} make run_cks_mock_clean` if you'd like to run with **clean** Terragrunt cache.
- Find `worker_pc_ip` in Terraform output.
- Connect to `worker_pc_ip` with your SSH key and user `ubuntu`.
- Open questions list `{mock_number}/README.MD` and do tasks.
- Use `ssh {kubernetes_nodename}` from work pc to connect to node.
- Run `time_left` on work pc to check time.
- Run `check_result` on work pc to check result.
- Delete mock CKS exam: `make delete_cks_mock`.
- Find exam solutions in `{mock_number}/worker/files/solutions` and [video](https://youtu.be/I8CPwcGbrG8) for [mock 1](tasks/cks/mock/01).
- Find exam tests in `{mock_number}/worker/files/tests.bats`.

</details>

<details>
<summary><strong>Mock CKAD Exam</strong></summary>

[Video instruction for launching **CKAD mock exam**](https://youtu.be/7X4Y9QhbTsk)

- Choose [a mock exam](tasks/ckad/mock) number.
- Change **ubuntu_version** in `{mock_number}/env.hcl` if needed.
- Change instance type from `spot` to `ondemand` in `{mock_number}/env.hcl` if needed.
- Create mock CKAD exam: `TASK={mock_number} make run_ckad_mock` or `TASK={mock_number} make run_ckad_mock_clean` if you'd like to run with **clean** Terragrunt cache.
- Find `worker_pc_ip` in Terraform output.
- Connect to `worker_pc_ip` with your SSH key and user `ubuntu`.
- Open questions list `{mock_number}/README.MD` and do tasks.
- Use `ssh {kubernetes_nodename}` from work pc to connect to node.
- Run `time_left` on work pc to check time.
- Run `check_result` on work pc to check result.
- Delete mock CKAD exam: `make delete_ckad_mock`.
- Find exam solutions in `{mock_number}/worker/files/solutions` and [video](https://youtu.be/yQK7Ca8d-yw) for [mock 1](tasks/ckad/mock/01).
- Find exam tests in `{mock_number}/worker/files/tests.bats`.

</details>

<details>
<summary><strong>Mock HR Exam</strong></summary>

[Video instruction for launching **HR mock exam**](https://youtu.be/4CTC1jl8lxE)

- Choose [a mock exam](tasks/hr/mock) number.
- Change **ubuntu_version** in `{mock_number}/env.hcl` if needed.
- Change instance type from `spot` to `ondemand` in `{mock_number}/env.hcl` if needed.
- Create mock HR exam: `TASK={mock_number} make run_hr_mock` or `TASK={mock_number} make run_hr_mock_clean` if you'd like to run with **clean** Terragrunt cache.
- Find `worker_pc_ip` in Terraform output.
- Connect to `worker_pc_ip` with your SSH key and user `ubuntu`.
- Open questions list `{mock_number}/README.MD` and do tasks.
- Use `ssh {kubernetes_nodename}` from work pc to connect to node.
- Run `time_left` on work pc to check time.
- Run `check_result` on work pc to check result.
- Delete mock HR exam: `make delete_hr_mock`.
- Find exam solutions in `{mock_number}/worker/files/solutions` and [video](https://youtu.be/4CTC1jl8lxE) for [mock 1](tasks/hr/mock/01).
- Find exam tests in `{mock_number}/worker/files/tests.bats`.

</details>

<details>
<summary><strong>EKS Hands-On Lab</strong></summary>

- Choose [labs](docs/labs.MD#eks-labs) number.
- Create hands-on lab: `TASK={lab_number} make run_eks_task`.
- Find `worker_pc_ip` in Terraform output.
- Log in to worker pc node via SSH: `ssh ubuntu@{worker_pc_ip} -i {key}`.
- Read lab descriptions in `{lab_number}/README.MD`.
- Check solution in `{lab_number}/SOLUTION.MD`.
- Delete EKS lab cluster: `make delete_eks_task`.

</details>

## [Simultaneous Work with Independent Environments](docs/multiple_users_envs.MD)

## [Useful Links](docs/links.MD)

## [Tips and Tricks](docs/tips_and_tricks.MD)

## [CHANGELOG](CHANGELOG/CHANGELOG.MD)

## [Code of Conduct](docs/CODE_OF_CONDUCT.md)

## Contribution
If you want to be part of the project development team, get in touch with [us](https://github.com/ViktorUJ/cks/tree/master#contacts). We are always happy to welcome new members to our development team.

If you want to say **thank you** or support the active development of the **SRE Learning Platform project**:
- [Star](https://github.com/ViktorUJ/cks) the **SRE Learning Platform project** on GitHub.
- Feel free to write articles about the project on [dev.to](https://dev.to/), [Medium](https://medium.com/), [Hackernoon](https://hackernoon.com) or on your personal blog and share your experiences.

## License and Usage Agreement
- [Apache License 2.0](LICENSE)

## Channels for Cooperative Preparation
- [CKA](https://t.me/sre_platform_cka)
- [CKS](https://t.me/sre_platform_cks)
- [CKAD](https://t.me/sre_platform_ckad)

## Contacts

If you encounter any issues or have questions about the project, you can reach out to:

[![Email](https://badgen.net/badge/icon/email?icon=email&label)](mailto:viktoruj@gmail.com) [![Telegram](https://badgen.net/badge/icon/telegram?icon=telegram&label)](https://t.me/viktor_uj) [![LinkedIn](https://badgen.net/badge/icon/linkedin?icon=linkedin&label)](https://www.linkedin.com/in/viktar-mikalayeu-mns)
