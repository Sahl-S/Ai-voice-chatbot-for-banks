
import cv2
from pyzbar.pyzbar import decode


def detect_and_scan_qr(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # QR code detection
    detector = cv2.QRCodeDetector()
    decoded_objects = decode(gray)

    if decoded_objects:
        print("QR Code detected successfully.")
        # Print QR code data
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            print("QR Code Data:", data)
    else:
        print("No QR Code found in the image.")


# Example usage
if __name__ == "__main__":
    image_path = 'QR.jpg'  #The path to your image file
    detect_and_scan_qr(image_path)



import ast

'''
# Updated output string
output_string = "[([[1252, 140], [1955, 140], [1955, 252], [1252, 252]], 'HRT FRTT', 0.1875675295812381), ([[1977, 114], [2098, 114], [2098, 204], [1977, 204]], '7', 0.9115476790466346), ([[1116, 314], [2152, 314], [2152, 406], [1116, 406]], 'GOVERNMENT OF INDIA', 0.793597425466348), ([[849, 605], [1512, 605], [1512, 716], [849, 716]], 'ek gDDG OdR', 0.030966887500471718), ([[836, 707], [2252, 707], [2252, 857], [836, 857]], 'Jeseem Mohamed Raheem', 0.9802517377540853), ([[862, 904], [1065, 904], [1065, 967], [862, 967]], 'eXD', 0.6920208452712742), ([[1067, 843], [2235, 843], [2235, 989], [1067, 989]], 'dDo/DOB: 21/10/2002', 0.4491295911745678), ([[854, 980], [1502, 980], [1502, 1128], [854, 1128]], 'sjauc/ MALE', 0.12547185423923574), ([[897, 1487], [1274, 1487], [1274, 1625], [897, 1625]], '7921', 0.9390061822014539), ([[1317, 1488], [1705, 1488], [1705, 1624], [1317, 1624]], '3879', 0.9274259238408514), ([[1746, 1490], [2134, 1490], [2134, 1627], [1746, 1627]], '1604', 0.9999945621727252), ([[239, 1711], [2804, 1711], [2804, 1906], [239, 1906]], 'MERA AADHAAR, MERI PEHCHAN', 0.9177232555834941), ([[25, 321], [157, 321], [157, 341], [25, 341]], 'ABDU RAHEEM', 0.7889266562331422), ([[25, 373], [133, 373], [133, 393], [25, 393]], '21/10/2002', 0.9906158225414202)]"

# Splitting the string into a list of tuples
data_list = ast.literal_eval(output_string)

# Extracting required information
name = ''
dob = ''
father_name = ''

for item in data_list:
    text = item[1]
    if 'DOB' in text:
        dob = text.split(': ')[1]
    elif 'Father' in text:
        father_name = text.split(': ')[1]
    else:
        name = text

print("Name:", name)
print("Date of Birth:", dob)
print("Father's Name:", father_name)
'''





