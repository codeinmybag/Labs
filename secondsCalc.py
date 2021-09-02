def main():
        num = int(input("input time in seconds: "))
        one_year = 31536000
        one_day = 86400
        one_hour = 3600
        one_min = 60
        one_second = 1 
        number_of_years=(num//one_year)
        yearrem=(num%one_year)
        number_of_days=(yearrem//one_day)
        dayrem=(num%one_day)
        number_of_hours=(dayrem//one_hour)
        hourrem=(num%one_hour)
        number_of_minutes=(hourrem//one_min)
        minrem=(num%one_min)
        number_of_seconds=(minrem//one_second)
        secrem=(number_of_seconds%one_second)
        
        print(number_of_years,'years',number_of_days,'days',number_of_hours,'hours', number_of_minutes, 'minutes',  number_of_seconds,'seconds')
        
        
main()  
