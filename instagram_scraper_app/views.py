# from django.shortcuts import render
# from .forms import InstagramScrapeForm
# from django.http import HttpResponse
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# import time
# import os
# import wget

# def scrape_instagram(request):
#     if request.method == 'POST':
#         form = InstagramScrapeForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             hashtag = form.cleaned_data['hashtag']

#             try:
#                 # Initialize WebDriver
#                 driver = webdriver.Firefox()  # NOTE: Use appropriate WebDriver for your system
#                 driver.get("http://www.instagram.com")

#                 # Login to Instagram
#                 username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
#                 password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
#                 username_field.clear()
#                 username_field.send_keys(username)
#                 password_field.clear()
#                 password_field.send_keys(password)
#                 login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#                 # Handle alerts/pop-ups during login
#                 try:
#                     alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
#                     alert.accept()
#                 except TimeoutException:
#                     # No alert found, continue with the login process
#                     pass

#                 # Perform Instagram scraping
#                 searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
#                 searchbox.clear()
#                 searchbox.send_keys(hashtag)
#                 time.sleep(5)
#                 searchbox.send_keys(Keys.ENTER)
#                 time.sleep(5)
#                 searchbox.send_keys(Keys.ENTER)
#                 time.sleep(5)
#                 driver.execute_script("window.scrollTo(0,4000);")

#                 # Locate and download images
#                 images = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
#                 image_urls = [image.get_attribute('src') for image in images]

#                 path = os.getcwd()
#                 path = os.path.join(path, hashtag[1:] + "s")
#                 os.makedirs(path, exist_ok=True)
                
#                 for index, image_url in enumerate(image_urls):
#                     try:
#                         save_as = os.path.join(path, f"{hashtag[1:]}_{index}.jpg")
#                         wget.download(image_url, save_as)
#                     except Exception as e:
#                         print(f"Error downloading image {image_url}: {str(e)}")

#                 driver.quit()

#                 return HttpResponse("Instagram scraping completed successfully!")
#             except Exception as e:
#                 # Handle any exceptions that occur during scraping
#                 return HttpResponse(f"An error occurred during scraping: {str(e)}")
#     else:
#         form = InstagramScrapeForm()

#     return render(request, 'scrape_instagram.html', {'form': form})


# views.py
from django.shortcuts import render
from .forms import InstagramScrapeForm
from django.http import HttpResponse
from .modules.scraper import scrape_instagram_data
from django.views import View  # Import the View class from django.views

class InstagramScrapeView(View):
    template_name = 'scrape_instagram.html'

    def get(self, request):
        form = InstagramScrapeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InstagramScrapeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            hashtag = form.cleaned_data['hashtag']

            if scrape_instagram_data(username, password, hashtag):
                return HttpResponse("Instagram scraping completed successfully!")
            else:
                return HttpResponse("An error occurred during scraping.")
        return render(request, self.template_name, {'form': form})
























