
from . import ResourceBase


class Credential(ResourceBase):

    resource = 'credential'

    def find_parent(self, parent):
        filters = "parent='{}'".format(parent)
        creds = self.nuvla.search(self.resource, filter=filters, select="id")
        return creds.resources


class CredentialK8s(Credential):

    def create(self, ca, cert, key, infra_service_id, name, description=None):
        iscred_k8s = {
            "name": name,
            "description": description or name,
            "template": {
                "href": "credential-template/infrastructure-service-swarm",
                "parent": infra_service_id,
                "ca": ca,
                "cert": cert,
                "key": key
            }
        }
        return self.add(iscred_k8s)
