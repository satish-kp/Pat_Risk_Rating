import tkinter as tk
import tkinter.messagebox
import customtkinter
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Experience the new interactive Healthcare Insurance Recomendation Engine")
        self.geometry(f"{1020}x{400}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=2)
        self.grid_rowconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure((1,3,5,7,9,11), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=16, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(16, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Assessment Form", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Appearance Mode
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 10))
        # Scaling Mode
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=13, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=14, column=0, padx=20, pady=(10, 20))
        # Client Name
        self.label_1 = customtkinter.CTkLabel(self, text="Client Name:")
        self.label_1.grid(row=0, column=1, padx=(2, 0), pady=(2, 0), sticky="nsew")
        self.textbox_1 = customtkinter.CTkTextbox(self,width=25,height=1)
        self.textbox_1.grid(row=0, column=7, padx=(2, 0), pady=(2, 0), sticky="nsew")
        # Client Age
        self.label_2 = customtkinter.CTkLabel(self, text="Age:")
        self.label_2.grid(row=2, column=1, padx=(2, 0), pady=(2, 0), sticky="nsew")
        self.textbox_2 = customtkinter.CTkTextbox(self,width=25,height=1)
        self.textbox_2.grid(row=2, column=7, padx=(2, 0), pady=(2, 0), sticky="nsew")
        # Gender
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=4, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Gender:")
        self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0, text="Male")
        self.radio_button.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1, text="Female")
        self.radio_button.grid(row=1, column=3, pady=10, padx=20, sticky="n")
        self.radio_button = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2, text="Others")
        self.radio_button.grid(row=1, column=4, pady=10, padx=20, sticky="n")
        # Blood Group
        self.label_3 = customtkinter.CTkLabel(self, text="Blood Group:")
        self.label_3.grid(row=6, column=1, padx=10, pady=10)
        self.combobox_1 = customtkinter.CTkComboBox(self,values=['Please Select', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
        self.combobox_1.grid(row=6, column=7, padx=20, pady=(10, 10))
        # Pre Medical Condition
        self.label_4 = customtkinter.CTkLabel(self, text="Any Pre Medical Condition:")
        self.label_4.grid(row=8, column=1, padx=10, pady=10)
        self.combobox_2 = customtkinter.CTkComboBox(self,values=['Please Select', 'Not Applicable', 'Cancer', 'Obesity', 'Diabetes', 'Asthma', 'Hypertension', 'Arthritis'])
        self.combobox_2.grid(row=8, column=7, padx=20, pady=(10, 10))
        # Avg Last Year Expenses
        self.label_3 = customtkinter.CTkLabel(self, text="Avg Last Year Expenses:")
        self.label_3.grid(row=10, column=1, padx=(2, 0), pady=(2, 0), sticky="nsew")
        self.textbox_3 = customtkinter.CTkTextbox(self,width=25,height=1)
        self.textbox_3.grid(row=10, column=7, padx=(2, 0), pady=(2, 0), sticky="nsew")
        # Run Assessment
        self.button_1 = customtkinter.CTkButton(master=self, text="Run Assessment", command=self.on_button_click)
        self.button_1.grid(row=12, column=7, padx=20, pady=10)
        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def on_button_click(cls):
        print("=====================")
        var_Name = cls.textbox_1.get("1.0", "end-1c")
        print(f"Name: {var_Name}")
        var_Age = cls.textbox_2.get("1.0", "end-1c")
        print(f"Age: {var_Age}")
        var_Gender_value = cls.radio_var.get()
        if var_Gender_value == 0:
            var_Gender = "Male"
        elif var_Gender_value == 1:
            var_Gender = "Female"
        elif var_Gender_value == 2:
            var_Gender = "Others"
        print(f"Gender: {var_Gender}")
        var_Blood = cls.combobox_1.get()
        print(f"Blood Group: {var_Blood}")
        var_Med_Cond = cls.combobox_2.get()
        print(f"Pre Medical Condition: {var_Med_Cond}")
        var_Med_Exp = cls.textbox_3.get("1.0", "end-1c")
        print(f"Avg Last Year Expenses: {var_Med_Exp}")
        Y_value =  cls.run_Model(var_Age, var_Gender, var_Blood, var_Med_Cond, var_Med_Exp)
        print(f"Y Value: {Y_value}")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def run_Model(self, v1,v2,v3,v4,v5):
        X_live = pd.DataFrame(columns=['Age', 'Gender', 'Blood Type','Medical Condition','Billing Amount'])
        new_row = pd.DataFrame({'Age': [v1], 'Gender': [v2], 'Blood Type': [v3], 'Medical Condition': [v4], 'Billing Amount': [v5]})
        X_live = pd.concat([X_live, new_row], ignore_index=True)
        multi_1 = MultiColumnLabelEncoder(columns=['Gender','Blood Type','Medical Condition'])
        X_live = multi_1.fit_transform(X_live)
        Model_filepath = os.path.abspath(os.getcwd())+'/model.pkl'
        print(f"Path: {Model_filepath}")
        loaded_model = pickle.load(open(Model_filepath, 'rb'))
        result = loaded_model.predict(X_live)
        return result

class MultiColumnLabelEncoder:
    def __init__(self, columns=None):
        self.columns = columns # array of column names to encode
    def fit(self, X, y=None):
        self.encoders = {}
        columns = X.columns if self.columns is None else self.columns
        for col in columns:
            self.encoders[col] = LabelEncoder().fit(X[col])
        return self
    def transform(self, X):
        output = X.copy()
        columns = X.columns if self.columns is None else self.columns
        for col in columns:
            output[col] = self.encoders[col].transform(X[col])
        return output
    def fit_transform(self, X, y=None):
        return self.fit(X,y).transform(X)
    def inverse_transform(self, X):
        output = X.copy()
        columns = X.columns if self.columns is None else self.columns
        for col in columns:
            output[col] = self.encoders[col].inverse_transform(X[col])
        return output

if __name__ == "__main__":
    app = App()
    app.mainloop()


