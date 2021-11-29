import pandas as pd
import acquire as aqr
import prepare as prep
import matplotlib.pyplot as plt
import seaborn as sns
 

def univariate_analysis(df):
    '''
    This function takes in a clean dataset then drops the customer_id, tenure and numerical columns.
    It also renders a univariate visualisation on all the categorical features.
    '''
    df =df.copy()
    # dropping custusmer id , tenure 
    df.drop(columns=['customer_id','tenure'], axis= 1, inplace=True)

    for i, predictor in enumerate(df.drop(columns=['churn','total_charges','monthly_charges'])):
        plt.figure(i)
        plt.figure(figsize=(10,8))
        sns.countplot(data=df, x=predictor,hue='churn')

        plt.show()

    return univariate_analysis
    


def tenure(df):
    tenure_yes = df[df.churn == 1].tenure
    tenure_no = df[df.churn == 0].tenure
    plt.hist([tenure_yes, tenure_no], color=['red','green'], label=['Churn = YES','Churn NO'])
    plt.legend()
    plt.title('Tenure')
    return tenure
    
def mth_charge(df):
    mth_charges_yes = df[df.churn == 1].monthly_charges
    mth_charges_no = df[df.churn == 0].monthly_charges

    plt.hist([mth_charges_yes, mth_charges_no], color=['red','green'], label=['Churn = YES','Churn NO'])
    plt.title('Monthly charge')
    plt.legend()
        
    return mth_charge

def total_charge(df):
    total_charges_yes = df[df.churn == 1].total_charges
    total_charges_no = df[df.churn == 0].total_charges

    plt.hist([total_charges_yes, total_charges_no], color=['red','green'], label=['Churn = YES','Churn NO'])
    plt.title('Total charges')
    plt.legend()
    
    return total_charge
    
         
def bivariate_viz(df):
    mth = sns.kdeplot(df.monthly_charges[(df.churn ==0)], 
                  color ="Red", shade = True)
    mth = sns.kdeplot(df.monthly_charges[(df.churn ==1)], 
                  ax = mth, color ="Green", shade = True)
    mth.legend(['Churn,',"No Churn"], loc = 'upper right')
    mth.set_ylabel("Density")
    mth.set_xlabel("Monthly charges")
    mth.set_title("Monthly Charges by churn ")
    
    return bivariate_viz

def bivariate_viz2(df):
    total_C = sns.kdeplot(df.total_charges[(df.churn ==0)], 
                  color ="Red", shade = True)
    total_C = sns.kdeplot(df.total_charges[(df.churn ==1)], 
                  ax = total_C, color ="Green", shade = True)
    total_C.legend(['Churn,',"No Churn"], loc = 'upper right')
    total_C.set_ylabel("Density")
    total_C.set_xlabel("Total charges")
    total_C.set_title("Total Charges by churn ")
    
    return bivariate_viz2


def multivar1(df):
    a = sns.PairGrid(df, y_vars = ['tenure'], x_vars = ['monthly_charges','total_charges'], height=4.5, hue='churn')
    ax = a.map(plt.scatter)
    
    return multivar1


def correlat(df):
    plt.figure(figsize=(20,8))
    df.corr()['churn'].sort_values(ascending= False).plot(kind ='bar')
    
    return correlat
    
    
    
def correlat_heatmap(df):
    f, ax = plt.subplots(figsize =(14,10))
    sns.heatmap(df.corr(),cmap='YlGnBu', center=0, annot=True)
    plt.title('Correlation Heatmap',fontsize =23)
    plt.show()
    return correlat_heatmap
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
