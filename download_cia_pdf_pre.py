from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def outputText(outputFileName, outputText, num):
    f = open(outputFileName, 'a')
    try:
        for i in range(0, len(outputText)):
            # f.write(num + "," + outputText[i] + "\n")
            if i == (len(outputText) - 1):
                f.write(num + "," + outputText[i])
            else:
                f.write(num + "," + outputText[i] + "\n")

    except:
        print('file write error')
    finally:
        f.write("\n")
        f.close()

driver = webdriver.Chrome()
# driver.get("http://example.com/sample.pdf")
# for i in range(0, 94015):
outputFileName = 'pdf_url.txt'
n= None
try:
    for i in range(0, 94015):
        driver.get('https://www.cia.gov/library/readingroom/document-type/crest?page=' + str(i))
        tmpTag = driver.find_elements_by_tag_name("a")
        outputTextArray = []
        for j in range(0, len(tmpTag)):
            if isinstance(n, type(tmpTag[j].get_attribute('href'))) == False:
                if tmpTag[j].get_attribute('href')[-4:].find('.pdf') == 0:
                    outputTextArray.append(tmpTag[j].get_attribute('href'))
                    # print(tmpTag[j].get_attribute('href'))
        outputText(outputFileName, outputTextArray, str(i))
except:
    print('error')
# driver.quit()
