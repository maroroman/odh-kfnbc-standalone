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

```shell
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

```shell
$ make deploy
```

Verify that notebook controller manager pod is running:

```shell
$ oc get pods -l app=notebook-controller -n opendatahub
NAME                                            READY   STATUS    RESTARTS   AGE
notebook-controller-deployment-cd65889c-9jpvb   1/1     Running   0          7s
```

## Deploy JWA (Jupyter Web App)

Deploy the Jupyter web app with the `Openshift` overlay:

```shell
$ cd kubeflow-components/crud-web-apps/jupyter
$ kustomize build manifests/overlays/openshift | oc apply -f -
```

Verify that Jupyter web app pods are running, and the route is accessible:

```shell
$ oc get pods -l app=jupyter-web-app -n opendatahub
NAME                                          READY   STATUS    RESTARTS   AGE
jupyter-web-app-deployment-54b74f4b8b-2hkwp   2/2     Running   0          76s
jupyter-web-app-deployment-54b74f4b8b-6k7lw   2/2     Running   0          102s
jupyter-web-app-deployment-54b74f4b8b-ds8fq   2/2     Running   0          87s

$ oc get route jupyter -n opendatahub
NAME      HOST/PORT
jupyter   jupyter-opendatahub.apps.user.dev.datahub.redhat.com
```

## Spawn a Notebook

Set up the `kubeflow-user` namespace to allow the operator to instantiate
notebooks in it:

```shell
$ oc apply -f notebooks/namespace -n kubeflow-user
```

Allow the `openldap-user1` user to create notebooks in the `kubeflow-user`
namespace:

```shell
$ oc apply -f notebooks/users/openldap-user1.yaml -n kubeflow-user
```

Log in into the Jupyter web app interface and create a new notebook with that
user:

![SciPy Notebook](assets/jwa-jupyter-scipy.png)

## References

- https://github.com/kubeflow/kubeflow
