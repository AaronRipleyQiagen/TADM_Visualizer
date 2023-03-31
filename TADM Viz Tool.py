import nmdatalytix as nmdx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from matplotlib.lines import Line2D


class UI(Frame):      
    def __init__(self, master=None):
        self.ColorDict36  = {1:'#FF0000',#Red 1
                2:'#00B050',#Green 2
                3:'#0070C0',#Blue 3
                4:'#7030A0',#Purple 4
                5:'#808080',#Light Grey 5
                6:'#FF6600',#Orange 6
                7:'#FFCC00',#Yellow 7
                8:'#9999FF',#Light Purple 8
                9:'#333333',#Black 9
                10:'#808000',#Goldish 10
                11:'#FF99CC',#Hot Pink 11
                12:'#003300',#Dark Green 12
                13:'#FF0000',#Red 1
                14:'#00B050',#Green 2
                15:'#0070C0',#Blue 3
                16:'#7030A0',#Purple 4
                17:'#808080',#Light Grey 5
                18:'#FF6600',#Orange 6
                19:'#FFCC00',#Yellow 7
                20:'#9999FF',#Light Purple 8
                21:'#333333',#Black 9
                22:'#808000',#Goldish 10
                23:'#FF99CC',#Hot Pink 11
                24:'#003300',#Dark Green 12  
                25:'#FF0000',#Red 1
                26:'#00B050',#Green 2
                27:'#0070C0',#Blue 3
                28:'#7030A0',#Purple 4
                29:'#808080',#Light Grey 5
                30:'#FF6600',#Orange 6
                31:'#FFCC00',#Yellow 7
                32:'#9999FF',#Light Purple 8
                33:'#333333',#Black 9
                34:'#808000',#Goldish 10
                35:'#FF99CC',#Hot Pink 11
                36:'#003300',#Dark Green 12  
                }    
        
        Frame.__init__(self, master)
        
        self.myParser = nmdx.nmdx_file_parser()
        
        self.raw_data = pd.DataFrame()
        self.tadm_data = pd.DataFrame()
        self.merged_data = pd.DataFrame()

        ##Draw Buttons related to dataManagement
        self.dataManagementFrame = tk.Frame(master, bg='white')
        self.dataManagementFrame.place(relx=0.01, rely=0.01, relheight=0.48, relwidth=0.48, anchor='nw')

        self.GetDataButton = tk.Button(self.dataManagementFrame, text="Select Raw Data", bg='white', command=self.load_raw_data)
        self.GetDataButton.place(relx=0.04, rely=0.05, anchor='nw', relwidth=0.2, relheight=0.25)

        self.GetTADMReferenceButton = tk.Button(self.dataManagementFrame, text="Select TADM Data", bg='white', command=self.get_tadm_data)
        self.GetTADMReferenceButton.place(relx=0.28, rely=0.05, anchor='nw', relwidth=0.2, relheight=0.25)

        self.MergeDataButton = tk.Button(self.dataManagementFrame, text="Process Data", bg='white', command=self.merge_data)
        self.MergeDataButton.place(relx=0.52, rely=0.05, anchor='nw', relwidth=0.2, relheight=0.25)
        
        self.SaveDataButton = tk.Button(self.dataManagementFrame, text="Save Data", bg='white', command=self.save_data)
        self.SaveDataButton.place(relx=0.76, rely=0.05, anchor='nw', relwidth=0.2, relheight=0.25)

        self.resetButton = tk.Button(self.dataManagementFrame, text="Clear Data", bg='white', command=self.clearData)
        self.resetButton.place(relx=0.28, rely=0.35, anchor='nw', relwidth=0.48, relheight=0.20)

        ##Draw Options Related to Data Filtering
        self.dataFilteringOptionsFrame = tk.Frame(master, bg='white')
        self.dataFilteringOptionsFrame.place(relx=0.51, rely=0.01, relheight=0.48, relwidth=0.48, anchor='nw')

        self.ProcessDataButton = tk.Button(self.dataFilteringOptionsFrame, text='Visualize Data', bg='white', command=self.plotData)
        self.ProcessDataButton.place(relx=0.28, rely=0.775, anchor='nw', relwidth=0.48, relheight=0.20)

        self.VisualizationTypeSelectionLabel = tk.Label(self.dataFilteringOptionsFrame, text="Choose Visualization Type", bg='White', anchor='nw')
        self.VisualizationTypeSelectionLabel.place(relx=0.025, rely=0.025, anchor='nw', relwidth=0.35, relheight=0.10)

        VisualizationTypeVar = tk.StringVar()
        self.VisualizationTypeOptions = ['PCR Data', 'TADM Data']
        
        self.VisualizationTypeOption = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=VisualizationTypeVar)
        self.VisualizationTypeOption['values'] = self.VisualizationTypeOptions
        self.VisualizationTypeOption.place(relx=0.40, rely=0.025, anchor='nw', relwidth=0.55, relheight=0.10)

        self.ComparisonTypeLabel = tk.Label(self.dataFilteringOptionsFrame, text="Select Main Comparison Type(s):", bg='White', anchor='nw')
        self.ComparisonTypeLabel.place(relx=0.025, rely=0.15, anchor='nw', relwidth=0.35, relheight=0.10)

        ComparisonTypeVar = tk.StringVar()
        self.ComparisonTypeOptions = ['Please Input Data Prior to Proceeding']
        self.ComparisonTypeOption = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=ComparisonTypeVar)
        self.ComparisonTypeOption['values'] = self.ComparisonTypeOptions
        self.ComparisonTypeOption.place(relx=0.40, rely=0.15, anchor='nw', relwidth=0.25, relheight=0.10)
        self.ComparisonTypeOption.bind('<KeyRelease>', self.check_input_ComparisonType)
        self.ComparisonTypeOption.bind("<<ComboboxSelected>>", self.update_ComparisonTypeSelections)

        ComparisonTypeVar2 = tk.StringVar()
        self.ComparisonTypeOptions2 = ['Please Input Data Prior to Proceeding']
        self.ComparisonTypeOption2 = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=ComparisonTypeVar2)
        self.ComparisonTypeOption2['values'] = self.ComparisonTypeOptions
        self.ComparisonTypeOption2.place(relx=0.70, rely=0.15, anchor='nw', relwidth=0.25, relheight=0.10)
        self.ComparisonTypeOption2.bind('<KeyRelease>', self.check_input_ComparisonType)
        self.ComparisonTypeOption2.bind("<<ComboboxSelected>>", self.update_ComparisonTypeSelections)


        self.ComparisonTypeSelectionLabel = tk.Label(self.dataFilteringOptionsFrame, text="Filter Data to:", bg='White', anchor='nw')
        self.ComparisonTypeSelectionLabel.place(relx=0.025, rely=0.275, anchor='nw', relwidth=0.35, relheight=0.10)

        ComparisonSelectionVar = tk.StringVar()
        self.ComparisonTypeSelections = ['Please Input Data Prior to Proceeding']
        self.ComparisonTypeSelection = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=ComparisonSelectionVar)
        self.ComparisonTypeSelection['values'] = self.ComparisonTypeOptions
        
        self.ComparisonTypeSelection.place(relx=0.40, rely=0.275, anchor='nw', relwidth=0.25, relheight=0.10)
        self.ComparisonTypeSelection.bind('<KeyRelease>', self.check_input_ComparisonSelect)
        
        ComparisonSelectionVar2 = tk.StringVar()
        self.ComparisonTypeSelections2 = ['Please Input Data Prior to Proceeding']
        self.ComparisonTypeSelection2 = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=ComparisonSelectionVar2)
        self.ComparisonTypeSelection2['values'] = self.ComparisonTypeOptions
        self.ComparisonTypeSelection2.place(relx=0.70, rely=0.275, anchor='nw', relwidth=0.25, relheight=0.10)
        self.ComparisonTypeSelection2.bind('<KeyRelease>', self.check_input_ComparisonSelect)

        self.ComparisonColLabel = tk.Label(self.dataFilteringOptionsFrame, text="Select Column Comparison Type:", bg='White', anchor='nw')
        self.ComparisonColLabel.place(relx=0.025, rely=0.40, anchor='nw', relwidth=0.35, relheight=0.10)
        
        ComparisonColVar = tk.StringVar()
        self.ComparisonColOptions = ['Please Input Data Prior to Proceeding']
        self.ComparisonColOption = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=ComparisonColVar)
        self.ComparisonColOption['values'] = self.ComparisonColOptions
        self.ComparisonColOption.place(relx=0.40, rely=0.40, anchor='nw', relwidth=0.55, relheight=0.10)
        self.ComparisonColOption.bind('<KeyRelease>', self.check_input_ComparisonCol)

        self.ComparisonRowLabel = tk.Label(self.dataFilteringOptionsFrame, text="Select Row Comparison Type:", bg='White', anchor='nw')
        self.ComparisonRowLabel.place(relx=0.025, rely=0.525, anchor='nw', relwidth=0.35, relheight=0.10)

        ComparisonRowVar = tk.StringVar()
        self.ComparisonRowOptions = ['Please Input Data Prior to Proceeding']
        self.ComparisonRowOption = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=ComparisonRowVar)
        self.ComparisonRowOption['values'] = self.ComparisonRowOptions
        self.ComparisonRowOption.place(relx=0.40, rely=0.525, anchor='nw', relwidth=0.55, relheight=0.10)
        self.ComparisonRowOption.bind('<KeyRelease>', self.check_input_ComparisonRow)

        ComparisonColorVar = tk.StringVar()
        self.ComparisonColorOptions = ['Please Input Data Prior to Proceeding']
        self.ComparisonColorOption = ttk.Combobox(self.dataFilteringOptionsFrame, textvariable=ComparisonColorVar)
        self.ComparisonColorOption['values'] = self.ComparisonColorOptions
        self.ComparisonColorOption.place(relx=0.40, rely=0.65, anchor='nw', relwidth=0.55, relheight=0.10)
        self.ComparisonColorOption.bind('<KeyRelease>', self.check_input_ComparisonColor)

        self.ComparisonColorLabel = tk.Label(self.dataFilteringOptionsFrame, text="Select Color Comparison Type:", bg='White', anchor='nw')
        self.ComparisonColorLabel.place(relx=0.025, rely=0.65, anchor='nw', relwidth=0.35, relheight=0.10)

        ##Draw Data Visualization Frame
        self.dataVisualizationFrame = tk.Frame(master, bg='white')
        self.dataVisualizationFrame.place()
    def check_input_ComparisonType(self,event):
        value = event.widget.get()

        if value == '':
            self.ComparisonTypeOption['values'] = self.ComparisonTypeOptions
            self.ComparisonTypeOption2['values'] = self.ComparisonTypeOptions
        else:
            data = []
            for item in self.ComparisonTypeOptions:
                if value in item:
                    data.append(item)

            self.ComparisonTypeOption['values'] = data
            self.ComparisonTypeOption2['values'] = data
    def check_input_ComparisonCol(self,event):
        value = event.widget.get()

        if value == '':
            self.ComparisonColOption['values'] = self.ComparisonColOptions
        else:
            data = []
            for item in self.ComparisonColOptions:
                if value in item:
                    data.append(item)

            self.ComparisonColOption['values'] = data
    def check_input_ComparisonRow(self,event):
        value = event.widget.get()

        if value == '':
            self.ComparisonRowOption['values'] = self.ComparisonRowOptions
        else:
            data = []
            for item in self.ComparisonRowOptions:
                if value in item:
                    data.append(item)

            self.ComparisonRowOption['values'] = data       
    def check_input_ComparisonColor(self,event):
        value = event.widget.get()

        if value == '':
            self.ComparisonColorOption['values'] = self.ComparisonColorOptions
        else:
            data = []
            for item in self.ComparisonColorOptions:
                if value in item:
                    data.append(item)

            self.ComparisonColorOption['values'] = data
    def check_input_ComparisonSelect(self,event):
        value = event.widget.get()
        if value == '':
            self.ComparisonTypeSelection['values'] = sorted(self.tadm_data[self.ComparisonTypeOption.get()].unique())
            self.ComparisonTypeSelection2['values'] = sorted(self.tadm_data[self.ComparisonTypeOption.get()].unique())
        else:
            data = []
            for item in self.ComparisonTypeSelections:
                if value in item:
                    data.append(item)
            self.ComparisonTypeSelection['values'] = data
            self.ComparisonTypeSelection2['values'] = data
    def update_ComparisonTypeSelections(self,event):
        value = event.widget.get()
        if self.VisualizationTypeOption.get() == 'PCR Data':
            self.ComparisonTypeSelection['values'] = sorted([x for x  in self.raw_data[self.ComparisonTypeOption.get()].unique() if pd.isnull(x)==False])
            self.ComparisonTypeSelection2['values'] = sorted([x for x  in self.raw_data[self.ComparisonTypeOption2.get()].unique() if pd.isnull(x)==False])
        elif self.VisualizationTypeOption.get() == 'TADM Data':
            if len(self.merged_data) == 0:
                self.ComparisonTypeSelection['values'] = ["No TADM Data found."]
                self.ComparisonTypeSelection2['values'] = ["No TADM Data found."]
            else:
                self.ComparisonTypeSelection['values'] = sorted([x for x  in self.merged_data[self.ComparisonTypeOption.get()].unique() if pd.isnull(x)==False])
                self.ComparisonTypeSelection2['values'] = sorted([x for x  in self.merged_data[self.ComparisonTypeOption2.get()].unique() if pd.isnull(x)==False])
        else:
            self.ComparisonTypeSelection['values'] = ["Choose Visualization Type."]
    def load_raw_data(self):
        self.ReadingLabels = tk.Label(self.dataManagementFrame, text="Parsing Raw Data", bg='blue', fg='white')
        self.ReadingLabels.place(relx=0, rely=0.825, anchor='nw', relwidth=1, relheight=0.20)
        files = [('XLSX', '*.xlsx')] 
        files = askopenfilenames(filetypes = files, defaultextension = files)
        for file in files:
            print("Reading Raw Data from file: "+str(file))
            self.raw_data = pd.concat([self.raw_data,self.myParser.scrapeFile(file=file, filename='test')])
            self.raw_data['Sample Prefix'] = self.raw_data['Sample ID'].str[0]
        nmdx.datalabeler.retrieveConsumableSerials(self.raw_data)
        nmdx.datalabeler.retrieveConsumableLots(self.raw_data)
        options = sorted([x for x in self.raw_data.columns if 'Readings ' not in x])
        self.ComparisonTypeOptions = options
        self.ComparisonTypeOption['values']  = self.ComparisonTypeOptions
        self.ComparisonColOptions = options
        self.ComparisonColOption['values']  = self.ComparisonColOptions
        self.ComparisonRowOptions = options
        self.ComparisonRowOption['values']  = self.ComparisonRowOptions
        self.ComparisonColorOptions = options
        self.ComparisonColorOption['values']  = self.ComparisonColorOptions
        self.ReadingLabels.destroy()  
    def get_tadm_data(self):
        self.ReadingLabels = tk.Label(self.dataManagementFrame, text="Parsing TADM Data", bg='blue', fg='white')
        self.ReadingLabels.place(relx=0, rely=0.825, anchor='nw', relwidth=1, relheight=0.20)
        self.dataManagementFrame.update()
        files = [('CSV', '*.csv')] 
        files = askopenfilenames(filetypes = files, defaultextension = files)
        for file in files:
            print("Reading TADM Data from file: "+str(file))
            self.tadm_data = pd.concat([self.tadm_data,pd.read_csv(file)])
        self.longest_time = self.tadm_data.columns[-1]
        print(self.longest_time)
        self.ReadingLabels.destroy()  
    def merge_data(self):
        self.ReadingLabels = tk.Label(self.dataManagementFrame, text="Matching TADM data with NMDX Data", bg='blue', fg='white')
        self.ReadingLabels.place(relx=0, rely=0.825, anchor='nw', relwidth=1, relheight=0.20)
        self.dataManagementFrame.update()        
        self.merged_data = self.raw_data.rename({'Channel':'Optics Channel'}, axis=1).drop_duplicates(['Test Guid', 'Replicate Number']).set_index(['Test Guid', 'Replicate Number']).join(self.tadm_data.set_index(['Test Guid', 'Replicate Number']).loc[:, [x for x in self.tadm_data.columns if x not in self.raw_data.columns]+['Channel']])
        self.merged_data['LiquidClass'] = self.merged_data['LiquidClassName'] + "_" + self.merged_data['StepType']
        self.merged_data['LiquidHandlingProcessOrder'] = self.merged_data['LiquidHandlingProcessOrder'].fillna(0).astype(str).replace({'.1':'','.2':'','.3':'','.4':''}).astype(float).astype(int)
        print(self.merged_data['Sample Prefix'].unique())
        self.ReadingLabels.destroy()
        options = self.ComparisonTypeOptions + ['Channel', 'TadmError', 'LiquidClass', 'LiquidHandlingProcessOrder']
        self.ComparisonTypeOptions = options
        self.ComparisonTypeOption['values']  = self.ComparisonTypeOptions
        self.ComparisonColOptions = options
        self.ComparisonColOption['values']  = self.ComparisonColOptions
        self.ComparisonRowOptions = options
        self.ComparisonRowOption['values']  = self.ComparisonRowOptions
        self.ComparisonColorOptions = options
        self.ComparisonColorOption['values']  = self.ComparisonColorOptions
    def save_data(self):
        self.ReadingLabels = tk.Label(self.dataManagementFrame, text="Exporting CSV File of Matched TADM Data", bg='blue', fg='white')
        self.ReadingLabels.place(relx=0, rely=0.825, anchor='nw', relwidth=1, relheight=0.15)
        self.dataManagementFrame.update()
        try:
            output_dir = asksaveasfilename(title="Choose where to save TADM Data", defaultextension=".xlsx", initialfile="TADM_output", filetypes=[("CSV", "*.csv")])
            self.merged_data.to_csv(output_dir)
        except:
            print("Failed to save Data.")
        self.ReadingLabels.destroy()
    def clearData(self):
        self.tadm_data = pd.DataFrame()
        self.raw_data = pd.DataFrame()
        self.merged_data = pd.DataFrame()
    def plotData(self):
        if self.VisualizationTypeOption.get() == 'TADM Data':
            self.plotTADMData()
        elif self.VisualizationTypeOption.get() == 'PCR Data':
            self.plotPCRData()
        else:
            print('Invalid selections.')
    def plotTADMData(self):             
        end_value = int(self.longest_time)
        data_selection = self.merged_data.reset_index().set_index([self.ComparisonTypeOption.get()]).loc[self.ComparisonTypeSelection.get()] 
        if self.ComparisonTypeOption2.get() != '':
            data_selection = data_selection.set_index([self.ComparisonTypeOption2.get()]).loc[self.ComparisonTypeSelection2.get()]
        for col in [str(i) for i in range(0, int(self.longest_time), 10)]:
            if pd.isnull(data_selection[col].values[1]):
                end_value = col
                break

        

        y_var_col = self.ComparisonRowOption.get()
        print(y_var_col)
        x_var_col = self.ComparisonColOption.get()
        print(x_var_col)
        color_var_col = self.ComparisonColorOption.get()

        x_vars = sorted(data_selection[x_var_col].unique())
        print(x_vars)
        y_vars = sorted(data_selection[y_var_col].unique())
        print(y_vars)
        color_vars = sorted(data_selection[color_var_col].unique())

        color_options = [self.ColorDict36[x] for x in self.ColorDict36]

        colors = {}

        for color_var in color_vars:
            colors[color_var] = color_options[color_vars.index(color_var)]

        fig_width = len(x_vars)*2.5
        fig_height = (len(y_vars)+1)*1.5
        print(fig_width, fig_height)

        share_x_var = True
        share_y_var = True

        fig, axs = plt.subplots(len(y_vars),len(x_vars)+1, figsize=(fig_width,fig_height),sharex=share_x_var, sharey=share_y_var)
        #plt.subplots_adjust(wspace=0.05)
        data_selection_plotable = data_selection.reset_index()
        
        for item in data_selection_plotable.index:
            
            ##Get row, column & color variables for object under evaluation.
            x_var = data_selection_plotable.loc[item, x_var_col]
            y_var = data_selection_plotable.loc[item, y_var_col]
            color_var = data_selection_plotable.loc[item, color_var_col]

            ##Create Line that represents object on correct axis object
            if x_var in x_vars and y_var in y_vars:
                pressure_values = data_selection_plotable.loc[item, [str(i) for i in range(0, int(end_value), 10)]].values
                sns.lineplot(x=[str(i) for i in range(0, int(end_value), 10)], y=pressure_values, color=colors[color_var], ax=axs[y_vars.index(y_var), x_vars.index(x_var)])

        ##Add Title Labels uing Row Variable Options
        for x_var in x_vars:
            axs[0, x_vars.index(x_var)].set_title(x_var)

        ##Add Column Labels uing Row Variable Options
        for y_var in y_vars:
            axs[y_vars.index(y_var), 0].set_ylabel(y_var)
            axs[y_vars.index(y_var), len(x_vars)].axis('Off')

        ##Add Row Labels uing Row Variable Options
        for x_var in x_vars:
            for y_var in y_vars:
                start, end = axs[y_vars.index(y_var),x_vars.index(x_var)].get_xlim()
                axs[y_vars.index(y_var),x_vars.index(x_var)].xaxis.set_ticks(np.arange(start, end, int(end-start)/4))
            axs[y_vars.index(y_var),x_vars.index(x_var)].set_xlabel('Time (ms)')

        ##Create Legend using Color Variable Options
        legend_elements = []
        for color in colors:
            newLabel = Line2D([0], [0], color=colors[color], lw=3,label=color)
            legend_elements.append(newLabel)
        
        axs[0, len(x_vars)].legend(handles=legend_elements, fontsize=12, loc='upper left', ncol=1, title=color_var_col)
        fig.suptitle(self.ComparisonTypeSelection.get(),fontsize=18)
        plt.show()
        return
    def plotPCRData(self):
        plotData = self.raw_data.set_index([self.ComparisonTypeOption.get()]).loc[self.ComparisonTypeSelection.get()]
        if self.ComparisonTypeOption2.get() != '':
            plotData = plotData.set_index([self.ComparisonTypeOption2.get()]).loc[self.ComparisonTypeSelection2.get()]
        plotData.to_csv('test.csv')
        nmdx.amplificationPlot(data=plotData, colField=self.ComparisonColOption.get(), rowField=self.ComparisonRowOption.get(), colorField=self.ComparisonColorOption.get())
        plt.show()
        return

window_width = 1200
window_height = 800
windowsize = str(window_width)+"x"+str(window_height)
root = Tk()
root.title("TADM Viz Tool v0.4")
root.geometry(windowsize)
my_gui = UI(root)
root.mainloop()