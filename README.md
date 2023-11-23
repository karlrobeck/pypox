# Pypox README

## Overview

The Pypox module is designed to dynamically generate a FastAPI application and API routers based on predefined conventions within a specified directory. It automatically discovers and integrates Python modules within the directory to create endpoints and configure API-related settings.

### Key Aspects

1. **Dynamic API Construction:** Pypox dynamically constructs APIs by inspecting the contents of modules within a specified directory. It follows a convention-based approach where modules adhering to predefined naming patterns are automatically integrated into the API structure.

2. **Convention-Driven Approach:** Modules within the designated directory must comply with specific naming conventions to be recognized and utilized by Pypox. These conventions define the purpose and functionality of each module, facilitating automatic endpoint creation and configuration.

3. **Flexibility and Extensibility:** While relying on conventions, Pypox provides flexibility in managing the API structure. Users can extend functionalities by adding modules that adhere to the prescribed naming conventions, enabling seamless integration into the API structure.

4. **Simplified Application Management:** Pypox handles various aspects of API construction, including route creation, endpoint configurations, and application lifecycle management. It streamlines the process of building FastAPI applications, reducing the need for manual configuration and setup.

5. **Lifespan Management:** The module supports the execution of startup and shutdown functions provided within modules. This feature enables proper initialization and cleanup routines, ensuring a well-managed application lifecycle.

### Use Cases

- **Rapid API Prototyping:** Pypox is particularly useful in scenarios requiring quick prototyping or development of RESTful APIs. By adopting a convention-driven approach, developers can focus more on implementing business logic and less on boilerplate code for setting up API endpoints.

- **Microservices Architecture:** In microservices-based architectures, where numerous services communicate via APIs, Pypox aids in standardizing API creation and configuration across multiple services. It promotes consistency in API development while allowing for individual service customization through conventions.

- **API Development Automation:** For projects involving frequent updates or additions to API endpoints, Pypox automates the process of integrating new endpoints or modifying existing ones. This feature helps in scaling applications without compromising on maintainability.

### Advantages

- **Reduced Development Time:** By automating API creation and configuration, Pypox significantly reduces the time spent on manual setup and management, accelerating the development cycle.

- **Consistency and Maintainability:** Enforcing naming conventions ensures a consistent API structure, simplifying maintenance and making the codebase more accessible to new developers.

- **Scalability and Adaptability:** Pypox's modular and convention-driven approach fosters scalability, allowing applications to grow while maintaining a coherent API structure.

- **Improved Collaboration:** The standardized approach to API development enhances collaboration among team members by establishing a common ground for understanding API endpoints and configurations.

## Features

- Automatic discovery of modules within a specified directory following specific file naming conventions.
- Dynamically generates FastAPI application and API routers based on discovered modules.
- Configures endpoints, their methods, and associated configurations based on module contents.
- Supports startup and shutdown functions to manage the application's lifespan.

## Installation

No specific installation steps are required as Pypox is a self-contained Python module. Ensure that the required dependencies such as `fastapi` are installed in your environment.

## Usage

To use Pypox, follow these steps:

1. **Instantiate Pypox:** Create an instance of the `Pypox` class by providing a directory path containing modules following defined naming conventions.

   ```python
   pypox_instance = Pypox(directory_path)
   ```

2. **Invoke Pypox:** Call the `Pypox` instance as a function to generate the FastAPI application and API routers based on the discovered modules.

   ```python
   fastapi_app = pypox_instance()
   ```

3. **Run the FastAPI application:** Utilize the generated `FastAPI` instance to run the application.

   ```python
   import uvicorn

   if __name__ == "__main__":
       uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
   ```

### `Pypox` Class Structure

#### `__init__(self, directory: str)`

- **Purpose:** Initializes an instance of the `Pypox` class with the specified directory path.
- **Parameters:**
  - `directory` (str): The path to the directory containing Python modules following specific naming conventions.
- **Returns:** None

#### `get_modules(self) -> "Pypox"`

- **Purpose:** Retrieves the list of modules within the specified directory following predefined file naming conventions.
- **Returns:** Instance of `Pypox`
- **Note:** Iterates through the directory's content, identifying and loading modules that adhere to predefined file naming conventions (`FILE_CONVENTIONS`). It utilizes `importlib` to dynamically load these modules.

#### `__create_lifespan(self, modules: List[ModuleType]) -> Callable | None`

- **Purpose:** Creates a context manager function to manage the application's lifespan based on presence of "startup" and "shutdown" functions in discovered modules.
- **Parameters:**
  - `modules` (List[ModuleType]): List of modules to check for "startup" and "shutdown" functions.
- **Returns:** A lifespan context manager function if both "startup" and "shutdown" functions are present in the modules, otherwise `None`.

#### `__create_config(self, modules: List[ModuleType], type: str) -> dict[str, Any]`

- **Purpose:** Generates configuration dictionaries for FastAPI and API routers based on module contents.
- **Parameters:**
  - `modules` (List[ModuleType]): List of modules to generate the configuration from.
  - `type` (str): Type of configuration to generate, either "FastAPI" or "APIRouter".
- **Returns:** Configuration dictionary containing parameters defined in `FASTAPI_PARAMETERS` or `API_ROUTER_PARAMETERS`.

#### `__get_endpoints(self, modules: list[ModuleType]) -> tuple[list[Callable], list[dict[str, Any]]]`

- **Purpose:** Extracts endpoints and their configurations from a list of modules.
- **Parameters:**
  - `modules` (list[ModuleType]): List of modules containing endpoint information.
- **Returns:**
  - Tuple containing:
    - `endpoints`: A list of endpoint functions.
    - `configs`: A list of endpoint configurations.

#### `__call__(self, *args: Any, **kwds: Any) -> FastAPI`

- **Purpose:** Executes the instance as a function to generate and configure the FastAPI application and API routers.
- **Parameters:**
  - `*args` (Any): Variable length arguments.
  - `**kwds` (Any): Keyword arguments.
- **Returns:** The constructed FastAPI application based on discovered modules and configurations.

#### `Note`

- The `Pypox` class orchestrates the dynamic integration of modules into the FastAPI application and API routers based on naming conventions. It automates the creation of routes, configuration parameters, and execution of startup/shutdown routines, allowing for a streamlined API setup process.
- Utilizing this class involves instantiating `Pypox`, calling it as a function, and obtaining a configured `FastAPI` instance ready for use.

## Conventions

- Pypox expects modules in the specified directory to adhere to certain file naming conventions:
  - `socket.py`
  - `config.py`
  - `startup.py`
  - `shutdown.py`
  - `get.py`
  - `post.py`
  - `put.py`
  - `delete.py`

### File Naming Conventions:

1. **Socket Handling:** Module for Web Socket handling.

   - Example: `socket.py`

2. **Configuration:** Module containing router / main application configurations.

   - Example: `config.py`

3. **Startup Routine:** Module for defining startup procedures.

   - Example: `startup.py`

4. **Shutdown Routine:** Module for defining shutdown procedures.

   - Example: `shutdown.py`

5. **HTTP Methods (CRUD Operations):**
   - Module for handling HTTP GET requests.
     - Example: `get.py`
   - Module for handling HTTP POST requests.
     - Example: `post.py`
   - Module for handling HTTP PUT requests.
     - Example: `put.py`
   - Module for handling HTTP DELETE requests.
     - Example: `delete.py`

### Endpoint Naming Conventions:

For the HTTP methods mentioned above, the expected naming conventions for defining endpoints follow the HTTP verbs in uppercase:

- `GET` endpoint:

  - The module should define an `endpoint` function, often named as `endpoint` or `get`, responsible for handling GET requests.

- `POST` endpoint:

  - The module should define an `endpoint` function, often named as `endpoint` or `post`, responsible for handling POST requests.

- Similarly for `PUT`, `DELETE`, and other HTTP methods.

### Example:

Let's consider an example directory structure adhering to these conventions:

```
/project_directory
    |-- socket.py
    |-- config.py
    |-- startup.py
    |-- shutdown.py
    |-- get.py
    |-- post.py
    |-- put.py
    |-- delete.py
    |-- other_module.py
    |-- ...
```

In this scenario:

- `socket.py` handles socket-related operations.
- `config.py` stores application configurations.
- `startup.py` contains procedures executed on application startup.
- `shutdown.py` contains procedures executed on application shutdown.
- `get.py`, `post.py`, `put.py`, `delete.py`, and potentially other similar files each define endpoints for handling GET, POST, PUT, DELETE requests, respectively.

Pypox will recognize and utilize these modules for building the FastAPI application and API routers based on their functionalities and the defined conventions.

## Dependencies

Pypox requires the following dependencies:

- `fastapi`
- `uvicorn[standard]`

## Limitations

- The module assumes specific file naming conventions for modules within the directory.
- It requires the presence of specific functions (`startup` and `shutdown`) for managing application lifespan.

## Contributions

Contributions to enhance Pypox by supporting additional functionality, improving error handling, or expanding conventions are welcome! Feel free to create pull requests or raise issues.

## MIT License (for Business Use)

Copyright (c) [2023] [Po-key]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

For any inquiries or support, reach out to the maintainers through [karlalferezfx\@gmail.com](mailto:karlalferezfx@gmail.com?subject=ResponsePypox).

---
