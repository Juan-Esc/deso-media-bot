import deso
import os
import schedule
import time
import random
from dotenv import load_dotenv

load_dotenv()

public_key = os.getenv('public_key')
seed_hex = os.getenv('seed_hex')

desoMedia = deso.Media(public_key, seed_hex)
p = deso.Social(public_key, seed_hex)

imageFiles = os.listdir("images")
imageFiles.remove(".gitkeep")
print(imageFiles)

def randomItem(array):
    return array[random.randint(0, len(array) - 1)]

def tweetRandomImage():
    image = randomItem(imageFiles)
    imageUrl = ""
    imageFileList = [
        ('file', ('screenshot.jpg', open('images/'+image, "rb"), 'image/png'))
    ]
    try:
        urlResponse = desoMedia.uploadImage(imageFileList)
        print(urlResponse.json()['ImageURL']) # type: ignore
        imageUrl = urlResponse.json()['ImageURL'] # type: ignore
    except Exception as e:
        print(e)

    try:
        response = p.submitPost("", [imageUrl])
        print(response)
    except  Exception as e:
        print(e)

    # Delete image
    os.remove('images/'+image)
    imageFiles.remove(image)
    print(imageFiles)

# Tweet every 6 hours approximately
schedule.every().day.at("12:00") .do(tweetRandomImage)
schedule.every().day.at("18:00").do(tweetRandomImage)
schedule.every().day.at("22:00").do(tweetRandomImage)

while True:
    schedule.run_pending()
    time.sleep(1)