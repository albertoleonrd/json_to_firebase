# JSON to Firebase

## Description

This tool allows importing data from JSON files to a Firebase Firestore database. It can be used to import any type of structured data in JSON format to Firestore, facilitating migration or bulk loading of information.

## Project Structure

The project contains the following files:

- `json_to_firebase.py`: Main script that handles data import to Firebase.
- `example_data.json`: Example file containing sample data in JSON format.
- `.gitignore`: File to exclude specific files from version control.

## Requirements

- Python 3.6 or higher
- Firebase account with Firestore enabled
- Firebase service account credentials file

## Installation

1. Clone this repository or download the files.
2. Install the necessary dependencies:

```bash
pip install firebase-admin
```

3. Place your Firebase service account credentials file (`firebase-service-account.json`) in the project directory.

## Configuration

Open the `json_to_firebase.py` file and modify the following variables as needed:

```python
# Replace with the path to your service account key file
SERVICE_ACCOUNT_KEY_PATH = "firebase-service-account.json"

# Replace with the path to your JSON file
JSON_FILE_PATH = "example_data.json"

# Name of the Firestore collection where you want to import the data
COLLECTION_NAME = "words"

# Batch size for writes (Firestore has a limit of 500 operations per batch)
BATCH_SIZE = 499
```

## Usage

Run the main script:

```bash
python json_to_firebase.py
```

The script will perform the following actions:

1. Initialize the connection to Firebase using the provided credentials.
2. Load the data from the specified JSON file.
3. Import the data to the specified Firestore collection, using batches to optimize performance.
4. Display information about the progress and results of the import.

## Data Structure

The `example_data.json` file contains an array of objects with the following structure:

```json
[
  {
    "id": "001",
    "name": "Smartphone XYZ",
    "category": "Electronics",
    "price": 599.99,
    "specifications": {
      "brand": "TechCorp",
      "model": "XYZ-2000",
      "color": "Black",
      "storage": "128GB",
      "features": ["5G", "Water Resistant", "Dual Camera"]
    },
    "inStock": true,
    "reviews": [
      {
        "user": "user123",
        "rating": 4.5,
        "comment": "Great phone, excellent camera quality!"
      }
    ]
  }
]
```

## Important Notes

- The script is configured to handle large amounts of data using batches to avoid exceeding Firestore limits.
- By default, automatic IDs are generated for each document in Firestore. If you want to use a specific field from your data as an ID, you can modify the `import_data_to_firestore` function.
- Make sure you have the appropriate permissions in your Firebase project to write to the database.

## License

This project is available as open source under the terms of the MIT license.