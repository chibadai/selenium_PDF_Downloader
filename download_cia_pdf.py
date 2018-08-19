from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# driver.get("http://example.com/sample.pdf")
# for i in range(0, 94015):
n= None
try:
    for i in range(0, 94015):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
          "download.default_directory": 'D:\GitHub\selenium\selenium_PDF_Downloader\cia\\' + str(i),
          "download.prompt_for_download": False,
          "download.directory_upgrade": True,
          "plugins.plugins_disabled": ["Chrome PDF Viewer"],
          "plugins.always_open_pdf_externally": True
        })
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-print-preview")

        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.cia.gov/library/readingroom/document-type/crest?page=' + str(i))
        tmpTag = driver.find_elements_by_tag_name("a")
        for i in range(0, len(tmpTag)):
            print(i)
            if isinstance(n, type(tmpTag[i].get_attribute('href'))) == False:
                if tmpTag[i].get_attribute('href')[-4:].find('.pdf') == 0:
                    print(tmpTag[i].get_attribute('href'))
                    driver.get(tmpTag[i].get_attribute('href'))
except:
    print('error')
# driver.get('https://www.cia.gov/library/readingroom/docs/CIA-RDP80-00810A002400700004-3.pdf')
# driver.get('https://www.cia.gov/library/readingroom/docs/CIA-RDP80-00810A002400700002-5.pdf')
# driver.quit()
