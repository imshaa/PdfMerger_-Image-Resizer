import PyPDF2
import cv2
def check(x):
    match x:
        case 1:
            pdf_files = input("Enter the PDF filenames to merge (separated by space): ").split()
            merger = PyPDF2.PdfMerger()


            for filename in pdf_files:
                try:
                    with open(filename, "rb") as pdf_file:
                        merger.append(pdf_file)  
                except FileNotFoundError:
                    print(f"Error: '{filename}' not found. Skipping...")


            output_filename = "merged.pdf"  
            merger.write(output_filename)
            merger.close()

            print(f" PDFs merged successfully into '{output_filename}'")
        case 0:

            source = input("Enter the Image name you want to resize: ")
            destination = input("Enter the new name for image: ")
            scale_percent = 50
            src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

            new_w = int(src.shape[1] * scale_percent / 100)
            new_h = int(src.shape[0] * scale_percent / 100)

            output =  cv2.resize(src, (new_w, new_h))
            cv2.imwrite(destination, output)

print("You Can do Your Image Resizing And PDF Merging Here !")
a = int(input("Enter 0 for Image resizing Or 1 for PdfMerger: "))
check(a)