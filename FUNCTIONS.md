## Links
- [Home](https://github.com/XamNalpak/xampy)
- [Code of Conduct](https://github.com/XamNalpak/xampy/blob/main/CODE-OF-CONDUCT.md)
- [Contributing](https://github.com/XamNalpak/xampy/blob/main/CONTRIBUTING.md)
- [Issues](https://github.com/XamNalpak/xampy/issues)
- [License](https://github.com/XamNalpak/xampy/blob/main/LICENSE)


# Please find the current functions for this repository below
<br/>

# The format for xampy documentation will be as follows

<br/>
<br/>


## Function Name

```
Summary:
--------
description of function.


Parameters
----------
arg1 : int
    Description of arg1
arg2 : str
    Description of arg2


Returns
-------
int
    Description of return value



Example code if applicable:
---------------------------

``` 
</span>

# CURRENT XAMPY FUNCTIONS

<br/>

## xp.makeData(filepath)

```
Summary:
--------
takes in the file path of a csv file and returns a dataframe


Parameters
----------
filepath : str

    string of the path to the data you want to load in

Returns
-------
DataFrame
    returns a pandas dataframe with header = True



Example code if applicable:
---------------------------
data = xp.makeData('test.csv')

``` 
<br/>

## xp.showInfo(dataframe)

```
Summary:
--------
takes in a pandas dataframe and returns quick summary statistics to help the user decide their next plan of action.


Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

Returns
-------
NOTHING
    returns a print statement showing the information at hand
    also prints out the head count specified by the user



Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#printing out the information of our new data in two lines of code.
xp.showInfo(data)

``` 
<br/>

## xp.numBarPlot(dataframe,items:list)

```
Summary:
--------
takes in a pandas dataframe and a list of the columns of interest. 

This function graphs the counts of the values in the cols.

THIS FUNCTION IS NOT FULLY FUNCTIONING PLEASE CONTRIBUTE.

FOR THIS FUNCTION THE COLUMNS MUST BE OF NUMERICAL DATA TYPE.

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

items : list

    list containing the numerical column nammes of the dataframe

Returns
-------
bar plot
    returns a bar plot of the numerical data and the counts



Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#printing out the information of our new data in two lines of code.
numCols = ['num1','num2']

xp.numBarPlot(data,numCols)

``` 
<br/>

## xp.catPlots(dataframe,items:list)

```
Summary:
--------
takes in a pandas dataframe and a list of the columns of interest. 

This function graphs the counts of the values in the cols.

THIS FUNCTION IS NOT FULLY FUNCTIONING PLEASE CONTRIBUTE.

FOR THIS FUNCTION THE COLUMNS MUST BE OF NON NUMERICAL DATA TYPE.

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

items : list

    list containing the numerical column nammes of the dataframe

Returns
-------
bar plot
    returns a bar plot of the non numerical data and the counts



Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#printing out the information of our new data in two lines of code.
numCols = ['Gender','Job_Title']

xp.catPlots(data,numCols)

``` 
<br/>

## xp.countMissing(dataframe)

```
Summary:
--------
takes in a pandas dataframe and counts the total missing values in each column

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest


Returns
-------
Nothing
    Prints out the column name followed by the count of missing values


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#printing out the information of our new data in two lines of code.
numCols = ['Gender','Job_Title']

xp.catPlots(data,numCols)

``` 
<br/>

## xp.modeFill(dataframe,col)

```
Summary:
--------
takes in a pandas dataframe and a column. 

Fills the missing values in the column with the column mode.

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

col : str

    a column name in the dataframe

Returns
-------
dataframe
    returns a dataframe with the values filled in the specified column with the mode.


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#printing out the information of our new data in two lines of code.
data = xp.modeFill(data,'Gender')

``` 
<br/>

## xp.meanFill(dataframe,col)

```
Summary:
--------
takes in a pandas dataframe and a column. 

Fills the missing values in the column with the column mean.

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

col : str

    a column name in the dataframe

Returns
-------
dataframe
    returns a dataframe with the values filled in the specified column with the mean rounded to 3 places.
            Should this be changed to more or less than 3 places.


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#printing out the information of our new data in two lines of code.
data = xp.modeFill(data,'Age')

``` 
<br/>

## xp.subSetDf(dataframe,col,value,condition)

```
Summary:
--------
takes in a pandas dataframe, column, value and a condition. 

returns a dataframe filted by this columnar filter

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

col : str

    a column name in the dataframe

value : datatype of interest

    the datatype of input here should match the datatype in the dataframe.

    i.e. 

    if you are searching for age greated than 50, value would be 50 not '50'.

    if searching for a string make sure you use the quotations.

condition : string

    comparison operators for filtering

    'gte' -> 'greater than or equal to'
    'lte' -> 'less than or equal to'
    'eq' -> 'equal to'
    'lt' -> 'less than'
    'gt' -> 'greater than'

Returns
-------
dataframe
    returns a dataframe with the data filtered by the condition places.


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#filtering the data frame to entries where age is less than or equal to 21
data = xp.subSetDf(data,'Age',21,'lte')


#filtering the data frame to entries where gender is Male after filtering by age less than or equal to 21
data = xp.subSetDf(data,'Gender','Male,'eq')


``` 
<br/>

## xp.OutDF(dataframe,col,value)

```
Summary:
--------
takes in a pandas dataframe, column, value and a condition. 

returns a dataframe filtered by everything without this value

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

col : str

    a column name in the dataframe

value : datatype of interest

    the datatype of input here should match the datatype in the dataframe.

    i.e. 

    if you are searching for age greated than 50, value would be 50 not '50'.

    if searching for a string make sure you use the quotations.


Returns
-------
dataframe
    returns a dataframe with the data filtered by everything besides entries with the specified value!


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#filtering the data frame to entries where job is not equal to 'Student', filters DF to remove students
data = xp.outDF(data,'Job','Student')

``` 
<br/>

## xp.renameCols(dataframe,remove,replace)

```
Summary:
--------
takes in a pandas dataframe, character you want to remove and the character that replaces the removed character in the column name.

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

remove : str

    character in the column title or titles you want replaced

replace : str

    the thing that will replace the removed character


Returns
-------
dataframe
    returns a dataframe with the new renamed columns!


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#removing white space in column names to underscores
data = xp.renameCols(data,' ','-')


``` 
<br/>

## xp.dataTypeSplit(dataframe)

```
Summary:
--------

takes in a pandas dataframe and splits the data into numerical datatypes and non-numerical datatypes

LOOKING FOR UPGRADES!!

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest


Returns
-------
dataframe X 2
    - returns two dataframes
         - one containing numerical data
         - one containing non-numerical data


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#assinging new data to var names after data split
numdata,catdata = xp.dataTypeSplit(data)


``` 
<br/>

## xp.bigSenti(dataframe,column)

```
Summary:
--------

takes in a pandas dataframe and column containing text data.

performs senitment analysis using textblob.
This function is better for larger chunks of text (paragraphs)

PREPROCESSING INCLUDED
- removal of
 - stop words
 - punctuation
 - tokenization of words

Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

column : string

    col containing text data, preferably bigger paragraph text


Returns
-------
dataframe
    - Appended cols
         - polarity,subjectivity
         - polarity
         - subjectivity


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#assinging new data to var names after data split
data = bigSenti(data,'Paragraphs')


``` 
<br/>

## xp.socialSentiment(dataframe,column)

```
Summary:
--------

takes in a pandas dataframe and column containing text data.

performs senitment analysis using textblob.
This function is better for social media data


Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

column : string

    col containing text data, preferably bigger paragraph text


Returns
-------
dataframe
    - Appended cols
         - compound score
         - neutral score
         - positive score
         - negative score


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#assinging new data to var names after data split
data = socialSentiment(data,'Tweets')


``` 
<br/>

## xp.linAlgo(dataframe,target,test_size,random_state)

```
Summary:
--------

takes in a pandas dataframe, your target and a few parameters

Should be used only on numerical data for linear regression


Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

target : string

    col containing target data

test_size : decimal percentage 33% => .33

    hold out size for testing the data

random_state : integer

    sets a seed to the random generator, so that your train-test splits are always deterministic.

    if you dont know what to use 42 is the meta

Returns
-------
prints out information regarding the linear model.

The column along with their coeffs and a few different error measures.

BELOW IS JUST AN EXAMPLE OF RANDOM DATA.

The feature and its respective coefficient: 

('id', -3.143645927291232e-06)
('age', 0.10381650991388383)
('hypertension', 1.69514708182813)
('heart_disease', -1.5444623358401837)
('avg_glucose_level', 0.015230558301408315)
('stroke', -1.64634612908427)

Mean squared error: 50.7619


Coefficient of determination: 0.1318


Mean Absolute Error: 5.4525


Max Error: 37.4967


Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)

#assinging new data to var names after data split
# df = data, Target = 'Age', test_size = .33, random_state = 42
xp.linAlgo(data,'Age',.33,42)


``` 
<br/>

## xp.countUnique(dataframe,col,n)

```
Summary:
--------

takes in a pandas dataframe and the column you want to view the unique counts of


Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

col : string

    col containing target data

n : int

    the count of everything
    if set to 0 it returns all

Returns
-------

prints the unque values along with their counts

Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)


xp.countUnique(data,'Jobs')

``` 
<br/>

## xp.dropnaDim(dataframe,dimension)

```
Summary:
--------

takes in a pandas dataframe and returns the cleaned data frame with how you drop the values!



Parameters
----------
dataframe : DataFrame

    pandas dataframe containing the data of interest

dimension : string

    either 'row' or 'col' on which way to drop if there is a null value


Returns
-------

returns cleaned DF without nulls

Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)


data = xp.dropnaDim(data,'row')

``` 
<br/>

## xp.groupedAVG(df,cols)

```
Summary:
--------

takes in a pandas dataframe and finds the averages of the other columns based on the filtered inputs



Parameters
----------
df : DataFrame

    pandas dataframe containing the data of interest

cols : string/list

    either a string or list showing the columns you want the group the data by


Returns
-------

returns dataframe with the filtered sections with their averages

Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)


data = xp.groupedAVG(data,['Sex','Age'])

``` 
<br/>

## xp.dropCol(df,cols)

```
Summary:
--------

takes in a pandas dataframe and a column name and drops the specified column



Parameters
----------
df : DataFrame

    pandas dataframe containing the data of interest

cols : string/list

    either a string or list showing the columns you want to drop


Returns
-------

returns dataframe with the filtered sections with their averages

Example code if applicable:
---------------------------
#reading data using makeData
data = xp.makeData('test.csv)


data = xp.dropCol(data,['Age','Sex'])

``` 
<br/>