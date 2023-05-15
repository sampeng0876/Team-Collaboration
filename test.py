                next_day = appt_date + timedelta(days=1)
                
                print(f'this is next_day {next_day}')
                
                if next_day.month > appt_date.month:
                    driver.find_element(By.XPATH,'//*[@id="ipgrid_0"]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[3]').click()    
                    sleep(1)
                    continue