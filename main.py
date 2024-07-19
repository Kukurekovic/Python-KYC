from ocr import extract_text_from_image
from kyc_verification import verify_kyc_extracted_data

def main():
    image_path = 'sample_id_card.png'
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:")
    print(extracted_text)
    
    is_verified, data = verify_kyc_extracted_data(extracted_text)
    
    if is_verified:
        print("KYC Verification Successful!")
        print(f"Extracted Data: {data}")
    else:
        print("KYC Verification Failed!")

if __name__ == '__main__':
    main()