import re

def verify_kyc_extracted_data(extracted_data):
    """
    Verify the extracted KYC data.
    :param extracted_data: Text extracted from the ID document
    :return: Verification result as a boolean
    """
    # Define simple patterns for name and ID (modify as needed)
    name_pattern = r"Test (\w+)"
    id_pattern = r"ID (\w+)"
    
    name_match = re.search(name_pattern, extracted_data)
    id_match = re.search(id_pattern, extracted_data)
    
    if name_match and id_match:
        return True, {
            'name': name_match.group(1),
            'id': id_match.group(1)
        }
    return False, {}