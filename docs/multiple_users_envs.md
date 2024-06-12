# Why is it Needed?

### Creating independent environments is essential for:

- **Multiple Identical Environments**: Perfect for groups of students working in parallel.
- **Diverse Task Environments**: Allows one student to work on different tasks in separate environments.

To set up an independent environment, define the `USER_ID` and `ENV_ID` variables before running the make command.

### Example Usage:

- Create an Environment: `USER_ID='myuser' ENV_ID='3' TASK=01 make run_ckad_mock`

  - Creates environment **3** for user **myuser** with task set **01** CKAD mock.

- Delete an Environment: `USER_ID='myuser' ENV_ID='3' TASK=01 make delete_ckad_mock`
  - Deletes environment **3** for user **myuser** with task set **01** CKAD mock.

[Watch the Example Usage Video](https://youtu.be/3H0RMLXGmgg)

## CMDB Commands

- Get a list of all resources in CMDB: `make cmdb_get_env_all`
- Show all created resources of a user in a specific environment: `USER_ID='myuser' ENV_ID='01' make cmdb_get_user_env_data`
- Show all lock resources of a user in a specific environment: `USER_ID='myuser' ENV_ID='01' make cmdb_get_user_env_lock`
- Show all lock resources of a user in all environments: `USER_ID='myuser' make cmdb_get_user_env_lock`
- Show all data resources of a user in all environments: `USER_ID='myuser' make cmdb_get_user_env_data`
- Get detailed information about a specific resource: `CMDB_ITEM='CMDB_data_myuser_01_k8s_cluster1' make cmdb_get_item`
