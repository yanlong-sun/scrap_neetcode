from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

browser = webdriver.Chrome()
url = 'https://neetcode.io/practice'
browser.get(url)
tabs = browser.find_element(
    By.CLASS_NAME, "tabs-list").find_elements(
    By.TAG_NAME, 'span')

file_names = ['neetcode75', 'neetcode150', 'neetcode300']

for tab, file in zip(tabs, file_names):
    filename = file
    tab.click()
    problem_list_by_type = browser.find_elements(
        By.TAG_NAME, 'app-pattern-table')
    type_name_link_diff = []
    for problem_type in problem_list_by_type:
        type = problem_type.find_elements(
            By.TAG_NAME, 'p')[0].text
        problems = problem_type.find_element(
            By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for problem in problems:
            problem_info = problem.find_elements(By.TAG_NAME, 'td')
            link_obj = problem_info[2].find_element(By.TAG_NAME, 'a')
            difficulty = problem_info[3].find_element(
                By.TAG_NAME, 'b').get_attribute('innerHTML')
            name = link_obj.get_attribute('innerHTML')
            href = link_obj.get_attribute('href')
            type_name_link_diff.append((type, name, href, difficulty))
    df = pd.DataFrame(type_name_link_diff, columns=[
                      'type', 'name', 'link', 'difficulty'])
    df.to_csv(f'./{filename}.csv', index=False)
