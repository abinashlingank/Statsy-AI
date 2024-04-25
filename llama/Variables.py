prompt = '''
Give me the python code to generate all the possible statiscal plots for data in the data.csv file and the output plot has to be saved in output directory as images.
# Your output should be in the following json format.
# {code : <python code of your response>}
Don't use plt.show() in the code, use only plt.savefig() to save the plot as image in the directory named 'output'.
The sample data is,
'''
# Overall rank,Country or region,Score,GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Generosity,Perceptions of corruption
# 1,Finland,7.769,1.340,1.587,0.986,0.596,0.153,0.393
# 2,Denmark,7.600,1.383,1.573,0.996,0.592,0.252,0.410
# 3,Norway,7.554,1.488,1.582,1.028,0.603,0.271,0.341
# 4,Iceland,7.494,1.380,1.624,1.026,0.591,0.354,0.118
# 5,Netherlands,7.488,1.396,1.522,0.999,0.557,0.322,0.298
# 6,Switzerland,7.480,1.452,1.526,1.052,0.572,0.263,0.343
# 7,Sweden,7.343,1.387,1.487,1.009,0.574,0.267,0.373
# 8,New Zealand,7.307,1.303,1.557,1.026,0.585,0.330,0.380
# 9,Canada,7.278,1.365,1.505,1.039,0.584,0.285,0.308
# 10,Austria,7.246,1.376,1.475,1.016,0.532,0.244,0.226