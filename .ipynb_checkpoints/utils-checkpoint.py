import zipfile
import os

import pandas as pd

SCRIPT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

FUTURES_LIST = ['F_AD','F_BO','F_BP','F_C','F_CC','F_CD','F_CL','F_CT','F_DX','F_EC','F_ED','F_ES','F_FC',
                'F_FV','F_GC','F_HG','F_HO','F_JY','F_KC','F_LB','F_LC','F_LN','F_MD','F_MP','F_NG','F_NQ',
                'F_NR','F_O','F_OJ','F_PA','F_PL','F_RB','F_RU','F_S','F_SB','F_SF','F_SI','F_SM','F_TU',
                'F_TY','F_US','F_W','F_XX','F_YM','F_AX','F_CA','F_DT','F_UB','F_UZ','F_GS','F_LX','F_SS',
                'F_DL','F_ZQ','F_VX','F_AE','F_BG','F_BC','F_LU','F_DM','F_AH','F_CF','F_DZ','F_FB','F_FL',
                'F_FM','F_FP','F_FY','F_GX','F_HP','F_LR','F_LQ','F_ND','F_NY','F_PQ','F_RR','F_RF','F_RP',
                'F_RY','F_SH','F_SX','F_TR','F_EB','F_VF','F_VT','F_VW','F_GD','F_F']

STOCKS_LIST = ['AAPL', 'MMM', 'ABT', 'ABBV', 'ACN', 'ALL', 'MO', 'AMZN', 'AEP', 'AXP', 'AIG', 'AMGN', 'APC',
               'APA', 'AAPL', 'T', 'BAC', 'BK', 'BAX', 'BRK.B', 'BA', 'BMY', 'COF', 'CAT', 'CVX', 'CSCO', 'C',
               'KO', 'CL', 'CMCSA', 'COP', 'COST', 'CVS', 'DVN', 'DOW', 'DD', 'EBAY', 'EMC', 'EMR', 'EXC',
               'XOM', 'FB', 'FDX', 'F', 'FCX', 'GD', 'GE', 'GM', 'GILD', 'GS', 'GOOG', 'GOOGL', 'HAL', 'HPQ',
               'HD', 'HON', 'INTC', 'IBM', 'JNJ', 'JPM', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDT', 'MRK', 'MET',
               'MSFT', 'MDLZ', 'MON', 'MS', 'NOV', 'NKE', 'NSC', 'OXY', 'ORCL', 'PEP', 'PFE', 'PM', 'PG', 'QCOM',
               'RTN', 'SLB', 'SPG', 'SO', 'SBUX', 'TGT', 'TXN', 'TWX', 'FOXA', 'USB', 'UNP', 'UPS', 'UTX', 'UNH',
               'VZ', 'V', 'WBA', 'WMT', 'DIS', 'WFC', 'A', 'AA', 'ABC', 'ACE', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS',
               'ADSK', 'ADT', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIV', 'AIZ', 'AKAM', 'ALLE', 'ALTR',
               'ALXN', 'AMAT', 'AME', 'AMG', 'AMP', 'AMT', 'AN', 'AON', 'APD', 'APH', 'ARG', 'ATI', 'AVB', 'AVGO',
               'AVP', 'AVY', 'AZO', 'BBBY', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHI', 'BLK', 'BLL', 'BMS',
               'BRCM', 'BSX', 'BWA', 'BXP', 'CA', 'CAG', 'CAH', 'CAM', 'CB', 'CBG', 'CBS', 'CCE', 'CCI', 'CCL',
               'CELG', 'CERN', 'CF', 'CHK', 'CHRW', 'CI', 'CINF', 'CLX', 'CMA', 'CME', 'CMG', 'CMI', 'CMS', 'CNP',
               'CNX', 'COG', 'COH', 'COL', 'CPB', 'CRM', 'CSC', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVC', 'D',
               'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DISCA', 'DISCK', 'DLPH', 'DLTR', 'DNB', 'DNR', 'DO',
               'DOV', 'DPS', 'DRI', 'DTE', 'DUK', 'DVA', 'EA', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EOG', 'EQR',
               'EQT', 'ESRX', 'ESS', 'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXPD', 'EXPE', 'FAST', 'FE', 'FFIV', 'FIS',
               'FISV', 'FITB', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOSL', 'FSLR', 'FTI', 'FTR', 'GAS', 'GCI', 'GGP', 'GIS',
               'GLW', 'GMCR', 'GME', 'GNW', 'GPC', 'GPS', 'GRMN', 'GT', 'GWW', 'HAR', 'HAS', 'HBAN', 'HCBK', 'HCN',
               'HCP', 'HES', 'HIG', 'HOG', 'HOT', 'HP', 'HRB', 'HRL', 'HRS', 'HST', 'HSY', 'HUM', 'ICE', 'IFF', 'INTU',
               'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'ITW', 'IVZ', 'JCI', 'JEC', 'JNPR', 'JOY', 'JWN', 'K', 'KEY', 'KIM',
               'KLAC', 'KMB', 'KMI', 'KMX', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LLL', 'LLTC',
               'LM', 'LNC', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MAC', 'MAR', 'MAS', 'MAT', 'MCHP', 'MCK', 'MCO',
               'MHFI', 'MHK', 'MJN', 'MKC', 'MLM', 'MMC', 'MNK', 'MNST', 'MOS', 'MPC', 'MRO', 'MSI', 'MTB', 'MU', 'MUR',
               'MYL', 'NAVI', 'NBL', 'NBR', 'NDAQ', 'NE', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NLSN', 'NOC', 'NRG',
               'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWSA', 'OI', 'OKE', 'OMC', 'ORLY', 'PAYX', 'PBCT', 'PBI', 'PCAR',
               'PCG', 'PCL', 'PCLN', 'PCP', 'PDCO', 'PEG', 'PFG', 'PGR', 'PH', 'PHM', 'PKI', 'PLD', 'PNC', 'PNR', 'PNW',
               'POM', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'QEP', 'R', 'RAI', 'REGN',
               'RF', 'RHI', 'RHT', 'RIG', 'RL', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'SCG', 'SCHW', 'SE', 'SEE', 'SHW',
               'SJM', 'SNA', 'SNDK', 'SNI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STJ', 'STT', 'STX', 'STZ', 'SWK', 'SWN', 'SYK',
               'SYMC', 'SYY', 'TAP', 'TDC', 'TE', 'TEL', 'THC', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO',
               'TSN', 'TSO', 'TSS', 'TWC', 'TXT', 'TYC', 'UA', 'UHS', 'UNM', 'URBN', 'URI', 'VAR', 'VFC', 'VIAB', 'VLO',
               'VMC', 'VNO', 'VRSN', 'VRTX', 'VTR', 'WAT', 'WDC', 'WEC', 'WFM', 'WHR', 'WIN', 'WM', 'WMB', 'WU', 'WY',
               'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XRAY', 'XRX', 'XYL', 'YHOO', 'YUM', 'ZION', 'ZTS' ]

def unzip_ticker_data(source=os.path.join(SCRIPT_DIRECTORY, "tickerData.zip"), destination=SCRIPT_DIRECTORY):
    with zipfile.ZipFile(source, 'r') as zip_ref:
        zip_ref.extractall(destination)
        zip_ref.close()
        
def make_ticker_dict(source=os.path.join(SCRIPT_DIRECTORY, "tickerData"), data_subset=None):
    data_dict = {}
    
    files_in_directory = os.listdir(source)
    if not data_subset:
        data_subset = [item[:-len(".txt")] for item in files_in_directory]
        
    for filename in files_in_directory:
        if filename[:-len(".txt")] in data_subset:
            df = pd.read_table(os.path.join(source, filename), sep=",")
            df["DATE"] = pd.to_datetime(df["DATE"], format="%Y%m%d")
            df = df.set_index("DATE")
            data_dict[filename[:filename.find(".txt")]] = df
            df.columns = [item.strip() for item in df.columns]
            
    return data_dict