# Examples of usage of nuvla-api Python package

The Python scripts in this directory use `nuvla-api` package. To install this
package run:

```
pip3 install nuvla-api
```

The code in the scripts is well documented. Please refer to the scripts for
details.

# Prerequisites

To start using the library, you need to import `nuvla.api.Api` module. This
module acts as a lower level API client to Nuvla. The default endpoint is
`https://nuvla.io`:

```
from nuvla.api import Api as Nuvla

# Create Nuvla client. By default `https://nuvla.io` endpoint is used.
nuvla = Nuvla()
```

In case of using different Nuvla instance provide `endpoint=https://<host|IP>`,
and if self-signed TLS certificate is used, provide `insecure=True`.

```
from nuvla.api import Api as Nuvla

nuvla = Nuvla(endpoint='https://nuvla.local', insecure=True)
```

# Notes

To see the dump of the HTTP communication between the client and the Nuvla
server provide `debug=True` when initializing the Nuvla low-level API client.

```python
nuvla = Nuvla(debug=True)
```

This can be very handy when you want to see the HTTP operations used on
different resources, and the structure of the Nuvla resource documents being
created on the server or retrieved from it.

# Create User

[user-create.py](user-create.py)

User creation doesn't require login to Nuvla. The script can be run as follows:

```
$ ./user-create.py
New user created: user/b8762055-4dec-4724-a65d-65b006d694ae
Follow instructions in validation email that was sent to konstan+new@sixsq.com.
$
```

To confirm the signup to the service, the user now has to validate it by
clicking on the validation link in the email. Note: Nuvla instance must have
been configured with SMPT server.

# User login and logout

[user-loginout.py](user-loginout.py) shows how to login and logout a user. As a
result of login operation a session is returned.

```
$ ./user-loginout.py
session/228cb944-821f-4123-8100-bfcedd6d7200
$
```

# Create Infrastructure Service Group

Before starting provisioning containers using Nuvla, endpoints and credentials
of Container Orchestration Engines (Docker Swarm and Kubernetes) must be added
to Nuvla as infrastructure services (IS). To facilitate the management of the
infrastructure services they can be grouped into infrastructure service groups.
In the case of the grouping, the group becomes parent of infrastructure
services.

Nuvla allows defining private Docker Registries with their corresponding
credentials to facilitate deployment of containers from the images coming from 
private registries. It's a good practice to define infrastructure service group
for the registry as well.

[create-infra-service-group.py](create-infra-service-group.py) shows how to
create infrastructure service group.

```
$ ./create-infra-service-group.py
infra service group: infrastructure-service-group/19ce4191-da42-4831-9903-ef056b7d4d4f
infra service registry group: infrastructure-service-group/3a88ced8-0ab2-46d4-bfe1-95c235e77af6
$
```

# Create Infrastructure Service

Different types of infrastructure services can be added to Nuvla: Docker
Swarm, Kubernetes, S3, Docker Registry.

Infrastructure services set infrastructure service group ID as their parent to
indicate they are part of the same group. Knowing infrastructure service group
ID one can discover services that belong to the same "site" and hence, are
logically grouped. This promotes discovery. For example, if one knows
infrastructure service ID of data endpoint - S3, it's possible to discover the
corresponding Kubernetes or Docker swarm ones, and visa versa. This mechanism
for example can be used in scheduling of data processing related tasks.

[create-infra-service.py](create-infra-service.py) shows how infrastructure
services can be created and added to a group (only one group is possible).
Please take the IDs of the groups created in the previous step and change group
IDs defined in the script.

```
$ ./create-infra-service.py
Kubernetes: infrastructure-service/13b419c0-c50a-4f97-826f-8eae16f68f64
S3: infrastructure-service/6d0b48c4-2608-46f4-9734-6a7e5a2135d8
Docker registry: infrastructure-service/19e1c37b-8bdc-43b8-8dab-eb378ac61e1f
$
```

# Create Infrastructure Service Credential

To access any of the infrastructure services users need credentials.

[create-infra-service-cred.py](create-infra-service-cred.py) shows how to create
such credentials on the example of Kubernetes, S3 and Docker Registry
infrastructure services. To express the relationship, credential defines an IS
as its parent (only one parent is possible).

```
$ ./create-infra-service-cred.py
Kubernetes creds:  credential/e5cffc7c-bc69-41a5-8881-7fc1dd0ec552
S3 creds:  credential/2c6b463e-9039-46c0-8dca-1697065e9754
Docker Registry creds:  credential/0bfc1e15-3e52-4b17-bdf0-c55fc3d74090
$
```

# Create Application

Internally Nuvla uses concept of a module, and structures user defined projects
and applications using the modules. There are following module types: project,
component, application. 

[create-app.py](create-app.py) first creates a module of type project and then
creates an application of subtype kubernetes inside of the project.

```
$ ./create-app.py
module/92614bdc-4afa-49e1-891f-0eb3a4db0635
```

# Create data records

Data records is on of the two data types in Nuvla. It is designed to hold
location of the data and its description - meta-data. It's a document with a
number of requered root level fields with all the rest being free schema for the
user to define prefixed with <user prefix>:.

```
$ ./create-data-record.py
data-record/93344bdc-4afa-49e1-891f-0eb3a4db0886
```

# Create data object

```
$ ./create-data-object.py
data-object/72614bdc-4afa-49e1-891f-0eb3a4db0634
```

# Search for data records/objects

```
$ ./search-data.py
data-record/93344bdc-4afa-49e1-891f-0eb3a4db0886
```

# Bulk delete data records/objects

```
$ ./bulk-delete-data.py
deleted: data-record/93344bdc-4afa-49e1-891f-0eb3a4db0886
deleted: data-record/93344bdc-4afa-49e1-891f-0eb3a4db0886
```

# Create data set

```
$ ./create-data-set.py
data-set/98744bdc-4afa-49e1-891f-0eb3a4db0ea7
```

# Deploy Application

```
$ ./deploy-app.py
deployment/ec344bdc-4afa-49e1-891f-0eb3a4db0971
```

# Get Application logs

```
$ ./app-logs.py
...
```