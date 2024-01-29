## Loading the Model

These are manual instructions, by default the repository and notebook are configured to run automatically.

Typically, this process has been automated in the notebook. But in case there may be an issues, you may use the below manual to setup the model.

To load the model, follow these simple instructions:

### Step 1: Install Required Packages

Install the requirements from the `reqs.txt` file in the root folder.

### Step 2: Download the Model Files

Download the model file from the repository. The model files typically include:

- `train_model.pkl`: The trained model file. This file is in the root folder.

### Step 3: Load the Model

In your Python environment, use the following code to load the model:

```
def load_model(model_path):
    """Loads a CatBoost model from a pickle file.

    Args:
        model_path (str): Path to the pickle file containing the CatBoost model.

    Returns:
        catboost.CatBoost: The loaded CatBoost model.
    """

    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model
```

### Load the model

```
model_path = './train_model.pkl'
loaded_model = load_model(model_path)
```

### Step 4: Make Predictions (Run the cell with testing_hidden_data)
NOTE: This process takes a few minutes please be patient :D

Now that the model is loaded, you can use them to make predictions on new data. Here's a simple example:

Run the `testing_hidden_data` function towards the bottom of the file in the jupyter notebook.

### Step 5: Getting the results

Use the code below to get your predictions.

```
test_df  =  pd.read_parquet("./catA_train.parquet")

test_df  =  test_df.drop(columns=['Sales (Domestic Ultimate Total USD)'])

print(testing_hidden_data(test_df))
```
