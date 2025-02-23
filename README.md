# PDF Merger & Image Resizer

## Description
This Python script provides two functionalities:
1. Merging multiple PDF files into a single PDF.
2. Resizing an image by 50% and saving it with a new filename.

## Features
- **PDF Merger:** Allows users to merge multiple PDFs into a single document.
- **Image Resizer:** Resizes an image to 50% of its original size.
- **User Input Friendly:** Users can choose between PDF merging and image resizing via an input prompt.

## Requirements
Ensure you have the following dependencies installed before running the script:

```bash
pip install PyPDF2 opencv-python
```

## How to Use
1. Run the script:
    ```bash
    python script.py
    ```
2. Choose an option:
    - Enter `0` for image resizing.
    - Enter `1` for PDF merging.
3. Follow the on-screen instructions:
    - **For PDF merging:** Enter the filenames of the PDFs you want to merge (separated by space).
    - **For Image resizing:** Enter the filename of the image to resize and the desired output filename.
4. **Important:** If you want to resize an image or merge PDFs, make sure to drag your file to your IDE or the folder where you are running this project. At the input prompt, enter the name of that file correctly.

## Example Usage
### Merging PDFs
```bash
Enter 1 for PdfMerger: 1
Enter the PDF filenames to merge (separated by space): file1.pdf file2.pdf file3.pdf
```
_Output:_ A new file `merged.pdf` will be created.

### Resizing an Image
```bash
Enter 0 for Image resizing: 0
Enter the Image name you want to resize: image.jpg
Enter the new name for image: resized_image.jpg
```
_Output:_ A new resized image `resized_image.jpg` will be saved.

## License
This project is open-source and available for use under the MIT License.

## Author
IMSHA NADEEM

