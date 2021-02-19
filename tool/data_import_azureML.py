from azureml.core import Workspace, Dataset, Datastore
import tempfile
def dataset_to_cluster(name):

    subscription_id = 'd665bfa1-de16-487d-9b6a-fd94daf68293'
    resource_group = 'rg-ovam-poc'
    workspace_name = 'OVAM'
    
    workspace = Workspace(subscription_id, resource_group, workspace_name)
    dataset = Dataset.get_by_name(workspace, name=name)
    #streams data, use this mounted path to reference it
    mounted_path = tempfile.mkdtemp()
    # mount dataset onto the mounted_path of a Linux-based compute
    mount_context = dataset.mount(mounted_path)
    mount_context.start()
    return mounted_path