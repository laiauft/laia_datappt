import pandas as pd
import statistics

def convert_to_dataframe(uploaded_file):
    dataframe = pd.read_csv(uploaded_file, sep=';')
    return dataframe

def get_file_information(uploaded_file, dataframe):
    get_file_name = uploaded_file.name
    get_file_number_attributes = dataframe.shape[1]
    get_file_number_instances = len(dataframe)
    list_of_columns = []
    for column in dataframe.columns:
        list_of_columns.append(column)
    return get_file_name, get_file_number_attributes, get_file_number_instances, list_of_columns

def get_all_attributes_basic_information(dataframe):
    list_of_columns = []

    for col in dataframe.columns:

        attributes = ['Mean', 'Standard Deviation', 'Maximun Value', 'Minimun Value']
        column_mean = dataframe[col].mean()
        column_std = dataframe[col].std()
        column_max = dataframe[col].max()
        column_min = dataframe[col].min()

        column = pd.Series(
            data = [column_mean, column_std, column_max, column_min], 
            index = [attributes], 
            name = col
        )

        list_of_columns.append(column)
        dataframe_att_basic_info = pd.DataFrame(list_of_columns)
        
    return dataframe_att_basic_info

def outliers_verification_method_one(std_value):
    max_std = 10
    if(std_value >= max_std):
        return True
    else:
        return False
    
def outliers_verification_method_two(dataframe, selected_attribute_out):
    column = dataframe[selected_attribute_out].tolist()
    median =  statistics.median(column)
    defaultDeviation = statistics.stdev(column)
    medianWithFourDefaultDeviation = median + (defaultDeviation * 4)
    medianWithOutFourDefaultDeviation = median - (defaultDeviation * 4)
    outLiers = []
    
    for item in column:
        if item > round(medianWithFourDefaultDeviation, 2):
            outLiers.append(item)
            item = round(medianWithFourDefaultDeviation, 2)
        if item < round(medianWithOutFourDefaultDeviation, 2):
            outLiers.append(item)
            item = round(medianWithOutFourDefaultDeviation, 2)
    
    return medianWithFourDefaultDeviation, medianWithOutFourDefaultDeviation, outLiers
    
    
    