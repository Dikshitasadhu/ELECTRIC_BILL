#!/usr/bin/env python
# coding: utf-8

# # ELECTRIC BILL

# In[1]:


def calculate_electric_bill(units_consumed):
    if units_consumed <= 100:
        return units_consumed * 1.20
    elif units_consumed <= 300:
        return 100 * 1.20 + (units_consumed - 100) * 2.00
    elif units_consumed <= 500:
        return 100 * 1.20 + 200 * 2.00 + (units_consumed - 300) * 3.00
    else:
        return 100 * 1.20 + 200 * 2.00 + 200 * 3.00 + (units_consumed - 500) * 4.00
units = int(input("Enter the units consumed: "))
bill_amount = calculate_electric_bill(units)
print("The electric bill for", units, "units is: $", bill_amount)


# In[ ]:




