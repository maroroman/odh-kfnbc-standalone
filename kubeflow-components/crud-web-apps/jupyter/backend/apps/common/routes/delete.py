from . import config_app

if not config_app.TESTING_MODE:
    from kubeflow.kubeflow.crud_backend import api, logging
    log = logging.getLogger(__name__)
else:
    log = config_app.Logger

from . import bp


@bp.route(
    "/api/namespaces/<namespace>/notebooks/<notebook>", methods=["DELETE"]
)
def delete_notebook(notebook, namespace):
    log.info("Deleting Notebook '%s/%s'" % (namespace, notebook))
    api.delete_notebook(notebook, namespace)

    return api.success_response(
        "message", "Notebook %s successfully deleted." % notebook
    )
