# Calorie calculator
CALORIES_PER_POUND = 3500

def main():
    try:
    	current_weight = float(input('please enter your current weight in pounds: '))
    	target_weight = float(input('please enter your target weight in pounds: '))
    	NumDays = int(input('please enter the number of days you have been on the diet: '))
    	calories_burned = float(input('please enter the number of calories you burn per day: '))
    except ValueError as err:
        print "please enter a numeric value"
        return 
    
    calc_weight(current_weight, target_weight, NumDays, calories_burned)
    
def calc_weight(v, w, x, y):
    days_required = (v - w) * CALORIES_PER_POUND / y
    months_required = (days_required / 30)
    remaining_days = (days_required - x)
    remaining_months = (remaining_days / 30)
    pounds_remaining = ((v - w) - (y * x) / CALORIES_PER_POUND)
    pounds_burned = ((v - w) - pounds_remaining)
    
    print 'days required: ', days_required, 'months required: ', months_required, 'remaining days: ', remaining_days 
    print 'months remaining: ', remaining_months, 'pounds burned: ', pounds_burned, 'pounds remaining: ', pounds_remaining
    
    
main()
    