import docscanner
import cv2
import Search


class ResumeScanner:
    
    def __init__(self, resume):
        self.resume = resume
        
    def get_skills(self):
        docscanner.initLicense("DKU21-S6650-GHOP7-RELT3-28FCD")
        scanner = docscanner.createInstance()
        image = cv2.imread(self.resume)
        results = scanner.detect(image)
        for result in results:
            print(f" Top left: {result.x1} {result.y1}")
            print(f" Top right: {result.x2} {result.y2}")
            print(f" Bottom left {result.x3} {result.y3}")
            print(f" Bottom right {result.x4} {result.y4}")
        
    def skills_list(self, skill):
        skills = []
        skills.append(skill)
        return skills