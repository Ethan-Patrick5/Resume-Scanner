import docscanner
import cv2
import Search


class Scanner:
    
    def __init__(resume):
        Scanner.resume = resume
        
    def get_skills(self):
        docscanner.initlicense("DKU21-S6650-GHOP7-RELT3-28FCD")
        scanner = docscanner.createInstance()
        image = scanner.capture_image(Scanner.resume)
        scanner_resume = scanner.scan(image)
        
    def skills_list(self, skill):
        skills = []
        skills.append(skill)
        return skills