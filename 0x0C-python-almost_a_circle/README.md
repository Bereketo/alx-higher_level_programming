# Python - Almost a circle

# Tests :heavy_check_mark:

* [tests/test_models](./tests/test_models): Folder containing the following independently-developed test files:
  * [test_base.py](./tests/test_models/test_base.py)
  * [test_rectangle.py](./tests/test_models/test_rectangle.py)
  * [test_square.py](./tests/test_models/test_square.py)

## Classes :cl:

### Base
Represents the "base" class for all other classes in the project. Includes:

* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Class constructor `def __init__(self, id=None):`
  * If `id` is `None`, increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  * Otherwise, sets the public instance attribute `id` to the provided `id`.
* Static method `def to_json_string(list_dictionaries):` that returns the JSON string serialization of a list of dictionaries.
  * If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
* Class method `def save_to_file(cls, list_objs):` that writes the JSON serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.json` (ie. `Rectangle.json`)
  * Overwrites the file if it already exists.
* Static method `def from_json_string(json_string):` that returns a list of objects deserialized from a JSON string.
  * The parameter `json_string` is expected to be a string representing a list of dictionaries.
  * If `json_string` is `None` or empty, the function returns an empty list.
* Class method `def create(cls, **dictionary):` that instantiates an object with provided attributes.
  * Instantiates an object with the attributes given in `**dictionary`.
* Class method `def load_from_file(cls):` that returns a list of objects instantiated from a JSON file.
  * Reads from the JSON file `<cls name>.json` (ie. `Rectangle.json`)
  * If the file does not exist, the function returns an empty list.
* Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited instances.
  * If `list_objs` is `None`, the function saves an empty list.


### Rectangle

Represents a rectangle. Inherits from `Base` with:

* Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  * Each private instance attribute features its own getter/setter.



### Square

Represents a square. Inherits from `Rectangle` with:

* Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  * The `width` and `height` of the `Rectangle` superclass are assigned using the value of `size`.
* Overwrite of `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance of a `Square` with the given attributes.
