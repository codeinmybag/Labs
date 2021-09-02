def main():
    itemTotal=float(input('What was the total?  $'))
    paidAmt=float(input('How much did you pay?  $'))
    itemTotalIP=(itemTotal * 100)
    amount_in_pennies=(paidAmt*100)
    difference=(amount_in_pennies-itemTotalIP)

    twentyD= 2000
    tenD= 1000
    fiveD= 500
    oneD= 100
    quarters= 25
    dimes= 10
    nickles= 5
    pennies= 1

    change_in_twenties=(difference//twentyD)
    twentiesRem=(difference%twentyD)

    change_in_tens=(twentiesRem//tenD)
    tendiesRem=(difference%tenD)

    change_in_fives=(tendiesRem//fiveD)
    fivesRem=(difference%fiveD)

    change_in_ones=(fivesRem//oneD)
    onesRem=(difference%oneD)
   
    change_in_quarters=(onesRem//quarters)
    quartersRem=(difference%quarters)

    change_in_dimes=(quartersRem//dimes)
    dimesRem=(difference%dimes)

    change_in_nickles=(dimesRem//nickles)
    nickelsRem=(difference%nickles)

    changes_in_pennies=(nickelsRem//pennies)
    penniesRem=(difference%pennies)

    print(int(change_in_twenties),'twenty dollar bills')
    print(int(change_in_tens),'ten dollar bills')
    print(int(change_in_fives),'five dollar bills')
    print(int(change_in_ones),'one dollar bills')
    print(int(change_in_quarters),'quarters')
    print(int(change_in_dimes),'dimes')
    print(int(change_in_nickles),'nickles')
    print(int(changes_in_pennies),'pennies')

   
main()
