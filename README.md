
# Construction Material Estimator

A command-line Python application that estimates concrete, aggregate, and soil quantities for common construction tasks.

## Why I Built It

This project combines my construction engineering background with my transition into software development. It demonstrates how software can reduce manual calculations and improve consistency during construction planning.

## Features

- Concrete volume calculation in cubic yards
- Estimated number of 80-pound concrete bags
- Aggregate volume and tonnage estimation
- Soil volume with waste and compaction factors
- Input validation and clear error handling
- Automated unit tests

## Technologies

- Python 3
- Dataclasses
- Object-oriented design
- Unit testing with `unittest`

## Run the Application

```bash
python main.py
```

## Run the Tests

```bash
python -m unittest discover -s tests
```

## Example

For a 10 ft × 10 ft slab with a 4-inch depth and 10% waste:

- Base concrete: approximately 1.23 cubic yards
- Concrete with waste: approximately 1.36 cubic yards
- Estimated 80-pound bags: calculated automatically

## Skills Demonstrated

- Python functions and classes
- Data validation
- Exception handling
- Modular code organization
- Construction-domain problem solving
- Automated testing
- Technical documentation

## Future Improvements

- Add a graphical user interface
- Export estimates to CSV or PDF
- Support metric units
- Add cost estimation
- Add a web API
