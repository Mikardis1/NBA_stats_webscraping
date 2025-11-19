from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.nba.com/stats")
    wait = WebDriverWait(driver, 60)

    try:
        accept_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']")))
        accept_cookies.click()
    except Exception as e:
        print("No cookie popup found or error accepting cookies:", e)

    try:
        all_player_stats = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[3]/div/div[1]/section[1]/div/div[1]/div[2]/a")))
        driver.execute_script("arguments[0].click();", all_player_stats)
    except Exception as e:
        print("No Button found", e)

    try:
        table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Crom_table__p1iZz")))
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.Crom_table__p1iZz tbody tr")))

        rows = table.find_elements(By.TAG_NAME, "tr")

        data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 7:
                player = cells[1].text.strip()
                pts = cells[7].text.strip()
                if player and pts:
                    data.append([player, pts])
                    print(f"Added {player} | {pts}")
        df = pd.DataFrame(data, columns=["PLAYER", "PTS"])
        df.to_csv("nba.csv", index=False)
        print("Succesfull scrapped")
    except Exception as e:
        print("No data found")
finally:
    driver.quit()
