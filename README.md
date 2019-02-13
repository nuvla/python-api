# SlipStreamPythonAPI

Python client for the SlipStream CIMI API.

## Installation

  `$ pip install nuvla-api`

  or

  `$ yum install nuvla-python-api`

## Usage

```python
  from nuvla.api import Api
  
  api = Api('https://nuv.la')
  
  # Login with username & password
  api.login_internal('username', 'password')
  # or
  # Login with api-key & secret
  api.login_apikey('credential/uuid', 'secret')

  api.search('user')

  # Logout
  api.logout()
  ```

## Contribute

### Development helper

```sh
git clone https://github.com/nuvla/python-api.git
cd SlipStreamPythonAPI/api/
pip install --editable .
```

### Push version to pypi

Configure `~/.pypirc` with pypi repo credentials. This file should look
like as following:

```
[distutils]
index-servers=pypi

[pypi]
username = <username>
password = <password>
```

From repo root directory, launch following commands:
```sh
git checkout <release-version>
mvn clean install -P release
```

## Documentation
### Simple docstring based documentation
You can get the full documentation by typing:

_Python shell/code_
```python
from nuvla.api import Api
help(Api)
```
_Shell_
```sh
pydoc nuvla.api.Api
```

Or for a specific function:

_Python shell/code_
```python
from nuvla.api import Api
help(Api.search)
```
_Shell_
```sh
pydoc nuvla.api.Api.cimi_search
```

Or to get only the docstring:

_Python shell/code_
```python
from nuvla.api import Api
print Api.search.__doc__
```

Currently there is no HTML version of the documentation, only
docstring inside the code but the documentation can be generated by
the user.

To run a local webserver with the documentation you can run:
```shell
pydoc -p 8080 slipstream.api.Api
```
and then
[http://localhost/nuvla.api.api.html#Api](http://localhost/nuvla.api.api.html#Api)

### Sphinx documentation

There is a Sphinx documentation available at
http://nuvla.github.io/NuvlaPythonAPI

#### Generate and publish the Sphinx documentation to GitHub Pages

You can use the provided makefile (in the `doc` directory or in the
root directory):

```shell
make gh-pages
```

## Copyright

Copyright &copy; 2019, SixSq Sàrl

## License

Licensed under the Apache License, Version 2.0 (the "License"); you
may not use this file except in compliance with the License.  You may
obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.  See the License for the specific language governing
permissions and limitations under the License.
