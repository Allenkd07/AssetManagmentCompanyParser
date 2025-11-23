import pandas as pd
from collections import Counter

# 1. Load your data
bse_df = pd.read_csv(r"reference\SCHMSTRPHY_04112025.csv", encoding='latin1', low_memory=False)
# (Assuming you have a sample list of your parsed AMC names)
amc_names = ["360 ONE Mutual Fund"
"Aditya Birla Sun Life Mutual Fund"
"Angel One Mutual Fund"
"Axis Mutual Fund"
"Bajaj Finserv Mutual Fund"
"Bandhan Mutual Fund"
"Bank of India Mutual Fund"
"Baroda BNP Paribas Mutual Fund"
"Canara Robeco Mutual Fund"
"DSP Mutual Fund"
"Edelweiss Mutual Fund"
"Franklin Templeton Mutual Fund"
"Groww Mutual Fund"
"HDFC Mutual Fund"
"Helios Mutual Fund"
"HSBC Mutual Fund"
"ICICI Prudential Mutual Fund"
"Invesco Mutual Fund"
"ITI Mutual Fund"
"JM Financial Mutual Fund"
"Kotak Mahindra Mutual Fund"
"LIC Mutual Fund"
"Mahindra Manulife Mutual Fund"
"Mirae Asset Mutual Fund"
"Motilal Oswal Mutual Fund"
"Navi Mutual Fund"
"Nippon India Mutual Fund"
"NJ Mutual Fund"
"Old Bridge Mutual Fund"
"PGIM India Mutual Fund"
"PPFAS Mutual Fund"
"Quant Mutual Fund"
"Quantum Mutual Fund"
"Samco Mutual Fund"
"SBI Mutual Fund"
"Shriram Mutual Fund"
"Sundaram Mutual Fund"
"Tata Mutual Fund"
"Taurus Mutual Fund"
"Trust Mutual Fund"
"Unifi Mutual Fund"
"Union Mutual Fund"
"UTI Mutual Fund"
"WhiteOak Capital Mutual Fund",
"Zerodha Mutual Fund"] 

# 2. Flatten the BSE names into a list of all words
all_bse_words = " ".join(bse_df["Scheme Name"].astype(str).tolist()).lower().split()

# 3. Flatten the AMC names into a list of all words
all_amc_words = " ".join(amc_names).lower().split()

# 4. Find words that appear frequently in BSE but RARELY in AMC
bse_counts = Counter(all_bse_words)
amc_counts = Counter(all_amc_words)

print(f"{'WORD':<20} | {'BSE COUNT':<10} | {'AMC COUNT':<10}")
print("-" * 45)

# Check top 50 most common words in BSE
for word, count in bse_counts.most_common(50):
    # If the word is common in BSE but missing/rare in AMC, it's likely NOISE
    if amc_counts[word] < (count * 0.1): 
        print(f"{word:<20} | {count:<10} | {amc_counts[word]:<10} <--- Potential Noise")