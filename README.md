# Construction Material Estimator

A Python command-line application that calculates concrete, aggregate, and soil quantities for common construction projects. The application uses validated user input, reusable calculation logic, object-oriented design, and automated testing.

---

## Objective

This project combines my military and civilian construction experience with my transition into software engineering. It was built to strengthen Python programming skills while demonstrating how software can improve the speed and consistency of construction quantity calculations.

---

## Features

- Calculate concrete volume in cubic yards
- Estimate the number of 80-pound concrete bags
- Calculate aggregate volume and estimated tonnage
- Calculate soil volume
- Apply waste and compaction factors
- Validate user input
- Display formatted calculation results
- Organize calculation logic into reusable modules
- Verify functionality with automated unit tests

---

## Technologies

- Python 3
- Dataclasses
- Object-oriented programming
- `unittest`
- Git
- GitHub

---

## Skills Demonstrated

- Python functions and classes
- Object-oriented design
- Dataclasses
- Input validation
- Exception handling
- Modular programming
- Construction-domain problem solving
- Automated unit testing
- Technical documentation
- Git version control

---

## Project Structure

```text
construction-material-estimator/
│
├── src/
│   └── ...
│
├── tests/
│   └── ...
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Prerequisites

- Python 3.10 or later
- Git, optional for cloning the repository

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/radjivbatuli/construction-material-estimator.git
```

### 2. Navigate to the project folder

```bash
cd construction-material-estimator
```

### 3. Run the application

```bash
python main.py
```

---

## Run the Tests

```bash
python -m unittest discover -s tests
```

---

## Example Calculation

For a slab measuring 10 feet by 10 feet with a depth of 4 inches and a 10% waste factor, the application calculates:

```text
Base concrete volume: approximately 1.23 cubic yards
Concrete with waste: approximately 1.36 cubic yards
Estimated 80-pound bags: calculated automatically
```

---

## Future Improvements

- Add metric-unit support
- Export results to CSV or PDF
- Add project cost calculations
- Add a graphical user interface
- Add a web API
- Expand automated test coverage

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
