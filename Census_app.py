# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_main.py'.

# Import modules
import numpy as np
import pandas as pd

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 
	df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

# Configure the main page by setting its title and icon that will be displayed in a browser tab.
# Import the streamlit Python module.
import streamlit as st
# Configure your home page.
st.set_page_config(page_title = 'Census Visualisation App',
                    layout = 'centered',
                    initial_sidebar_state = 'auto'
                    )

# Set the title to the home page contents.
st.title('Census Visualisation App')
# Provide a brief description for the web app.
st.write('This app can be used to visualize census data.')

# View Dataset Configuration
st.header('View Data')
# Add an expander and display the dataset as a static table within the expander.
with st.beta_expander('View Dataset'):
  st.table(census_df)

st.subheader('Columns Description:')

# Create three beta_columns.
beta1, beta2, beta3=st.beta_columns(3)
# Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
with beta1:
  if st.checkbox('Display column names'):
    st.table(list(census_df.columns))

# Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
with beta2:
  if st.checkbox('Display column datatypes'):
    st.table(census_df.dtypes)

# Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
with beta3:
  if st.checkbox('Display column data'):
    data=st.selectbox('Select column: ', tuple(census_df.columns))
    st.write(census_df[data])

# Display summary of the dataset on the click of checkbox.
if st.checkbox('Display summary'):
  st.table(census_df.describe())


# Configure the main page by setting its title and icon that will be displayed in a browser tab.
# Import the streamlit Python module.
import streamlit as st
# Configure your home page.
st.set_page_config(page_title = 'Census Visualisation App',
                    layout = 'centered',
                    initial_sidebar_state = 'auto'
                    )

# Set the title to the home page contents.
st.title('Census Visualisation App')
# Provide a brief description for the web app.
st.write('This app can be used to visualize census data.')

# View Dataset Configuration
st.header('View Data')
# Add an expander and display the dataset as a static table within the expander.
with st.beta_expander('View Dataset'):
  st.table(census_df)

st.subheader('Columns Description:')

# Create three beta_columns.
beta1, beta2, beta3=st.beta_columns(3)
# Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
with beta1:
  if st.checkbox('Display column names'):
    st.table(list(census_df.columns))

# Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
with beta2:
  if st.checkbox('Display column datatypes'):
    st.table(census_df.dtypes)

# Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
with beta3:
  if st.checkbox('Display column data'):
    data=st.selectbox('Select column: ', tuple(census_df.columns))
    st.write(census_df[data])

# Display summary of the dataset on the click of checkbox.
if st.checkbox('Display summary'):
  st.table(census_df.describe())
