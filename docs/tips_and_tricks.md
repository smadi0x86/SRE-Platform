## Vim

When you take the CKA/CKS/CKAD exams, you need to edit, create, or delete resources in the Kubernetes cluster.

The Vim editor is used by default, which means you should be aware of how to use shortcuts.

More information about Vim can be found [here](https://www.vim.org/).

## Shortcuts

`G` # go to end of file
`gg` # first line of file
`Shift + A` # go to the end of the current row (insert mode)
`Shift + C` # delete everything after the cursor (insert mode)
`Shift + I` # go to the first letter on the current row (insert mode)
`/Pod` # find any instances of 'Pod' in the file
`e` # jump to the end of the next word
`w` # jump to the start of the next word
`:25` # go to the 25th row in the file
`Shift + V` # select the current row
`Shift + V` `Shift + G` # select everything from the current row to the end of the file
`100 dd` # delete 100 rows
`ggVG` # select everything in the file

## Aliases

To make your life easier, you can create aliases for the `kubectl` command.

```bash
export do="--dry-run=client -o yaml"
```

## Usage to create pod template

To create a pod template, use the following command:

```bash
k run test --image nginx $do
```
