hour_wage = int(input("Enter the hourly wage : "))
total_reg_hours = int(input("Enter the total regular hours : "))
total_ovrt_hours = int(input("Enter the total overtime hours : "))

ovrt_wage = 1.5 * hour_wage
total_weekly_pay = (hour_wage*total_reg_hours)+(ovrt_wage*total_ovrt_hours)

print("Total weekly pay is : ",total_weekly_pay)