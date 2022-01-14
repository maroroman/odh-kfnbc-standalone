# ODH KFNBC Standalone

Deploy Kubeflow Notebook Controller in Openshift.

## Fetch KFNBC

Fetch KFNBC components from Kubeflow upstream:

```shell
$ git clone git@github.com:kubeflow/kubeflow.git kubeflow-components
$ cd kubeflow-components
$ git filter-repo --subdirectory-filter components
```

Prune everything but `notebook-controller` and `jupyter` components:

```
$ git filter-repo \
    --path common \
    --path notebook-controller \
    --path crud-web-apps/common \
    --path crud-web-apps/jupyter
$ rm -rf .git
```

## References

- https://github.com/kubeflow/kubeflow
