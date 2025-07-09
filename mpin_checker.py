def generate_common_4_digit_mpins()->set:
    common =set()

    #Repeating digits 
    for i in range(0,10):
        common.add(str(i)*4)
    
    # Increasing sequential digits
    for i in range(0,7):
        seq=""
        for j in range(0,4):
            seq+=(str(i+j))
        common.add(seq)
    
    #Decreasing sequential digits
    for i in range(9,2,-1):
        seq=""
        for j in range(4):
            seq+=(str(i-j))
        common.add(seq)

    #Pallindromes
    for i in range(10):
        for j in range(10):
            pal = f"{i}{j}{j}{i}"
            common.add(pal)
    
    return sorted(common)

#Function to check if the pin is in common-mpins list or not 
def is_common_4_digit_mpin(mpin):
    common_mpins=generate_common_4_digit_mpins()
    return mpin in common_mpins

#Function to extract from date
def extract_date_patterns(date_str:str):
    patterns = set()
    try:
        if not date_str or '-' not in date_str:
            return patterns  # Return empty set if input is empty or invalid
        day, month, year = date_str.strip().split('-')
        year_2d = year[-2:]

        # 4-digit combinations
        patterns.update([
            day + month, 
            month + day,
            year_2d + day, 
            day + year_2d,
            month + year_2d, 
            year_2d + month,
            year,
        ])

        # 6-digit combinations
        patterns.update([
            day + month + year_2d,
            month + day + year_2d,
            year_2d + month + day,
            year_2d + day + month,
            year + day,
            day + year,
            month + year_2d + day,
            month + day + year,
            day + month + year,
            year + month + day  
        ])
    except:
        pass
    return patterns

def check_mpin_strength_part_b(mpin:str,dob_self:str,dob_spouse:str,wedding_date:str)->str:
    patterns=set()
    patterns.update(extract_date_patterns(dob_self))
    patterns.update(extract_date_patterns(dob_spouse))
    patterns.update(extract_date_patterns(wedding_date))

    if mpin in patterns:
        return "WEAK"
    return "STRONG"

def check_mpin_strength_part_c(mpin:str,dob_self:str,dob_spouse:str,wedding_date:str)->str:
    reasons=[]
    if is_common_4_digit_mpin(mpin):
        reasons.append("COMMONLY USED")
    if mpin in extract_date_patterns(dob_self):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if mpin in extract_date_patterns(dob_spouse):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if mpin in extract_date_patterns(wedding_date):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    if reasons:
        return ("WEAK", reasons)
    return ("STRONG", [])


def generate_common_6_digit_mpins() -> set:
    common = set()
    
    # 1. Repeating digits
    for i in range(10):
        common.add(str(i) * 6)

    # 2. Sequential increasing
    for i in range(0,4):  # 0 to 4
        seq = ""
        for j in range(6):
            seq += str(i + j)
        common.add(seq)

    # 3. Sequential decreasing
    for i in range(9, 4, -1):  # 9 to 5
        seq = ""
        for j in range(6):
            seq += str(i - j)
        common.add(seq)

    # 4. Palindromes: format like abc|cba
    for i in range(10):
        for j in range(10):
            for k in range(10):
                pal = f"{i}{j}{k}{k}{j}{i}"
                common.add(pal)

    return sorted(common)

def is_common_6_digit_pin(mpin):
    common_6_digit_pins=generate_common_6_digit_mpins()
    return mpin in common_6_digit_pins

def check_mpin_strength_part_d(mpin: str, dob_self: str, dob_spouse: str, wedding_date: str) -> tuple:
    reasons = []
    length = len(mpin)

    # Step 1: Check against common patterns
    if length == 4 and is_common_4_digit_mpin(mpin):
        reasons.append("COMMONLY_USED")
    elif length == 6 and is_common_6_digit_pin(mpin):
        reasons.append("COMMONLY_USED")

    # Step 2: Check against demographic patterns
    if mpin in extract_date_patterns(dob_self):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if mpin in extract_date_patterns(dob_spouse):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if mpin in extract_date_patterns(wedding_date):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    # Step 3: Return strength and reasons
    if reasons:
        return ("WEAK", reasons)
    return ("STRONG", [])


if __name__ == "__main__":
    print(is_common_4_digit_mpin("8923"))
    print(extract_date_patterns("12-01-2005"))
    print(check_mpin_strength_part_b("7239", "02-01-1998", "01-02-1996", "15-08-2020"))
    print(check_mpin_strength_part_c("9802", "02-01-1998", "01-02-1996", "15-08-2020"))
    
    print(check_mpin_strength_part_d("987654", "02-01-1998", "01-02-1996", "15-08-2020"))