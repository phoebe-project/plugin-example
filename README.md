# plugin-example
example template of a phoebe2 alternate-backend plugin

**NOTE**: plugin-support in phoebe2 is currently a work-in-progress and so this format may change before it is officially supported and released.

Things to do when creating a plugin:
* start from this template
* replace the code in `pluginexample/compute.py` and `pluginexample/backends.py`
* update the `_supported_phoebe_versions` list in `<pluginexample>/__init__.py`
* rename the `pluginexample` directory to name of your desired plugin module
* update the `name` variable in `setup.py` to the name of your desired plugin module
* update this README with usage instructions
