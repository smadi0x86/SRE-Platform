# Why is it Needed?

- **Create Multiple Identical Independent Environments**: Ideal for a group of students.
- **Create Several Independent Environments for One Student**: Allows different tasks for each environment.

To create an independent environment, set the additional variables `USER_ID='myuser'` and `ENV_ID='01'` before running the make command.

[Example](https://youtu.be/3H0RMLXGmgg):

- `USER_ID='myuser' ENV_ID='3' TASK=01 make run_ckad_mock` - Create environment **3** for user **myuser** with task set **01** CKAD mock.
- `USER_ID='myuser' ENV_ID='3' TASK=01 make delete_ckad_mock` - Delete environment **3** for user **myuser** with task set **01** CKAD mock.

## CMDB Commands

- `make cmdb_get_env_all` - Get a list of all resources in CMDB.
- `USER_ID='myuser' ENV_ID='01' make cmdb_get_user_env_data` - Show all created resources of user **myuser** in environment **01**.
- `USER_ID='myuser' ENV_ID='01' make cmdb_get_user_env_lock` - Show all lock resources of user **myuser** in environment **01**.
- `USER_ID='myuser' make cmdb_get_user_env_lock` - Show all lock resources of user **myuser** in **all** environments.
- `USER_ID='myuser' make cmdb_get_user_env_data` - Show all data resources of user **myuser** in **all** environments.
- `CMDB_ITEM='CMDB_data_myuser_01_k8s_cluster1' make cmdb_get_item` - Get detailed information about **CMDB_data_myuser_01_k8s_cluster1** resource.
