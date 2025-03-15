# Google Cloud Storage Bucket Downloader

This script downloads files from a specified Google Cloud Storage (GCS) bucket to a local directory.

It utilizes the Firebase Admin SDK to authenticate and interact with GCS, allowing you to easily retrieve and store files from your cloud storage.

## Requirements

1.  Python 3.9 or higher.
2.  Install the required Python package using pip:
    ```bash
    pip install -r requirements.txt
    ```
3.  A Google Cloud service account credentials JSON file (e.g., `cred.json`) must be present in the same directory as the script.

## How to Use

1.  **Prepare Credentials:** Download your Google Cloud service account credentials JSON file and rename it to `cred.json`. Place it in the script's directory.
2.  **Install Dependencies:** Run `pip install -r requirements.txt` to install the required Python package.
3.  **Configure the Script:**
    * Open `download_data.py` in a code editor.
    * Ensure the bucket name inside the `run()` function is correct.
    * If needed, modify the `prefix` and `directory` arguments inside the `storage_handling.photo_download()` call to download files from a specific folder, and to store them in a specific location.
4.  **Run the Script:** Execute the script using Python:
    ```bash
    python download_data.py
    ```
5.  **Verify Downloaded Files:** The downloaded files will be stored in the specified directory (default: `download`).

## Customization

* **Credentials:** If your credentials file is named differently or located elsewhere, update the `cred.json` path in `download_data.py`.
* **Bucket Name:** Ensure the bucket name in `download_data.py` matches the GCS bucket you want to download from.
* **Download Directory:** Modify the `directory` parameter in `storage_handling.photo_download()` to change the download location.
* **File Prefix:** Use the `prefix` parameter in `storage_handling.photo_download()` to download files with a specific prefix (e.g., a folder within the bucket).
* **Error Handling:** Enhance error handling by catching specific exceptions and providing more informative error messages.
* **Logging:** Implement logging to record script activity and errors.