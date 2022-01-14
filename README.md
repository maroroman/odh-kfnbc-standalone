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

## Deploy controller manager

Install the `notebooks.kubeflow.org` CRD in your cluster:

```shell
$ cd kubeflow-components/notebook-controller
$ make install
$ oc get crd notebooks.kubeflow.org
NAME                     CREATED AT
notebooks.kubeflow.org   2022-01-14T11:15:14Z
```

Deploy the notebook controller manager:

```
$ make deploy
$ oc get pods -n opendatahub
NAME                                            READY   STATUS    RESTARTS   AGE
notebook-controller-deployment-cd65889c-9jpvb   1/1     Running   0          7s
```

## References

- https://github.com/kubeflow/kubeflow
