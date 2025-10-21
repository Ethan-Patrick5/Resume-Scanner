import docscanner
import cv2
import Search

class Scanner:
    
    def __init__(resume):
        Scanner.resume = resume
        
    def get_skills(self):
        docscanner.initlicense("DKU21-S6650-GHOP7-RELT3-28FCD")
        scanner = docscanner.createInstance()
        results = scanner