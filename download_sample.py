from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {
#   "download.default_directory": 'D:\GitHub\selenium\selenium_PDF_Downloader\cia\0',
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "plugins.plugins_disabled": ["Chrome PDF Viewer"],
#   "plugins.always_open_pdf_externally": True
# })
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-print-preview")
#
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('https://www.cia.gov/library/readingroom/docs/CIA-RDP80-00810A002400700004-3.pdf')
# driver.get('https://www.cia.gov/library/readingroom/docs/CIA-RDP80-00810A002400700002-5.pdf')
# driver.quit()
for i in range(0, 2):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
      "download.default_directory": 'D:\GitHub\selenium\selenium_PDF_Downloader\cia\\' + str(i+1),
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "plugins.plugins_disabled": ["Chrome PDF Viewer"],
      "plugins.always_open_pdf_externally": True
    })
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-print-preview")

    driver = webdriver.Chrome(chrome_options=options)
    if i == 0:
        driver.get('https://www.cia.gov/library/readingroom/docs/CIA-RDP80-00810A002400700004-3.pdf')
    elif i == 1:
        driver.get('https://www.cia.gov/library/readingroom/docs/CIA-RDP80-00810A002400700002-5.pdf')
