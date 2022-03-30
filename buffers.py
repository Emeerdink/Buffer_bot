import pandas as pd

def making_stock(MW,Final_concentration,amount):
    gram_in = Final_concentration * MW * amount
    return(gram_in)

  
def make_input_df(df='no'):
    if df != 'no':
        stock,df_buffer = full_buffer(df)
        print('To make the stock buffers:')
        [print(i) for i in stock]
        print('\n To mix the buffer:')
        [print(df_buffer.loc[i,'name'] + ': add ' + str(df_buffer.loc[i,'volume']) + 'ml') for i in range(len(df_buffer))]
    
    else:
        df = pd.DataFrame(columns=['name','[stock]','[Final]','Total_volume'])
        count = 0
        Final_volume = float(input('What is the final volume? '))
        while count != 'stop':
            Name = input('What is the name of the chemical? \n (not important)')
            if input('Do you have a stock? (y/n) ') == 'y':
                Stock_available = 'yes'
                MlW = 0 
                Stock_concentration = float(input('What is the concentration of the stock solution? '))
                Stock_volume = 0

            else:
                Stock_available = 'no'
                MlW = float(input('What is the molecular weight of the chemical? '))
                Stock_concentration = float(input('What should the concentration of the stock solution be? '))
                Stock_volume = float(input('What should the volume of the stock solution be? '))
            Final_concentration = float(input('What is the final concentration of the chemical in the buffer? '))
            df.loc[count] = [Name,[Stock_available,MlW,Stock_concentration,Stock_volume],Final_concentration,Final_volume]
            
            if input('do you want to add something more? (y/n) ') != 'n':
                count += 1
            else:
                count = 'stop'
        stock,df_buffer = full_buffer(df)
        print('To make the stock buffers:')
        [print(i) for i in stock]
        print('\n To mix the buffer:')
        [print(df_buffer.loc[i,'name'] + ': add ' + str(df_buffer.loc[i,'volume']) + 'ml') for i in range(len(df_buffer))]
    
    return(stock,df_buffer)

def full_buffer(df):
    stock = []
    df_buffer = pd.DataFrame(columns=['name','volume','Final_volume'])
    for row in range(len(df)):
        Stock_concentration = df.loc[row,'[stock]'][2]
        chem = df.loc[row,'name']
        if df.loc[row,'[stock]'][0] == 'no':
            MlW = df.loc[row,'[stock]'][1]
            Stock_volume = df.loc[row,'[stock]'][3]
            in_gram = making_stock(MlW,Stock_concentration,Stock_volume)
            stock.append('Use ' + str(in_gram) + 'g ' + chem + ' and fill up with ' + str(Stock_volume) + 'L DEPC H2O')
        
        Final_volume = df.loc[row,'Total_volume']
        Final_concentration = df.loc[row,'[Final]']
        volume = Final_volume/(Stock_concentration/Final_concentration)
        df_buffer.loc[row] = [chem,volume,Final_volume]
    
    depc = df.loc[0,'Total_volume'] - df_buffer.volume.sum()
    df_buffer.loc[len(df)] = ['DEPC',depc,Final_volume]
    return(stock,df_buffer)
    

make_input_df()
