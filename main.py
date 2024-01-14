import pandas as pd
import re

# Read the Excel file
df = pd.read_excel('mank_transfers.xls')

# Convert 'Data waluty' column to datetime format
df['Data waluty'] = pd.to_datetime(df['Data waluty'])

keyword_groups = {
    'KAUFLAND': 'Spożywcze',
    'JMP S.A. BIEDRONKA 2971': 'Spożywcze',
    'LIDL SLONECZNA': 'Spożywcze',
    'Revolut**5050*' : 'Revolut',
    'SKLEP U BEATY' : 'Spożywcze',
    'JMP S.A. BIEDRONKA 4826' : 'Spożywcze',
    'Autopay Mobility' : 'Autostrada',
    'Apteka Blisko Ciebie 02' : 'Apteka',
    'ZABKA Z9435 K.2' : 'Spożywcze',
    'CARREFOUR 5 MINUT' : 'Spożywcze',
    'CDA PL' : 'Rozrywka',
    'KIOSK OGOLNO-SPOZYWCZY' : 'Spożywcze',
    'JMP S.A. BIEDRONKA 6569' : 'Spożywcze',
    'JMP S.A. BIEDRONKA 3600' : 'Spożywcze',
    'MARKET OGOLNOSPOZYWCZY' : 'Spożywcze',
    'JMP S.A. BIEDRONKA 3600' : 'Spożywcze',
    'KSIEGARNIA SW.JACKA' : 'Książki',
    'Apteka Blisko Ciebie 01' : 'Apteka',
    'WORDPRESS 21G2FBM3T9' : 'Internet',
    'APTEKA DR MAX' : 'Apteka',
    'MARKET OGOLNOSPOZYWCZY' : 'Spożywcze',
    'Apteka Blisko Ciebie My' : 'Apteka',
    'ME M07' : 'Nie wiem co to',
    'Poczta Polska 05' : 'Poczta',
    'LUCART O / MYSLOWICE'  : 'Auto',
    'Stacja Paliw MOYA nr 32' : 'Paliwo',
    'BOBBY BURGER' : 'Restauracja',
    'Microsoft*Microsoft 365 B' : 'Internet',
    'Zielono mi' : 'Nie wiem co to',
    'Castorama' : 'Budowlane',
    'TU KUBA S.C.' : 'Nie wiem co to',
    'VISION EXPRESS 4238' : 'Okulary',
    'ALDI Sp. z o.o. 012' : 'Spożywcze',
    'ZABKA Z7966 K.1' : 'Spożywcze',
    'UBER   *TRIP' : 'Taxi',
    'Atemi' : 'Nie wiem co to',
    'ORLEN STACJA NR 197' : 'Paliwo',
    'HIPNOZA' : 'Nie wiem co to',
    'Action A028' : 'Action',
    'DENTALMED PREMIUM' : 'Dentysta',
    'PRALNIA EBS' : 'Pralnia',
    'ROSSMANN' : 'Kosmetyczne',
    'UL. MIKOLOWSKA 12A' : 'Nie wiem co to',
    'Revolut**8227*' : 'Revolut',
    'MARKET OBI 006' : 'Budowlane',
    'Rossmann 01' : 'Kosmetyczne',
    'MIEJSKI ZARZAD ULIC I MOS' : 'Nie wiem co to',
    'TRANSGOURMET' : 'Nie wiem co to',
    'P4 SP. Z O.O. SALON PL' : 'Komórka',
    '5 Balice Manual (2)' : 'Autostrada',
    '16 Brzeczkowice Manual (2' : 'Autostrada',
    'DELIKATESY CENTRUM' : 'Spożywcze',
    'Tarkom           24877' : 'Nie wiem co to',
    'DINO POLSKA S.A.' : 'Spożywcze',
    'ORLEN STACJA NR 4479' : 'Paliwo',
    'PLANET CASH OSWOBODZENIA' : 'Nie wiem co to',
    'MPL SERVICES SP. Z O.O.' : 'Nie wiem co to',
    'BOLT.EU/O/2311251708' : 'Taxi',
    'ZAPIEKANKI TRADYCYJNE' : 'Spożywcze',
    'RYLKO 12 KATOWICE SILESIA' : 'Ubrania',
    'PIWIARNIA MARIACKA' : 'Restauracja',
    'Microsoft*Store' : 'Internet',
    'JARMARKI SLASKIE' : 'Nie wiem co to',
    'AMNEZJA' : 'Restauracja',
    'TU KUBA' : 'Nie wiem co to',
    'CHOPINA DENTAL PARK' : 'Dentysta',
    'TABAK POLSKA 161' : 'Nie wiem co to',
    'MARTES SPORT' : 'Ubrania',
    'GO KINO MYSLOWICE' : 'Rozrywka',
    'NOVOTEL CENTRUM RECEPC' : 'Hotel',
    'Apteka Zdrowit' : 'Apteka',
    'UBER *TRIP HELP.UBER.COM' : 'Taxi',
    'OCHNIK SALON FIRMOWY' : 'Ubrania',
    'NOVA SUSHI' : 'Restauracja',
    'ORLEN STACJA NR 273' : 'Paliwo',
    'BP-MAGNOLIA 566' : 'Paliwo',
    'SHELL' : 'Paliwo',
    'SHELL 01' : 'Paliwo',
    'AKADEMIA SMAKU SPZOO' : 'Restauracja',
    'F.H.U. WOJTOWICZ S.C.' : 'Nie wiem co to',
    'CARREFOUR HIPERMARKET' : 'Spożywcze',
    '6 Brzeczkowice Manual (2)' : 'Autostrada',
    'Inmedio 41188' : 'Nie wiem co to',
    'BP-MAGNOLIA 566' : 'Paliwo',
    'BOLT.EU/O/2310250836' : 'Taxi',
    '6 Balice Manual (2)' : 'Autostrada',
    'ORLEN STACJA NR 4479' : 'Paliwo',
    'EVAPIFY Nowy Swiat' : 'Nie wiem co to',
    'DELIKATESY CENTRUM' : 'Spożywcze',
    'Delikatesy Centrum' : 'Spożywcze',
    'V.GIANNI' : 'Nie wiem co to',
    'RYSPOL APTEKA ARNIKA CH' : 'Apteka',
    'BP-STANISLAWICE 296' : 'Paliwo',
    'UL  MIKOLOWSKA 42D' : 'Nie wiem co to',
    'PEPCO 1643 MYSLOWICE 1' : 'Pepco',
    'JMP S.A. BIEDRONKA 3182': 'Nie wiem co to',
    'JMP S.A. BIEDRONKA 3861': 'Spożywcze',
    'JMP S.A. BIEDRONKA 3590': 'Spożywcze',
    'Revolut**8892*': 'Nie wiem co to',
    'ZABKA ZB383 K.1': 'Apteka',
    'ZABKA Z9435 K.1': 'Paliwo',
    'ZABKA Z5095 K.1': 'Nie wiem co to',
}

# Function to create separate DataFrames for each month
def separate_by_month(df):
    month_dataframes = {}
    for month in range(1, 13):
        month_dataframes[month] = df[df['Data waluty'].dt.month == month]
    return month_dataframes

def separate_by_transaction_type(df):
    transaction_types = [
        'Płatność kartą', 'Płatność web - kod mobilny', 'Przelew na konto', 'Polecenie Zapłaty', 'Przelew z karty', 'Opłata', 'Przelew z rachunku', 'Zakup w terminalu - kod mobilny', 'Wypłata w bankomacie - kod mobilny', 'MOBILE_PAYMENT_C2C_EXTERNAL', 'Zlecenie stałe'
    ]
    transaction_dataframes = {}
    unlisted_types = []

    for t_type in df['Typ transakcji'].unique():
        if t_type in transaction_types:
            transaction_dataframes[t_type] = df[df['Typ transakcji'] == t_type]
        elif pd.notna(t_type):
            unlisted_types.append(t_type)

    if unlisted_types:
        print("Unlisted Transaction Types Found:")
        for unlisted_type in unlisted_types:
            print(unlisted_type)

    return transaction_dataframes, unlisted_types

# Regular expression pattern to find keywords between 'Adres :' and 'Miasto :'
pattern = r'Adres : (.*?) Miasto :'

# Assuming Column M is named 'ColumnM'. Replace it with the actual name
column_name = 'Opis transakcji'

# Function to extract keywords, including None for no keyword
def extract_keywords(df):
    pattern = r'Adres : (.*?) Miasto :'
    keywords = df[column_name].dropna().apply(lambda x: re.search(pattern, x))
    return [match.group(1) if match else None for match in keywords]

# Function to search for keywords in the file, including handling None
def search_keywords_in_file(keywords,df):
    data_for_keywords = {'Spożywcze': pd.DataFrame(),'Revolut': pd.DataFrame(), 'Autostrada': pd.DataFrame(), 'Apteka': pd.DataFrame(), 'Internet': pd.DataFrame(), 'Rozrywka': pd.DataFrame(), 'Książki': pd.DataFrame(), 'Restauracja': pd.DataFrame(), 'Nie wiem co to': pd.DataFrame(), 'Kosmetyczne': pd.DataFrame(), 'Pepco': pd.DataFrame(), 'Okulary': pd.DataFrame(), 'Dentysta': pd.DataFrame(), 'Auto': pd.DataFrame(), 'Budowlane': pd.DataFrame(), 'Ubrania': pd.DataFrame(), 'Taxi': pd.DataFrame(), 'Paliwo': pd.DataFrame(), 'Budowlane': pd.DataFrame(), 'Komórka': pd.DataFrame(), 'Action': pd.DataFrame(), 'Pralnia': pd.DataFrame(), 'Poczta': pd.DataFrame(), 'Apteka': pd.DataFrame(), 'Internet': pd.DataFrame(), 'Hotel': pd.DataFrame(), 'No Keyword': pd.DataFrame(), 'Unassigned': []}

    for keyword in keywords:
        if keyword:
            keyword_pattern = re.escape(keyword)  # Escape to handle special characters in keyword
            keyword_group = keyword_groups.get(keyword)

            # Check if keyword is assigned to a group
            if keyword_group:
                matched_data = df[df[column_name].str.contains(keyword_pattern, na=False)]
                data_for_keywords[keyword_group] = pd.concat([data_for_keywords[keyword_group], matched_data])
            else:
                # If the keyword is not assigned to any group, add it to the 'Unassigned' list
                data_for_keywords['Unassigned'].append(keyword)
        else:
            # Handle the None case (no keyword found)
            data_for_keywords['No Keyword'] = pd.concat([data_for_keywords['No Keyword'],
                                                         df[df[column_name].apply(
                                                             lambda x: re.search(pattern, x) is None)]])

    # Check for unassigned keywords and print them
    if data_for_keywords['Unassigned']:
        print("The following keywords are not assigned to any group:")
        for unassigned_keyword in data_for_keywords['Unassigned']:
            print(unassigned_keyword)

    return data_for_keywords

# Function to check if all unique keywords are included in keyword_groups
def check_keyword_coverage(unique_keywords, keyword_groups):
    group_keywords = set(keyword_groups.keys())
    uncovered_keywords = [kw for kw in unique_keywords if kw not in group_keywords and kw is not None]

    if uncovered_keywords:
        print("The following keywords are not covered in keyword groups:")
        for keyword in uncovered_keywords:
            print(keyword)

def sum_positive_column_values(df):
    if column_name in df.columns:
        # Convert negative values to positive and sum up
        return (df['Kwota'] * -1).sum()
    else:
        print(f"Column 'Kwota' not found in DataFrame.")
        return 0
# Extract keywords, including None

# Extracting unique categories
#unique_categories = set(keyword_groups.values())
# Converting the set to a list for better readability
#unique_categories_list = list(unique_categories)
# Print the list of unique categories
#print(unique_categories_list)

unique_keywords = extract_keywords(df)#define keywords from complete year file
print(unique_keywords)
check_keyword_coverage(unique_keywords, keyword_groups)

# Search for these keywords in the file and aggregate data
#aggregated_data = search_keywords_in_file(set(unique_keywords))

# The aggregated_data dictionary now includes a 'No Keyword' key for rows with no keywords
#no_keyword_data = aggregated_data.get('No Keyword')

# Now you can work with no_keyword_data, which contains rows where no keyword was found

monthly_dataframes = separate_by_month(df)
january_data = monthly_dataframes[1]  # 1 for January
december_data = monthly_dataframes[12]  # 1 for January
october_data = monthly_dataframes[10]  # 1 for January
november_data = monthly_dataframes[11]  # 1 for January
#print(january_data)
#print(type(january_data))

transaction_dataframes, unlisted_transaction_types = separate_by_transaction_type(january_data)
card_payment_data_january = transaction_dataframes.get('Płatność kartą', pd.DataFrame())

#aggregated_data = search_keywords_in_file(set(unique_keywords),january_data)
#print(aggregated_data.get('KAUFLAND', pd.DataFrame()))
#no_keyword_data = aggregated_data.get('No Keyword')
#print(no_keyword_data)

grouped_data_january = search_keywords_in_file(set(unique_keywords), card_payment_data_january)#tu są wzięte pod uwagę tylko wpisy dla 'Płatność kartą'
food_january_data = grouped_data_january['Spożywcze']
motorway_january_data = grouped_data_january['Autostrada']
no_keyword_data = grouped_data_january['No Keyword']
food_money_january = sum_positive_column_values(food_january_data)
motorway_money_january = sum_positive_column_values(motorway_january_data)

print(food_january_data)
print(motorway_january_data)
print(food_money_january)
print(motorway_money_january)
