from DAO import CameraDAO
import decimal

def checkLocation(cameraID,latitude, longitude,errRange):
    row = CameraDAO.SelectCamera(cameraID)

    if decimal.Decimal(row[0]) - errRange <= decimal.Decimal(latitude) <= decimal.Decimal(row[0]) + errRange:
        if decimal.Decimal(row[1]) - errRange <= decimal.Decimal(longitude) <= decimal.Decimal(row[1]) + errRange:
            return True
        else:
            return False
    else:
        return False