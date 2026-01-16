# PDB Query 
PDB is a database for storing and retrieving protein structures. Computational biologists, bioinformatician, and researchers from various fields use PDB to access structures of proteins, nucleic acids, and complex assemblies that are crucial for understanding biological functions and processes. 

Quering the PDB database can done through various methods including web interfaces, a RESTful API and GraphQL endpoints. These methods allow users to search for specific structures, download data files, and access metadata related to the entries in the database.

Querying the PDB database from within a Python script typically involves constructing a JSON like query, sending it to the PDB API endpoint, and then parsing the returned data. This process can be complex and requires a good understanding of both the PDB schema and the API itself. The web interface for constructing the queries are not very user friendly either. 

It is my belief that users in this field should be focued on their research and not have to deal with the complexities of querying databases, hence this package was born. This package aims to simplify this process and make querying the database more accessible and intiutive for regular users.

## Installation
ToDo: Add installation instructions

## Usage
We provide a simple, clean interface for querying the PDB database. This involves creating a separate file for your queries which should end with .pdbq extension. It is also possible to include custom Python code for handling outputs ensuring that your main Python scripts stays nice and clean. Every project should include only one .pdbq file, however, it is possible to include multiple queries into a single file. The .pdbq file can broken up into three sections which should appear in order: 
- the configurations section - makes it possible to specify configurations for the query like the return type, sorting format, etc.
- the query section - this is where the actual queries are defined. It is possible to include multiple queries in one file. Read the [query strings](#query-strings) section below for more information on how to construct query strings.
- user code - you can customize the way the results are handled by providing your own user code. This is optional. Any valid Python code can be included here.

Single line comments should start with a # character and can be included anywhere in the file.

### Writing custom configurations
ToDo: Add documentation for configurations

### Writing Queries
ToDo: Add documentation for writing queries

### Writing User Code for output handling
You can optionally include a function called handle_results(results) in the user code section of your .pdbq file. This function will be called with the results of the query as its argument. You can then process, analyze, or save the results as needed. The function should accept a single parameter, results, which will be a list of dictionaries representing the query results. You may return any data from this function, but it will not affect the main execution flow.

Here's an example of how to define the handle_results function:

```python
def handle_results(results):
    for entry in results:
        print(f"Entry ID: {entry['entry_id']}, Title: {entry['title']}")
    return None
```

If no handle_results function is provided, the default behavior will be to return the results as returned by the PDB API without any additional processing. 

## Query Strings
Query strings are used to define the actual queries that will be sent to the PDB database. I have tried to put simplicity and intuitiveness at the heart of the design of query strings. The query strings are designed to be easy to read and write, even for users who are not familiar with the underlying PDB schema or API. 

Each query string starts with the keyword QUERY. Multi-line queries should be enclosed in curly ({}) brackets. You can use parentheses to group conditions and control the order of evaluation. All fields and values are case-insensitive. All attributes available in the rcsb database can be used in query strings. 

It is possible to build complex queries using logical operators like AND, OR, NOT. Comparison operators like ==, !=, <, >, <=, >= can also be used to create more specific conditions. A special operator called "NOT_EMPTY" is also supported and more operators will be added in future releases. Please feel free to open an issue if you have any specific operator requests.