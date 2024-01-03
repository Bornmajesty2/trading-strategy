def load_data(orcl):
   # Load data from rocl
    data_set = []
    with open(orcl, 'r') as file:
        title = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            data_point = dict(zip(title, values))
            data_set.append(data_point)
    return data_set

def calculate_sma(data, window=5):
    
    #Moving averages for a 5-day window
    data_of_sma = []
    for i in range(len(data)):
        if i < window - 1:
            sma = None  # SMA is not defined for the first few days
        else:
            close_prices = [float(data[j]['Close']) for j in range(i - window + 1, i + 1)]
            sma = sum(close_prices) / window
        data_of_sma.append({'Date': data[i]['Date'], 'SMA': sma})
    return data_of_sma

def calculate_rsi(data, window=14):
    
    #Calculating RSI for a 14-day window

    lose = []
    rsi_data = []
    gain = []


    for i in range(1, len(data)):
        difference_of_close_price = float(data[i]['Close']) - float(data[i - 1]['Close'])

        if difference_of_close_price > 0:
            gain.append(difference_of_close_price)
            lose.append(0)
        elif difference_of_close_price < 0:
            gain.append(0)
            lose.append(-difference_of_close_price)
        else:
            gain.append(0)
            lose.append(0)

        if i >= window:
            avg_gain = sum(gain[-window:]) / window
            avg_loss = sum(lose[-window:]) / window
            rs = avg_gain / avg_loss if avg_loss != 0 else float('inf')
            rsi = 100 - (100 / (1 + rs))
            rsi_data.append({'Date': data[i]['Date'], 'RSI': rsi})

    return rsi_data

def write_to_csv(data, file_path, header):

   #indicator as a file
    with open(file_path, 'w') as file:
        file.write(','.join(header) + '\n')
        for row in data:
            file.write(','.join(str(row[col]) for col in header) + '\n')

if __name__ == "__main__":
    #Loading historical data
    historical_data = load_data("orcl.csv")

    #Calculating indicators
    sma_data = calculate_sma(historical_data)
    rsi_data = calculate_rsi(historical_data)

    #Writing indicators as a file
    write_to_csv(sma_data, "orcl-sma.csv", header=['Date', 'SMA'])
    write_to_csv(rsi_data, "orcl-rsi.csv", header=['Date', 'RSI'])
